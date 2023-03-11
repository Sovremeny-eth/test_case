from kafka import KafkaProducer, KafkaConsumer
import json
import time

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n+1):
            c = a + b
            a, b = b, c
        return b


topic = 'fibonacci'

producer = KafkaProducer(bootstrap_servers=['kafka:9093'],
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))
consumer = KafkaConsumer(topic,
                         bootstrap_servers=['kafka:9093'],
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

tasks = [{'number': 10}, {'number': 100}, {'number': 56}]
for task in tasks:
    producer.send(topic, value=task)
    time.sleep(1)

producer.flush()

for message in consumer:
    val = message.value['number']
    result = fibonacci(val)
    print(f"Fibonacci({val}) -> {result}")

producer.close()
consumer.close()
