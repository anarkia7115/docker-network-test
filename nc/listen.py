import os

def main():
    port = 3123

    while True:
        listen_on_port(port)

def listen_on_port(port):
    os.system("nc -lp {}".format(port))

main()
    
