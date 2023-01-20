import RPi.GPIO as GPIO
import time
import numpy as np

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN)
counts = 0
long = 0
arr = np.array([])
setter = 0
letnum = 0
try:
    while True:
        counts += 1
        arr = np.append(GPIO.input(27), arr)
        if counts == 100:
           # if 0 in arr:
                # print('open')
                
            if 0 not in arr:
                # print('closed')
                long += 1
        
            else:
                long = 0
            if long == 1:
                letnum += 1
            if long == 3:
                # letnum -= 1
                if letnum == 1:
                    # first letter
                    if setter == 0:
                        letter1 = 'a'
                        print(letter1)
                        setter += 1
                    # first number
                    elif setter == 1:
                        num1 = 1
                        print(num1)
                        setter += 1
                    elif setter == 2:
                        letter2 = 'a'
                        print(letter2)
                        setter += 1
                    elif setter == 3:
                        num2 = 1
                        print(num1)
                        move = letter1 + str(num1) + letter2 + str(num2)
                        print(move)
                        setter = 0
                
                elif letnum == 2:
                    # first letter
                    if setter == 0:
                        letter1 = 'b'
                        print(letter1)
                        setter += 1
                    # first number
                    elif setter == 1:
                        num1 = 2
                        print(num1)
                        setter += 1
                    elif setter == 2:
                        letter2 = 'b'
                        print(letter2)
                        setter += 1
                    elif setter == 3:
                        num2 = 2
                        print(num2)
                        move = letter1 + str(num1) + letter2 + str(num2)
                        print(move)
                        setter = 0
                    
                elif letnum == 3:
                    # first letter
                    if setter == 0:
                        letter1 = 'c'
                        print(letter1)
                        setter += 1
                    # first number
                    elif setter == 1:
                        num1 = 3
                        print(num1)
                        setter += 1
                    elif setter == 2:
                        letter2 = 'c'
                        print(letter2)
                        setter += 1
                    elif setter == 3:
                        num2 = 3
                        print(num2)
                        move = letter1 + str(num1) + letter2 + str(num2)
                        print(move)
                        setter = 0
                
                elif letnum == 4:
                    # first letter
                    if setter == 0:
                        letter1 = 'd'
                        print(letter1)
                        setter += 1
                    # first number
                    elif setter == 1:
                        num1 = 4
                        print(num1)
                        setter += 1
                    elif setter == 2:
                        letter2 = 'd'
                        print(letter2)
                        setter += 1
                    elif setter == 3:
                        num2 = 4
                        print(num2)
                        move = letter1 + str(num1) + letter2 + str(num2)
                        print(move)
                        setter = 0
                    
                elif letnum == 5:
                    # first letter
                    if setter == 0:
                        letter1 = 'e'
                        print(letter1)
                        setter += 1
                    # first number
                    elif setter == 1:
                        num1 = 5
                        print(num1)
                        setter += 1
                    elif setter == 2:
                        letter2 = 'e'
                        print(letter2)
                        setter += 1
                    elif setter == 3:
                        num2 = 5
                        print(num2)
                        move = letter1 + str(num1) + letter2 + str(num2)
                        print(move)
                        setter = 0
                
                elif letnum == 6:
                    # first letter
                    if setter == 0:
                        letter1 = 'f'
                        print(letter1)
                        setter += 1
                    # first number
                    elif setter == 1:
                        num1 = 6
                        print(num1)
                        setter += 1
                    elif setter == 2:
                        letter2 = 'f'
                        print(letter2)
                        setter += 1
                    elif setter == 3:
                        num2 = 6
                        print(num2)
                        move = letter1 + str(num1) + letter2 + str(num2)
                        print(move)
                        setter = 0
                    
                elif letnum == 7:
                    # first letter
                    if setter == 0:
                        letter1 = 'g'
                        print(letter1)
                        setter += 1
                    # first number
                    elif setter == 1:
                        num1 = 7
                        print(num1)
                        setter += 1
                    elif setter == 2:
                        letter2 = 'g'
                        print(letter2)
                        setter += 1
                    elif setter == 3:
                        num2 = 7
                        print(num2)
                        move = letter1 + str(num1) + letter2 + str(num2)
                        print(move)
                        setter = 0
                
                elif letnum == 8:
                    # first letter
                    if setter == 0:
                        letter1 = 'g'
                        print(letter1)
                        setter += 1
                    # first number
                    elif setter == 1:
                        num1 = 8
                        print(num1)
                        setter += 1
                    elif setter == 2:
                        letter2 = 'g'
                        print(letter2)
                        setter += 1
                    elif setter == 3:
                        num2 = 8
                        print(num2)
                        move = letter1 + str(num1) + letter2 + str(num2)
                        print(move)
                        setter = 0
                    
                else:
                    print('error ' + str(letnum))
                    setter = 0
                    
                long = 0
                letnum = 0
                time.sleep(1)
                
            arr = np.array([])
            counts = 0
            
        
finally:    
    GPIO.cleanup()
            