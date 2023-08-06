import ssl
import socket


destinations={'Chennai': 750,'Hyderabad':1599,'Pondicherry': 740}


HOST = 'localhost'
PORT = 12345


context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile='localhost.crt', keyfile='localhost.key')


with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
   
    sock.bind((HOST, PORT))

    
    sock.listen()

    while True:
        
        conn, addr = sock.accept()

        with context.wrap_socket(conn, server_side=True) as sconn:
            
            data = sconn.recv(1024)

            if data == b'BookTicket':
                
                


                #Number of Tickets
                destination=sconn.recv(1024).decode()
                
                price=destinations[destination]
                num_tickets = int(sconn.recv(1024).decode())
                with open("ticket_info.txt", "r") as f:
                    for line in f:
                        place, tickets = line.strip().split(",")
                        if(place==destination):
                            tickets = int(tickets)
                            if(tickets<=0):
                                sconn.close()
                                break
                            else:
                                tickets=tickets-num_tickets
                total_price=price*num_tickets

                

                with open("ticket_info.txt", "r") as f:
                    lines = f.readlines()
                
                with open("ticket_info.txt", "w") as f:
                    for line in lines:
                        place, n_tickets = line.strip().split(",")
                        n_tickets=int(n_tickets)
                        if place == destination:
                            n_tickets = n_tickets-num_tickets
                        f.write(f"{place},{n_tickets}\n")
   
               
                sconn.sendall(f'The total price is {total_price}'.encode())

            elif data == b'Close':
                
                sconn.close()
                break