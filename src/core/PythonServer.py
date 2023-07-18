import socket




# Define the server's host and port

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)

PORT = 65432        # Port to listen on (non-privileged ports are > 1023)




def print_hello_world():

    print('Hello, World!')




# Create a new socket using the AF_INET address family (Internet) and SOCK_STREAM socket type (TCP)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # Bind the socket to the address and port

    s.bind((HOST, PORT))




    # Start listening for connections

    s.listen()




    print(f'Server started at {HOST}:{PORT}. Waiting for connection...')




    # Accept a connection

    while True:

        conn, addr = s.accept()




        with conn:

            print('Connected by', addr)




            while True:

                # Receive the command

                data = conn.recv(1024)




                if not data:

                    break




                # Here we ignore the received command and simply run our function

                print_hello_world()
                