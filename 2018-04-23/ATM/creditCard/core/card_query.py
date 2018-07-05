# Author： ninuxer
# Date： 2018/04/28 15:02
# File： card_query.py


from datahandler import handler


def query(sfzid):
    info = handler.main(sfzid, 'get')
    for k,v in info.items():
        print(k,'==>',v)


