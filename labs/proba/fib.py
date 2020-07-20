
def fib(n):
    if n<=1:
        return n
    return(fib(n-1)+fib(n-2))

def fib2(n):
    fi2 = [0, 1] + [0] * (n - 1)
    for z in range(2, n + 1):
        fi2[z] = fi2[z - 1] + fi2[z - 2]
    return fi2[n]

m=30
for k in range(m):
    print(fib(k), end=" ")
print()
for k in range(m):
    print(fib2(k), end=" ")
print()
