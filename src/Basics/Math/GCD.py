#GCD algorithm : gcd(a,b) = gcd(a, a mod b):
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = 463
num2 = 462
print(f"The GCD of {num1} and {num2} is {gcd(num1, num2)}")
