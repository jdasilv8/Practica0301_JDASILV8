import datetime

start_time = datetime.datetime.now()
num = int(input("Indique un número entero: "))
fibonacci = FibonacciBucles(num)
print ("El número de fibonacci de " + str(num) + " es " + str(fibonacci))
end_time = datetime.datetime.now()
print ("El tiempo de ejecución es:", end_time - start_time)

def FibonacciBucles (n):
    if n <= 1:
        return n
    else:
        a = 0
        b = 1
        for i in range (n-1):
            c = a + b
            a = b
            b = c
        return c