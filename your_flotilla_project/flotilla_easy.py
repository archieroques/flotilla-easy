#!/usr/bin/env python


try:
    import sys
    import time
    import prettytable
except ImportError:
    print("Rats! Looks like you don't have the right libraries installed. \nYou'll need the original (Pimoroni) flotilla library, as well as sys,\ntime and prettytable.")
    exit()

flot_lib = False

try:
    import flotilla
    import os
    os.system("sudo service flotillad stop")
    flot_lib = True
except ImportError:
    print("You don't have the flotilla library installed. Continuing in test mode")


cli_connected = False

COLOR_INFO = "{red},{green},{blue},{clear}"

if flot_lib == True:
    try:
        client = flotilla.Client()
        cli_connected = True
        while not client.ready:
            pass
      
        print("Dock connected!")  

    except AttributeError:
        print("Couldn't find a dock. Continuing in test mode")


#we should scale all values to 1000 I think

if cli_connected and flot_lib:
    col = client.first(flotilla.Colour) #y - the values scale 0 to 25
    mat = client.first(flotilla.Matrix)#y
    mot = client.first(flotilla.Motor)#y - values are 0 to 63/-63 (f/r)
    num = client.first(flotilla.Number)#n
    tou = client.first(flotilla.Touch)#y
    dia = client.first(flotilla.Dial)#y - the values scale 0-1023
    joy = client.first(flotilla.Joystick)#y - the values scale from 0 (right/btm) to 1023 (top/left) - scale -1k to 1k or will this cause errors?
    sli = client.first(flotilla.Slider)#y -s scales 0  to 1023
    wea = client.first(flotilla.Weather)#y
    acc = client.first(flotilla.Motion)#y
    lig = client.first(flotilla.Light)#y
else:
    col = 0
    mat = 0
    mot = 0
    num = 0
    tou = 0
    dia = 0
    joy = 0
    sli = 0
    wea = 0
    acc = 0
    lig = 0
    testmatrix = [[0 for x in range(8)] for y in range (8)]

def colour():
    try:
        if col != 0:
            COLOR_INFO = "{red},{green},{blue},{clear}"
            return COLOR_INFO.format(
            red= col.red,
            green=col.green,
            blue=col.blue,
            clear=col.clear)
        else:
            print("Test mode: sending simulated colours")
            return(100, 200, 300, 0)
    except AttributeError:
        if col == 0:
            print("Test mode: sending simulated values")
            return(100, 200, 300, 0)
        else:
            print("No module connected. Try again!")

def matrix(x,y,state):
    if state == True:
        state_numerical = 1
    elif state == False:
        state_numerical = 0
    try:
        mat.set_pixel(x, y, state_numerical).update()
    except AttributeError:
        if mat == 0:
            print("Test mode: lighting pixels")
            testmatrix[x][y] = state_numerical
            matrix_printing = prettytable.PrettyTable()
            for row in testmatrix:
                matrix_printing.add_row(row)

            print(matrix_printing.get_string(header=False, border=False))
        else:
            print("No module connected. Try again!")


def motor(speed):
    try:
        mot.set_speed(speed)
    except AttributeError:
        if mot == 0:
            print("Test mode: simulating speed: ", speed)
        else:
            print("No module connected. Try again!")

def number(numbertoshow):
    if numbertoshow > 9999:
        print("Sorry. Only numbers 0 to 9999 allowed! Showing the closest to your number.")
        numbertoshow = 9999
    if numbertoshow < 0:
        print("Sorry. Only numbers 0 to 9999 allowed! Showing the closest to your number.")
        numbertoshow = 0000        
    try:
        num.set_number(numbertoshow)
        num.update()
    except AttributeError:
        if num == 0:
            print("Test mode: showing number on the screen")
            print(numbertoshow)
        else:
            print("No module connected. Try again!")
            
def touch(touched_number):
    if touched_number > 4:
        print("Sorry. Only numbers 1 to 4 allowed! Using 4")
        touched_number = 4
    if touched_number < 1:
        print("Sorry. Only numbers 1 to 4 allowed! Using 1")
        touched_number = 1
        
    try:
        if touched_number == 1:
            if tou.one:
                return True
            else:
                return False
        elif touched_number == 2:
            if tou.two:
                return True
            else:
                return False
        elif touched_number == 3:
            if tou.three:
                return True
            else:
                return False
        elif touched_number == 4:
            if tou.four:
                return True
            else:
                return False
        
    except AttributeError:
        if tou == 0:
            print("Test mode - simulating a press")
            testpressed = input("1, 2, 3, or 4?")
            if testpressed == touched_number:
                return True
            else:
                return False

        else:
            print("No module connected. Try again!")


def dial():
        
    try:
        return dia.position
        
    except AttributeError:
        if dia == 0:
            print("Test mode - simulating a twist")
            testtwist = input("How much have you twisted from 0 to 1023?")
            return testtwist

        else:
            print("No module connected. Try again!")

def joystick(value):
        
    try:
        if value == "x":
            return joy.x
        if value == "y":
            return joy.y
        if value == "button":
            return joy.button
        else:
            print("sorry, I don't know what that is!")
        
    except AttributeError:
        if joy == 0:

            print("Test mode - simulating a joystick use")

            if value == "x":
                testx = input("Where is x? 0 is left, 512 is middle and 1024 is right.")
                return testx
            if value == "y":
                testy = input("Where is y? 0 is left, 512 is middle and 1024 is right.")
                return testy
            if value == "button":
                testbtn = input("Is the button pressed?")
                return testbtn
            else:
                print("sorry, I don't know what that is!")
        else:
            print("No module connected. Try again!")

def slider():
        
    try:
        return sli.position
        
    except AttributeError:
        if sli == 0:
            print("Test mode - simulating a slide")
            testslide = input("How much have you slid from 0 to 1023?")
            return testslide

        else:
            print("No module connected. Try again!")


def weather(value):
        
    try:
        if value == "temp":
            return wea.temperature
        if value == "press":
            return wea.pressure
        else:
            print("sorry, I don't know what that is!")
        
    except AttributeError:
        if wea == 0:

            print("Test mode - simulating weather")

            if value == "temp":
                testx = input("How hot is it? Room temperature is 25 C for reference. ")
                return testx
            if value == "press":
                testy = input("What is the pressure? Room pressure is 101325 hPa for reference. ")
                return testy
            else:
                print("sorry, I don't know what that is!")
        else:
            print("No module connected. Try again!")

def light():
    if lig != 0:    
        try:
            return lig.lux   
        except AttributeError:
            if lig == 0:
                print("Test mode - simulating light level")
                testlux = input("How many luxes of light are there? For reference, 500 is typical")
                return testlux

            else:
                print("No module connected. Try again!")

    else:
        print("No module connected. Try again!")
            
def motion(value):
        
    try:
        if value == "x":
            return acc.x
        if value == "y":
            return acc.y
        if value == "z":
            return acc.z
        else:
            print("sorry, I don't know what that is!")
        
    except AttributeError:
        if acc == 0:

            print("Test mode - simulating motion")

            if value == "x":
                testx = input("What is x?")
                return testx
            if value == "y":
                testy = input("What is y?")
                return testy
            if value == "z":
                testz = input("What is z?")
                return testz
            else:
                print("sorry, I don't know what that is!")
        else:
            print("No module connected. Try again!")

##'''
##if color is None:
##    client.stop()
##    sys.exit(1)
##'''
##i = 0
##'''
##
###mot.set_speed(0)
##num.set_number(1234)
##num.update()
##'''for i in range(10):
##    for j in range(10):
##        mat.set_pixel(i,j,0)'''
##mot.set_speed(-63)
##'''
###MONSTER EXAMPLE LOOP (comment out stuff you didn't connect)
##try:
##    while True:
##        print(COLOR_INFO.format(
##            red= col.red,
##            green=col.green,
##            blue=col.blue,
##            clear=col.clear))
##        time.sleep(0.5)
##        #mat.set_pixel(1, 1, 1).update()
##        #mot.set_speed(-63)
##
##        num.set_number(int(1234))
##        num.update()
##        if tou.one:
##            print("True")
##        print(dia.position)
##        print("x", joy.x, "y", joy.y, "button?", joy.button)
##        print("slider: ", sli.position)
##        print("temp: ", wea.temperature, "pres: ", wea.pressure)
##        print("ax: ", acc.x, "ay: ", acc.y, "az", acc.z)
##        #print('light: ', lig.light, "lux ", lig.lux)
##        
##        
##
##   
##        
##        
##except KeyboardInterrupt:
##    print("Stopping Flotilla...")
##    client.stop()
