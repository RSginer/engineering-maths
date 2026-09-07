# 🔟 Notación que debes reconocer (explicado paso a paso)

Las matemáticas usan símbolos para escribir ideas de forma corta. Aquí vamos a "traducir" cada símbolo relacionado con límites a un lenguaje normal, para que nunca te quedes bloqueado por no entender qué significa un símbolo.

---

## $\lim_{x\to a}f(x)$

**Se lee:** "el límite de $f(x)$ cuando $x$ tiende a $a$".

**Significa:** el valor al que se acerca $f(x)$ cuando $x$ toma valores cada vez más próximos a $a$. El valor exacto $f(a)$ no interviene en esta pregunta.

**Ejemplo:** $\lim_{x\to2}(3x^2-5x+4)$ pregunta: ¿a qué valor se acerca $3x^2-5x+4$ cuando $x$ se acerca a 2?

---

## $x\to a^-$

**Se lee:** "$x$ tiende a $a$ por la izquierda".

**Significa:** $x$ se acerca a $a$ tomando valores **menores** que $a$ (por ejemplo, si $a=2$: 1.9, 1.99, 1.999...).

---

## $x\to a^+$

**Se lee:** "$x$ tiende a $a$ por la derecha".

**Significa:** $x$ se acerca a $a$ tomando valores **mayores** que $a$ (por ejemplo, si $a=2$: 2.1, 2.01, 2.001...).

El límite bilateral existe y vale $L$ exactamente cuando ambos laterales existen y coinciden:

$$
\lim_{x\to a}f(x)=L
\iff
\lim_{x\to a^-}f(x)=\lim_{x\to a^+}f(x)=L.
$$

---

## $x\to+\infty$

**Se lee:** "$x$ tiende a más infinito".

**Significa:** $x$ crece sin parar, cada vez más grande (100, 1000, 1000000...).

---

## $x\to-\infty$

**Se lee:** "$x$ tiende a menos infinito".

**Significa:** $x$ decrece sin parar, cada vez más negativo (-100, -1000, -1000000...).

---

## $f(a)$

**Se lee:** "$f$ de $a$" o "el valor de $f$ en $a$".

**Significa:** el resultado de sustituir $x=a$ directamente en la función. **Ojo:** este valor puede no existir (por ejemplo, si $a$ anula el denominador), incluso aunque el **límite** en ese punto sí exista.

---

## $0/0$

**Se lee:** "cero partido de cero" o "indeterminación cero entre cero".

**Significa:** al sustituir directamente, tanto el numerador como el denominador dan 0. Esto **no** significa que el límite sea 0 ni que no exista — significa que hay que **investigar más** (normalmente factorizando o racionalizando) para encontrar el valor real del límite.

> [!WARNING]
> No escribas $\lim f(x)=0/0$. La forma $0/0$ describe lo que ocurre al sustituir y obliga a transformar la expresión; nunca es el resultado final.

---

## $\infty/\infty$

**Se lee:** "infinito partido de infinito".

**Significa:** al estudiar el límite en el infinito, tanto numerador como denominador crecen sin parar. Igual que $0/0$, es una indeterminación que hay que resolver comparando **grados de los polinomios** (ver el tema de grado de un polinomio).

---

## Notación de intervalos: $[a,b]$, $(a,b)$, $[a,b)$, $(a,b]$

**Se lee:** "intervalo cerrado/abierto entre $a$ y $b$".

**Significa:** un conjunto de números entre $a$ y $b$. El **corchete** ($[$ o $]$) incluye ese extremo; el **paréntesis** ($($ o $)$) lo excluye.

- $[a,b]$: incluye ambos extremos (cerrado)
- $(a,b)$: no incluye ninguno (abierto)
- $[a,b)$ / $(a,b]$: incluye solo uno de los dos

Se usa muchísimo para describir dominios e imágenes de funciones, por ejemplo $\text{Dom}(f)=[0,+\infty)$.

---

## $+\infty$ y $-\infty$ como resultado de un límite

**Significa:** los valores de la función crecen sin cota superior ($+\infty$) o disminuyen sin cota inferior ($-\infty$) a medida que $x$ se acerca al punto en cuestión. **No son números reales** ni valores que la función llegue a alcanzar.

---

## El signo $\pm$

**Se lee:** "más menos".

**Significa:** hay dos posibles resultados, uno sumando y otro restando. Aparece típicamente en la fórmula general de ecuaciones de segundo grado:

$$
x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}
$$

Esto en realidad son **dos fórmulas en una**: una con $+$ y otra con $-$.

---

## Tabla resumen

| Notación | Lectura | Significado |
|---|---|---|
| $\lim_{x\to a}f(x)$ | Límite de $f(x)$ cuando $x$ tiende a $a$ | Valor al que se acerca $f(x)$ cerca de $a$ |
| $x\to a^-$ | $x$ tiende a $a$ por la izquierda | Valores menores que $a$, acercándose |
| $x\to a^+$ | $x$ tiende a $a$ por la derecha | Valores mayores que $a$, acercándose |
| $x\to+\infty$ | $x$ tiende a más infinito | $x$ crece sin parar |
| $x\to-\infty$ | $x$ tiende a menos infinito | $x$ decrece sin parar |
| $f(a)$ | $f$ de $a$ | Valor real de la función en $a$ (puede no existir) |
| $0/0$ | Cero entre cero | Indeterminación — hay que investigar más |
| $\infty/\infty$ | Infinito entre infinito | Indeterminación — comparar grados |
| $[a,b]$ | Intervalo cerrado entre $a$ y $b$ | Incluye ambos extremos |
| $(a,b)$ | Intervalo abierto entre $a$ y $b$ | No incluye ningún extremo |

---

## 🧠 Por qué importa esto para los límites

Si no reconoces estos símbolos al instante, cada ejercicio se convierte en un puzzle de "descifrar el enunciado" antes de poder resolver nada. Memorizar esta tabla te permite leer cualquier ejercicio de límites y saber inmediatamente qué te están pidiendo.

---

## Comprueba lo aprendido

**1. Traduce $x\to4^-$ a lenguaje cotidiano.**

<details>
<summary>Comprobar respuesta</summary>

$x$ toma valores menores que $4$ y cada vez más próximos a $4$.

</details>

**2. ¿Qué dos igualdades laterales permiten afirmar que $\lim_{x\to a}f(x)=L$?**

<details>
<summary>Comprobar respuesta</summary>

$$
\lim_{x\to a^-}f(x)=L
\quad\text{y}\quad
\lim_{x\to a^+}f(x)=L.
$$

</details>

**3. ¿Qué diferencia hay entre $f(a)$ y $\lim_{x\to a}f(x)$?**

<details>
<summary>Comprobar respuesta</summary>

$f(a)$ es el valor en el punto exacto. El límite describe los valores de la función alrededor de $a$; ambos pueden coincidir, ser distintos o puede no existir uno de ellos.

</details>
