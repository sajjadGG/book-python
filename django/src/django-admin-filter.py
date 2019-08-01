from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class AgeFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Age')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'age'

    def lookups(self, request, model_admin):
        return [
            ('None', _('Not Specified')),
            ('0-10', _('0-10')),
            ('11-20', _('11-20')),
            ('21-30', _('21-30')),
            ('31-40', _('31-40')),
            ('41-50', _('41-50')),
            ('51-60', _('51-60')),
            ('Older', _('Older')),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'None':
            return queryset.filter(date_of_birth=None)
