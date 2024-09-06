n=int(input('Enter any natural number='))

def printNos(n):
    if n > 0:
        printNos(n - 1)
        print(n, end=' ')

printNos(n)