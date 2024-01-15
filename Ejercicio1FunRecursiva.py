import datetime

start_time = datetime.datetime.now()
num = int(input("Indique un número entero: "))
fibonacci = FibonacciRecur(num)
print ("El número de fibonacci de " + str(num) + " es " + str(fibonacci))
end_time = datetime.datetime.now()
print ("El tiempo de ejecución es:", end_time - start_time)

def FibonacciRecur (n):
    if n <= 1:
        return n
    else:
        return FibonacciRecur(n-1) + FibonacciRecur(n-2)