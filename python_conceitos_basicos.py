'''
a = 5
b = 'Buda'
a, b = b, a
print(a)
print(b)
print(a * b)
'''
def fatorial(n):
    if(n < 0):
        return "Não tem fatorial negativo!"

fat = 1
for i in range(n):
    fat *= (i + 1)
    return fat

print(fatorial(0))
print(fatorial(-1))