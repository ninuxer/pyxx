# Author： ninuxer
# Date： 2018/05/21 11:42
# File： 多进程-还原数据库v2.py


import os
import multiprocessing
import subprocess
import time


def restore(dbHost, dbUser, dbPass, dbName, sqlFile):
    print('[{}] 进程<{}>开始还原{}'.format(time.ctime(), os.getpid(), sqlFile))
    res = subprocess.Popen('mysql -u{} -p\"{}\" -h{} {} < {}'.format(dbUser, dbPass, dbHost, dbName, sqlFile),
                           shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE
                           )

    info = '[{}] Restore {} Success; stdout 为: {}\n'.format(time.strftime('%F_%T'),sqlFile,str(res.stdout.read(), 'utf8'))
    err = '[{}] {} ; stderr 为: {}\n'.format(time.strftime('%F_%T'),sqlFile,str(res.stderr.read(), 'utf8'))

    with open('multi_logs/Info.log', 'a') as f1:
        f1.write(info)

    with open('multi_logs/Error.log', 'a') as f2:
        f2.write(err)


if __name__ == '__main__':

    restoreDbName = 'ifc_{}'.format(time.strftime('%Y%m%d'))
    dbUser = 'root'
    dbPass = 'R3GXiAbIi0'
    dbHost = 'localhost'
    restoreSqlDir = './ifc_db_180511/split'
    process_count = 16

    # 还原表数据
    p = multiprocessing.Pool(process_count)
    for i in os.listdir(restoreSqlDir):
        dbsqlpath = os.path.join(restoreSqlDir, i)
        for j in os.listdir(dbsqlpath):
            full_path = os.path.join(dbsqlpath, j)
            p.apply_async(func=restore, args=(dbHost, dbUser, dbPass, restoreDbName, full_path))

    p.close()
    p.join()
    print('===================ALL DONE[{}]====================='.format(time.ctime()))
