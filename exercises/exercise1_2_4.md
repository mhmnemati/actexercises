# ACT Answers

-   **Answer Set**: No. 01, Part 02, Chapter 4
-   **Full Name**: Mohammad Hosein Nemati
-   **Student Code**: `610300185`

---

## Page 69, Problem 3

> **Problem**: Let $HALT^{1}(x)$ be defined $HALT^{1}(x) \iff HALT(l(x), r(x))$. Show that $HALT^{1}(x)$ is not computable.

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

---

### (c)

> **Problem**: Give an infinite set $B$ such that $\forall\; b \in B \;:\; \Phi(b, b) \uparrow$ and such that:
>
> $$
> \begin{aligned}
>     & H_3(x) =
>     \begin{cases}
>         1 & if\; \Phi(x, x) \downarrow
>         \\
>         0 & if\; x \in B
>         \\
>         \uparrow & \text{Otherwise}
>     \end{cases}
> \end{aligned}
> $$
>
> is partially computable.

---

### (d)

> **Problem**: Give an infinite set $C$ such that $\forall\; c \in C \;:\; \Phi(c, c) \uparrow$ and such that:
>
> $$
> \begin{aligned}
>     & H_4(x) =
>     \begin{cases}
>         1 & if\; \Phi(x, x) \downarrow
>         \\
>         0 & if\; x \in C
>         \\
>         \uparrow & \text{Otherwise}
>     \end{cases}
> \end{aligned}
> $$
>
> is not partially computable.

---

## Page 84, Problem 4

> **Problem**: Let $B = \{f(n) \;|\; n \in \N\}$, where $f$ is a strictly increasing computable function [i.e., $\forall\; n \;:\; f(n + 1) \gt f(n)$]. Prove that $B$ is recursive.

---

## Page 84, Problem 10

### (a)

> **Problem**: Let $A = \{y \;|\; (\exists\; t) P(t, y)\}$, where $P$ is a computable predicate. Show that $A$ is r.e.

---

### (b)

> **Problem**: Let $B = \{y \;|\; (\exists\; t_1) \dots (\exists\; t_n) Q(t_1, \dots, t_n, y)\}$, where $Q$ is a computable predicate. Show that $B$ is r.e.

---

## Page 84, Problem 11

> **Problem**: Give a computable predicate $R(x, y)$ such that $\{y \;|\; (\forall\; t) R(t, y)\}$ is not r.e.

---

## Page 87, Problem 1

> **Problem**: Given a partially computable function $f(x, y)$, find a primitive recursive function $g(u, v)$ such that
>
> $$
> \begin{aligned}
>     & \Phi_{g(u, v)}(x) = f(\Phi_u(x), \Phi_v(x))
> \end{aligned}
> $$

---

## Page 87, Problem 3

> **Problem**: Let us call a partially computable function $g(x)$ **extendable** if there is a computable function $f(x)$ such that $f(x) = g(x)$ for all $x$ for which $g(x) \downarrow$.
>
> Show that there is no algorithm for determining of a given $z$ whether or not $\Phi_z(x)$ is extendable. [Hint: Exercise 8 of Section 4 shows that $\Phi(x, x) + 1$ is not extendable. Find an extendable function $k(x)$ such that the function:
>
> $$
> \begin{aligned}
>     & h(x, t) =
>     \begin{cases}
>         \Phi(x, x) + 1 & if\; \Phi(t, t) \downarrow
>         \\
>         k(x) & \text{Otherwise}
>     \end{cases}
> \end{aligned}
> $$
>
> is partially computable.]

---

## Page 94, Problem 9

### (a)

---

### (b)

---

## Page 94, Problem 10

---

## Page 94, Problem 11

---

## Page 97, Problem 4

---

## Page 97, Problem 7

---

## Page 97, Problem 8

---

## Page 104, Problem 2

---

## Page 104, Problem 8

---

## Page 104, Problem 9

---

## Page 104, Problem 12

---

## Page 104, Problem 13

---
