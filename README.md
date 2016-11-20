# flotilla_easy
A simpler python library for use with Pimoroni's Flotilla system (https://shop.pimoroni.com/products/flotilla-mega-treasure-chest). Aimed at kids. 

This library builds on the work of Pimoroni in their flotilla-python library (https://github.com/pimoroni/flotilla-python), but wraps up a lot of the setup and other stuff into easy functions so that you can get started with Flotilla with just one line of code.

At the moment it's quite simple, and deals with the bare minimum needed for teaching. Hopefully, it will improve in time to be as full-featured as the main flotilla library, but with more simplicity. 

One feature it does have is a slightly crude simulation of the modules, if you don't have a dock plugged in. This is so that you can have one Flotilla set for loads of kids, and they can each program on their own computer with the simulation and then transfer their code to a Raspberry Pi and run it on the Flotilla without changes. We tested this with a group of 12 kids, some of whom had no experience and it mostly worked great. 

To get started, just put 'import flotilla_easy' at the top of your code. Then use one of the commands below. 

#Using the different output modules:
 -To run the motor, use 'motor(speed)' where speed is an integer between -63 and 63
 -To turn on a pixel in the matrix, use 'matrix(x, y, state)' where x and y are integers from 0 to 7 and state is True or False
 -To show a number on the number module, use 'number(x)' where x is an integer from 0 to 9999
 
 
#Using the different input modules:
 -To use the light sensor, use 'light()' - which returns the light level in lux
 -To use the colour sensor, use 'colour()' - which returns the colour level as (red, green, blue, all)
 -To use the slider or dial, use slider() or dial() - which return integers between 0 and 1023
 -To use the touch sensor, use touch(x) where x is an either 1, 2, 3, or 4 depending on which sensor you want to check. Returns True or False depending if the sensor is being touched
 -To use the joystick, use 'joystick(what)' where what is either 'x', 'y', or 'button' depending on what you want to sense. Returns an integer from 0 to 1023 for the x and y, and a True or False for the button.
 -To use the weather moudle, use 'weather(what)' where what is either 'temp' or 'press' for temperature or pressure. Temp is in C, pressure in hPa. 
 -To use the motion module, use 'motion(what)' where what is either 'x' 'y' or 'z'
 
 
This is far from finished - it was knocked up hours before I was due to teach a workshop - but it's a start, and I will improve it. 

Planned improvements are:
 -Adding support for the rainbow module (we only just got one)
 -Adding a clear_matrix() function
 -Adding commands to set the decimal points and the colon on the number module
 -Adding support for multiple modules (especially motor and light)


It needs the prettytable module, which is a bit of a pain to install on everyone's laptops if you are running a workshop. This code isn't properly wrapped into a library with all the bits, so to quickly solve this I just stuck everything in a folder and got the kids to put their code in there. It all worked fine!
