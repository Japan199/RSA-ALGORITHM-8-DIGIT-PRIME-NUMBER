import sympy

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

def power(x, y, p):
    res = 1;  # Initialize result

    # Update x if it is
    # more than or equal to p
    x = x % p;

    while (y > 0):

        # If y is odd, multiply
        # x with the result
        if (y & 1):
            res = (res * x) % p;

            # y must be even now
        y = y >> 1;  # y = y/2
        x = (x * x) % p;

    return res;

#print(sympy.isprime(5))
#print(list(sympy.primerange(0, 100)))

cs = input("Enter string : ")


p = sympy.randprime(10000000,100000000)
print("p = ",p)

q = sympy.randprime(10000000,100000000)
print("q = ",q)

n = p*q
print("n = ",n)

print("GCD of p and q is : ", gcd(p,q))

phi = (p-1) * (q-1)     #24
print("phi(n) = ",phi)

for e in range(2,phi):
    if gcd(e,phi) == 1:
        break

print("e = ",e)

for i in range(1,phi):
    x = 1 + i*phi
    if x % e == 0:
        d = int(x/e)
        break
print("d = ",d)
print(e*d)
print((e*d)%phi)

deciphered_list=[]
for i in range(0,len(cs)):
    pt=ord(cs[i])
    print(pt)

    ciser = (pt**e) % n
    print("ciser = ",ciser)

    reduced_d = 0
    d_string = str(d)
    for j in range(len(d_string)):
        reduced_d = ((reduced_d * 10 + ord(d_string[j]) - 48) % (n - 1));

    plain = power(ciser, reduced_d, n)
    print("decipher = ",plain)
    print("decipher = ",chr(plain))
    deciphered_list.append(chr(plain))
print(deciphered_list)
string_deciphered = "".join(deciphered_list)
print(string_deciphered)









