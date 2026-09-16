---
name: latex-math-expert
description: >-
  Comprehensive guide and authoritative reference for formatting mathematical equations,
  statistical models, matrices, and scientific notation in LaTeX/MathJax within Obsidian and Markdown notes.
when_to_use: |
  - Writing mathematical, statistical, or computer science formulas in Markdown
  - Formatting matrices, systems of equations, calculus notation, and probability distributions
  - Debugging MathJax rendering errors, whitespace issues, or multi-line alignments in Obsidian
license: MIT
metadata:
  author: Gemini Notebook
  version: 1.0.0
---

# LaTeX & MathJax Mathematical Notation Skill

## Purpose
This skill provides complete, spec-valid instructions, syntax tables, and design patterns for formatting mathematics, calculus, linear algebra, discrete logic, and statistical distributions using LaTeX and MathJax inside Obsidian vaults and academic Markdown documents.

---

## 1. Syntax Rules & Delimiters in Obsidian

### 1.1 Inline Math (`$...$`)
- **Rule**: Single dollar signs with **no whitespace** immediately inside the delimiters.
- **Correct**: `$E = mc^2$` or `$P(A|B) = \frac{P(A \cap B)}{P(B)}$`
- **Incorrect**: `$ E = mc^2 $` (Leading/trailing spaces prevent MathJax parsing in Obsidian).

### 1.2 Display / Block Math (`$$...$$`)
- **Rule**: Double dollar signs placed on separate lines enclosing the equation block:
  ```latex
  $$
  f(x) = \frac{1}{\sigma \sqrt{2\pi}} \exp\left( -\frac{1}{2}\left(\frac{x - \mu}{\sigma}\right)^2 \right)
  $$
  ```

---

## 2. Symbols, Greek Letters & Set Theory

### 2.1 Greek Alphabet

| Lowercase | Symbol | Uppercase | Symbol | Lowercase | Symbol | Uppercase | Symbol |
| :--- | :---: | :--- | :---: | :--- | :---: | :--- | :---: |
| `\alpha` | $\alpha$ | `A` | $A$ | `
u` | $
u$ | `N` | $N$ |
| `\beta` | $\beta$ | `B` | $B$ | `\xi` | $\xi$ | `\Xi` | $\Xi$ |
| `\gamma` | $\gamma$ | `\Gamma` | $\Gamma$ | `\pi`, `\varpi` | $\pi, \varpi$ | `\Pi` | $\Pi$ |
| `\delta` | $\delta$ | `\Delta` | $\Delta$ | `\rho`, `\varrho` | $\rho, \varrho$ | `P` | $P$ |
| `\epsilon`, `\varepsilon` | $\epsilon, \varepsilon$ | `E` | $E$ | `\sigma`, `\varsigma` | $\sigma, \varsigma$ | `\Sigma` | $\Sigma$ |
| `\zeta` | $\zeta$ | `Z` | $Z$ | `	au` | $	au$ | `T` | $T$ |
| `\eta` | $\eta$ | `H` | $H$ | `\upsilon` | $\upsilon$ | `\Upsilon` | $\Upsilon$ |
| `	heta`, `\vartheta` | $	heta, \vartheta$ | `\Theta` | $\Theta$ | `\phi`, `\varphi` | $\phi, \varphi$ | `\Phi` | $\Phi$ |
| `\iota` | $\iota$ | `I` | $I$ | `\chi` | $\chi$ | `X` | $X$ |
| `\kappa` | $\kappa$ | `K` | $K$ | `\psi` | $\psi$ | `\Psi` | $\Psi$ |
| `\lambda` | $\lambda$ | `\Lambda` | $\Lambda$ | `\omega` | $\omega$ | `\Omega` | $\Omega$ |
| `\mu` | $\mu$ | `M` | $M$ | — | — | — | — |

### 2.2 Set Theory, Logic & Number Systems

| Concept | Syntax | Rendered Output |
| :--- | :--- | :---: |
| **Number Sets** | `\mathbb{R}, \mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{C}` | $\mathbb{R}, \mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{C}$ |
| **Set Membership** | `x \in A, y 
otin B` | $x \in A, y 
otin B$ |
| **Subset / Superset** | `A \subset B, A \subseteq B, A \supset B, A \supseteq B` | $A \subset B, A \subseteq B, A \supset B, A \supseteq B$ |
| **Union / Intersection** | `A \cup B, A \cap B, A \setminus B, A^\complement` | $A \cup B, A \cap B, A \setminus B, A^\complement$ |
| **Empty Set** | `\emptyset, \varnothing` | $\emptyset, \varnothing$ |
| **Quantifiers** | `\forall x, \exists y, 
exists z` | $\forall x, \exists y, 
exists z$ |
| **Logical Connectives** | `P \land Q, P \lor Q, 
eg P, P \implies Q, P \iff Q` | $P \land Q, P \lor Q, 
eg P, P \implies Q, P \iff Q$ |

---

## 3. Arithmetic, Algebra & Calculus

### 3.1 Fractions, Roots & Powers

```latex
$$
\frac{a + b}{c + d}, \quad \dfrac{1}{1 + \dfrac{1}{x}}, \quad \sqrt{x^2 + y^2}, \quad \sqrt[n]{x_1 \cdot x_2 \dotsm x_n}
$$
```
$$
\frac{a + b}{c + d}, \quad \dfrac{1}{1 + \dfrac{1}{x}}, \quad \sqrt{x^2 + y^2}, \quad \sqrt[n]{x_1 \cdot x_2 \dotsm x_n}
$$

### 3.2 Sums, Products & Limits

```latex
$$
\lim_{x 	o 0} \frac{\sin x}{x} = 1, \quad \sum_{i=1}^{n} i = \frac{n(n+1)}{2}, \quad \prod_{k=1}^{n} k = n!
$$
```
$$
\lim_{x 	o 0} \frac{\sin x}{x} = 1, \quad \sum_{i=1}^{n} i = \frac{n(n+1)}{2}, \quad \prod_{k=1}^{n} k = n!
$$

### 3.3 Derivatives & Integrals

```latex
$$
\frac{df}{dx} = \lim_{\Delta x 	o 0} \frac{f(x+\Delta x) - f(x)}{\Delta x}, \quad \frac{\partial^2 f}{\partial x \partial y}, \quad 
abla f(\mathbf{x})
$$
$$
\int_{a}^{b} f(x) \, dx = F(b) - F(a), \quad \iint_{D} f(x, y) \, dx \, dy, \quad \oint_{C} \mathbf{F} \cdot d\mathbf{r}
$$
```

---

## 4. Linear Algebra & Matrices

### 4.1 Vectors & Norms
- Column Vector: $\mathbf{x} = \begin{bmatrix} x_1 \ x_2 \ \vdots \ x_n \end{bmatrix}$ (`\mathbf{x} = \begin{bmatrix} x_1 \ x_2 \ \vdots \ x_n \end{bmatrix}`)
- Vector Norms: $\lVert \mathbf{x} \rVert_2 = \sqrt{\sum_{i=1}^n x_i^2}$, $\lVert \mathbf{x} \rVert_1 = \sum_{i=1}^n |x_i|$, $\mathbf{x}^T \mathbf{y} = \mathbf{x} \cdot \mathbf{y}$

### 4.2 Matrix Environments

| Environment | Enclosing Delimiters | LaTeX Syntax Example | Output Preview |
| :--- | :--- | :--- | :---: |
| `matrix` | Plain (No brackets) | `\begin{matrix} a & b \ c & d \end{matrix}` | $\begin{matrix} a & b \ c & d \end{matrix}$ |
| `pmatrix` | Parentheses `( )` | `\begin{pmatrix} a & b \ c & d \end{pmatrix}` | $\begin{pmatrix} a & b \ c & d \end{pmatrix}$ |
| `bmatrix` | Square Brackets `[ ]` | `\begin{bmatrix} a & b \ c & d \end{bmatrix}` | $\begin{bmatrix} a & b \ c & d \end{bmatrix}$ |
| `vmatrix` | Single Vertical Bars `\| \|` (Determinant) | `\begin{vmatrix} a & b \ c & d \end{vmatrix}` | $\begin{vmatrix} a & b \ c & d \end{vmatrix}$ |
| `Vmatrix` | Double Vertical Bars `\|\| \|\|` | `\begin{Vmatrix} a & b \ c & d \end{Vmatrix}` | $\begin{Vmatrix} a & b \ c & d \end{Vmatrix}$ |

```latex
$$
\mathbf{A} = \begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \
a_{21} & a_{22} & \cdots & a_{2n} \
\vdots & \vdots & \ddots & \vdots \
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{bmatrix}, \quad
\det(\mathbf{A}) = \begin{vmatrix}
a & b \
c & d
\end{vmatrix} = ad - bc
$$
```

---

## 5. Probability, Statistics & Machine Learning Models

### 5.1 Common Statistical Operators

```latex
$$
\mathbb{E}[X] = \int_{-\infty}^{\infty} x f(x) \, dx, \quad 	ext{Var}(X) = \mathbb{E}[(X - \mu)^2] = \mathbb{E}[X^2] - (\mathbb{E}[X])^2
$$
$$
	ext{Cov}(X, Y) = \mathbb{E}[(X - \mu_X)(Y - \mu_Y)], \quad \rho_{X,Y} = \frac{	ext{Cov}(X, Y)}{\sigma_X \sigma_Y}
$$
```

### 5.2 Bayes' Theorem & Total Probability

```latex
$$
P(B_k | A) = \frac{P(A | B_k) P(B_k)}{P(A)} = \frac{P(A | B_k) P(B_k)}{\sum_{i=1}^{n} P(A | B_i) P(B_i)}
$$
```

### 5.3 Loss Functions & Machine Learning Equations

```latex
$$
\mathcal{L}_{	ext{MSE}}(\mathbf{w}) = \frac{1}{N} \sum_{i=1}^{N} \left( y_i - \mathbf{w}^T \mathbf{x}_i \right)^2 + \lambda \lVert \mathbf{w} \rVert_2^2
$$
$$
\sigma(z) = \frac{1}{1 + e^{-z}}, \quad 	ext{Softmax}(\mathbf{z})_i = \frac{e^{z_i}}{\sum_{j=1}^{K} e^{z_j}}
$$
```

---

## 6. Multi-line Alignments, Piecewise & Systems

### 6.1 `aligned` Environment (Aligned Equations)
Use `&` as alignment anchors and `\` for line breaks:
```latex
$$
\begin{aligned}

abla \cdot \mathbf{E} &= \frac{\rho}{\varepsilon_0} \

abla \cdot \mathbf{B} &= 0 \

abla 	imes \mathbf{E} &= -\frac{\partial \mathbf{B}}{\partial t} \

abla 	imes \mathbf{B} &= \mu_0 \mathbf{J} + \mu_0 \varepsilon_0 \frac{\partial \mathbf{E}}{\partial t}
\end{aligned}
$$
```

### 6.2 `cases` Environment (Piecewise Functions)
```latex
$$
f(x) = \begin{cases}
\frac{\sin x}{x}, & 	ext{if } x 
eq 0 \
1, & 	ext{if } x = 0
\end{cases}
$$
```

---

## 7. Math Typography, Fonts & Spacing

| Command | Usage / Effect | Example |
| :--- | :--- | :--- |
| `	ext{word}` | Normal upright text inside math mode | `x 	ext{ is positive}` $\rightarrow x 	ext{ is positive}$ |
| `\mathbf{X}` | Bold upright font (Vectors, Matrices) | `\mathbf{A}, \mathbf{x}` $\rightarrow \mathbf{A}, \mathbf{x}$ |
| `\mathbb{R}` | Blackboard Bold (Sets, Expected values) | `\mathbb{R}, \mathbb{E}` $\rightarrow \mathbb{R}, \mathbb{E}$ |
| `\mathcal{L}` | Calligraphic font (Loss functions, Sets) | `\mathcal{L}, \mathcal{N}` $\rightarrow \mathcal{L}, \mathcal{N}$ |
| `\boldsymbol{	heta}` | Bold Greek letters / symbols | `\boldsymbol{	heta}, \boldsymbol{\mu}` $\rightarrow \boldsymbol{	heta}, \boldsymbol{\mu}$ |
| `\,` | Thin space | `\int f(x)\,dx` |
| `\quad` | 1 em space | `x = 1 \quad y = 2` |
| `\qquad` | 2 em space | `x = 1 \qquad y = 2` |

---

## 8. Obsidian-Specific Best Practices & Error Prevention

1. **Frontmatter YAML Conflicts**: If an equation contains colons `:` or brackets `[]` inside a frontmatter string, always wrap the property value in double quotes (`"`).
2. **Escaping in Tables**: When rendering LaTeX formulas inside Markdown tables, pipe characters `|` inside math (like absolute values `$|x|$` or conditional probability `$P(A|B)$`) must be written as `\vert` or `\mid` (e.g., `$P(A \mid B)$`) to avoid breaking Markdown table cell borders.
3. **Parentheses Sizing**: Always use `\left(` and `\right)` (or `\left[`, `\right]`, `\left\{`, `\right\}`) around tall fractions and matrices to scale delimiters automatically.
