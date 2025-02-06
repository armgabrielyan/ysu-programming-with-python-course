# Solution No. 01 

## Problem set 1

### Problem 1

```python
n = int(input("Enter a positive integer: "))

if n == 1:
    print(f"{n} is a composite number")

i = 2

while i <= n ** 0.5:
    if n % i == 0:
        print(f"{n} is a composite number")
        break
    i += 1
else:
    print(f"{n} is a prime number")
```

### Problem 2

```python
n = int(input("Enter a number: "))
x = n

sum_ = 0

while x != 0:
    sum_ += x % 10
    x //= 10

print(f"The sum of digits in {n} is {sum_}")
```

<!-- $$\pagebreak$$ -->

### Problem 3

```python
n = int(input("Enter a number: "))
x = n

n_reversed = 0

while x != 0:
    n_reversed = 10 * n_reversed + x % 10
    x //= 10

if n == n_reversed:
    print(f"{n} is a palindrome number")
else:
    print(f"{n} is not a palindrome number")
```

### Problem 4

```python
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

while b != 0:
    a, b = b, a % b

print(f"The gcd is {a}")
```

<!-- $$\pagebreak$$ -->

### Problem 5

```python
n = int(input("Enter a number: "))
x = n

binary = ""

while x != 0:
    binary = str(x % 2) + binary
    x //= 2

print(f"The binary value of {n} is {binary}")
```
