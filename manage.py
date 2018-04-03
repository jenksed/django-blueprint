#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys

if __name__ == '__main__':
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            'Failed to import Django modules. Are you sure it is actually '
            'installed and available on your PYTHONPATH? Maybe you simply '
            'forgot to activate your virtual environment?'            
        ) from exc
    execute_from_command_line(sys.argv)
    