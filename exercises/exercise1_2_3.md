# ACT Answers

-   **Answer Set**: No. 01, Part 02, Chapter 3
-   **Full Name**: Mohammad Hosein Nemati
-   **Student Code**: `610300185`

---

## Page 47, Problem 6

### (a)

> **Problem**: Let $E(x) = 0$ if $x$ is even, $E(x) = 1$ if $x$ is odd. Show that $E(x)$ is primitive recursive.

First, we need to write $E(x)$ function:

$$
\begin{aligned}
    & E(x) =
    \begin{cases}
        1 & x \;rem\; 2 = 1
        \\
        0 & x \;rem\; 2 = 0
    \end{cases}
    \\
    \\
    & E(0) = 0
    \\
    & E(1) = 1
    \\
    & E(2) = 0
    \\
    & E(3) = 1
    \\
    & \vdots
\end{aligned}
$$

We will write a recursive equation for $E(x)$:

$$
\begin{aligned}
    & E(0) = 0
    \\
    & E(n) = 1 \dot{\;-\;} E(n-1)
\end{aligned}
$$

As we know, the $\dot{-}$ operator is primitive recursive, so $E(x)$ is primitive recurisve.

---

### (b)

> **Problem**: Let $H(x) = x/2$ if $x$ is even, $(x-1)/2$ if $x$ is odd. Show that $H(x)$ is primitive recursive.

First, we need to write $H(x)$ function:

$$
\begin{aligned}
    & H(x) =
    \begin{cases}
        \frac{x}{2} & x \;rem\; 2 = 1
        \\
        \frac{x-1}{2} & x \;rem\; 2 = 0
    \end{cases}
    \\
    \\
    & H(0) = 0
    \\
    & H(1) = 0
    \\
    & H(2) = 1
    \\
    & H(3) = 1
    \\
    & \vdots
\end{aligned}
$$

We will write a recursive equation for $H(x)$:

$$
\begin{aligned}
    & H(0) = 0
    \\
    & H(n) = H(n - 1) + E(n - 1)
\end{aligned}
$$

As we know, the $E(x)$ and $+$ operator both are primitive recursive, so $H(x)$ is primitive recurisve.

---

## Page 47, Problem 7

> **Problem**: Let $f(0) = 0, f(1) = 1, f(2) = 2^2 , f(3) = 3^{3^3} = 3^{27}$, etc. In general, $f(n)$ is written as a stack $n$ high, of n's as exponents. Show that $f$ is primitive recursive.

First, we need to define a new function $h(x, t)$:

$$
\begin{aligned}
    & h(x, 0) = 1
    \\
    & h(x, t + 1) = x^{h(x, t)}
\end{aligned}
$$

So, we can prove that $h(x, t)$ is primitive recursive:

$$
\begin{aligned}
    & h(x, 0) = s(n(x)) = 1
    \\
    & h(x, t + 1) = g(t, h(x, t), x) = x^{h(x, t)}
    \\
    & g(x_1, x_2, x_3) = {\underbrace{u_3^3(x_1, x_2, x_3)}_{P.R}}^{\underbrace{u_2^3(x_1, x_2, x_3)}_{P.R}}
\end{aligned}
$$

As we know, when $x, y$ are primitive recursive, then $x^y$ is primitive recursive, so $h(x, y)$ is also primitive recursive.

Now, we define $f(x)$ as:

$$
\begin{aligned}
    & f(x) = h(x, x) = h(\overbrace{u_1^1(x)}^{P.R}, \overbrace{u_1^1(x)}^{P.R})
\end{aligned}
$$

As we know, combination of two primitive recursive function is also primitive recursive, so $f(x)$ is primitive recursive.

---

## Page 48, Problem 8

> **Problem**: Let $k$ be some fixed number, let $f$ be a function such that $f(x + 1) < x + 1$ for all $x$, and let:
>
> $$
> \begin{aligned}
>     & h(0) = k
>     \\
>     & h(t + 1) = g(h(f(t + 1)))
> \end{aligned}
> $$
>
> Show that if $f$ and $g$ belong to some PRC class $L$, then so does $h$. [Hint: Define $f'(x) = min_{t \leq x} f^t(x) = 0$. See Exercise 5 for the definition of $f^t(x)$.]

Let's write $h(x)$ recursion:

$$
\begin{aligned}
    & h(t + 1) = g(h(f(t + 1)))
    \\
    & h(f(t + 1)) = g(h(f(f(t + 1))))
    \\
    & h(f(f(t + 1))) = g(h(f(f(f(t + 1)))))
    \\
    & \vdots
    \\
    & h(f^{n}(t + 1)) = g(h(f^{n + 1}(t + 1)))
\end{aligned}
$$

We know $x + 1 \gt f(x + 1) \gt 0$, so by induction: $f^{n}(x + 1) \gt f^{n + 1}(x + 1)$

Define $f'(x) = min_{t \leq x} f^{t}(x)$, we know that by applying $f$, the value will reduce, so we apply $f$ on a fixed number, until we get $0$, let's assume $f'(x) = m$, so $f^{m}(x) = 0$:

$$
\begin{aligned}
    & h(t + 1) = g(h(f(t + 1)))
    \\
    & h(f(t + 1)) = g(h(f(f(t + 1))))
    \\
    & h(f(f(t + 1))) = g(h(f(f(f(t + 1)))))
    \\
    & \vdots
    \\
    & h(f^{n}(t + 1)) = g(h(f^{n + 1}(t + 1)))
    \\
    & \vdots
    \\
    & h(f^{m - 1}(t + 1)) = g(h(f^{m}(t + 1)))
    \\
    & h(f^{m}(t + 1)) = h(0) = k
\end{aligned}
$$

---

## Page 48, Problem 9

> **Problem**: Let $g(x)$ be a primitive recursive function and let $f(0, x) = g(x), f(n + 1, x) = f(n, f(n, x))$. Prove that $f(n, x)$ is primitive recursive.

---

## Page 48, Problem 10

> **Problem**: Let $COMP$ be the class of functions obtained from the initial functions by a finite sequence of compositions.

### (a)

> **Problem**: Show that for every function $f(x_1, \dots, x_n)$ in $COMP$, either $f(x_1, \dots, x_n) = k$ for some constant $k$, or $f(x_1, \dots, x_n) = x_i + k$ for some $1 \leq i \leq n$ and some constant $k$.

---

### (b)

> **Problem**: An n-ary function $f$ is **monotone** if for all n-tuples $(x_1, \dots, x_n), (y_1, \dots, y_n)$ such that $x_i \leq y_i$ and $1 \leq i \leq n$ and $f(x_1, \dots, x_n) \leq f(y_1, \dots, y_n)$.
>
> Show that every function in $COMP$ is monotone.

---

### (c)

> **Problem**: Show that $COMP$ is a proper subset of the class of primitive recursive functions.

---

### (d)

> **Problem**: Show that the class of functions computed by straightline $P$ programs is a proper subset of $COMP$. [See Exercise 4.6 in Chapter 2 for the definition of straightline programs.]

---

## Page 48, Problem 11

> **Problem**: Let $P_1$ be the class of all functions obtained from the initial functions by any finite number of compositions and no more than one recursion (in any order).

### (a)

> **Problem**: Let $f(x_1, \dots, x_n)$ belong to $COMP$. [See Exercise 10 for the definition of $COMP$.]
>
> Show that there is a $k \gt 0$ such that $f(x_1, \dots, x_n) \leq max\{x_1, \dots, x_n\} + k$.

---

### (b)

> **Problem**: Let:
>
> $$
> \begin{aligned}
>     & h(0) = c
>     \\
>     & h(t + 1) = g(t, h(t))
> \end{aligned}
> $$
>
> where $c$ is some given number and $g$ belongs to $COMP$.
>
> Show that there is a $k \gt 0$ such that $h(t) \leq tk + c$.

---

### (c)

> **Problem**: Let:
>
> $$
> \begin{aligned}
>     & h(x_1, \dots, x_n, 0) = f(x_1, \dots, x_n)
>     \\
>     & h(x_1, \dots, x_n, t + 1) = g(t, h(x_1, \dots, x_n, t), x_1, \dots, x_n)
> \end{aligned}
> $$
>
> where $f, g$ belongs to $COMP$.
>
> Show that there are $k, l \gt 0$ such that $h(x_1, \dots, x_n, t) \leq tk + max\{x_1, \dots, x_n\} + l$.

---

### (d)

> **Problem**: Let $f(x_1, \dots, x_n)$ belong to $P_1$.
>
> Show that there are $k, l \lt 0$ such that $f(x_1, \dots, x_n) \leq max\{x_1, \dots, x_n\} . k + l$.

---

### (e)

> **Problem**: Show that $P_1$ is a proper subset of the class of primitive recursive functions.

---

## Page 62, Problem 5

> **Problem**: (Course-of-Values Recursion)

### (a)

> **Problem**: For $f(n)$ any function, we write:
>
> $$
> \begin{aligned}
>     & \tilde{f}(0) = 1
>     \\
>     & \tilde{f}(n) = [f(0), f(1), \dots, f(n-1)] \;\text{if}\; n \neq 0
> \end{aligned}
> $$
>
> Let $f(n) = g(n, \tilde{f}(n))$.
>
> For all $n$. Show that if $g$ is primitive recursive so is $f$.

---

### (b)

> **Problem**: Let:
>
> $$
> \begin{aligned}
>     & f(0) = 1, f(1) = 4, f(2) = 6
>     \\
>     & f(x + 3) = f(x) + f(x + 1)^2 + f(x + 2)^3
> \end{aligned}
> $$
>
> Show that $f(x)$ is primitive recursive.

---

### (c)

> **Problem**: Let:
>
> $$
> \begin{aligned}
>     & h(0) = 3
>     \\
>     & h(x + 1) = \sum_{t=0}^{x} h(t)
> \end{aligned}
> $$
>
> Show that $h(x)$ is primitive recursive.

---

## Page 62, Problem 6

> **Problem**: (Unnested Double Recursion), Let:
>
> $$
> \begin{aligned}
>     & f(0, y) = g_1(y)
>     \\
>     & f(x + 1, 0) = g_2(x)
>     \\
>     & f(x + 1, y + 1) = h(x, y, f(x, y + 1), f(x + 1, y))
> \end{aligned}
> $$
>
> Show that if $g_1, g_2$, and $h$ all belong to some PRC class $L$, then $f$ also belongs to $L$.

---
