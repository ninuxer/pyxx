# Author： ninuxer
# Date： 2018/05/16 15:33
# File： 多进程备份还原数据库.py
# Desc：定义同时运行备份或还原的进程个数，对指定库里面的单个表使用单独的进程备份或还原


import os
import multiprocessing
import subprocess
import time


def restore(dbHost, dbUser, dbPass, dbName, sqlFile):
    print('进程<>开始还原{}'.format(sqlFile))
    res = subprocess.Popen('mysql -u {} -p {} -h {} {} < {}'.format(dbUser, dbPass, dbHost, dbName, sqlFile),
                           shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE
                           )

    info = '[{}] Restore {} Success; stdout 为: {}'.format(time.strftime('%F_%T'),sqlFile,str(res.stdout.read(), 'utf8'))
    err = '[{}] {} ; stdout 为: {}'.format(time.strftime('%F_%T'),sqlFile,str(res.stderr.read(), 'utf8'))

    with open('restoreOut.log', 'a') as f1:
        f1.write(info)

    with open('restoreError.log', 'a') as f2:
        f2.write(err)


if __name__ == '__main__':

    # backDbName = 'ifc'
    restoreDbName = 'ifc_restore_test_{}'.format(time.strftime('%Y%m%d'))
    dbUser = 'root'
    dbPass = '123456'
    dbHost = '127.0.0.1'
    # dbPort = '3306'
    # backSqlDir = './{}_bak'.format(time.strftime('%F'))
    restoreSqlDir = './ifc'

    create_database = r'mysql -u{} -p{} -h{} -e "create database {} default charset \'utf8\';"'.format(dbUser, dbPass, dbHost, restoreDbName)
    print('建库语句为：{}'.format(create_database))
    ret = subprocess.Popen(create_database, shell=True, stderr=subprocess.PIPE)
    print(str(ret.stderr.read(),'utf8'))

    p = multiprocessing.Pool(8)
    for i in os.listdir(restoreSqlDir):
        full_path = os.path.join(restoreSqlDir,i)
        p.apply_async(func=restore, args=(dbHost, dbUser, dbPass, restoreDbName, full_path))

    p.close()
    p.join()
