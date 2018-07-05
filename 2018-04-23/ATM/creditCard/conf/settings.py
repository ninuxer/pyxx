# Author： ninuxer
# Date： 2018/04/23 10:36
# File： settings.py

import os, logging

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOG_ABOUT = {
    'LOG_LEVEL': logging.INFO,
    'FILE_PATH': os.path.join(BASEDIR,'logs/access.log')
}

DATA_STORAGE_TYPE = 'file'  # file or mysql

IF_FILE = {
    'FILE_PATH': os.path.join(BASEDIR,'files')
}

IF_MYSQL = {
    'HOST': 'localhost',
    'PORT': 3306,
    'USER': 'root',
    'PASSWORD': '123456'
}

TRANSACTION_TYPE = {
    # 存款
    'payback': {'action': 'plus', 'interest': 0},
    # 取款
    'withdraw': {'action': 'minus', 'interest': 0.05}
}



