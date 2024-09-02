from kafka import KafkaConsumer

def main():
    # Configurar el consumidor de Kafka
    consumer = KafkaConsumer(
        'hola-mundo',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        group_id='grupo-hola-mundo',
        enable_auto_commit=True
    )
    
    # Leer mensajes de Kafka
    for message in consumer:
        print(f"Recibido mensaje: {message.value.decode('utf-8')}")

if __name__ == "__main__":
    main()
