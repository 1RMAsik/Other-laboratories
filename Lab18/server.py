import socket
import threading
from tkinter import *
from tkinter import scrolledtext

def start_server():
    global server_socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind(('localhost', int(port_entry.get())))

    server_socket.listen()

    server_status.insert(END, "Server started\n")

    while True:
        client_socket, client_address = server_socket.accept()
        server_status.insert(END, f"Client connected: {client_address}\n")

        data = client_socket.recv(1024).decode()

        command, _, params = data.partition(":")

        if command == "SEND_MESSAGE":
            response = "".join(c if i % 3 != 2 else "_" for i, c in enumerate(params))
            client_socket.send(f"MESSAGE:{response}".encode())
        elif command == "ECHO":
            client_socket.send(f"ECHO:{params}".encode())
        elif command == "DISCONNECT":
            client_socket.send("DISCONNECTED".encode())

        client_socket.close()

def stop_server():
    global server_socket
    server_socket.close()
    server_status.insert(END, "Server stopped\n")

root = Tk()

root.title("Nikita Samoilov 9PZ-56 Server")
root.geometry("400x200")

port_label = Label(root, text="Port")
port_entry = Entry(root)
start_button = Button(root, text="Start", command=lambda: threading.Thread(target=start_server).start())
stop_button = Button(root, text="Stop", command=stop_server)
server_status = scrolledtext.ScrolledText(root)

port_label.pack()
port_entry.pack()
start_button.pack()
stop_button.pack()
server_status.pack()


root.mainloop()