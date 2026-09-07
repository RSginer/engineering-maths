# 📝 Examen de Cálculo — Límites

**Tiempo recomendado:** 60 minutos  
**Puntuación:** 10 puntos  
**Calculadora:** Intenta hacerlo sin calculadora.

Antes de empezar, puedes repasar la [teoría de límites](teoria-limites.md). Durante el examen, escribe el procedimiento: una respuesta correcta sin justificar puede no recibir toda la puntuación.

---

## Ejercicio 1 — Cálculo directo [1 punto]

Calcula:

$$
\lim_{x\to2}(3x^2-5x+4)
$$

---

## Ejercicio 2 — Indeterminación $0/0$ [1,5 puntos]

Calcula:

$$
\lim_{x\to3}\frac{x^2-9}{x-3}
$$

Indica:

1. Qué ocurre al sustituir directamente.
2. Qué tipo de indeterminación aparece.
3. Cómo transformas la expresión para resolverla.
4. El resultado final.

---

## Ejercicio 3 — Límites laterales e infinitos [1,5 puntos]

Sea:

$$
f(x)=\frac{x^2+x+2}{x+1}
$$

Calcula:

$$
\lim_{x\to-1^-}f(x)
$$

y

$$
\lim_{x\to-1^+}f(x)
$$

Después determina si existe:

$$
\lim_{x\to-1}f(x)
$$

Justifica el signo de cada infinito.

---

## Ejercicio 4 — Límite en el infinito [1,5 puntos]

Calcula:

$$
\lim_{x\to+\infty}
\frac{4x^2-3x+1}{2x^2+5x-7}
$$

Justifica el procedimiento utilizado.

---

## Ejercicio 5 — Grados diferentes [1 punto]

Calcula:

$$
\lim_{x\to+\infty}
\frac{3x+2}{x^2-1}
$$

Explica por qué obtienes ese resultado.

---

## Ejercicio 6 — Asíntota vertical [1,5 puntos]

Calcula los límites laterales:

$$
\lim_{x\to2^-}\frac{1}{x-2}
$$

$$
\lim_{x\to2^+}\frac{1}{x-2}
$$

Después responde:

- ¿Existe el límite bilateral cuando $x\to2$?
- ¿Tiene la función una asíntota vertical?
- En caso afirmativo, ¿cuál?

---

## Ejercicio 7 — Límite trigonométrico [1 punto]

Estudia:

$$
\lim_{x\to\frac{\pi}{2}^-}\tan(x)
$$

y

$$
\lim_{x\to\frac{\pi}{2}^+}\tan(x)
$$

Determina si existe:

$$
\lim_{x\to\frac{\pi}{2}}\tan(x)
$$

Justifica tu respuesta.

---

## Ejercicio 8 — Conceptos [1 punto]

Explica con tus propias palabras qué significa:

$$
\lim_{x\to a}f(x)=L
$$

Responde también:

> ¿Es necesario que $f(a)=L$ para que el límite sea $L$?

Justifica tu respuesta.

---

## Pistas opcionales

Abre una pista solo después de haber intentado el ejercicio. Las pistas indican el siguiente paso, pero no contienen el desarrollo completo.

<details>
<summary>Pista del Ejercicio 1</summary>

Es un polinomio. Comprueba si puedes usar continuidad y sustitución directa.

</details>

<details>
<summary>Pista del Ejercicio 2</summary>

Reconoce $x^2-9$ como una diferencia de cuadrados y conserva la restricción $x\ne3$ al simplificar.

</details>

<details>
<summary>Pista del Ejercicio 3</summary>

El numerador se aproxima a un número positivo. Estudia el signo de $x+1$ a cada lado de $-1$.

</details>

<details>
<summary>Pista del Ejercicio 4</summary>

Numerador y denominador tienen el mismo grado. Divide todos los términos entre $x^2$.

</details>

<details>
<summary>Pista del Ejercicio 5</summary>

El denominador tiene mayor grado. Divide numerador y denominador entre $x^2$ y observa qué términos tienden a cero.

</details>

<details>
<summary>Pista del Ejercicio 6</summary>

Prueba el signo de $x-2$ con un valor menor que $2$ y otro mayor que $2$.

</details>

<details>
<summary>Pista del Ejercicio 7</summary>

Escribe $\tan x=\sin x/\cos x$ y recuerda los signos del coseno en los cuadrantes primero y segundo.

</details>

<details>
<summary>Pista del Ejercicio 8</summary>

Compara qué información aporta el comportamiento alrededor de $a$ con la que aporta el valor aislado $f(a)$.

</details>

---

# Puntuación

| Ejercicio | Puntos |
|---|---:|
| 1 | 1 |
| 2 | 1,5 |
| 3 | 1,5 |
| 4 | 1,5 |
| 5 | 1 |
| 6 | 1,5 |
| 7 | 1 |
| 8 | 1 |
| **Total** | **10** |

Cuando termines, compara tu procedimiento con las [soluciones razonadas](soluciones-examen-limites-1.md).
