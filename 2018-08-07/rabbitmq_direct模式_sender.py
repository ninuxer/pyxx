# Author： ninuxer
# Date： 2018/08/07 9:58
# File： rabbitmq_广播_sender.py


import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.200.11.110'))
channel = connection.channel()

# make message persistent
# 声明了一个名为logs，类型为fanout的 exchange
# durable参数可以保证当mq服务挂了后，当mq恢复后，队列还在，但不保证队列里面的消息还在
channel.exchange_declare(exchange='logs', exchange_type='fanout', durable=True)

send_content = 'Hello World, [{}]'.format(time.ctime())

channel.basic_publish(exchange='logs',   # 表示消息发布到logs这个exchange上
                      routing_key='',   # 由于exchange为fanout广播类型，因此无需绑定对应的queue，因为所有的queue都能收到消息
                      body=send_content,   # 发送的内容
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent，此参数就可以保证mq挂了后，队列里面的消息还在
                      ))
print(" [发送者] 发送 {}".format(send_content))
connection.close()
