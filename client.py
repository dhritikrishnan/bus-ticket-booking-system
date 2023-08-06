import streamlit as st
import ssl
import socket

destinations=['Chennai','Hyderabad','Pondicherry']


context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.load_verify_locations('localhost.crt')


HOST = 'localhost'
PORT = 12345


def app():
    st.title('Bus Ticket Booking System')

  
    b_name = st.text_input('Enter name to book under:')

    
    email = st.text_input('Enter your email id:')

    
    destination = st.selectbox('Select your destination:', destinations)

    
    num_tickets = st.number_input('Enter the number of tickets to book (maximum 10):', min_value=1, max_value=10)



    passenger_names = st.text_input('Enter the names of the passengers (comma-separated):')
    names = passenger_names.split(',')

   
   
    if st.button('Book tickets'):
        input_client = [destination, str(num_tickets)]

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
            with context.wrap_socket(sock, server_hostname=HOST) as ssock:
                ssock.connect((HOST, PORT))
                ssock.sendall(b'BookTicket')
                
                ssock.sendall(destination.encode())
                ssock.sendall(str(num_tickets).encode())
                data = ssock.recv(1024)
                st.write("Ticket Details")
                st.write("Name: ",b_name)
                st.write("Email: ",email)
                st.write("Number of Tickets: ",num_tickets)
                st.write(f'Tickets booked for {", ".join(names)}.')
                st.write(data.decode())
                
                
                ssock.sendall(b'Close')


if __name__ == '__main__':
    app()
