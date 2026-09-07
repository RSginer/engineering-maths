# 1️⃣ Aritmética y operaciones básicas (explicado paso a paso)

Vamos a repasar las cosas más básicas de las matemáticas, explicadas muy despacio, como si nunca las hubieras visto.

---

## Las fracciones

Una fracción es una forma de repartir algo en partes iguales. Si partes una pizza en 4 trozos iguales y te comes 1, te has comido $\dfrac{1}{4}$ de la pizza.

- El número de **arriba** (numerador) dice cuántos trozos tienes.
- El número de **abajo** (denominador) dice en cuántos trozos se ha dividido el total.

### Sumar y restar fracciones

Solo puedes sumar o restar fracciones si tienen el **mismo denominador** (el mismo número abajo).

$$
\frac{1}{5}+\frac{2}{5}=\frac{1+2}{5}=\frac{3}{5}
$$

Si los denominadores son distintos, hay que buscar un denominador común. Conviene usar el mínimo común múltiplo; multiplicarlos siempre funciona, aunque no siempre produce el número más pequeño:

$$
\frac{1}{2}+\frac{1}{3}=\frac{3}{6}+\frac{2}{6}=\frac{5}{6}
$$

(Aquí hemos convertido ambas fracciones para que tengan denominador 6, porque $2\times3=6$.)

### Multiplicar fracciones

Se multiplica arriba con arriba, y abajo con abajo:

$$
\frac{2}{3}\times\frac{4}{5}=\frac{2\times4}{3\times5}=\frac{8}{15}
$$

### Dividir fracciones

Se multiplica por la fracción "del revés" (invertida):

$$
\frac{2}{3}\div\frac{4}{5}=\frac{2}{3}\times\frac{5}{4}=\frac{10}{12}=\frac{5}{6}
$$

### Simplificar fracciones

Si arriba y abajo se pueden dividir por el mismo número, la fracción se simplifica:

$$
\frac{10}{12}=\frac{10\div2}{12\div2}=\frac{5}{6}
$$

---

## Los signos (positivos y negativos)

Piensa en una recta numérica: a la derecha del 0 están los positivos, a la izquierda los negativos.

Reglas para multiplicar y dividir:

| Operación | Resultado | Ejemplo |
|---|---|---|
| $+\times+$ | $+$ | $3\times2=6$ |
| $+\times-$ | $-$ | $3\times(-2)=-6$ |
| $-\times+$ | $-$ | $(-3)\times2=-6$ |
| $-\times-$ | $+$ | $(-3)\times(-2)=6$ |

**Truco para recordarlo:** si los dos signos son iguales, el resultado es positivo. Si son distintos, el resultado es negativo. (Igual para la división.)

---

## Las potencias

Una potencia es una multiplicación repetida del mismo número.

$$
a^n = \underbrace{a\times a\times\cdots\times a}_{n\text{ veces}}
$$

Por ejemplo: $2^3=2\times2\times2=8$

Reglas importantes:

- **Cualquier número no nulo elevado a 0 es 1:** $a^0=1$ si $a\ne0$. La expresión $0^0$ no se trata con esta regla.
- **Exponente negativo** significa "el inverso":
$$
a^{-n}=\frac{1}{a^n}
$$
Ejemplo: $2^{-3}=\dfrac{1}{2^3}=\dfrac{1}{8}$

- **Exponente fraccionario** es una raíz:
$$
a^{m/n}=\sqrt[n]{a^m}
$$
Ejemplo: $8^{1/3}=\sqrt[3]{8}=2$

---

## Las raíces

La raíz cuadrada principal de un número no negativo es el número **no negativo** que, multiplicado por sí mismo, da ese resultado.

$$
\sqrt{9}=3 \quad\text{porque}\quad 3\times3=9
$$

Propiedad útil en los números reales: si $a\ge0$ y $b\ge0$, puedes separar una raíz de una multiplicación en dos raíces:

$$
\sqrt{a\times b}=\sqrt{a}\times\sqrt{b}
$$

Ejemplo: $\sqrt{4\times9}=\sqrt{4}\times\sqrt{9}=2\times3=6$ (y en efecto, $\sqrt{36}=6$) ✅

**Cuidado:** $\sqrt{a+b}$ no es, en general, $\sqrt a+\sqrt b$. Las raíces se separan en productos bajo las condiciones anteriores, no en sumas.

### Racionalizar un denominador

Una forma equivalente sin raíces en el denominador suele ser más cómoda para operar. En este caso, multiplicamos numerador y denominador por la misma raíz:

$$
\frac{1}{\sqrt{2}}=\frac{1}{\sqrt{2}}\times\frac{\sqrt{2}}{\sqrt{2}}=\frac{\sqrt{2}}{2}
$$

---

## El orden de las operaciones (jerarquía)

Cuando en una cuenta hay varias operaciones mezcladas, hay un orden que **siempre** hay que seguir, como si fueran las reglas de un juego:

1. **Paréntesis** primero: $(\;)$
2. **Potencias y raíces**
3. **Multiplicaciones y divisiones** (de izquierda a derecha)
4. **Sumas y restas** (de izquierda a derecha)

### Ejemplo paso a paso

$$
2+3\times(4-1)^2
$$

1. Paréntesis: $4-1=3$ → queda $2+3\times3^2$
2. Potencia: $3^2=9$ → queda $2+3\times9$
3. Multiplicación: $3\times9=27$ → queda $2+27$
4. Suma: $2+27=29$

**Resultado:** 29

---

## 🧠 Por qué importa esto para los límites

Cuando calculamos un límite, constantemente vamos a **sustituir números**, **simplificar fracciones** y **operar con potencias**. Si estas bases no están firmes, es muy fácil equivocarse en un paso sencillo y que todo el ejercicio salga mal, aunque hayas entendido la idea del límite perfectamente.
