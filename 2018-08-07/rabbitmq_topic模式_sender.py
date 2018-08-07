# Author： ninuxer
# Date： 2018/08/07 9:58
# File： rabbitmq_direct模式_sender.py


import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.200.11.110'))
channel = connection.channel()

# make message persistent
# 声明了一个名为logs，类型为direct的 exchange
# durable参数可以保证当mq服务挂了后，当mq恢复后，队列还在，但不保证队列里面的消息还在
channel.exchange_declare(exchange='direct_logs', exchange_type='direct', durable=True)

import random  # 随机选取一个名称，作为发送方发送时绑定的queue的条件
level = ['debug', 'info', 'warning', 'error']
bound_key = random.choice(level)

send_content = '[{}] Hello World, [{}]'.format(bound_key, time.ctime())

channel.basic_publish(exchange='direct_logs',   # 表示消息发布到logs这个exchange上
                      routing_key=bound_key,  # 发送消息时，exchange发送到queue时的选择条件,
                                              # 也就是只有当消费者queue绑定了此关键字后，才能收到消息
                      body=send_content,   # 发送的内容
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent，此参数就可以保证mq挂了后，队列里面的消息还在
                      ))
print(" [发送者] 发送 {}".format(send_content))
connection.close()
