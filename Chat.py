import paho.mqtt.client as mqtt
import time

# --- CONFIGURACIÓN ---
BROKER = "broker.hivemq.com"
TOPIC = "facultad/proyecto/isra" # <--- Este debe ser igual en el HTML

# Esta función se activa cuando llega un mensaje
def al_recibir_mensaje(client, userdata, message):
    mensaje_texto = message.payload.decode()
    print(f"\n[Mensaje recibido]: {mensaje_texto}")
    print("> ", end="") # Para que no se borre el prompt al recibir mensaje

# Configuración del cliente
cliente = mqtt.Client()
cliente.on_message = al_recibir_mensaje

try:
    print("Conectando al servidor de mensajería...")
    cliente.connect(BROKER, 1883)
    
    # Nos suscribimos al canal para leer lo que enviamos
    cliente.subscribe(TOPIC)
    
    # Iniciar el hilo para escuchar mensajes en segundo plano
    cliente.loop_start()
    
    print(f"--- Chat Activo en: {TOPIC} ---")
    print("Escribe tus mensajes abajo. (Presiona Ctrl+C para salir)")

    while True:
        msj = input("> ")
        if msj:
            cliente.publish(TOPIC, msj)
            
except KeyboardInterrupt:
    print("\nSaliendo del chat...")
finally:
    cliente.loop_stop()
    cliente.disconnect()