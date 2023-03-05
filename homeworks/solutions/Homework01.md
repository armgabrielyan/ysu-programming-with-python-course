# Solution No. 01 

## Problem 1

- **Declarative:** A natural number is called a prime number if it is greater than $1$ and cannot be represented as a product of two natural numbers.
- **Imperative**
    1. If the given number $n$ is equal to $1$, then we stop and $n$ is not prime.
    2. Let $i = 2$.
    3. Check if $i \le \lfloor \sqrt{n} \rfloor$. If not, then we stop and $n$ is prime. Otherwise, we continue to the next step.
    4. Check if $n$ is divisible by $i$. If yes, then we stop and $n$ is not prime.
    5. Otherwise, let $i = i + 1$ and go back to step $3$.

<!-- $$\pagebreak$$ -->

## Problem 2

- $x = 9$

**Step 1**

1. Let $g = 1$
2. $|g^2 - x| = |1 - 9| = 8 > 10^{-3}$, so we continue.
3. $g = \frac{1 + \frac{9}{1}}{2} = 5$ is the new guess.
4. Go back to $2.$ and repeat.

**Step 2**

1. Let $g = 5$
2. $|g^2 - x| = |25 - 9| = 16 > 10^{-3}$, so we continue.
3. $g = \frac{5 + \frac{9}{5}}{2} = 3.4$ is the new guess.
4. Go back to $2.$ and repeat.

**Step 3**

1. Let $g = 3.4$
2. $|g^2 - x| = |11.56 - 9| = 2.56 > 10^{-3}$, so we continue.
3. $g = \frac{3.4 + \frac{9}{3.4}}{2} = 3.02352941$ is the new guess.
4. Go back to $2.$ and repeat.

**Step 4**

1. Let $g = 3.02352941$
2. $|g^2 - x| = |9.14173 - 9| = 0.14173 > 10^{-3}$, so we continue.
3. $g = \frac{3.02352941 + \frac{9}{3.02352941}}{2} = 3.00009155$ is the new guess.
4. Go back to $2.$ and repeat.

**Step 5**

1. Let $g = 3.00009155$
2. $|g^2 - x| = |9.0005493 - 9| = 0.0005493 < 10^{-3}$, so we stop.

The answer is $g = 3.00009155$.

- $x = 3$

This can be calculated like the method above.

<!-- $$\pagebreak$$ -->

## Problem 3

1. Calculate $4 \cdot 5 + 3 \cdot (6 - \frac{4}{7}$.
    - **Syntax:** Invalid. Brackets are not balanced.
    - **Static semantics:** Not relevant.
    - **Semantics:** Not relevant.
2. In Euclidean geometry, the distance between two points $(x_1, y_1)$ and $(x_2, y_2)$ can be calculated by $\sqrt{(x_2 - x_1) ^ 2 + (y_2 - y_1) ^ 2}$ formula.
    - **Syntax:** Correct. The statements and formula are well-defined.
    - **Static semantics:** Valid. The statements and formula have meaning.
    - **Semantics:** The meaning is to give a formula for calculating the distance between two points in Euclidean geometry.
3. Let $f(x, y) = x^2 + y^2$. Find the value of $f(1, 2, 3)$.
    - **Syntax:** Correct. The statements and formula are well-defined.
    - **Static semantics:** Invalid. The function $f(x, y)$ has two arguments, but it is called with three parameters.
    - **Semantics:** Not relevant.
4. Let $A = \{ 1, 2, \dots, 10 \} + 42$. State the elements of the set $A$.
    - **Syntax:** Invalid. Addition between a set and number is not well-formed.
    - **Static semantics:** Not relevant.
    - **Semantics:** Not relevant.
5. Let $A \in {R ^ {2 \times 4}}$ and $B \in {R ^ {4 \times 3}}$ be two matrices.
    - Find $AB$.
        - **Syntax:** Correct. The statements and notation are well-defined.
        - **Static semantics:** Valid. The statements and notation have meaning.
        - **Semantics:** The meaning is that the product of matrices $A$ and $B$ can be found.
    - Find $BA$.
        - **Syntax:** Correct. The statements and notation are well-defined.
        - **Static semantics:** Invalid. There is a mismatch in dimensions and the product of matrices $B$ and $A$ cannot be computed.
        - **Semantics:** Not relevant.
6. Let $f(x, y) = \frac{x}{y}$.
    - Given $x = 12$ and $y = 4$ numbers, find the value of $f(x, y)$.
        - **Syntax:** Correct. The statements and notation are well-defined.
        - **Static semantics:** Valid. The statements and notation have meaning.
        - **Semantics:** The meaning is the division between two numbers which is correctly defined.
    - Given $\vec{x} = \begin{bmatrix} 1 & 2  \end{bmatrix} ^ T$ and $\vec{y} = \begin{bmatrix} 3 & 4  \end{bmatrix}  ^ T$, find the value of $f(\vec{x}, \vec{y})$.
        - **Syntax:** Correct. The statements and notation are well-defined.
        - **Static semantics:** Invalid. Division operation is not defined on vectors.
        - **Semantics:** Not relevant.
7. $A = \{ 1, 2, \dots, 5 \}$ and $B = \{ 6, 7, \dots, 10 \}$. Find $A \times B$.
    - **Syntax:** Correct. The statements and notation are well-defined.
    - **Static semantics:** Valid. The statements and notation have meaning.
    - **Semantics:** The meaning is that the Cartesian product between sets $A$ and $B$ is computed.
8. Calculate $\sum_1^{100}{\frac{1}{\log}}$
    - **Syntax:** Incorrect. $\log$ has a missing argument.
    - **Static semantics:** Not relevant.
    - **Semantics:** Not relevant.
9. If $a$, $b$ are sides and $c$ is the hypotenuse of a right triangle, then $a^2 + b^2 = c^2$.
    - **Syntax:** Correct. The statements and formula are well-defined.
    - **Static semantics:** Valid. The statements and formula have meaning.
    - **Semantics:** The meaning is to state the Pythagorean theorem.
10. Find $\int e^x$.
    - **Syntax:** Incorrect. Integral is missing $dx$.
    - **Static semantics:** Not relevant.
    - **Semantics:** Not relevant.

<!-- $$\pagebreak$$ -->

## Problem 4

1. `xyz123`: Valid. It consists of only English letters and numbers.
2. `XyZ`: Valid. It consists of only English letters.
3. `True`: invalid. `True` is a keyword in Python.
4. `false`: Valid. It consists of only English letters and it is not a Python keyword. Instead, `False` is a keyword.
5. `first_name`: Valid. It consists of only English letters and underscore (`_`).
6. `last-name`: Invalid. It contains hyphen (`-`).
7. `$account_balance`: Invalid. It contains dollar sign (`$`).
8. `two_%_increase`: Invalid. It contains percent sign (`%`).
9. `42_percent_decrease`: Invalid. It starts with a number.
10. `if_`: Valid. It consists of only English letters and an underscore (`_`), and it is not a Python keyword. Instead, `if` is a keyword.
11. `__False`: Valid. It consists of only English letters and underscores (`_`), and it is not a Python keyword. Instead, `False` is a keyword.

<!-- $$\pagebreak$$ -->

## Problem 5

1. 

```python
x = 10 # int
y = '10' # str
z = "10" # str
```

2. 

```python
x = 'True' # str
y = False # bool
z = "False" # str
```

3.

```python
x = 7.0 # float
y = "7" # str
z = -7 # int
```

4.

```python
x = 1.7j - 2 # complex
y = "1.7j - 2" # str
z = "1 + i" # str
```

5.

```python
x = "John Doe" # str
y = 'Jane Lee' # str
z = 'programming' # str
```

6.

```python
x = "None" # str
y = None # NoneType
z = 'none' # str
```

7.

```python
x = 3e4 # float
y = 5.6e-4 # float
z = '5e7' # str
```

<!-- $$\pagebreak$$ -->

## Problem 6

```python
first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
dob = input('What is your date of birth? ')

print('Welcome', first_name, last_name, dob)
```
