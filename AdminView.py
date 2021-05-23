from Dbview import *
import DesignColors
color = DesignColors.Fonts()

def main1():
    print(color.BOLD + color.DARKCYAN +'1. ADMIN DETAILS'+color.END)
    print(color.BOLD + color.DARKCYAN +'2. QUIZ DETAILS'+color.END)
    n=int(input('Press 1 for ADMIN and Press 2 for QUIZ: '))
    if n==1:
        main()
    elif n==2:
        Quizmain()

def CheckA():
    a=checkAdmin()
    if a==1:
        main1()
