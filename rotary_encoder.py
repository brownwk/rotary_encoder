from machine import PIN

DATA 7
CLOCK 2

def setup() 
  clk_in = Pin(CLOCK, Pin.IN, Pin.PULL_DOWN)
  data_in = Pin(DATA, Pin.IN, Pin.PULL_DOWN)


prevNextCode = 0;
store=0;

void loop() {
c,val = 0
  if( val=read_rotary() ) 
      c +=val
      if ( prevNextCode==0x0b) 
         print("eleven ")
         print("{} {}".format(store))
      

      if (prevNextCode==0x07) 
         print("seven ")
         print(store)

def read_rotary() 
  rot_enc_table = [0,1,1,0,1,0,0,1,1,0,0,1,0,1,1,0]
  prevNextCode <<= 2
  if (digitalRead(DATA))
    prevNextCode |= 0x02
  if (digitalRead(CLK))
    prevNextCode |= 0x01
  prevNextCode &= 0x0f
  if  (rot_enc_table[prevNextCode] ) 
    store <<= 4
    store |= prevNextCode;
    if ((store&0xff)==0x2b)
      return -1
    if ((store&0xff)==0x17)
      return 1
  return 0
