#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Fibonacci.settings")
    try:
        from django.core.management import execute_from_command_line
    except Exception, e:
        print e
    execute_from_command_line(sys.argv)
