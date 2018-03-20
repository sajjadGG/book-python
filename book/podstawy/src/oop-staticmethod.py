from django.db import models
from django.utils.translation import ugettext_lazy as _


class Click(models.Model):
    result = models.ForeignKey(verbose_name=_('Result'), to='api_v3.Result')
    datetime = models.DateTimeField(verbose_name=_('Datetime'))
    color = models.CharField(verbose_name=_('Target'), max_length=50)
    is_valid = models.NullBooleanField(verbose_name=_('Is Valid?'), default=None)

    class Meta:
        verbose_name = _('Click')
        verbose_name_plural = _('Click')

    def __str__(self):
        return f'[{self.datetime:%Y-%m-%d %H:%M:%S.%f}] {self.color}'


class Result(models.Model):
    request_sha1 = models.CharField(verbose_name=_('HTTP Request SHA1'),
                                    max_length=40, db_index=True, unique=True)

    start_datetime = models.DateTimeField(verbose_name=_('Start datetime'))
    end_datetime = models.DateTimeField(verbose_name=_('End datetime'),
                                        db_index=True)
    location = models.CharField(verbose_name=_('Location'), max_length=50)
    email = models.EmailField(verbose_name=_('User Email'), db_index=True)
    regularity = models.PositiveSmallIntegerField(verbose_name=_('Regularity'),
                                                  help_text=_(
                                                      'Click every X seconds'))
    time_between_clicks = models.TextField(
        verbose_name=_('Time between clicks'), blank=True, null=True,
        default=None)
    results = models.NullBooleanField(verbose_name=_('Results was shown?'),
                                      blank=True, null=True, default=None)

    def __str__(self):
        return f'({self.request_sha1:.7}) [{self.start_datetime:%Y-%m-%d %H:%M}] {self.email}'

    @staticmethod
    def add(request_sha1, result, clicks):
        try:
            # TODO: Remove this temporary fix
            if 'survey_sleep' in result.keys():
                del result['survey_sleep']

            result, _ = Result.objects.get_or_create(request_sha1=request_sha1,
                                                     defaults=result)

            for click in clicks:
                Click.objects.get_or_create(result=result, **click)

            result.validate()
            result.calculate()

            Click.objects.filter(result=result).delete()
            return result

        except Exception as message:
            from backend.logger.models import HTTPRequest
            http_request = HTTPRequest.objects.get(sha1=request_sha1)
            http_request.error(message)
