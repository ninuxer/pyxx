# Author： ninuxer
# Date： 2018/05/18 11:05
# File： 多进程--备份数据库.py

# !/usr/local/python3/bin/python3

import os
import time
import multiprocessing
import subprocess
import pymysql


def bak_table(host, user, pwd, db, tb, sql_file, log_file):
    cmd = 'mysqldump -u{} -p\"{}\" -h\"{}\" --opt --default-character-set=utf8 ' \
          '--extended-insert=FALSE -R -E -t {} {} > {}'.format(user, pwd, host, db, tb, sql_file)

    # print(cmd)

    ret = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE)
    error_info = '[ERROR]:[{}] tb: {} >> {}'.format(time.ctime(), tb, str(ret.stderr.read(), 'utf8'))
    with open(log_file, 'a') as f:
        f.write(error_info)
    # return [tb, sql_file, 0]  # 0代表备份失败，1代表备份成功
    return [tb, sql_file, 1]


def big_table_split(s):
    split_path = os.path.join(os.path.dirname(os.path.dirname(s[1])), 'split', s[0])
    os.makedirs(split_path)
    split_lines = 500000
    cmd = 'split -a 10 -d -l {} {} {}/{}.'.format(split_lines, s[1], split_path, s[0])
    ret = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE)
    split_log = os.path.join(os.path.dirname(os.path.dirname(s[1])), 'logs', 'split.log')
    error_info = '[ERROR]:[{}] sql_file: {} >> {}'.format(time.ctime(), s[1], str(ret.stderr.read(), 'utf8'))
    with open(split_log, 'a') as f:
        f.write(error_info)


def show_tables(host, user, pwd, db):
    conn = pymysql.connect(host=host, user=user, password=pwd, db=db)
    cur = conn.cursor()

    sql = 'show tables from {}'.format(db)
    cur.execute(sql)
    res = cur.fetchall()
    table_list = [x[0] for x in res]
    # print(res)
    # print(type(res))
    conn.close()
    return table_list


def bak_struct(host, user, pwd, db, tb, struct_file, log_file):
    cmd = 'mysqldump -u{} -p\"{}\" -h\"{}\" --opt --default-character-set=utf8 ' \
          '-d {} {} > {}'.format(user, pwd, host, db, tb, struct_file)

    # print(cmd)

    ret = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE)
    error_info = '[ERROR]:[{}] tb: {} >> {}'.format(time.ctime(), tb, str(ret.stderr.read(), 'utf8'))
    with open(log_file, 'a') as f:
        f.write(error_info)


if __name__ == '__main__':
    print('==== [{}] Start Backup And Split ===='.format(time.ctime()))
    dbName = 'ifc'
    # dbName = 'ifc_restore_test_20180518'
    dbUser = 'root'
    dbPass = 'R3GXiAbIi0'
    # dbPass = '1q2w3e,./'
    dbHost = 'localhost'

    bak_dir = os.path.join(os.path.dirname(__file__), 'bak_{}'.format(time.strftime('%F_%H')))
    log_dir = os.path.join(bak_dir, 'logs')
    sql_dir = os.path.join(bak_dir, 'sqls')
    struct_dir = os.path.join(bak_dir, 'struct')
    os.makedirs(bak_dir)
    os.makedirs(log_dir)
    os.makedirs(sql_dir)
    os.makedirs(struct_dir)

    bak_log_file = os.path.join(log_dir, 'dbbak.log')
    struct_log_file = os.path.join(log_dir, 'struct.log')

    # print(bak_log_file)

    tb_list = show_tables(dbHost, dbUser, dbPass, dbName)
    for i in tb_list:
        structFile = os.path.join(struct_dir, '{}.sql'.format(i))
        bak_struct(dbHost, dbUser, dbPass, dbName, i, structFile, struct_log_file)

    # print(tb_list)

    p = multiprocessing.Pool(8)

    # print(p)

    for tbName in tb_list:
        # print(tbName)
        sqlFile = os.path.join(sql_dir, '{}.sql'.format(tbName))
        # print(sqlFile)
        p.apply_async(
            func=bak_table,
            args=(dbHost, dbUser, dbPass, dbName, tbName, sqlFile, bak_log_file),
            callback=big_table_split)

    p.close()
    p.join()
    print('==== [{}] Stop Backup And Split ===='.format(time.ctime()))







