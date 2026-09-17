# Alternating Sum Calculator
Type of the sum is
for n in N*
S = a - (a+1) + (a+2) - (a-3) . . . + (-1)^n(a+n)
or
S = sum from k=0 to n of (-1)^k(a+k)

A lightweight Python script designed to compute the sum of an alternating series between two integer bounds ($a$ and $n$).

## 📌 Features

- **Fast Calculation:** Calculates alternating series sums using direct mathematical logic.
- **Input Validation:** Built-in exception handling to prevent errors when non-integer values are entered.
- **Simple Interface:** Clean CLI interface for fast input and quick output.

## 🧮 How It Works

The script calculates the sum based on whether the upper bound $n$ is even or odd:
- If $n$ is **even**: $\text{Sum} = a + \frac{n}{2}$
- If $n$ is **odd**: $\text{Sum} = -\frac{n + 1}{2}$

## 🚀 Getting Started

### Prerequisites

Make sure you have **Python 3.x** installed on your system.


Ayoub Lagnaoui XX