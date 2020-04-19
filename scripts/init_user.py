#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
import django

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "s25.settings")
django.setup()  # os.environ['DJANGO_SETTINGS_MODULE']

from web import models

# 往数据库添加数据：链接数据库、操作、关闭链接
models.UserInfo.objects.create(username='陈硕', email='chengshuo@live.com', mobile_phone='13838383838', password='123123')
