# ACT Answers

-   **Answer Set**: No. 01
-   **Full Name**: Mohammad Hosein Nemati
-   **Student Code**: `610300185`

---

## Problem 1

### (a)

> **Problem**: Write a program using macro like $W \leftarrow f(V_1, \dots, V_n)$ to compute $f(x) = \sqrt{x}$.

First, we need to define a macro named $Y \leftarrow pow2(X)$ to write the $X^2 = X \times X$ into the $Y$:

$$
\begin{aligned}
    & Z_1 \leftarrow X_1
    \\
    [A_1]\; & IF\; Z_1 \neq 0 \;GOTO\; A_2
    \\
    & GOTO\; E
    \\
    [A_2]\; & Z_1 \leftarrow Z_1 - 1
    \\
    & Z_2 \leftarrow X_1
    \\
    [A_3]\; & IF\; Z_2 \neq 0 \;GOTO\; A_4
    \\
    & GOTO\; A_1
    \\
    [A_4]\; & Z_2 \leftarrow Z_2 - 1
    \\
    & Y \leftarrow Y + 1
    \\
    & GOTO\; A_3
\end{aligned}
$$

Second, we need to define a macro named $Y \leftarrow greater(X_1, X_2)$ to check the predicate $X_1 \gt X_2$:

$$
\begin{aligned}
    [A_1]\; & IF\; X_1 \neq 0 \;GOTO\; A_2
    \\
    & GOTO\; E
    \\
    [A_2]\; & IF\; X_2 \neq 0 \;GOTO\; A_3
    \\
    & Y \leftarrow Y + 1
    \\
    & GOTO\; E
    \\
    [A_3]\; & X_1 \leftarrow X_1 - 1
    \\
    & X_2 \leftarrow X_2 - 1
    \\
    & GOTO\; A_1
\end{aligned}
$$

Now, we can write our final program:

$$
\begin{aligned}
    & Z_1 \leftarrow 0
    \\
    [A_1]\; & Z_2 \leftarrow pow2(Z_1)
    \\
    & IF\; greater(Z_2, X_1) \;GOTO\; A_2
    \\
    & Z_1 \leftarrow Z_1 + 1
    \\
    & GOTO\; A_1
    \\
    [A_2]\; & Z_1 \leftarrow Z_1 - 1
    \\
    & IF\; Z_1 \neq 0 \;GOTO\; A_3
    \\
    & GOTO\; E
    \\
    [A_3]\; & Y \leftarrow Y + 1
    \\
    & GOTO\; A_2
\end{aligned}
$$

---

### (b)

> **Problem**: Rewrite your program using macro expansion.

$$
\begin{aligned}
    & Z_1 \leftarrow 0
    \\
    \\
    [A_1]\; & Z_4 \leftarrow 0
    \\
    & Z_5 \leftarrow X_1
    \\
    & Z_6 \leftarrow 0
    \\
    & Z_6 \leftarrow Z_5
    \\
    [A_4]\; & IF\; Z_6 \neq 0 \;GOTO\; A_5
    \\
    & GOTO\; E_4
    \\
    [A_5]\; & Z_6 \leftarrow Z_6 - 1
    \\
    & Z_2 \leftarrow Z_5
    \\
    [A_6]\; & IF\; Z_2 \neq 0 \;GOTO\; A_7
    \\
    & GOTO\; A_4
    \\
    [A_7]\; & Z_2 \leftarrow Z_2 - 1
    \\
    & Z_4 \leftarrow Z_4 + 1
    \\
    & GOTO\; A_6
    \\
    [E_4]\; & Z_2 \leftarrow Z4
    \\
    \\
    & Z_8 \leftarrow 0
    \\
    & Z_9 \leftarrow X_1
    \\
    & Z_{10} \leftarrow X_2
    \\
    [A_8]\; & IF\; Z_9 \neq 0 \;GOTO\; A_9
    \\
    & GOTO\; E
    \\
    [A_9]\; & IF\; Z_{10} \neq 0 \;GOTO\; A_{10}
    \\
    & Z_8 \leftarrow Z_8 + 1
    \\
    & GOTO\; E_8
    \\
    [A_{10}]\; & Z_9 \leftarrow Z_9 - 1
    \\
    & Z_{10} \leftarrow Z_{10} - 1
    \\
    & GOTO\; A_8
    \\
    [E_8]\; & IF\; Z_8 \neq 0 \;GOTO\; A_2
    \\
    \\
    & Z_1 \leftarrow Z_1 + 1
    \\
    & GOTO\; A_1
    \\
    [A_2]\; & Z_1 \leftarrow Z_1 - 1
    \\
    & IF\; Z_1 \neq 0 \;GOTO\; A_3
    \\
    & GOTO\; E
    \\
    [A_3]\; & Y \leftarrow Y + 1
    \\
    & GOTO\; A_2
\end{aligned}
$$

---

## Problem 2

> **Problem**: Write a progrem without macro to compute $\Psi_P^{(1)}(r) = r - 2$.

$$
\begin{aligned}
    & X_1 \leftarrow X_1 - 1
    \\
    & X_1 \leftarrow X_1 - 1
    \\
    [A_1]\; & IF\; X_1 \neq 0 \;GOTO\; A_2
    \\
    & GOTO\; E
    \\
    [A_2]\; & X_1 \leftarrow X_1 - 1
    \\
    & Y \leftarrow Y + 1
    \\
    & GOTO\; A_1
\end{aligned}
$$

---

## Problem 3

### (a)

> **Problem**: Write a program using macro like $W \leftarrow P(V)$ to compute $\Psi_P^{(1)}(r) = r - 4$.

First, we need to define a macro named $Y \leftarrow copy(X)$ to copy content of variable $X$ into $Y$:

$$
\begin{aligned}
    [A_1]\; & IF\; X_1 \neq 0 \;GOTO\; A_2
    \\
    & GOTO\; A_3
    \\
    [A_2]\; & X_1 \leftarrow X_1 - 1
    \\
    & Z_1 \leftarrow Z_1 + 1
    \\
    & GOTO\; A_1
    \\
    [A_3]\; & IF\; Z_1 \neq 0 \;GOTO\; A_4
    \\
    & GOTO\; E
    \\
    [A_4]\; & Z_1 \leftarrow Z_1 - 1
    \\
    & X_1 \leftarrow X_1 + 1
    \\
    & Y \leftarrow Y + 1
    \\
    & GOTO\; A_3
\end{aligned}
$$

Now, we can write program using this macro:

$$
\begin{aligned}
    & X_1 \leftarrow X_1 - 1
    \\
    & X_1 \leftarrow X_1 - 1
    \\
    & X_1 \leftarrow X_1 - 1
    \\
    & X_1 \leftarrow X_1 - 1
    \\
    & Y \leftarrow copy(X_1)
\end{aligned}
$$

---

### (b)

> **Problem**: Rewrite your program using macro expansion.

$$
\begin{aligned}
    & X_1 \leftarrow X_1 - 1
    \\
    & X_1 \leftarrow X_1 - 1
    \\
    & X_1 \leftarrow X_1 - 1
    \\
    & X_1 \leftarrow X_1 - 1
    \\
    \\
    & Z_1 \leftarrow 0
    \\
    & Z_2 \leftarrow X_1
    \\
    & Z_3 \leftarrow 0
    \\
    [A_1]\; & IF\; Z_2 \neq 0 \;GOTO\; A_2
    \\
    & GOTO\; A_3
    \\
    [A_2]\; & Z_2 \leftarrow Z_2 - 1
    \\
    & Z_3 \leftarrow Z_3 + 1
    \\
    & GOTO\; A_1
    \\
    [A_3]\; & IF\; Z_3 \neq 0 \;GOTO\; A_4
    \\
    & GOTO\; E_1
    \\
    [A_4]\; & Z_3 \leftarrow Z_3 - 1
    \\
    & Z_2 \leftarrow Z_2 + 1
    \\
    & Z_1 \leftarrow Z_1 + 1
    \\
    & GOTO\; A_3
    \\
    [E_1]\; & Y \leftarrow Z_1
\end{aligned}
$$

---

## Problem 4

> **Problem**: Predicate $P(x_1, x_2)$ is defined like bellow:
>
> $$
> \begin{aligned}
>     & P(x_1, x_2) =
>     \begin{cases}
>         1 & x_1 \geq 2x_2 + 3
>         \\
>         0 & otherwise
>     \end{cases}
> \end{aligned}
> $$

---

### (a)

> **Problem**: Write a program without macro to compute $P(x_1, x_2)$.

First, we should write a macro to compute $f(x) = 2x + 3$:

$$
\begin{aligned}
    [A_1]\; & IF\; X \neq 0 \;GOTO\; A_2
    \\
    & Y \leftarrow Y + 1
    \\
    & Y \leftarrow Y + 1
    \\
    & Y \leftarrow Y + 1
    \\
    & GOTO\; E
    \\
    [A_2]\; & X \leftarrow X - 1
    \\
    & Y \leftarrow Y + 1
    \\
    & Y \leftarrow Y + 1
    \\
    & GOTO\; A_1
\end{aligned}
$$

Now, we should write a macro to compute $g(x_1, x_2) = x_1 \geq x_2$:

$$
\begin{aligned}
    [A_1]\; & IF\; X_2 \neq 0 \;GOTO\; A_2
    \\
    & Y \leftarrow Y + 1
    \\
    & GOTO\; E
    \\
    [A_2]\; & IF\; X_1 \neq 0 \;GOTO\; A_3
    \\
    & GOTO\; E
    \\
    [A_3]\; & X_1 \leftarrow X_1 - 1
    \\
    & X_2 \leftarrow X_2 - 1
    \\
    & GOTO\; A_1
\end{aligned}
$$

Now, we should write a program to compute $g(x_1, f(x_2))$:

$$
\begin{aligned}
    & Z_2 \leftarrow Z_2 + 1
    \\
    [A_1]\; & IF\; X_2 \neq 0 \;GOTO\; A_2
    \\
    & Z_1 \leftarrow Z_1 + 1
    \\
    & Z_1 \leftarrow Z_1 + 1
    \\
    & Z_1 \leftarrow Z_1 + 1
    \\
    & IF\; Z_2 \neq 0 \;GOTO\; B_1
    \\
    [A_2]\; & X_2 \leftarrow X_2 - 1
    \\
    & Z_1 \leftarrow Z_1 + 1
    \\
    & Z_1 \leftarrow Z_1 + 1
    \\
    & IF\; Z_2 \neq 0 \;GOTO\; A_1
    \\
    [B_1]\; & IF\; Z_1 \neq 0 \;GOTO\; B_2
    \\
    & Y \leftarrow Y + 1
    \\
    & IF\; Z_2 \neq 0 \;GOTO\; E_1
    \\
    [B_2]\; & IF\; X_1 \neq 0 \;GOTO\; B_3
    \\
    & IF\; Z_2 \neq 0 \;GOTO\; E_1
    \\
    [B_3]\; & X_1 \leftarrow X_1 - 1
    \\
    & Z_1 \leftarrow Z_1 - 1
    \\
    & IF\; Z_2 \neq 0 \;GOTO\; B_1
\end{aligned}
$$

---

### (b)

> **Problem**: Write all snapshots on computing $P(5, 2)$.

Each snapshot is in the form $\braket{i, [Y, X_1, Z_1, X_2, Z_2]}$:

$$
\begin{aligned}
    & \braket{1, [0, 5, 0, 2, 0]} \\
    & \braket{2, [0, 5, 0, 2, 1]} \\
    & \braket{7, [0, 5, 0, 2, 1]} \\
    & \braket{8, [0, 5, 0, 1, 1]} \\
    & \braket{9, [0, 5, 1, 1, 1]} \\
    & \braket{10, [0, 5, 2, 1, 1]} \\
    & \braket{2, [0, 5, 2, 1, 1]} \\
    & \braket{7, [0, 5, 2, 1, 1]} \\
    & \braket{8, [0, 5, 2, 0, 1]} \\
    & \braket{9, [0, 5, 3, 0, 1]} \\
    & \braket{10, [0, 5, 4, 0, 1]} \\
    & \braket{2, [0, 5, 4, 0, 1]} \\
    & \braket{3, [0, 5, 4, 0, 1]} \\
    & \braket{4, [0, 5, 5, 0, 1]} \\
    & \braket{5, [0, 5, 6, 0, 1]} \\
    & \braket{6, [0, 5, 7, 0, 1]} \\
    & \braket{11, [0, 5, 7, 0, 1]} \\
    & \braket{14, [0, 5, 7, 0, 1]} \\
    & \braket{16, [0, 5, 7, 0, 1]} \\
    & \braket{17, [0, 4, 7, 0, 1]} \\
    & \braket{18, [0, 4, 6, 0, 1]} \\
    & \braket{11, [0, 4, 6, 0, 1]} \\
    & \braket{14, [0, 4, 6, 0, 1]} \\
    & \braket{16, [0, 4, 6, 0, 1]} \\
    & \braket{17, [0, 3, 6, 0, 1]} \\
    & \braket{18, [0, 3, 5, 0, 1]} \\
    & \braket{11, [0, 3, 5, 0, 1]} \\
    & \braket{14, [0, 3, 5, 0, 1]} \\
    & \braket{16, [0, 3, 5, 0, 1]} \\
    & \braket{17, [0, 2, 5, 0, 1]} \\
    & \braket{18, [0, 2, 4, 0, 1]} \\
    & \braket{11, [0, 2, 4, 0, 1]} \\
    & \braket{14, [0, 2, 4, 0, 1]} \\
    & \braket{16, [0, 2, 4, 0, 1]} \\
    & \braket{17, [0, 1, 4, 0, 1]} \\
    & \braket{18, [0, 1, 3, 0, 1]} \\
    & \braket{11, [0, 1, 3, 0, 1]} \\
    & \braket{14, [0, 1, 3, 0, 1]} \\
    & \braket{16, [0, 1, 3, 0, 1]} \\
    & \braket{17, [0, 0, 3, 0, 1]} \\
    & \braket{18, [0, 0, 2, 0, 1]} \\
    & \braket{11, [0, 0, 2, 0, 1]} \\
    & \braket{14, [0, 0, 2, 0, 1]} \\
    & \braket{15, [0, 0, 2, 0, 1]} \\
\end{aligned}
$$

---
