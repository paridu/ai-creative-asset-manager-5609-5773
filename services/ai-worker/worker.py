import pika
import json
import time

def process_ai_tasks(ch, method, properties, body):
    data = json.loads(body)
    asset_id = data['asset_id']
    print(f"[*] Processing Asset: {asset_id}")
    
    # SIMULATED AI PIPELINE
    # 1. Generate Embeddings (CLIP Model)
    # 2. Extract Color Palette (OpenCV)
    # 3. Object Detection / Tagging
    
    time.sleep(5) # Simulate heavy ML workload
    
    print(f"[x] Finished Processing: {asset_id}")
    # Update Vector DB and SQL DB via API
    ch.basic_ack(delivery_tag=method.delivery_tag)

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='ingestion_queue')

channel.basic_consume(queue='ingestion_queue', on_message_callback=process_ai_tasks)

print('[*] AI Worker waiting for messages. To exit press CTRL+C')
channel.start_consuming()