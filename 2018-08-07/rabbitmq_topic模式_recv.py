# Author： ninuxer
# Date： 2018/08/07 9:58
# File： rabbitmq_direct模式_recv.py

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.200.11.110'))
channel = connection.channel()

# make message persistent
# 消费者这边也需要申明一个exchange，因为我们不知道发送者和消费者谁先启动，如果后启动的发现声明的exchange已存在，不会生成新的exchange
channel.exchange_declare(exchange='direct_logs', exchange_type='direct', durable=True)

result = channel.queue_declare(exclusive=True)   # 相当于为每个消费者，生产了一个唯一的queue
queue_name = result.method.queue

import sys
bound_key_list = sys.argv[1:]   # 运行消费者程序时，后面跟上绑定的关键字信息，要与发送者定义的关键字信息匹配，消费者可以绑定多个关键字
if not bound_key_list:
    sys.stderr.write("Usage: %s [debug] [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

for bound_key in bound_key_list:
    channel.queue_bind(exchange='direct_logs',
                       queue=queue_name,
                       routing_key=bound_key)   # 将上述生成的唯一的队列，绑定到名为'logs'的exchange,绑定的关键字为运行时传入的参数


def callback(ch, method, properties, body):
    print(" [消费者] 收到消息 %r" % body)
    import time
    time.sleep(10)     # 模拟处理消息的过程
    print(' [消费者] {} 此条消息处理完成'.format(body))
    ch.basic_ack(delivery_tag=method.delivery_tag)  # 发送处理完成的确认


channel.basic_qos(prefetch_count=1)  # 增加此设定

channel.basic_consume(callback,   # 表示收到消息后的回调函数，也就是处理消息的函数
                      queue=queue_name,  # 表示从哪个队列接受消息
                      no_ack=False)   # no-ack表示消费者接收到并处理完消息后，是否不要向生产者发生确认消息

print(' [消费者] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()   # 此处才是真正开始执行,相当于启动了一个死循环，一直处于监听状态
