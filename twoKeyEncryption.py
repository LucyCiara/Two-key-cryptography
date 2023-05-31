from math import gcd
from sympy import isprime
#*  A function which takes n and outputs the returned value. It is not realistically possible to do this without knowing q and p if they are big enough
def euler(n):
    return (p-1)*(q-1)
#*  ----------------------------------------------------------------------------------------------------------------------------------------------------------------




#!  Should be much larger when actually encrypting something
p = 229
q = 131
n = p*q
#!  --------------------------------------------------------




#*  p and q has to be primes for the program to work
if isprime(p) == False:
    print(f"p is not a prime. This will make the program non-functional")
if isprime(q) == False:
    print(f"q is not a prime. This will make the program non-functional")
#*  ------------------------------------------------




#!  e and ϕ(n) have to be coprimes for the program to work. 1 < e < ϕ(n) also has to be true
e = 29

if gcd(e, euler(n)) != 1:
    print(f"e and ϕ(n) are not coprimes. This will make the program non-functional")
if (1 < e < euler(n)) == False:
    print(f"1 < e < ϕ(n) is not the case. This will make the program non-functional")
#!  ------------------------------------------------------




#*  This part of the program creates the unique part of the private key by finding out what variable a has to be for the private key equation to give a whole number
run = True
a = 0
while run:
    a += 1
    d = (a*euler(n)+1)/e
    if d.is_integer():
        d = int(d)
        run = False
#*  -------------------------------------------------------------------------------------------------------------------------------------------------------------------

print(f"Private Key:    ({d}, {n})")
print(f"Public Key:    ({e}, {n})")






#!  There is an upper limit for the size of m, which depends on the size of the numbers. If the limit is 256 or more, the limit doesn't matter, as this is the biggest number you can write in a byte.
run = True
m = 0
while run:
    ec = m**e%n
    dc = ec**d%n
    if dc != m:
        print(f"Max size of message    {m}")
        run = False
    elif m == 256:
        print(f"The primes are large enough to encrypt a byte")
        run = False
    m += 1
#!  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
