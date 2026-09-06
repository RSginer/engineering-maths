# 3️⃣ Racionalización (explicado paso a paso)

Racionalizar significa **quitar las raíces del denominador** de una fracción (la parte de abajo). A los matemáticos no les gusta dejar raíces abajo, así que hay un truco para eliminarlas.

---

## ¿Por qué molesta una raíz en el denominador?

Una fracción como:

$$
\frac{1}{\sqrt{2}}
$$

es totalmente válida, pero se prefiere escribirla sin raíz abajo. Vamos a ver cómo se hace.

---

## El truco: multiplicar por "1 disfrazado"

La idea es multiplicar la fracción por algo que valga 1 (para no cambiar su valor), pero que esté diseñado para eliminar la raíz de abajo.

### Caso simple: una sola raíz

$$
\frac{1}{\sqrt{2}} \times \frac{\sqrt{2}}{\sqrt{2}} = \frac{\sqrt{2}}{2}
$$

¿Por qué funciona? Porque \(\sqrt{2}\times\sqrt{2}=2\) (una raíz cuadrada multiplicada por sí misma "deshace" la raíz).

Y como \(\dfrac{\sqrt2}{\sqrt2}=1\), multiplicar por ella no cambia el valor de la fracción original, solo su forma.

---

## Caso con una resta de raíces: el conjugado

Cuando el denominador tiene una **resta** (o suma) con raíces, como:

$$
\frac{1}{\sqrt{x}-\sqrt{a}}
$$

no basta con multiplicar por la misma raíz. Aquí usamos el **conjugado**: la misma expresión pero cambiando el signo del medio.

- El conjugado de \(\sqrt{x}-\sqrt{a}\) es \(\sqrt{x}+\sqrt{a}\).

¿Por qué usamos el conjugado? Porque al multiplicar una resta por su "suma gemela", usamos el producto notable que ya conocemos:

$$
(a-b)(a+b)=a^2-b^2
$$

y las raíces **desaparecen** al elevarlas al cuadrado:

$$
\frac{1}{\sqrt{x}-\sqrt{a}}\times\frac{\sqrt{x}+\sqrt{a}}{\sqrt{x}+\sqrt{a}} = \frac{\sqrt{x}+\sqrt{a}}{(\sqrt{x})^2-(\sqrt{a})^2}=\frac{\sqrt{x}+\sqrt{a}}{x-a}
$$

Fíjate: las raíces han pasado del denominador al numerador, y abajo ha quedado una resta sin raíces (\(x-a\)).

---

## Ejemplo numérico paso a paso

Racionaliza: \(\dfrac{1}{\sqrt{5}-\sqrt{3}}\)

1. Multiplicamos arriba y abajo por el conjugado \(\sqrt{5}+\sqrt{3}\):

$$
\frac{1}{\sqrt{5}-\sqrt{3}}\times\frac{\sqrt{5}+\sqrt{3}}{\sqrt{5}+\sqrt{3}}
$$

2. Abajo aplicamos \((a-b)(a+b)=a^2-b^2\):

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

A veces, al calcular un límite con raíces, sustituir directamente da la indeterminación \(0/0\), pero **no se puede factorizar** porque hay una raíz de por medio. En esos casos, la solución es **racionalizar** (multiplicar por el conjugado) para poder simplificar el factor que causa el problema y así resolver el límite.
