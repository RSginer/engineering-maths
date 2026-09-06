# 5️⃣ Grado de un polinomio (explicado paso a paso)

El "grado" de un polinomio es simplemente un número que nos dice **qué tan grande** es ese polinomio cuando $x$ se hace muy grande. Vamos a verlo con calma.

---

## ¿Qué es un polinomio?

Es una suma de términos, donde cada término es un número multiplicado por $x$ elevado a alguna potencia:

$$
3x^2-5x+4
$$

Aquí tenemos tres términos: $3x^2$, $-5x$, y $4$.

---

## ¿Qué es el grado?

El grado es **el exponente más alto** que aparece en el polinomio.

### Ejemplos

| Polinomio | Grado | ¿Por qué? |
|---|---|---|
| $5$ | 0 | Es como $5x^0$ (porque $x^0=1$) |
| $3x+2$ | 1 | El exponente más alto de $x$ es 1 |
| $3x^2-5x+4$ | 2 | El exponente más alto de $x$ es 2 |
| $x^3+2x-1$ | 3 | El exponente más alto de $x$ es 3 |

**Truco:** busca el número más grande que está "volando" arriba de una $x$ (el exponente), y ese es el grado.

---

## El coeficiente principal

Es el número que **multiplica** al término de mayor grado.

Ejemplo: en $4x^2-3x+1$, el término de mayor grado es $4x^2$ (grado 2), así que el coeficiente principal es **4**.

---

## ¿Por qué importa comparar grados?

Cuando tenemos una fracción de dos polinomios:

$$
\frac{P(x)}{Q(x)}
$$

y $x$ se hace **muy, muy grande** (tiende a $+\infty$), lo que más importa es **quién crece más rápido**: el de arriba o el de abajo. Y eso se decide comparando los grados.

### Intuición con números grandes

Imagina que $x=1000$:

- Si el numerador es de grado 1 ($3x$) → da $3000$
- Si el denominador es de grado 2 ($x^2$) → da $1{,}000{,}000$

La fracción sería $\dfrac{3000}{1000000}$, un número **muy pequeño**, casi 0. Cuanto más grande sea $x$, más se acerca a 0. Por eso, cuando el grado de abajo es mayor, el límite en el infinito es 0.

Si en cambio ambos tuvieran el mismo grado, por ejemplo $4x^2$ arriba y $2x^2$ abajo, al hacerse $x$ muy grande, los términos con menor grado ($-3x$, $+1$, $+5x$, $-7$, etc.) se vuelven insignificantes comparados con los términos de $x^2$, y lo que domina es la razón entre los coeficientes principales: $\dfrac{4}{2}=2$.

---

## Resumen de comparación de grados (fracciones de polinomios cuando $x\to\infty$)

| Situación | Qué pasa | Resultado |
|---|---|---|
| Grado arriba = grado abajo | Se "empatan" en velocidad de crecimiento | Cociente de coeficientes principales |
| Grado arriba < grado abajo | Abajo crece mucho más rápido | 0 |
| Grado arriba > grado abajo | Arriba crece mucho más rápido | $\pm\infty$ |

---

## 🧠 Por qué importa esto para los límites

Los Ejercicios 4 y 5 del examen (límites cuando $x\to+\infty$) se resuelven **directamente** comparando el grado del numerador y del denominador, sin necesidad de operaciones complicadas. Si sabes identificar el grado y el coeficiente principal de un polinomio, estos ejercicios son casi automáticos.
