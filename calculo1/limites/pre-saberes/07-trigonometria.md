# 7️⃣ Trigonometría básica (explicado paso a paso)

La trigonometría estudia los ángulos y sus relaciones. Aquí nos centraremos en lo necesario para entender el límite de la tangente.

> [!IMPORTANT]
> En cálculo los ángulos se expresan normalmente en **radianes**: $\pi$ radianes equivalen a $180^\circ$.

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

## La identidad fundamental

Por el Teorema de Pitágoras aplicado al círculo unidad (el radio siempre vale 1), se cumple siempre, para cualquier ángulo $x$:

$$
\sin^2(x)+\cos^2(x)=1
$$

Esta identidad es muy útil para simplificar expresiones trigonométricas y para deducir otras relaciones.

## Las funciones trigonométricas recíprocas

Además de seno, coseno y tangente, existen sus "inversas multiplicativas" (uno dividido entre cada una):

$$
\csc(x)=\frac{1}{\sin(x)} \qquad \sec(x)=\frac{1}{\cos(x)} \qquad \cot(x)=\frac{\cos(x)}{\sin(x)}
$$

- **Cosecante** ($\csc$): no existe donde $\sin(x)=0$ (en $0$, $\pi$, $2\pi$...).
- **Secante** ($\sec$): no existe donde $\cos(x)=0$ (en $\pi/2$, $3\pi/2$...) — igual que la tangente.
- **Cotangente** ($\cot$): no existe donde $\sin(x)=0$. Donde ambas expresiones están definidas, también se cumple $\cot(x)=1/\tan(x)$.

Fíjate que todas siguen la misma lógica que ya conocemos: son fracciones, y **no existen donde su denominador se anula**.

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
  - $\tan x = \dfrac{\sin x}{\cos x}\to+\infty$

- **Un poco después** de $\pi/2$ (ya en el 2º cuadrante, ej. $91°$):
  - $\sin x$ sigue siendo positivo (cercano a 1)
  - $\cos x$ ahora es negativo pero muy pequeño (cercano a $0^-$)
  - $\tan x = \dfrac{\sin x}{\cos x}\to-\infty$

Como el resultado por la izquierda ($+\infty$) es distinto al de la derecha ($-\infty$), el límite **no existe** en $\pi/2$.

![El círculo unidad y la tangente al acercarse a pi medios](../animaciones/TangenteCercaDePiMedios.gif)

---

## 🧠 Por qué importa esto para los límites

El Ejercicio 7 del examen pide estudiar el límite de $\tan x$ cuando $x\to\pi/2$. Sin saber que la tangente es una división entre seno y coseno, sin saber dónde se anula el coseno, y sin saber estudiar el signo por cuadrantes, es imposible justificar por qué el límite da $+\infty$ por un lado y $-\infty$ por el otro.

---

## Comprueba lo aprendido

**1. Calcula $\tan(\pi/4)$ usando seno y coseno.**

<details>
<summary>Comprobar resultado</summary>

Como $\sin(\pi/4)=\cos(\pi/4)=\sqrt2/2$:

$$
\tan(\pi/4)=\frac{\sqrt2/2}{\sqrt2/2}=1.
$$

</details>

**2. ¿Dónde no está definida $\tan x$?**

<details>
<summary>Comprobar respuesta</summary>

Donde $\cos x=0$, es decir, en $x=\pi/2+k\pi$ para cualquier entero $k$.

</details>

**3. Predice el signo de $\tan x$ en el segundo cuadrante.**

<details>
<summary>Ver solución razonada</summary>

En el segundo cuadrante, $\sin x>0$ y $\cos x<0$. Por tanto, $\tan x=\sin x/\cos x<0$.

</details>
