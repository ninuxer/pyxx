# Author： ninuxer
# Date： 2018/04/19 9:46
# File： logging_configparser实践.py


### 需求：
# 定时application.ini配置文件，文件中有对应的[log]配置段，该配置段内有
# 日志级别、日志存储文件、单独记录到文件或输出到屏幕的限定

# logging通过读取application.ini文件的配置，提供提供接口给外部，外部只需调用如：log.debug|info|warning|critical方式进行记录即可


import configparser, logging


# 生产config文件

def create_cfg(level='warning', configfile='application.ini', mode='file', logfile='mytest.log'):
    config = configparser.ConfigParser()

    config['DEFAULT'] = {
        'logLevel': 'warning',
        'logFile': 'mytest.log',
        'logOut': 'file'
    }

    config['LOG'] = {
        'logLevel': level,
        'logFile': logfile,
        'logOut': mode
    }

    with open(configfile, 'w') as f:
        config.write(f)


def modify_cfg(k, v, configfile='application.ini'):
    config = configparser.ConfigParser()

    config.read(configfile)

    if k in config['LOG']:
        config.set('LOG', k, v)
        config.write(open(configfile, 'w'))
        print('{} is {} now!'.format(k, config.get('LOG', k)))
        return config.get('LOG', k)
    else:
        print('{} is not in {}'.format(k, config['LOG']))


def read_cfg(k, configfile='application.ini'):
    config = configparser.ConfigParser()
    config.read(configfile)

    if k in config['LOG']:
        v = config.get('LOG', k)
        return v
    else:
        print('{} is not in {}'.format(k, config['LOG']))


def log():
    logger = logging.getLogger()

    level = read_cfg('loglevel').upper()
    flevel = 'logging.'+level
    logger.setLevel(eval(flevel))  # 因为flevel返回的是字符串，此处我们要让字符串指代类似命令的方式，因此要用eval

    formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')

    mode = read_cfg('logout')
    if mode == 'file':
        fh = logging.FileHandler(read_cfg('logfile'))
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    elif mode == 'stdout':
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        logger.addHandler(ch)
    else:
        fh = logging.FileHandler(read_cfg('logfile'))
        ch = logging.StreamHandler()

        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(ch)

    return logger


modify_cfg('logout', 'all')
mylog = log()
mylog.error("##### This is my test ERROR log")




