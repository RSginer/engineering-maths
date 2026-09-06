# 6️⃣ Signo de una función / estudio de signos (explicado paso a paso)

Saber si un resultado es **positivo o negativo** (sin necesariamente calcular el número exacto) es una habilidad clave para los límites infinitos. Vamos a aprenderla paso a paso.

---

## La idea básica

El signo de una expresión nos dice si el resultado va a ser mayor que 0 (positivo) o menor que 0 (negativo), sin hacer falta calcular el valor exacto.

### Ejemplo sencillo

¿Es \(x-2\) positivo o negativo cuando \(x=5\)?

$$
5-2=3 \quad(\text{positivo})
$$

¿Y cuando \(x=1\)?

$$
1-2=-1 \quad(\text{negativo})
$$

Fíjate que el "punto de cambio" es \(x=2\) (donde \(x-2=0\)). A la derecha de 2, la expresión es positiva. A la izquierda de 2, es negativa.

---

## Método: elegir un "valor de prueba"

Cuando queremos saber el signo de una expresión **cerca de un punto** (sin sustituir exactamente ese punto, que puede estar prohibido, como cuando anula un denominador), elegimos un número muy cercano y vemos su signo.

### Ejemplo: signo de \(x-2\) cerca de \(x=2\)

- **Un poco a la izquierda** de 2, por ejemplo \(x=1.9\): \(1.9-2=-0.1\) → **negativo**
- **Un poco a la derecha** de 2, por ejemplo \(x=2.1\): \(2.1-2=0.1\) → **positivo**

Esto se resume así:

- Cuando \(x\to2^-\) (por la izquierda): \(x-2\to0^-\) (se acerca a 0 desde el lado negativo)
- Cuando \(x\to2^+\) (por la derecha): \(x-2\to0^+\) (se acerca a 0 desde el lado positivo)

---

## Regla de los signos en una división

Recuerda (del tema de aritmética) las reglas de signos:

$$
\frac{+}{+}=+ \qquad \frac{+}{-}=- \qquad \frac{-}{+}=- \qquad \frac{-}{-}=+
$$

Esto se aplica igual aunque el "0" tenga un signo pegado (\(0^+\) o \(0^-\)):

$$
\frac{2}{0^+}=+\infty \qquad \frac{2}{0^-}=-\infty \qquad \frac{-2}{0^+}=-\infty \qquad \frac{-2}{0^-}=+\infty
$$

**Explicación intuitiva:** dividir un número entre algo cada vez más pequeño (que tiende a 0) da un resultado cada vez más grande. Si el 0 se acerca por el lado positivo, el resultado tiende a \(+\infty\) (si el numerador es positivo). Si se acerca por el lado negativo, el resultado tiende a \(-\infty\).

---

## Ejemplo completo paso a paso

Queremos saber el signo de \(f(x)=\dfrac{1}{x-2}\) cerca de \(x=2\), por los dos lados.

1. El numerador es siempre \(1\) (positivo, no depende de \(x\)).
2. Estudiamos el denominador \(x-2\):
   - Por la izquierda (\(x\to2^-\), ej. \(x=1.9\)): \(1.9-2=-0.1\) → negativo → \(x-2\to0^-\)
   - Por la derecha (\(x\to2^+\), ej. \(x=2.1\)): \(2.1-2=0.1\) → positivo → \(x-2\to0^+\)
3. Aplicamos la regla de signos:
   - Izquierda: \(\dfrac{1}{0^-}=-\infty\)
   - Derecha: \(\dfrac{1}{0^+}=+\infty\)

---

## Truco rápido para el signo de un binomio \((x-a)\)

- Si \(x>a\) (estás a la derecha de \(a\)), entonces \(x-a>0\) (positivo).
- Si \(x<a\) (estás a la izquierda de \(a\)), entonces \(x-a<0\) (negativo).

Esto se puede aplicar sin necesidad de sustituir números concretos, con solo pensar en la posición relativa a \(a\).

---

## 🧠 Por qué importa esto para los límites

En los ejercicios de asíntotas verticales y límites infinitos (Ejercicios 3, 6 y 7), después de comprobar que el denominador se anula, el paso decisivo es **estudiar el signo** del numerador y del denominador por cada lado, para saber si el resultado es \(+\infty\) o \(-\infty\). Sin dominar esto, no se puede terminar correctamente ninguno de esos ejercicios.
