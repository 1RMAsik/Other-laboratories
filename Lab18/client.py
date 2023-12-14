import socket
import threading
from tkinter import *
from tkinter import scrolledtext

def connect_to_server():
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((address_entry.get(), int(port_entry.get())))

    client_status.insert(END, "Connected to server\n")

def disconnect_from_server():
    global client_socket
    client_socket.close()

    client_status.insert(END, "Disconnected from server\n")

def send_to_server():
    global client_socket
    client_socket.send(message_entry.get().encode())

    # Получите ответ от сервера
    response = client_socket.recv(1024).decode()

    client_status.insert(END, f"Sent: {message_entry.get()}\nReceived: {response}\n")

root = Tk()
root.title("Nikita Samoilov 9PZ-56 Client")
address_label = Label(root, text="Address")
address_entry = Entry(root)
port_label = Label(root, text="Port")
port_entry = Entry(root)
connect_button = Button(root, text="Connect", command=lambda: threading.Thread(target=connect_to_server).start())
disconnect_button = Button(root, text="Disconnect", command=disconnect_from_server)
message_label = Label(root, text="Message")
message_entry = Entry(root)
send_button = Button(root, text="Send", command=send_to_server)
client_status = scrolledtext.ScrolledText(root)

address_label.pack()
address_entry.pack()
port_label.pack()
port_entry.pack()
connect_button.pack()
disconnect_button.pack()
message_label.pack()
message_entry.pack()
send_button.pack()
client_status.pack()

root.mainloop()
