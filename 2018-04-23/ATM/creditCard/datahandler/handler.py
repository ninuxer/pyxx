# Author： ninuxer
# Date： 2018/04/25 10:42
# File： handler.py

import os, json
from conf import settings


def handle_file(sfzid, type):
    filepath = os.path.join(settings.IF_FILE.get('FILE_PATH'), sfzid)
    if type == 'get':
        if os.path.isfile(filepath):
            with open(filepath, 'r') as f:
                info = json.load(f)
                return info
        else:
            print('{} 尚未注册'.format(sfzid))
            return filepath
    else:
        return filepath


def handle_mysql(sfzid, type):
    pass


def main(sfzid, type):
    if settings.DATA_STORAGE_TYPE == 'file':
        ret = handle_file(sfzid,type)
        return ret
    else:
        ret = handle_mysql(sfzid,type)
        return ret
