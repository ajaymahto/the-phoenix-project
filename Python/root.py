# Python Program to Find the Square Root

from math import sqrt

def sqroot(a):
    ''' Function to return square root '''
    return(sqrt(a))

def main():
    ''' The main function '''
    a = int(input())
    print(sqroot(a))

if __name__ == '__main__':
    main()