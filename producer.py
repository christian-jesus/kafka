from kafka import KafkaProducer

def main():
    # Configurar el productor de Kafka
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    
    # Enviar un mensaje al tema "hola-mundo"
    producer.send('hola-mundo', b'Hola, Kafka con Python!')
    
    # Confirmar que todos los mensajes se envíen
    producer.flush()
    producer.close()
    print("Mensaje enviado a Kafka.")

if __name__ == "__main__":
    main()
