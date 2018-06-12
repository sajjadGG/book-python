************
Panel admina
************

- @admin.register
- StackedInline
- TabularInline
- readonly_fields
- search (``^``, ``=``, ``@``)
- class Media (js and css)

.. code-block:: python

    class Media:
        js = [
            'communication/js/email-reply-button.js',
            'communication/js/email-hide-save.js',
        ]
        css = {'all': [
            'communication/css/hide-id-field.css',
            'communication/css/resize-fields.css',
        ]}


- order
- filer
- własne kolumny i treść w komórkach

.. code-block:: python

    from django.contrib import admin

    admin.site.site_header = _('HabitatOS')
    admin.site.index_title = _('Dashboard')
    admin.site.site_title = _('HabitatOS')

.. code-block:: python

    from django.contrib import admin
    from habitat._common.admin import HabitatAdmin
    from habitat.sensors.models import ZWaveSensor


    @admin.register(ZWaveSensor)
    class ZWaveSensorAdmin(HabitatAdmin):
        change_list_template = 'sensors/change_list_charts.html'
        list_display = ['date', 'time', 'type', 'device', 'value', 'unit']
        list_filter = ['created', 'type', 'unit', 'device']
        search_fields = ['^date', 'device']
        ordering = ['-datetime']
        inlines = [SpacewalkerInline]
        raw_id_fields = ['contingencies', 'tools']
        autocomplete_lookup_fields = {'m2m': ['contingencies', 'tools']}


        def get_list_display(self, request):
            list_display = self.list_display

            if request.user.is_superuser:
                list_display = ['datetime'] + list_display

            return list_display

.. code-block:: python

    @admin.register(Repair)
    class RepairAdmin(HabitatAdmin):
        list_display = ['start', 'status', 'object', 'what', 'description', 'location']
        list_filter = ['status', 'size', 'start', 'reporter']
        search_fields = ['what', 'description', 'solution']
        exclude = ['reporter', 'created', 'updated', 'duration']
        date_hierarchy = 'start'
        raw_id_fields = ['object']
        autocomplete_lookup_fields = {'fk': ['object']}
        ordering = ['-modified']
        radio_fields = {
            'status': admin.HORIZONTAL,
            'size': admin.HORIZONTAL}

        def save_model(self, request, obj, form, change):
            obj.reporter = request.user
            super().save_model(request, obj, form, change)

.. code-block:: python

    from django.contrib import admin
    from django.db import models
    from django.forms import CheckboxSelectMultiple

    from habitat._common.admin import HabitatAdmin
    from django.utils.translation import ugettext_lazy as _
    from habitat.reporting.models import Sleep


    @admin.register(Sleep)
    class SleepAdmin(HabitatAdmin):
        list_display = ['reporter', 'type', 'duration', 'location', 'quality', 'asleep_time', 'wakeup_time']
        list_filter = ['reporter', 'type', 'quality', 'sleep_amount', 'sleepy', 'aid_ear_plugs', 'aid_eye_mask', 'aid_pills']
        search_fields = ['dream']
        readonly_fields = ['duration']
        exclude = ['reporter', 'created', 'modified']
        ordering = ['-modified']
        formfield_overrides = {models.ManyToManyField: {'widget': CheckboxSelectMultiple}}

        radio_fields = {
            'sleep_interrupted': admin.HORIZONTAL,
            'sleep_amount': admin.HORIZONTAL,
            'quality': admin.HORIZONTAL,
            'sleepy': admin.HORIZONTAL,
            'type': admin.HORIZONTAL,
            'aid_ear_plugs': admin.HORIZONTAL,
            'aid_eye_mask': admin.HORIZONTAL,
            'aid_pills': admin.HORIZONTAL,
        }

        fieldsets = [
            (_('General'), {'fields': ['type', 'location', 'asleep_time', 'wakeup_time', 'sleep_amount', 'quality', 'sleep_events', 'sleep_interrupted']}),
            (_('Interruptions'), {'fields': ['sleep_interruptions', 'impediments_count', 'impediments_remarks'], 'classes': ['sleep-interruptions']}),
            (_('Before Sleep'), {'fields': ['last_activity', 'sleepy', 'sleepy_remarks'], 'classes': ['sleep-report']}),
            (_('Sleep'), {'fields': ['asleep_bedtime', 'asleep_problems', 'aid_ear_plugs', 'aid_eye_mask', 'aid_pills'], 'classes': ['sleep-report']}),
            (_('After Sleep'), {'fields': ['wakeup_reasons', 'getup', 'dream'], 'classes': ['sleep-report']}),
        ]

        def get_queryset(self, request):
            queryset = super().get_queryset(request)

            if request.user.has_perm('reporting.delete_sleep'):
                return queryset
            else:
                return queryset.filter(reporter=request.user)

        def save_model(self, request, obj, form, change):
            obj.reporter = request.user
            super().save_model(request, obj, form, change)

        class Media:
            js = [
                'reporting/js/sleep-or-nap.js',
                'reporting/js/sleep-interruptions.js',
            ]

.. code-block:: python

    from django.contrib import admin
    from habitat._common.admin import HabitatAdmin
    from habitat.reporting.models import SleepQuality


    @admin.register(SleepQuality)
    class SleepQualityAdmin(HabitatAdmin):
        list_display_links = ['name']
        list_display = ['type', 'name']
        list_filter = ['type']
        list_editable = ['type']
        ordering = ['type', 'name']

.. code-block:: python

    from django.contrib import admin
    from habitat._common.admin import HabitatAdmin
    from habitat._common.admin import HabitatTabularInline
    from habitat.reporting.models import SociodynamicReport
    from habitat.reporting.models import SociodynamicReportEntry


    class SociodynamicReportEntryInline(HabitatTabularInline):
        model = SociodynamicReportEntry
        extra = 5
        max_num = 5
        min_num = 5


    @admin.register(SociodynamicReport)
    class SociodynamicReportAdmin(HabitatAdmin):
        list_display = ['date', 'reporter']
        list_filter = ['reporter']
        inlines = [SociodynamicReportEntryInline]
        exclude = ['reporter', 'created', 'updated']

        def get_queryset(self, request):
            queryset = super().get_queryset(request)

            if request.user.has_perm('reporting.delete_sociodynamicreport'):
                return queryset
            else:
                return queryset.filter(reporter=request.user)

        def save_model(self, request, obj, form, change):
            obj.reporter = request.user
            super().save_model(request, obj, form, change)

.. code-block:: python

    from django.contrib import admin
    from django.db import models
    from django.forms import CheckboxSelectMultiple
    from django.utils.translation import ugettext_lazy as _
    from habitat._common.admin import HabitatAdmin
    from habitat.food.models.meal import Meal


    @admin.register(Meal)
    class MealAdmin(HabitatAdmin):
        formfield_overrides = {models.ManyToManyField: {'widget': CheckboxSelectMultiple}}
        list_display = ['name', 'difficulty', 'type', 'display_diet', 'display_tags']
        ordering = ['-name']
        search_fields = ['name']
        list_filter = ['difficulty', 'type', 'diet', 'tags']

        def display_tags(self, obj):
            return ", ".join([tag.name for tag in obj.tags.all()])

        display_tags.short_description = _('Tags')

        def display_diet(self, obj):
            return ", ".join([diet.name for diet in obj.diet.all()])

        display_diet.short_description = _('Diet')

.. code-block:: python

    from django.conf import settings
    from django.contrib import admin
    from django.utils.timezone import now
    from django.utils.translation import ugettext_lazy as _
    from habitat._common.admin import HabitatAdmin
    from habitat._common.admin import HabitatTabularInline
    from habitat.communication.models import Email
    from habitat.communication.models import Attachment


    class InboxFilter(admin.SimpleListFilter):
        # Human-readable title which will be displayed in the
        # right admin sidebar just above the filter options.
        title = _('Show')

        # Parameter for the filter that will be used in the URL query.
        parameter_name = 'inbox'

        def lookups(self, request, model_admin):
            return [
                ('received', _('Received')),
                ('sent', _('Sent')),
            ]

        def queryset(self, request, queryset):
            if self.value() == 'sent':
                return queryset.filter(sender=request.user)

            if self.value() == 'received':
                return queryset.exclude(sender=request.user)


    class AttachmentInline(HabitatTabularInline):
        model = Attachment
        extra = 3
        readonly_fields = []

        def get_readonly_fields(self, request, obj=None):
            if obj:
                self.can_delete = False
                self.max_num = 0
                self.min_num = 0
                self.extra = 0
                return self.readonly_fields + ['file']
            else:
                return self.readonly_fields


    @admin.register(Email)
    class EmailAdmin(HabitatAdmin):
        actions = None
        list_display = ['date', 'time', 'sender', 'subject']
        list_filter = [InboxFilter, 'to']
        list_display_links = ['subject']
        search_fields = ['sender__username', 'to__username', 'subject', 'body']
        ordering = ['-modified']
        exclude = ['sender', 'date', 'time']
        raw_id_fields = ['to']
        autocomplete_lookup_fields = {'m2m': ['to']}
        readonly_fields = ['id']
        inlines = [AttachmentInline]

        def change_view(self, request, object_id, form_url='', extra_context=None):
            extra_context = extra_context or {}
            extra_context['readonly'] = True
            extra_context['show_save_and_add_another'] = False
            extra_context['show_save_and_continue'] = False
            extra_context['show_save'] = False
            extra_context['show_delete_link'] = False
            return super().change_view(request, object_id, form_url, extra_context)

        def get_readonly_fields(self, request, obj=None):
            if obj:
                return self.readonly_fields + ['sender', 'to', 'subject', 'body']
            else:
                return self.readonly_fields

        def get_queryset(self, request):
            queryset = super().get_queryset(request)

            if request.user.is_superuser:
                return queryset

            delay = now() - settings.HABITATOS['DELAY']
            received = queryset.filter(to=request.user, modified__lt=delay)
            sent = queryset.filter(sender=request.user)
            result = sent | received
            return result.distinct()

        def save_model(self, request, obj, form, change):
            if not change:
                obj.sender = request.user
            return super().save_model(request, obj, form, change)

        class Media:
            js = [
                'communication/js/email-reply-button.js',
                'communication/js/email-hide-save.js',
            ]
            css = {'all': [
                'communication/css/hide-id-field.css',
                'communication/css/resize-fields.css',
            ]}



Grapelli
========
.. code-block:: python

    GRAPPELLI_SWITCH_USER = True
    GRAPPELLI_ADMIN_TITLE = _('HabitatOS')
    GRAPPELLI_INDEX_DASHBOARD = 'habitat.dashboard.icares1.AdminDashboard'
    GRAPPELLI_AUTOCOMPLETE_SEARCH_FIELDS = {
        'auth': {
            'user': ['username__icontains']
        }
    }

