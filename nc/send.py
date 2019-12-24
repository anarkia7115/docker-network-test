import os
import time

def main():
    port = 3123
    msg_num = 10
    print("sending {} messages".format(msg_num))
    for i in range(msg_num):
        send(i, port)
        time.sleep(1)

def send(msg, port):
    print("sending {} to {}".format(msg, port))
    os.system("echo {} | nc 172.17.0.1 {}".format(msg, port))

main()
