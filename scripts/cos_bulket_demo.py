#!/usr/bin/env python
# -*- coding:utf-8 -*-

from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client

secret_id = 'AKIDFPJSXQEk8PXVL3Tx5zf6MSL0Sf7Qoikg'  # 替换为用户的 secretId
secret_key = 'yiCWfZCXcQxJZlqncKvRu5DKHySg8sMp'  # 替换为用户的 secretKey

region = 'ap-chengdu'  # 替换为用户的 Region

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)

client = CosS3Client(config)

response = client.create_bucket(
    Bucket='test-1251317460',
    ACL="public-read"  #  private  /  public-read / public-read-write
)