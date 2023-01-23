# ACT Answers

-   **Answer Set**: No. 01, Part 02
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
    & h(f^{n - 1}(t + 1)) = g(h(f^{n}(t + 1)))
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

Let's inverse this recursive unroll:

$$
\begin{aligned}
    & h(f^{m}(t + 1)) = h(0) = k
    \\
    & h(f^{m - 1}(t + 1)) = g(h(f^{m}(t + 1))) = g(k)
    \\
    & h(f^{m - 2}(t + 1)) = g(h(f^{m-1}(t + 1))) = g(g(k))
    \\
    & \vdots
    \\
    & h(f^{n}(t + 1)) = g(h(f^{n + 1}(t + 1)))
    \\
    & h(f^{n - 1}(t + 1)) = g(h(f^{n}(t + 1)))
    \\
    & \vdots
    \\
    & h(f(f(t + 1))) = g(h(f(f(f(t + 1)))))
    \\
    & h(f(t + 1)) = g(h(f(f(t + 1))))
    \\
    & h(t + 1) = g(h(f(t + 1)))
\end{aligned}
$$

Now, we will prove by induction, that if we can compute $h(f^{n}(t + 1))$ then we can compute $h(f^{n-1}(t + 1))$:

$$
\begin{aligned}
    & \text{Induction Base}:
    \\
    & h(f^{m}(t + 1)) = h(0) = k
    \\
    \\
    & \text{Induction Hypothesis}:
    \\
    & h(f^{n}(t + 1)) = g(h(f^{n + 1}(t + 1)))
    \\
    \\
    & \text{Induction}:
    \\
    & h(f^{n - 1}(t + 1)) = g(h(f^{n}(t + 1))) = g(g(h(f^{n + 1}(t + 1))))
    \\
\end{aligned}
$$

So, function $h$ is computable using multiple applying of $g^{n}(x)$.

---

## Page 48, Problem 9

> **Problem**: Let $g(x)$ be a primitive recursive function and let $f(0, x) = g(x), f(n + 1, x) = f(n, f(n, x))$. Prove that $f(n, x)$ is primitive recursive.

Let's unroll $f(n, x)$:

$$
\begin{aligned}
    & f(0, x) = g(x)
    \\
    & f(1, x) = f(0, f(0, x)) = f(0, g(x)) = g(g(x))
    \\
    & f(2, x) = f(1, f(1, x)) = f(1, g(g(x))) = g^{4}(x)
    \\
    & f(3, x) = f(2, f(2, x)) = f(2, g(g(g(g(x))))) = g^{8}(x)
    \\
    & \vdots
    \\
    & f(n, x) = g^{2^n}(x)
\end{aligned}
$$

Now, we will prove by **Mathematical Induction** that if $f(n, x)$ is primitive recursive, then $f(n + 1, x)$ is also:

$$
\begin{aligned}
    & \text{Induction Base}:
    \\
    & f(0, x) = g(x) \;\text{is P.R}
    \\
    \\
    & \text{Induction Hypothesis}:
    \\
    & f(n, x) = f(n - 1, f(n - 1, x))
    \\
    \\
    & \text{Induction Goal}:
    \\
    & f(n + 1, x) = f(n, f(n, x)) = f(n, g^{2^n}(x)) = g^{2^n}(g^{2^n}(x)) = g^{2^{n + 1}}(x)
\end{aligned}
$$

As we know, $g(x)$ and $x^y$ and $g^{y}(x)$ are primitive recursive, so $f(n, x)$ is also primitive recursive.

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

As we can see, $f$ is a composition of $\tilde{f}$ and $g$ which is primitive recursive, so if $\tilde{f}$ were primitive recursive, so $f$ is primitive recursive, now we will prove $\tilde{f}$ is primitive recursive

$$
\begin{aligned}
    & \tilde{f}(0) = 1
    \\
    & \tilde{f}(n + 1) = h(n, \tilde{f}(n)) = \tilde{f}(n) \times p_{n + 1}^{f(n)} = \tilde{f}(n) \times p_{n + 1}^{g(n, \tilde{f}(n))}
    \\ \implies
    & q(x_1, x_2) = x_1 \times p_{Lt(x) + 1}^{x_2}
\end{aligned}
$$

The $Lt(x)$ and $x^y$ and $p_n$ and $\times$ are primitive recursive, so $q(x_1, x_2)$ is primitive recursive, so $\tilde{f}$ is primitive recursive, so $f$ is primitive recursive.

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

Based on the previous section, we define $g$ such that:

$$
\begin{aligned}
    & f(x) =
    \begin{cases}
        1 & x = 0
        \\
        4 & x = 4
        \\
        6 & x = 2
        \\
        g(x, \tilde{f}(x)) & x \geq 3
    \end{cases}
    \\
    \\
    & g(x, y) = (y)_{x - 2} + (y)_{x - 1}^{2} + (y)_{x}^{3}
\end{aligned}
$$

$g(x, y)$ and $\tilde{f}(x)$ are primitive recursive, so $f$ is primitive recursive.

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

Based on the previous section, we define $g$ such that:

$$
\begin{aligned}
    & h(x) =
    \begin{cases}
        3 & x = 0
        \\
        g(x, \tilde{f}(x)) & x \geq 1
    \end{cases}
    \\
    \\
    & g(x, y) = \sum_{i=0}^{x-1} (y)_{i}
\end{aligned}
$$

$g(x, y)$ and $\tilde{f}(x)$ are primitive recursive, so $f$ is primitive recursive.

---

## Page 69, Problem 3

> **Problem**: Let $HALT^{1}(x)$ be defined $HALT^{1}(x) \iff HALT(l(x), r(x))$. Show that $HALT^{1}(x)$ is not computable.

Proof by contradiction, suppose that $HALT^{1}(x)$ is computable, we will write a program to compute $HALT(x, y)$:

$$
\begin{aligned}
    & HALT(x, y) \iff HALT^{1}(\braket{x, y})
\end{aligned}
$$

If $HALT^{1}(\braket{x, y})$ were computable, so $HALT(x, y)$ is computable, but it is not possible, so $HALT^{1}(x)$ is not compu

---

## Page 69, Problem 6

> **Problem**: Let:
>
> $$
> \begin{aligned}
>     & f(x) =
>     \begin{cases}
>         x & \text{If goldbach's conjecture is true}
>         \\
>         0 & \text{Otherwise}
>     \end{cases}
> \end{aligned}
> $$
>
> Show that $f(x)$ is primitive recursive.

There are two cases for **Goldbach's conjecture**:

1. **Goldbach's conjecture is true**: In this case $f(x) = x = \overbrace{u_1^1(x)}^{P.R}$
2. **Goldbach's conjecture is false**: In this case $f(x) = 0 = \underbrace{n(x)}_{P.R}$

On both cases, $f(x)$ is primitive recursive, so $f(x)$ is primitive recursive.

---

## Page 77, Problem 1

> **Problem**: Show that for each $u$, there are infinitely many different numbers $v$ such that $\forall x \;:\; \Phi_u(x) = \Phi_v(x)$.

We can show this by constructing a function that maps any given $u$ to an infinite number of different $v$ such that $\Phi_u(x) = \Phi_v(x)$ for all $x$.

One way to do this is to use a function $f(u, n)$ that takes a number $u$ and an integer $n$ as inputs, and outputs a number $v = f(u,n)$ such that $\Phi_u(x) = \Phi_{f(u,n)}(x)$ for all $x$.

For example, one possible function $f(u,n)$ is:

$f(u,n) = u + n$

We can see that for any given $u$, we can find infinitely many different numbers $v$ by using different values of $n$. For example:

$$
\begin{aligned}
    & \Phi_u(x) = \Phi_{u + 1}(x)
    \\
    & \Phi_u(x) = \Phi_{u + 2}(x)
    \\
    & \Phi_u(x) = \Phi_{u + 3}(x)
    \\
    & \Phi_u(x) = \Phi_{u + 4}(x)
\end{aligned}
$$

and so on.

Therefore, for any given $u$, there are infinitely many different numbers $v$ such that $\Phi_u(x) = \Phi_v(x)$

Note that the function $f(u,n)$ is just an example and there are infinitely many different functions that can be used to map $u$ to $v$ while they produce the same output.

---

## Page 77, Problem 2

### (a)

> **Problem**: Let:
>
> $$
> \begin{aligned}
>     & H_1(x) =
>     \begin{cases}
>         1 & if\; \Phi(x, x) \downarrow
>         \\
>         \uparrow & \text{Otherwise}
>     \end{cases}
> \end{aligned}
> $$
>
> Show that $H_1(x)$ is partially computable.

We will write a program for it:

$$
\begin{aligned}
    & Z_1 \leftarrow \Phi(X_1, X_1)
    \\
    & Y \leftarrow Y + 1
\end{aligned}
$$

---

### (b)

> **Problem**: Let $A = \{a_1, \dots, a_n\}$ be a finite set such that $\forall\; 1 \leq i \leq n \;:\; \Phi(a_i, a_i) \uparrow$ and let:
>
> $$
> \begin{aligned}
>     & H_2(x) =
>     \begin{cases}
>         1 & if\; \Phi(x, x) \downarrow
>         \\
>         0 & if\; x \in A
>         \\
>         \uparrow & \text{Otherwise}
>     \end{cases}
> \end{aligned}
> $$
>
> Show that $H_2(x)$ is partially computable.

We will write a program for it:

$$
\begin{aligned}
    & IF\; X_1 = a_1 \;GOTO\; E
    \\
    & IF\; X_1 = a_2 \;GOTO\; E
    \\
    & \vdots
    \\
    & IF\; X_1 = a_n \;GOTO\; E
    \\
    & Z_1 \leftarrow \Phi(X_1, X_1)
    \\
    & Y \leftarrow Y + 1
\end{aligned}
$$

---

## Page 84, Problem 4

> **Problem**: Let $B = \{f(n) \;|\; n \in \N\}$, where $f$ is a strictly increasing computable function [i.e., $\forall\; n \;:\; f(n + 1) \gt f(n)$]. Prove that $B$ is recursive.

A set $S$ is called recursive if there is a computable function $g$ such that for any $x$, $x \in S$ if and only if $g(x) = 1$.

In order to prove that $B = \{f(n) \;|\; n \in \N\}$ is recursive, we need to find a computable function $g$ that can decide whether a given number $x$ is an element of $B$ or not.

Since $f$ is a strictly increasing computable function, we can use binary search algorithm to find the smallest $n$ such that $f(n) \geq x$, and then check if $f(n) = x$.

We can create a computable function $g(x)$ that takes a number $x$ as input, and uses the binary search algorithm to find the smallest $n$ such that $f(n) \geq x$. If $f(n) = x$, then $g(x) = 1$, indicating that $x$ is an element of $B$. Otherwise, $g(x) = 0$, indicating that $x$ is not an element of $B$.

Therefore, we have found a computable function $g$ that can decide whether a given number $x$ is an element of $B$ or not, and thus $B$ is recursive.

---

## Page 84, Problem 10

### (a)

> **Problem**: Let $A = \{y \;|\; (\exists\; t) P(t, y)\}$, where $P$ is a computable predicate. Show that $A$ is r.e.

A set $S$ is called recursive if there is a computable function $g$ such that for any $x$, $x \in S$ if and only if $g(x) = 1$. A set $S$ is called recursively enumerable (r.e.) if there is a computable function $h$ such that for any $x$, if $x \in S$ then $h(x) = 1$.

In order to prove that $A = \{y \;|\; (\exists\; t) P(t, y)\}$ is recursively enumerable, we need to find a computable function $h$ that can decide whether a given number $y$ is an element of $A$ or not.

We can create a computable function $h(y)$ that takes a number $y$ as input, and for each natural number $t$ in turn, it checks if $P(t, y)$ holds. If there exists some $t$ such that $P(t, y)$ holds, then $h(y) = 1$, indicating that $y$ is an element of $A$. Otherwise, $h(y) = 0$, indicating that $y$ is not an element of $A$.

Therefore, we have found a computable function $h$ that can decide whether a given number $y$ is an element of $A$ or not, and thus $A$ is recursively enumerable.

It's worth noting that the function $h$ is an example of a general algorithm called the "Turing Machine", which is a theoretical model of a general-purpose computer that can be adapted to perform the task of any other computable algorithm.

---

### (b)

> **Problem**: Let $B = \{y \;|\; (\exists\; t_1) \dots (\exists\; t_n) Q(t_1, \dots, t_n, y)\}$, where $Q$ is a computable predicate. Show that $B$ is r.e.

A set $S$ is called recursive if there is a computable function $g$ such that for any $x$, $x \in S$ if and only if $g(x) = 1$. A set $S$ is called recursively enumerable (r.e.) if there is a computable function $h$ such that for any $x$, if $x \in S$ then $h(x) = 1$.

In order to prove that $B = \{y \;|\; (\exists\; t_1) \dots (\exists\; t_n) Q(t_1, \dots, t_n, y)\}$ is recursively enumerable, we need to find a computable function $h$ that can decide whether a given number $y$ is an element of $B$ or not.

We can create a computable function $h(y)$ that takes a number $y$ as input, and for each natural number $t_1, \dots, t_n$ in turn, it checks if $Q(t_1, \dots, t_n, y)$ holds. If there exists some $t_1, \dots, t_n$ such that $Q(t_1, \dots, t_n, y)$ holds, then $h(y) = 1$, indicating that $y$ is an element of $B$. Otherwise, $h(y) = 0$, indicating that $y$ is not an element of $B$.

Therefore, we have found a computable function $h$ that can decide whether a given number $y$ is an element of $B$ or not, and thus $B$ is recursively enumerable.

It is important to note that, similar to the previous answer, this function $h$ is not a specific algorithm but a general algorithm that can be adapted to perform the task of any other computable algorithm.

---

## Page 84, Problem 11

> **Problem**: Give a computable predicate $R(x, y)$ such that $\{y \;|\; (\forall\; t) R(t, y)\}$ is not r.e.

Suppose $R(t, y) = \neg STP(l(t), y, r(t))$, we can show that:

$$
\begin{aligned}
    & A = \{y \;|\; (\forall\; t) R(t, y)\}
    \\ \iff
    & A = \{y \;|\; (\forall\; t) \neg STP(l(t), y, r(t)) \}
    \\ \iff
    & A = \{y \;|\; (\forall\; t) \neg HALT(t, y) \}
    \\ \iff
    & A = \{y \;|\; W_y = \empty \}
\end{aligned}
$$

We know that $W_y = \empty$ is not $R.E$ so the given set is not $R.E$.

---
