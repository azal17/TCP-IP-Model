import random
import time

def send_frame(T_p,i):
  print(f"I am being sent the {i}th time")
  time.sleep(2*T_p)
  print(f"Not Sent! continue")
def Aloha():
  k_max = 4
  k = 0
  T_p = 1

  while k<=k_max:
        if k == 0:
           print(k)
           send_frame(T_p,k)
        else:
            R = random.randint(0,(2**k)-1)
            time.sleep(R*T_p)
            print(k)
            send_frame(T_p,k)
        k+=1

  print("Abort")

Aloha()