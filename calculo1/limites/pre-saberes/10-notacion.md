# 🔟 Notación que debes reconocer (explicado paso a paso)

Las matemáticas usan símbolos para escribir ideas de forma corta. Aquí vamos a "traducir" cada símbolo relacionado con límites a un lenguaje normal, para que nunca te quedes bloqueado por no entender qué significa un símbolo.

---

## \(\lim_{x\to a}f(x)\)

**Se lee:** "el límite de \(f(x)\) cuando \(x\) tiende a \(a\)".

**Significa:** el valor al que se acerca \(f(x)\) cuando \(x\) se acerca cada vez más a \(a\) (sin llegar a valer exactamente \(a\)).

**Ejemplo:** \(\lim_{x\to2}(3x^2-5x+4)\) pregunta: ¿a qué valor se acerca \(3x^2-5x+4\) cuando \(x\) se acerca a 2?

---

## \(x\to a^-\)

**Se lee:** "\(x\) tiende a \(a\) por la izquierda".

**Significa:** \(x\) se acerca a \(a\) tomando valores **menores** que \(a\) (por ejemplo, si \(a=2\): 1.9, 1.99, 1.999...).

---

## \(x\to a^+\)

**Se lee:** "\(x\) tiende a \(a\) por la derecha".

**Significa:** \(x\) se acerca a \(a\) tomando valores **mayores** que \(a\) (por ejemplo, si \(a=2\): 2.1, 2.01, 2.001...).

---

## \(x\to+\infty\)

**Se lee:** "\(x\) tiende a más infinito".

**Significa:** \(x\) crece sin parar, cada vez más grande (100, 1000, 1000000...).

---

## \(x\to-\infty\)

**Se lee:** "\(x\) tiende a menos infinito".

**Significa:** \(x\) decrece sin parar, cada vez más negativo (-100, -1000, -1000000...).

---

## \(f(a)\)

**Se lee:** "\(f\) de \(a\)" o "el valor de \(f\) en \(a\)".

**Significa:** el resultado de sustituir \(x=a\) directamente en la función. **Ojo:** este valor puede no existir (por ejemplo, si \(a\) anula el denominador), incluso aunque el **límite** en ese punto sí exista.

---

## \(0/0\)

**Se lee:** "cero partido de cero" o "indeterminación cero entre cero".

**Significa:** al sustituir directamente, tanto el numerador como el denominador dan 0. Esto **no** significa que el límite sea 0 ni que no exista — significa que hay que **investigar más** (normalmente factorizando o racionalizando) para encontrar el valor real del límite.

---

## \(\infty/\infty\)

**Se lee:** "infinito partido de infinito".

**Significa:** al estudiar el límite en el infinito, tanto numerador como denominador crecen sin parar. Igual que \(0/0\), es una indeterminación que hay que resolver comparando **grados de los polinomios** (ver el tema de grado de un polinomio).

---

## \(+\infty\) y \(-\infty\) como resultado de un límite

**Significa:** el resultado de la función crece (\(+\infty\)) o decrece (\(-\infty\)) sin parar a medida que \(x\) se acerca al punto en cuestión. **No es un número**, es una forma de decir "no existe un límite finito, y además la función se dispara hacia arriba/abajo".

---

## El signo \(\pm\)

**Se lee:** "más menos".

**Significa:** hay dos posibles resultados, uno sumando y otro restando. Aparece típicamente en la fórmula general de ecuaciones de segundo grado:

$$
x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}
$$

Esto en realidad son **dos fórmulas en una**: una con \(+\) y otra con \(-\).

---

## Tabla resumen

| Notación | Lectura | Significado |
|---|---|---|
| \(\lim_{x\to a}f(x)\) | Límite de \(f(x)\) cuando \(x\) tiende a \(a\) | Valor al que se acerca \(f(x)\) cerca de \(a\) |
| \(x\to a^-\) | \(x\) tiende a \(a\) por la izquierda | Valores menores que \(a\), acercándose |
| \(x\to a^+\) | \(x\) tiende a \(a\) por la derecha | Valores mayores que \(a\), acercándose |
| \(x\to+\infty\) | \(x\) tiende a más infinito | \(x\) crece sin parar |
| \(x\to-\infty\) | \(x\) tiende a menos infinito | \(x\) decrece sin parar |
| \(f(a)\) | \(f\) de \(a\) | Valor real de la función en \(a\) (puede no existir) |
| \(0/0\) | Cero entre cero | Indeterminación — hay que investigar más |
| \(\infty/\infty\) | Infinito entre infinito | Indeterminación — comparar grados |

---

## 🧠 Por qué importa esto para los límites

Si no reconoces estos símbolos al instante, cada ejercicio se convierte en un puzzle de "descifrar el enunciado" antes de poder resolver nada. Memorizar esta tabla te permite leer cualquier ejercicio de límites y saber inmediatamente qué te están pidiendo.
