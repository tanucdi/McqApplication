from AdminView import *
from Dbview import Usermain,allplaymain,checkAdmin
import DesignColors
color = DesignColors.Fonts()

def mains():
    while True:
        print(color.BOLD + color.RED +'WELCOME TO TANISHK MCQ QUIZ'+ color.END)
        print(color.BOLD + color.DARKCYAN +'1. SUPERUSER'+color.END)
        print(color.BOLD + color.DARKCYAN +'2. USER'+color.END)
        print(color.BOLD + color.DARKCYAN +'3. SEE TOP PLAYERS'+color.END)
        print(color.BOLD + color.DARKCYAN +'4. EXIT'+color.END)
        try:
            n=int(input('Enter Your Choice: '))
            if n==1:
                CheckA()
            elif n==2:
                Usermain()
            elif n==3:
                allplaymain()
            elif n==4:
                print(color.BOLD + color.WHITE+'Thank You For Playing.'+color.END)
                break
            else:
                print('Invalid Input ! Try again.')
        except Exception as e:
            print(e)
            print('Invalid Details ! Try again. ')
mains()