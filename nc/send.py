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

    os.system("echo {msg}|nc -q 1 {host} {port}".format(msg=msg, host="listen", port=port))

main()
