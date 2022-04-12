# Python Program to Add Two Numbers

def sum(a, b):
    ''' Function to add up two numbers '''
    return a+b

def main():
    ''' The main function '''
    a = int(input())
    b = int(input())
    print(sum(a,b))

if __name__ == '__main__':
    main()