from RPi import GPIO
from time import sleep

def detect(up_val,down_val):
    while ( (nr := GPIO.input(clk) << 1 | GPIO.input(dta)) not in(up_val,down_vaa
l)):
      pass
    if nr == up_val:
       return("Up")
    return("down")

clk = 17
dta = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dta, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
old_result = 0
while True:
  pr = GPIO.input(clk) << 1 | GPIO.input(dta)
  if(pr == 3):
    print(detect(2,1))
  elif(pr == 2):
    print(detect(0,3))
  elif(pr==0):
    print(detect(1,2))
  elif(pr==1):
    print(detect(3,0) )
  sleep(0.1)
