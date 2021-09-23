Management Commands
===================


Rationale
---------
Custom management commands are especially useful for running standalone scripts or for scripts that are periodically executed from the UNIX crontab or from Windows scheduled tasks control panel.


Built-in
--------
.. code-block:: text

    [auth]
        changepassword
        createsuperuser

    [contenttypes]
        remove_stale_contenttypes

    [dashboard]
        customdashboard

    [django]
        check
        compilemessages
        createcachetable
        dbshell
        diffsettings
        dumpdata
        flush
        inspectdb
        loaddata
        makemessages
        makemigrations
        migrate
        sendtestemail
        shell
        showmigrations
        sqlflush
        sqlmigrate
        sqlsequencereset
        squashmigrations
        startapp
        startproject
        test
        testserver

    [sessions]
        clearsessions

    [staticfiles]
        collectstatic
        findstatic
        runserver


Structure
---------
.. code-block:: text

    app
        management
        __init__.py
            commands
            __init__.py
            my_command.py


Minimal command boilerplate code
--------------------------------
.. code-block:: python

    from django.core.management.base import BaseCommand


    class Command(BaseCommand):
        help = 'What my command does?'

        def handle(self, *args, **options):
            pass


Writing own management commands
-------------------------------
.. code-block:: python

    import csv
    from django.core.management import BaseCommand
    from contact.models import Contact


    class Command(BaseCommand):
        help = 'What my command does?'

        def add_arguments(self, parser):
            parser.add_argument('--action', dest='action', help='Action to do')
            parser.add_argument('--file', dest='file', help='Filename to parse')

        def handle(self, *args, **options):
            action = options['action']
            file = options['file']

            if action == 'parse':
                with open(file) as f:
                    header = f.readline()
                    reader = csv.DictReader(f, fieldnames=['firstname', 'lastname'])
                    for line in reader:
                        Contact.add(**line)


Call
----
.. code-block:: python

    from django.core import management
    management.call_command("syncdata")



Use Case - Cleaning data in database
------------------------------------
.. code-block:: python

    from django.core.management.base import BaseCommand
    from addressbook.models import Person


    class Command(BaseCommand):
        help = 'Clean data in database'

        def handle(self, *args, **options):
            for p in Person.objects.all():
                p.firstname = p.firstname.title()
                p.lastname = p.lastname.title()
                p.save()


Use Case - Parse file line by line
----------------------------------
.. code-block:: python

    from django.core.management.base import BaseCommand
    from addressbook.models import Person


    class Command(BaseCommand):
        help = 'Moj tekst pomocy'

        def add_arguments(self, parser):
            parser.add_argument(
                '--file',
                dest='file',
                nargs='?',
                help='Log File',
            )

            parser.add_argument(
                '--format',
                nargs='?',
                dest='format',
                help='Log File Format',
            )

        def parse_line(self, line, format):
            if format == 'text':
                return line.upper()

        def handle(self, *args, **options):
            filename = options['file']
            format = options['format']
            content = []

            with open(filename, encoding='utf-8') as file:
                for line in file:
                    line = self.parse_line(line, format)
                    content.append(line)

            print('\n'.join(content))


Use cases
---------
.. code-block:: python

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
