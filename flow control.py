

import time
import random


def send_frame_token(i, t):
    print(f"I am the {i} frame and I have the {t} token")

def token_passing():
    N = int(input("Enter the number of devices for token passing: "))
    i = 0
    while i < N:
        j = 0
        token = 0
        while j < N:
            if token == j:
                send_frame_token(j % N, token)
                token += 1
            j += 1
        i += 1


def send_frame_stop_and_wait(i, n):
    if i != 0:
        print(f"I am the ack of {i-1}")
    print(f"I am the {i} frame and I am sending the message")
    if i == n-1:
        print(f"I am the ack of {i}")

def resend_frame(i):
    print(f"I am the {i-1} frame and I am resending the message")

def stop_and_wait():
    N = int(input("Enter the number of devices for stop and wait: "))
    i = 0
    send_frame_stop_and_wait(i, N)
    for i in range(1, N):
        ack = random.randint(0, 1)
        if ack != 0:
            send_frame_stop_and_wait(i, N)
        else:
            print(f"ack of {i-1} frame was lost")
            time.sleep(1)
            resend_frame(i)
            send_frame_stop_and_wait(i, N)
