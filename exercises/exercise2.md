# ACT Answers

-   **Answer Set**: No. 02
-   **Full Name**: Mohammad Hosein Nemati
-   **Student Code**: `610300185`

---

## Problem 1

> **Problem**: Predicate $P(x_1, x_2)$ is defined like bellow, write a program without macro to compute P.
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
    [A_1]\; & IF\; X_2 \neq 0 \;GOTO\; A_2
    \\
    & Z_2 \leftarrow Z_2 + 1
    \\
    & Z_2 \leftarrow Z_2 + 1
    \\
    & Z_2 \leftarrow Z_2 + 1
    \\
    & GOTO\; B_1
    \\
    [A_2]\; & X_2 \leftarrow X_2 - 1
    \\
    & Z_2 \leftarrow Z_2 + 1
    \\
    & Z_2 \leftarrow Z_2 + 1
    \\
    & GOTO\; A_1
    \\
    [B_1]\; & IF\; Z_2 \neq 0 \;GOTO\; B_2
    \\
    & Y \leftarrow Y + 1
    \\
    & GOTO\; E
    \\
    [B_2]\; & IF\; X_1 \neq 0 \;GOTO\; B_3
    \\
    & GOTO\; E
    \\
    [B_3]\; & X_1 \leftarrow X_1 - 1
    \\
    & Z_2 \leftarrow Z_2 - 1
    \\
    & GOTO\; B_1
\end{aligned}
$$

---

## Problem 3

> **Problem**: For the functions $f, g: \N \rightarrow \N$ define $f, g$ like bellow, if $S, g$ both are computable, then is $f$ computable?
>
> $$
> \begin{aligned}
>     & S(x) = max\{f(x), g(x)\}
>     \\
>     & M(x) = min\{f(x), g(x)\}
> \end{aligned}
> $$

The $S(x)$ program is like bellow:

$$
\begin{aligned}
    & Z_1 \leftarrow f(X_1)
    \\
    & Z_2 \leftarrow g(X_1)
    \\
    & IF\; Z_1 \leq Z_2 \;GOTO\; A_1
    \\
    & Y \leftarrow Z_1
    \\
    & GOTO\; E
    \\
    [A_1]\; & Y \leftarrow Z_2
\end{aligned}
$$

The $M(x)$ program is like bellow:

$$
\begin{aligned}
    & Z_1 \leftarrow f(X_1)
    \\
    & Z_2 \leftarrow g(X_1)
    \\
    & IF\; Z_1 \geq Z_2 \;GOTO\; A_1
    \\
    & Y \leftarrow Z_1
    \\
    & GOTO\; E
    \\
    [A_1]\; & Y \leftarrow Z_2
\end{aligned}
$$

**Proof by contradiction**: first we assume that $f$ is not computable, as we can see, the programs $S(x), M(x)$ needs to compute $f(x)$ and compare the result with $g(x)$, so they will become uncomputable which is **contradiction**, so $f$ is computable.

---

## Problem 4

> **Problem**: Suppose $A$ is a $R.E$ set, prove $B = \{x^2+1 \;|\; x \in A\}$ is $R.E$.

$A$ is a $R.E$ set, so there exists a partial computable $f(x)$ which $A = \{x \in \N \;|\; f(x) \downarrow \}$

We can rewrite the $B$ as:

$$
\begin{aligned}
    & B = \{x^2+1 \;|\; x \in A\}
    \\ \implies
    & B = \{x \in \N \;|\; \sqrt{x - 1} \in A\}
    \\ \implies
    & B = \{x \in \N \;|\; f(\sqrt{x - 1}) \downarrow\}
\end{aligned}
$$

As we know $g(x) = \sqrt{x}$ and $h(x) = x - 1$ both are primitive recursive, and $f(x)$ is partially computable, so $f(g(h(x))) = f(\sqrt{x - 1})$ is partialy computable, so set $B$ is $R.E$.

---

## Problem 5

> **Problem**: Suppose $\Phi$ program number is $2^{46} . 5^{2} . 7^{37} - 1$, describe function $\Psi_{\Phi}^{(1)}$.

$$
\begin{aligned}
    & \#P = 2^{46} . 3^{0} . 5^{2} . 7^{37} - 1
    \\
    & \#P = [46, 0, 2, 7] - 1
    \\
    \\
    & \#I_1 = 46 = \braket{x, y} = 2^{x} . (2.y + 1) - 1 = \braket{0, 23} = \braket{0, \braket{3, 1}}
    \\
    & \#I_2 = 0 = \braket{x, y} = 2^{x} . (2.y + 1) - 1 = \braket{0, 0} = \braket{0, \braket{0, 0}}
    \\
    & \#I_3 = 2 = \braket{x, y} = 2^{x} . (2.y + 1) - 1 = \braket{0, 1} = \braket{0, \braket{1, 0}}
    \\
    & \#I_4 = 37 = \braket{x, y} = 2^{x} . (2.y + 1) - 1 = \braket{1, 9} = \braket{1, \braket{1, 2}}
\end{aligned}
$$

Now, we can encode each instruction into the human readable code:

$$
\begin{aligned}
    & \#I_1 = \braket{0, \braket{3, 1}}
    \\
    & IF\; X_1 \neq 0 \;GOTO\; A_1
    \\
    \\
    & \#I_1 = \braket{0, \braket{0, 0}}
    \\
    & Y \leftarrow Y
    \\
    \\
    & \#I_1 = \braket{0, \braket{1, 0}}
    \\
    & Y \leftarrow Y + 1
    \\
    \\
    & \#I_1 = \braket{1, \braket{1, 2}}
    \\
    [A_1]\; & Z_1 \leftarrow Z_1 + 1
\end{aligned}
$$

So, the program source code is:

$$
\begin{aligned}
    & IF\; X_1 \neq 0 \;GOTO\; A_1
    \\
    & Y \leftarrow Y
    \\
    & Y \leftarrow Y + 1
    \\
    [A_1]\; & Z_1 \leftarrow Z_1 + 1
\end{aligned}
$$

---

## Problem 6

> **Problem**: Prove that primitive recursive function $H(z)$ exists, such that:
>
> $$
> \begin{aligned}
>     & \Phi^{(1)}(x, H(z)) = \Phi^{(2)}(1396, x, z)
> \end{aligned}
> $$

As we can see, the program $z$ will compute $f(x_1, x_2)$, now we need to fix the first parameter of function with $1396$, so we need to add these lines to the begining of program $z$:

$$
\begin{aligned}
    [A_1]\; & X_1 \leftarrow X_1 - 1
    \\
    & IF\; X_1 \neq 0 \;GOTO\; A_1
    \\
    & \begin{rcases}
        X_1 \leftarrow X_1 + 1
        \\
        X_1 \leftarrow X_1 + 1
        \\
        \vdots
        \\
        X_1 \leftarrow X_1 + 1
    \end{rcases}\text{1396 times}
\end{aligned}
$$

Now, we must compute the new instructions code:

$$
\begin{aligned}
    [A_1]\; & X_1 \leftarrow X_1 - 1
    \\
    & \#I_1 = \braket{1, \braket{2, 1}} = \braket{1, 11} = 45
    \\
    \\
    & IF\; X_1 \neq 0 \;GOTO\; A_1
    \\
    & \#I_1 = \braket{0, \braket{3, 1}} = \braket{0, 23} = 46
    \\
    \\
    & X_1 \leftarrow X_1 + 1
    \\
    & \#I_1 = \braket{0, \braket{1, 1}} = \braket{0, 5} = 10
\end{aligned}
$$

Now, we must compute the program code which prepends new instructions:

$$
\begin{aligned}
    & z = [\#I_1, \#I_2, \dots, \#I_n] - 1 = \prod_{i=1}^{n} (p_i)^{(z+1)_i} - 1
    \\
    & n = Ln(z + 1)
    \\
    \\
    & H(z) = [45, 46, \overbrace{10, \dots, 10}^{\text{1396 times}}, (z+1)_1, (z+1)_2, \dots, (z+1)_n] - 1
    \\
    \\
    & H(z) = 2^{45} \times 3^{46} \times (\prod_{i=1}^{1396} (p_{i+2})^{10}) \times (\prod_{i=1}^{Ln(z+1)} (p_{i+1398})^{(z+1)_i})
\end{aligned}
$$

---
