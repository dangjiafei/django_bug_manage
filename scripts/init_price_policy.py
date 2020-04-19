#!/usr/bin/env python
# -*- coding:utf-8 -*-
from scripts import base
from web import models


def run():
    exists = models.PricePolicy.objects.filter(category=1, title="个人免费版").exists()
    if not exists:
        models.PricePolicy.objects.create(
            category=1,  # 收费类型
            title="个人免费版",
            price=0,  # 价格
            project_num=3,  # 可以创建的项目数量
            project_member=2,  # 项目的最多人数
            project_space=20,  # 项目的空间为20M
            per_file_size=5  # 单个文件上传最大为5M
        )


if __name__ == '__main__':
    run()
