#numbers
num = int(input())
def del_slow(n):
    d = set()
    for i in range(1, n+1):
        if n%i==0:
            d.add(i)
    return d

print(del_slow(num))
