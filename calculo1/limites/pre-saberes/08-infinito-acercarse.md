# 8️⃣ El concepto de infinito y de "acercarse a" (explicado paso a paso)

Esta es quizás la idea más importante de todo el tema de límites, y también la más abstracta. Vamos a construirla poco a poco con ejemplos muy sencillos.

---

## El infinito no es un número

El símbolo $\infty$ **no representa un número concreto**. Representa la idea de **"crecer sin parar, sin llegar nunca a un tope"**.

Imagina que cuentas: 1, 2, 3, 4, 5... Por muy alto que llegues, siempre puedes seguir contando uno más. Nunca "llegas" al infinito, simplemente el proceso de contar **no tiene fin**. Eso es lo que significa $\infty$.

Por eso, cuando escribimos:

$$
\lim_{x\to+\infty} f(x)
$$

no estamos preguntando "¿qué pasa cuando $x$ es infinito?" (eso no tiene sentido, porque $x$ nunca *llega* a ser infinito). Estamos preguntando: **"¿qué le pasa a $f(x)$ a medida que $x$ se hace cada vez más y más grande, sin parar?"**

---

## La idea de "acercarse a" un valor

Cuando escribimos $x\to a$ ($x$ tiende a $a$), estudiamos qué ocurre para valores de $x$ **cada vez más cercanos** a $a$. El valor exacto $x=a$ se deja fuera del análisis: puede estar definido o no, pero no determina el límite.

### Ejemplo con números concretos

Supongamos que $a=3$. Valores de $x$ acercándose a 3 por la izquierda:

$$
2 \to 2.9 \to 2.99 \to 2.999 \to 2.9999 \to \dots
$$

Y por la derecha:

$$
4 \to 3.1 \to 3.01 \to 3.001 \to 3.0001 \to \dots
$$

La distancia $|x-3|$ se hace cada vez menor. Eso es lo importante; el valor que tenga la función justo en $x=3$ se estudia aparte.

- Si $x$ se acerca desde números **menores** que $a$, escribimos $x\to a^-$.
- Si $x$ se acerca desde números **mayores** que $a$, escribimos $x\to a^+$.

---

## ¿Qué significa que algo "tienda a 0"?

Cuando decimos que una cantidad tiende a $0^+$, queremos decir que se hace **cada vez más pequeña, pero manteniéndose positiva** (por ejemplo: 0.1, 0.01, 0.001, 0.0001...).

Si tiende a $0^-$, se hace cada vez más pequeña en valor absoluto pero manteniéndose **negativa** (-0.1, -0.01, -0.001...).

---

## ¿Qué pasa si divides un número entre algo que tiende a 0?

Esta es la clave para entender los límites infinitos. Observa qué ocurre con $1/t$ cuando $t$ es positivo y se acerca a cero:

- $1\div0.1=10$
- $1\div0.01=100$
- $1\div0.001=1000$

Cuanto más pequeño es el número por el que divides (más cerca de 0), **más grande** se hace el resultado. Por eso:

$$
\frac{1}{0^+}\to+\infty
$$

Y si divides entre un número negativo que se acerca a 0 (como -0.1, -0.01...):

$$
1\div(-0.1)=-10 \qquad 1\div(-0.01)=-100
$$

El resultado se hace **cada vez más negativo**, por eso:

$$
\frac{1}{0^-}\to-\infty
$$

Las expresiones $1/0^+$ y $1/0^-$ son abreviaturas para describir un proceso; no son divisiones reales entre cero.

![Valores de x acercándose a 3 mientras la función se acerca a 6](../animaciones/AcercamientoAlLimite.gif)

---

## Resumen visual

| Situación | Qué significa | Resultado |
|---|---|---|
| $x\to a^-$ | $x$ se acerca a $a$ desde valores menores | — |
| $x\to a^+$ | $x$ se acerca a $a$ desde valores mayores | — |
| $x\to+\infty$ | $x$ crece sin parar | — |
| $x\to-\infty$ | $x$ decrece sin parar (cada vez más negativo) | — |
| número positivo $\div\ 0^+$ | dividir entre algo positivo cada vez más pequeño | $+\infty$ |
| número positivo $\div\ 0^-$ | dividir entre algo negativo cada vez más pequeño (en valor absoluto) | $-\infty$ |

---

## 🧠 Por qué importa esto para los límites

Todo el examen gira en torno a estas dos ideas: **analizar valores arbitrariamente cercanos** y **crecer sin límite**. Si entiendes bien estas dos ideas con los ejemplos numéricos anteriores, comprenderás *por qué* funcionan las reglas de los límites en lugar de memorizarlas sin más.
