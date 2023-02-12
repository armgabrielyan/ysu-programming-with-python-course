# Homework No. 01

**Due:** 23:59, 19 February, 2023

**Max points:** 100

## Submission procedure

- Each problem solution should be saved in a separate file. The following naming convention should be used: `problem{number}.{extension}`. For example, `problem1.py` or `problem1.pdf`.
- At the start of each file, homework number, student full name and problem number should be mentioned. For example:

```python
"""
Homework 1
Name: John Doe
Problem 1
"""
```

- Solution files should be uploaded to [YSU Moodle](https://e-learning.ysu.am/). Alternatively, you can commit your solutions to a Git repository and provide the repository URL on Moodle.

## Problem 1

State an example of a **declarative** knowledge and its corresponding **imperative** knowledge.

## Problem 2

We have studied an example of an imperative algorithm for finding the square root of a number. Apply the algorithm to find the square root of a number $x$, when $x$ is defined as follows:

1. $x = 9$
2. $x = 3$

Please show the details of your calculations.

**Note 1:** In the context of this problem we define that $x$ is close enough to $y$ if and only if the absolute difference between $x$ and $y$ is less than $10^{-3}$, i.e. $|x - y| < 10^{-3}$.

**Note 2:** You can solve this problem manually and show your calculations on paper. Nevertheless, you are advised to use Python as a calculator and show your computations in a Python script.

## Problem 3

Let us consider Mathematics as a language. For each of the following exercises, state if the sentence is correct in terms of syntax and static semantics. If it is correct both syntactically and static semantically, then state its semantics. Explain your answers.

**Examples**

1. Let $f\{x\} = x^2$.
    - **Syntax:** Invalid. In mathematical notation, function arguments are not denoted by curly brackets $\{\}$, but by round brackets $()$.
    - **Static semantics:** Not relevant. It should be syntactically correct to be considered in terms of static semantics.
    - **Semantics:** Not relevant. It should be both syntactically and static semantically correct to be considered in terms of semantics.
2. Let $f(n, k) = {n \choose k}$. What is the value of $f(4, -2)$?
    - **Syntax:** Valid. The function and its value are both denoted correctly.
    - **Static semantics:** Invalid. Binomial coefficients are usually defined in terms of non-negative numbers $n$ and $k$, so the value of $f(4, -2)$ has no meaning.
    - **Semantics:** Not relevant.
3. Let $A = \{ 1, 2, \dots, 10 \}$ and $B = \{ 5, 6, \dots, 15 \}$. Find $A \cup B$?
    - **Syntax:** Valid. Sets $A$, $B$ and their unions are correctly formed.
    - **Static semantics:** Valid. Union operation defined on sets has a meaning.
    - **Semantics:** The meaning is that given a set of numbers from $1$ to $10$ and another set of numbers from $5$ to $15$, we need to find the set of numbers that are members of $A$ or $B$ or both.

**Exercises**

1. Calculate $4 \cdot 5 + 3 \cdot (6 - \frac{4}{7}$.
2. In Euclidean geometry, the distance between two points $(x_1, y_1)$ and $(x_2, y_2)$ can be calculated by $\sqrt{(x_2 - x_1) ^ 2 + (y_2 - y_1) ^ 2}$ formula.
3. Let $f(x, y) = x^2 + y^2$. Find the value of $f(1, 2, 3)$.
4. Let $A = \{ 1, 2, \dots, 10 \} + 42$. State the elements of the set $A$.
5. Let $A \in {R ^ {2 \times 4}}$ and $B \in {R ^ {4 \times 3}}$ be two matrices.
    - Find $AB$.
    - Find $BA$.
6. Let $f(x, y) = \frac{x}{y}$.
    - Given $x = 12$ and $y = 4$ numbers, find the value of $f(x, y)$.
    - Given $\vec{x} = \begin{bmatrix} 1 & 2  \end{bmatrix} ^ T$ and $\vec{y} = \begin{bmatrix} 3 & 4  \end{bmatrix}  ^ T$, find the value of $f(\vec{x}, \vec{y})$.
7. $A = \{ 1, 2, \dots, 5 \}$ and $B = \{ 6, 7, \dots, 10 \}$. Find $A \times B$.
8. Calculate $\sum_1^{100}{\frac{1}{\log}}$
9. If $a$, $b$ are sides and $c$ is the hypotenuse of a right triangle, then $a^2 + b^2 = c^2$.
<!-- 9. If $a$ and $b$ are sides of a right triangle and $c$ is its hypotenuse, then $a^2 + b^2 = c^2$. -->
10. Find $\int e^x$.

## Problem 4

Which of the following names are valid variable names in Python? Explain your reasoning.

**Examples**

1. `abc`: Valid. It consists of only lowercase English letters.
2. `var$`: Invalid. It contains a dollar sign (`$`), which is not a valid variable name character.

**Exercises**

1. `xyz123`
2. `XyZ`
3. `True`
4. `false`
5. `first_name`
6. `last-name`
7. `$account_balance`
8. `two_%_increase`
9. `42_percent_decrease`
10. `if_`
11. `__False`

**Note:** It is possible to check the answers using Python, but first try to find the answers yourself.

## Problem 5

State the types of `x`, `y` and `z` variables at the end of each Python code snippet.

**Example**

```python
x = 1
y = 2.5
z = "Hello world!"
```

- `x`: It is `int` because `1` is a positive integer.
- `y`: It is `float` because `2.5` is a floating-point number.
- `z`: It is `str` because `"Hello world!"` represent text.

```python
"""
A program that prints out the type of each variable.
"""
```

**Exercises**

1. 

```python
x = 10
y = '10'
z = "10"
```

2. 

```python
x = 'True'
y = False
z = "False"
```

3.

```python
x = 7.0
y = "7"
z = -7
```

4.

```python
x = 1.7j - 2
y = "1.7j - 2"
z = "1 + i"
```

5.

```python
x = "John Doe"
y = 'Jane Lee'
z = 'programming'
```

6.

```python
x = "None"
y = None
z = 'none'
```

7.

```python
x = 3e4
y = 5.6e-4
z = '5e7'
```

**Note:** It is possible to check the answers using Python, but first try to find the answers yourself. After that, you are advised to write a program that outputs the type of each variable.

## Problem 6

Write a Python program that asks the user to input the following details:

- first name
- last name
- date of birth

Afterwards the program welcomes the user and prints user's information.

The following shows an example program in action.

```sh
$ python problem2.py
What is your first name? John
What is your last name? Doe
What is your date of birth? 17/06/1942
Welcome John Doe 17/06/1942
```
