# 3️⃣ Racionalización (explicado paso a paso)

Racionalizar significa transformar una fracción para que su denominador no contenga raíces. La nueva expresión tiene el mismo valor, pero suele ser más fácil de simplificar y, en límites, puede revelar el factor que produce una indeterminación.

---

## ¿Por qué molesta una raíz en el denominador?

Una fracción como:

$$
\frac{1}{\sqrt{2}}
$$

es totalmente válida. Sin embargo, una forma equivalente sin raíz en el denominador facilita algunas operaciones. Vamos a ver cómo se obtiene.

---

## El truco: multiplicar por "1 disfrazado"

La idea es multiplicar la fracción por algo que valga 1 (para no cambiar su valor), pero que esté diseñado para eliminar la raíz de abajo.

### Caso simple: una sola raíz

$$
\frac{1}{\sqrt{2}} \times \frac{\sqrt{2}}{\sqrt{2}} = \frac{\sqrt{2}}{2}
$$

¿Por qué funciona? Porque $\sqrt{2}\times\sqrt{2}=2$ (una raíz cuadrada multiplicada por sí misma "deshace" la raíz).

Y como $\dfrac{\sqrt2}{\sqrt2}=1$, multiplicar por ella no cambia el valor de la fracción original, solo su forma.

---

## Caso con una resta de raíces: el conjugado

Cuando el denominador tiene una **resta** (o suma) con raíces, como:

$$
\frac{1}{\sqrt{x}-\sqrt{a}}
$$

no basta con multiplicar por la misma raíz. Aquí usamos el **conjugado**: la misma expresión pero cambiando el signo del medio.

- El conjugado de $\sqrt{x}-\sqrt{a}$ es $\sqrt{x}+\sqrt{a}$.

| Expresión | Conjugado |
|---|---|
| $\sqrt{x}-\sqrt{a}$ | $\sqrt{x}+\sqrt{a}$ |
| $\sqrt{x}+\sqrt{a}$ | $\sqrt{x}-\sqrt{a}$ |
| $u-v$ | $u+v$ |
| $u+v$ | $u-v$ |

¿Por qué usamos el conjugado? Porque al multiplicar una resta por su "suma gemela", usamos el producto notable que ya conocemos:

> [!IMPORTANT]
> Multiplica por el conjugado dividido entre sí mismo. Así multiplicas por $1$: cambia la forma de la expresión, pero no su valor.

$$
(a-b)(a+b)=a^2-b^2
$$

y las raíces **desaparecen** al elevarlas al cuadrado:

$$
\frac{1}{\sqrt{x}-\sqrt{a}}\times\frac{\sqrt{x}+\sqrt{a}}{\sqrt{x}+\sqrt{a}} = \frac{\sqrt{x}+\sqrt{a}}{(\sqrt{x})^2-(\sqrt{a})^2}=\frac{\sqrt{x}+\sqrt{a}}{x-a}
$$

Fíjate: las raíces han pasado del denominador al numerador, y abajo ha quedado una resta sin raíces ($x-a$). Esta igualdad se usa donde las expresiones están definidas; en particular, el denominador original no puede valer cero.

---

## Ejemplo numérico paso a paso

Racionaliza: $\dfrac{1}{\sqrt{5}-\sqrt{3}}$

1. Multiplicamos arriba y abajo por el conjugado $\sqrt{5}+\sqrt{3}$:

$$
\frac{1}{\sqrt{5}-\sqrt{3}}\times\frac{\sqrt{5}+\sqrt{3}}{\sqrt{5}+\sqrt{3}}
$$

2. Abajo aplicamos $(a-b)(a+b)=a^2-b^2$:

$$
(\sqrt5)^2-(\sqrt3)^2 = 5-3=2
$$

3. Resultado:

$$
\frac{\sqrt{5}+\sqrt{3}}{2}
$$

Ya no queda ninguna raíz abajo. ✅

---

## 🧠 Por qué importa esto para los límites

A veces, al calcular un límite con raíces, sustituir directamente da la indeterminación $0/0$, pero **no se puede factorizar** porque hay una raíz de por medio. En esos casos, la solución es **racionalizar** (multiplicar por el conjugado) para poder simplificar el factor que causa el problema y así resolver el límite.

---

## Comprueba lo aprendido

**1. ¿Cuál es el conjugado de $\sqrt{x}+4$?**

<details>
<summary>Comprobar respuesta</summary>

Es $\sqrt{x}-4$: se conservan los términos y se cambia el signo que los separa.

</details>

**2. Racionaliza $\dfrac{1}{\sqrt7+\sqrt5}$.**

<details>
<summary>Ver solución razonada</summary>

Multiplicamos por el conjugado $\sqrt7-\sqrt5$:

$$
\frac{1}{\sqrt7+\sqrt5}\cdot\frac{\sqrt7-\sqrt5}{\sqrt7-\sqrt5}
=\frac{\sqrt7-\sqrt5}{7-5}
=\frac{\sqrt7-\sqrt5}{2}.
$$

</details>

**3. Calcula $\displaystyle\lim_{x\to4}\dfrac{\sqrt{x}-2}{x-4}$.**

<details>
<summary>Ver solución razonada</summary>

Al sustituir aparece $0/0$. Multiplicamos por el conjugado del numerador:

$$
\frac{\sqrt{x}-2}{x-4}\cdot\frac{\sqrt{x}+2}{\sqrt{x}+2}
=\frac{x-4}{(x-4)(\sqrt{x}+2)}
=\frac{1}{\sqrt{x}+2}, \qquad x\ne4.
$$

Ahora sustituimos en la expresión simplificada y obtenemos $1/(2+2)=1/4$.

</details>
