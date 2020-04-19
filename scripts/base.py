#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
import django

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_bug_manage.settings")
django.setup()  # os.environ['DJANGO_SETTINGS_MODULE']
