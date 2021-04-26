from kafka import KafkaConsumer


consumer = KafkaConsumer('virtual-mind')
for msg in consumer:
     print (msg.value.decode("utf-8"))