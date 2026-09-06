# ✅ Soluciones — Examen de Cálculo (Límites)

---

## Ejercicio 1 — Cálculo directo

$$
\lim_{x\to2}(3x^2-5x+4) = 3(2)^2-5(2)+4 = 12-10+4 = 6
$$

**Resultado:** 6

![Gráfica del Ejercicio 1](img/ejercicio1.png)

---

## Ejercicio 2 — Indeterminación $0/0$

$$
\lim_{x\to3}\frac{x^2-9}{x-3}
$$

1. Al sustituir directamente: $0/0$ (indeterminación).
2. Tipo de indeterminación: $0/0$.
3. Factorizamos y simplificamos:
$$
\frac{x^2-9}{x-3}=\frac{(x-3)(x+3)}{x-3}=x+3
$$
4. Sustituimos $x=3$: $3+3=6$

**Resultado:** 6

![Gráfica del Ejercicio 2](img/ejercicio2.png)

---

## Ejercicio 3 — Límites laterales e infinitos $k/0$

$$
f(x)=\frac{x^2+x+2}{x+1}
$$

En $x=-1$: numerador $=1-1+2=2$ (positivo), denominador $=0$ → forma $2/0$ (infinito, no indeterminación).

- Por la izquierda ($x\to-1^-$): $x+1\to0^-$, numerador $\approx2>0$ → $f(x)\to\dfrac{2}{0^-}=-\infty$
- Por la derecha ($x\to-1^+$): $x+1\to0^+$, numerador $\approx2>0$ → $f(x)\to\dfrac{2}{0^+}=+\infty$

Como los límites laterales son distintos ($-\infty \neq +\infty$), el **límite no existe** (asíntota vertical en $x=-1$).

**Resultado:** no existe (izq. $-\infty$, der. $+\infty$)

![Gráfica del Ejercicio 3](img/ejercicio3.png)

---
