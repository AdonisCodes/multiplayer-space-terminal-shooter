import socket
import threading
import keyboard

grid = [[' ' for _ in range(100)] for _ in range(100)]
def draw_file_pos(x, y, symbol):
    grid[y][x] = symbol
    with open(self_player+'.txt', 'w') as f:
        for row in grid:
            f.write(''.join(row) + '\n')

def send_message(sock, addr):
    while True:
        inpt = keyboard.read_event()
        if self_player not in inpt.device:
            print('other player')
            continue

        match inpt.name.strip():
            case "l":
                self_pos[0] -= 1
            case "r":
                self_pos[0] += 1
            case "u":
                self_pos[1] -= 1
            case "d":
                self_pos[1] += 1
        message = ",".join([str(i) for i in self_pos])
        draw_file_pos(self_pos[0], self_pos[1], 'x')
        sock.sendto(message.encode(), addr)

self_pos = [0, 0]
self_player = input("Enter your player name: ")
other_pos = [0, 0]

def receive_message(sock):
    while True:
        message, addr = sock.recvfrom(1024)
        x, y = message.decode().split(',')
        other_pos[0], other_pos[1] = int(x), int(y)
        draw_file_pos(other_pos[0], other_pos[1], 'o')
        print(other_pos)

def main():
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Get own IP address
    own_ip = socket.gethostbyname(socket.gethostname())
    own_port = int(input("Port: "))
    
    # Bind the socket to own IP and port
    sock.bind((own_ip, own_port))
    
    print(f"Your IP address: {own_ip}")
    print("Waiting for another player to connect...")
    
    # Get peer's IP address and port
    peer_ip = input("Enter peer's IP address: ")
    peer_port = int(input("Port: "))
    
    # Start sending and receiving messages in separate threads
    send_thread = threading.Thread(target=send_message, args=(sock, (peer_ip, peer_port)))
    recv_thread = threading.Thread(target=receive_message, args=(sock,))
    
    send_thread.start()
    recv_thread.start()
    
    # Wait for threads to finish
    send_thread.join()
    recv_thread.join()

# Run the main function
if __name__ == "__main__":
    main()

