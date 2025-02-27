n = int(input())
i = 1
divisores = 0
while i <= n:
    if n % i == 0:
        divisores = divisores + 1
    i = i + 1
if divisores > 2:
    print("No es primo")
else:
    print("Es primo")