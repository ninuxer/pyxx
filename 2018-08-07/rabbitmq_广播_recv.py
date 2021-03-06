# Author： ninuxer
# Date： 2018/08/07 9:58
# File： rabbitmq_1对1_recv.py

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.200.11.110'))
channel = connection.channel()

# make message persistent
# 消费者这边也需要申明一个队列，因为我们不知道发送者和消费者谁先启动，如果后启动的发现声明的队列已存在，不会生成新的队列
channel.queue_declare(queue='hello', durable=True)


def callback(ch, method, properties, body):
    print(" [消费者] 收到消息 %r" % body)
    import time
    time.sleep(10)     # 模拟处理消息的过程
    print(' [消费者] {} 此条消息处理完成'.format(body))
    ch.basic_ack(delivery_tag=method.delivery_tag)  # 发送处理完成的确认


channel.basic_qos(prefetch_count=1)  # 增加此设定

channel.basic_consume(callback,   # 表示收到消息后的回调函数，也就是处理消息的函数
                      queue='hello',  # 表示从哪个队列接受消息
                      no_ack=False)   # no-ack表示消费者接收到并处理完消息后，是否不要向生产者发生确认消息

print(' [消费者] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()   # 此处才是真正开始执行,相当于启动了一个死循环，一直处于监听状态
