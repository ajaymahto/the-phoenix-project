# Python Program to Calculate the Area of a Triangle
# If a, b and c are three sides of a triangle. Then,
# s = (a+b+c)/2
# area = √(s(s-a)*(s-b)*(s-c))

from math import sqrt

def area(a,b,c):
    s = (a+b+c) / 2
    ar = sqrt(s*(s-a)*(s-b)*(s-c))
    return(ar)

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    print(area(a,b,c))
    
if __name__ == '__main__':
    main()