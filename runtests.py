import os
import sys
import django
from django.test.utils import get_runner
from django.conf import settings

def run_tests(*args):
    if not args:
        args = ['tests']

    os.environ['DJANGO_SETTINGS_MODULE'] = 'app.conf.settings'
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner()

    failures = test_runner.run_tests(args)
    sys.exit(bool(failures))


if __name__ == '__main__':
    run_tests(*sys.argv[1:])

