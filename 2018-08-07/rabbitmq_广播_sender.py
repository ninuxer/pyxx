# Author： ninuxer
# Date： 2018/08/07 9:58
# File： rabbitmq_1对1_sender.py


import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.200.11.110'))
channel = connection.channel()

# make message persistent
# durable参数可以保证当mq服务挂了后，当mq恢复后，队列还在，但不保证队列里面的消息还在
# queue参数表示声明一个队列，队列名为hello
channel.queue_declare(queue='hello', durable=True)

send_content = 'Hello World, [{}]'.format(time.ctime())

channel.basic_publish(exchange='',
                      routing_key='hello',   # 表示发布到hello这个队列
                      body=send_content,   # 发送的内容
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent，此参数就可以保证mq挂了后，队列里面的消息还在
                      ))
print(" [发送者] 发送 {}".format(send_content))
connection.close()
