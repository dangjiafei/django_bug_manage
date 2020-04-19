#!/usr/bin/env python
# -*- coding:utf-8 -*-

from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client

secret_id = 'AKIDFPJSXQEk8PXVL3Tx5zf6MSL0Sf7Qoikg'  # 替换为用户的 secretId
secret_key = 'yiCWfZCXcQxJZlqncKvRu5DKHySg8sMp'  # 替换为用户的 secretKey

region = 'ap-chengdu'  # 替换为用户的 Region

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)

client = CosS3Client(config)

# client.delete_object(
#     Bucket='wangyang-1251317460',
#     Key='p1.png'
# )


objects = {
    "Quiet": "true",
    "Object": [
        {
            "Key": "day2牛存果.py"
        },
        {
            "Key": "小米CC9e.jpg"
        }
    ]
}

client.delete_objects(
    Bucket='wangyang-1251317460',
    Delete=objects
)
