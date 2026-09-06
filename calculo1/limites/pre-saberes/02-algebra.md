# 2️⃣ Álgebra básica (explicado paso a paso)

El álgebra es como la aritmética, pero usando letras (normalmente $x$) para representar números que no conocemos todavía. Vamos a verlo con mucha calma.

---

## ¿Qué es una expresión algebraica?

Es una "receta" con números y letras, como:

$$
3x+2
$$

Aquí $x$ es un número desconocido. Si nos dicen que $x=4$, sustituimos:

$$
3(4)+2=12+2=14
$$

### Simplificar (agrupar términos semejantes)

Los "términos semejantes" son los que tienen la misma letra con el mismo exponente. Se pueden sumar entre sí, como si contaras manzanas con manzanas:

$$
3x+5x-2x = (3+5-2)x = 6x
$$

No se pueden mezclar términos distintos: $3x+2$ no se puede simplificar más, porque $x$ y el número suelto $2$ son "cosas distintas".

---

## Ecuaciones de primer grado

Una ecuación es una igualdad con una incógnita ($x$) que hay que despejar, es decir, dejar sola en un lado.

**Ejemplo:** $2x+3=11$

Pasos (lo que hagas en un lado, lo deshaces pasando al otro lado con la operación contraria):

1. Restamos 3 en los dos lados: $2x=11-3=8$
2. Dividimos entre 2 en los dos lados: $x=\dfrac{8}{2}=4$

**Comprobación:** $2(4)+3=8+3=11$ ✅

---

## Ecuaciones de segundo grado

Tienen la forma:

$$
ax^2+bx+c=0
$$

Se resuelven con la **fórmula general**:

$$
x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}
$$

**Ejemplo:** $x^2-5x+6=0$ (aquí $a=1$, $b=-5$, $c=6$)

1. Calculamos el interior de la raíz (discriminante): $b^2-4ac=(-5)^2-4(1)(6)=25-24=1$
2. Aplicamos la fórmula:
$$
x=\frac{-(-5)\pm\sqrt{1}}{2(1)}=\frac{5\pm1}{2}
$$
3. Dos soluciones:
   - $x=\dfrac{5+1}{2}=3$
   - $x=\dfrac{5-1}{2}=2$

Esto nos servirá muchísimo para **factorizar polinomios** en los límites.

---

## Productos notables

Son atajos que aparecen muchísimo y conviene memorizar:

### Cuadrado de una suma

$$
(a+b)^2=a^2+2ab+b^2
$$

Ejemplo: $(x+3)^2=x^2+2(x)(3)+3^2=x^2+6x+9$

### Cuadrado de una resta

$$
(a-b)^2=a^2-2ab+b^2
$$

Ejemplo: $(x-2)^2=x^2-4x+4$

### Suma por diferencia (¡el más importante para límites!)

$$
(a+b)(a-b)=a^2-b^2
$$

Esto también funciona **al revés**: si ves $a^2-b^2$, puedes convertirlo en $(a+b)(a-b)$.

Ejemplo: $x^2-9=(x-3)(x+3)$ porque $9=3^2$.

Este truco es exactamente el que se usa para resolver la indeterminación $0/0$ en el Ejercicio 2 del examen.

---

## Factorizar polinomios

Factorizar significa escribir una suma/resta como una **multiplicación**. Es como "deshacer" el desarrollo de un producto notable.

### 1. Factor común

Si todos los términos comparten algo, se saca fuera:

$$
6x^2+9x = 3x(2x+3)
$$

($3x$ divide exactamente a $6x^2$ y a $9x$)

### 2. Diferencia de cuadrados

$$
x^2-16=(x-4)(x+4)
$$

### 3. Trinomio de segundo grado

Para $x^2+bx+c$, buscamos dos números que **multiplicados** den $c$ y **sumados** den $b$.

Ejemplo: $x^2-5x+6$ → buscamos dos números que multiplicados den 6 y sumados den -5 → son $-2$ y $-3$.

$$
x^2-5x+6=(x-2)(x-3)
$$

(Coincide con las soluciones que sacamos antes con la fórmula general: $x=2$ y $x=3$.)

### 4. Regla de Ruffini (para polinomios más grandes)

Si sabes que $x=a$ es una solución del polinomio (es decir, si sustituyes $x=a$ el polinomio da 0), entonces $(x-a)$ es un factor. Puedes dividir el polinomio entre $(x-a)$ usando Ruffini para sacar el resto de factores.

**Idea clave:** si $P(a)=0$, entonces $P(x) = (x-a)\cdot Q(x)$ para algún polinomio $Q(x)$ más pequeño.

---

## 🧠 Por qué importa esto para los límites

Cuando un límite da la indeterminación $0/0$, la salida casi siempre es **factorizar** el numerador y el denominador para encontrar un factor común que se pueda simplificar (cancelar). Sin saber factorizar bien, no se puede resolver ese tipo de ejercicio.
