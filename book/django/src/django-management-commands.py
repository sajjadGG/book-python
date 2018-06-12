from django.core.management.base import BaseCommand, CommandError
from polls.models import Question as Poll


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('poll_id', nargs='+', type=int)
        parser.add_argument(
            '--delete',
            action='store_true',
            dest='delete',
            help='Delete poll instead of closing it',
        )

    def handle(self, *args, **options):

        for poll_id in options['poll_id']:
            try:
                poll = Poll.objects.get(pk=poll_id)
            except Poll.DoesNotExist:
                raise CommandError('Poll "%s" does not exist' % poll_id)

            if options['delete']:
                return self.delete_poll(poll)
            else:
                return self.close_poll(poll)

    def close_poll(self, poll):
        poll.opened = False
        poll.save()
        self.stdout.write(self.style.SUCCESS('Successfully closed poll "{poll.pk}"'))

    def delete_poll(self, poll):
        poll.delete()