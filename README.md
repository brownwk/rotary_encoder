# rotary_encoder
Rotary encoder code for pi.

Works like a state engine.
For example if we read in 1,1 from the clk and dta channels we only expect to get either a 1,0 for Up/Right or a 0,1 for Down/Left.

According to https://www.best-microcontroller-projects.com/rotary-encoder.html:

For clockwise motion you can only perform the following actions:

(11 > 10), (10 > 00), (00 > 01) and (01 >11)

Similarly only the following encoder output transitions are valid for Anti-Clockwise rotation:

(01 > 00), (00 > 10), (10 > 11), and (11 > 01)

This should help with cheaper rotary encoders that tend to have a lot of bounce causing invalid readings. 
