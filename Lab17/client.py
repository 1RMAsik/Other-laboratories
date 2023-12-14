import socket
import tkinter as tk
from tkinter import messagebox, scrolledtext

def connect():
    global sock
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        sock.connect((host_entry.get(), int(port_entry.get())))
        messagebox.showinfo("Result", "Connection successful!")
    except Exception as e:
        messagebox.showinfo("Result", "Connection failed!")

def disconnect():
    global sock
    sock.close()
    messagebox.showinfo("Result", "Disconnected!")

def send():
    global sock
    message = message_entry.get()
    sock.sendall((message + '\n').encode())
    response = sock.recv(1024).decode()
    text_box.insert(tk.END, '> ' + message + '\n')
    text_box.insert(tk.END, '< ' + response + '\n')

root = tk.Tk()
root.title("Nikita Samoilov 9PZ-56")
root.geometry("500x500")

host_label = tk.Label(root, text="Host:")
host_label.pack()

host_entry = tk.Entry(root)
host_entry.pack()

port_label = tk.Label(root, text="Port:")
port_label.pack()

port_entry = tk.Entry(root)
port_entry.pack()

connect_button = tk.Button(root, text="Connect", command=connect)
connect_button.pack()

disconnect_button = tk.Button(root, text="Disconnect", command=disconnect)
disconnect_button.pack()

message_label = tk.Label(root, text="Message:")
message_label.pack()

message_entry = tk.Entry(root)
message_entry.pack()

send_button = tk.Button(root, text="Send", command=send)
send_button.pack()

text_box = scrolledtext.ScrolledText(root)
text_box.pack()

name_label = tk.Label(root, text="Your Name")
name_label.pack()

group_label = tk.Label(root, text="Your Group Number")
group_label.pack()

root.mainloop()