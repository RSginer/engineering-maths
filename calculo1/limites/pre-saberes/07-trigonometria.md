# 7️⃣ Trigonometría básica (explicado paso a paso)

La trigonometría estudia los ángulos y los triángulos, y aquí vamos a centrarnos en lo mínimo necesario para entender el límite de la tangente.

---

## El círculo unidad

Imagina un círculo perfecto, de radio 1, centrado en el punto (0,0) de una gráfica. Si giras un punto alrededor de ese círculo, según el ángulo $x$ que gires, obtienes dos coordenadas:

- La coordenada horizontal es $\cos x$ (coseno)
- La coordenada vertical es $\sin x$ (seno)

Y la tangente se define como:

$$
\tan x = \frac{\sin x}{\cos x}
$$

Es literalmente una **división**, así que todo lo que sabemos de fracciones (¡y de que no se puede dividir entre 0!) se aplica aquí también.

---

## Ángulos notables (los que hay que memorizar)

| Ángulo | $\sin$ | $\cos$ | $\tan$ |
|---|---|---|---|
| $0$ | 0 | 1 | 0 |
| $\pi/6$ (30°) | $1/2$ | $\sqrt3/2$ | $\sqrt3/3$ |
| $\pi/4$ (45°) | $\sqrt2/2$ | $\sqrt2/2$ | 1 |
| $\pi/3$ (60°) | $\sqrt3/2$ | $1/2$ | $\sqrt3$ |
| $\pi/2$ (90°) | 1 | 0 | no existe (dividir entre 0) |

Fíjate en la última fila: en $\pi/2$, el coseno vale 0, así que la tangente (que divide entre el coseno) **no se puede calcular** ahí.

---

## Los cuadrantes y el signo

El círculo se divide en 4 partes (cuadrantes), y en cada uno el seno y el coseno tienen signos distintos:

| Cuadrante | Ángulos | $\sin x$ | $\cos x$ |
|---|---|---|---|
| 1º | $0$ a $\pi/2$ | + | + |
| 2º | $\pi/2$ a $\pi$ | + | - |
| 3º | $\pi$ a $3\pi/2$ | - | - |
| 4º | $3\pi/2$ a $2\pi$ | - | + |

**Truco para recordarlo:** en el primer cuadrante todo es positivo. Al pasar al segundo cuadrante, el coseno se vuelve negativo (pero el seno sigue positivo).

---

## ¿Dónde se anula el coseno?

El coseno vale 0 en:

$$
x=\frac{\pi}{2}+k\pi \quad (k=0,\pm1,\pm2,\dots)
$$

Es decir, en $\pi/2$, $3\pi/2$, $-\pi/2$, etc. Justo en esos puntos, la tangente **no está definida** (estaríamos dividiendo entre 0), y por lo tanto ahí aparecen **asíntotas verticales** en la gráfica de la tangente.

---

## Estudiando el signo de la tangente cerca de $\pi/2$

Vamos a ver qué pasa un poquito antes y un poquito después de $\pi/2$:

- **Un poco antes** de $\pi/2$ (todavía en el 1er cuadrante, ej. $89°$):
  - $\sin x$ es positivo (cercano a 1)
  - $\cos x$ es positivo pero muy pequeño (cercano a $0^+$)
  - $\tan x = \dfrac{\sin x}{\cos x} \to \dfrac{1}{0^+} = +\infty$

- **Un poco después** de $\pi/2$ (ya en el 2º cuadrante, ej. $91°$):
  - $\sin x$ sigue siendo positivo (cercano a 1)
  - $\cos x$ ahora es negativo pero muy pequeño (cercano a $0^-$)
  - $\tan x = \dfrac{\sin x}{\cos x} \to \dfrac{1}{0^-} = -\infty$

Como el resultado por la izquierda ($+\infty$) es distinto al de la derecha ($-\infty$), el límite **no existe** en $\pi/2$.

---

## 🧠 Por qué importa esto para los límites

El Ejercicio 7 del examen pide estudiar el límite de $\tan x$ cuando $x\to\pi/2$. Sin saber que la tangente es una división entre seno y coseno, sin saber dónde se anula el coseno, y sin saber estudiar el signo por cuadrantes, es imposible justificar por qué el límite da $+\infty$ por un lado y $-\infty$ por el otro.
