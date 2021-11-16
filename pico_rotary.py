from machine import Pin
from time import sleep

def detect(up_val,down_val):
    global clock
    global data
    while ( (nr := clock.value() << 1 | data.value()) not in(up_val,down_val)):
      pass
    if nr == up_val:
       return("1")
    return("-1")

clk = 17
dta = 18
data = Pin(dta, Pin.IN, Pin.PULL_UP) # USE PULL_DOWN if pot has voltage pin
clock = Pin(clk, Pin.IN, Pin.PULL_UP) # As above...

while True:
  pr = clock.value() << 1 | data.value()
  if(pr == 3):
    print(detect(2,1))
  elif(pr == 2):
    print(detect(0,3))
  elif(pr==0):
    print(detect(1,2))
  elif(pr==1):
    print(detect(3,0) )
  sleep(0.1)
