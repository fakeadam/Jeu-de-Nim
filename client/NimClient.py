import socket
import threading
import os
from dotenv import load_dotenv

def getAnswers(socket):
    while True:
        try:
            reponse = socket.recv(1024).decode('utf-8')
            print(reponse)
        except Exception as e:
            print(f"Erreur lors de la réception de la réponse : {e}")
            break

def sendCommand(socket, commande):
    socket.send(commande.encode('utf-8'))

def openSession():
    """
    Ouvre une session avec le serveur.
    """
    load_dotenv()
    server_ip = os.getenv("SERVER_IP")
    # Connexion au serveur
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, 5555))

    # Lancement du thread pour recevoir les réponses du serveur en arrière-plan
    thread_reception = threading.Thread(target=getAnswers, args=(client_socket,))
    thread_reception.start()

    return client_socket