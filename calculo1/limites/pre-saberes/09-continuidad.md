# 9️⃣ Continuidad (idea intuitiva, explicado paso a paso)

La continuidad es una idea muy visual e intuitiva. Vamos a construirla con dibujos imaginarios y ejemplos sencillos.

---

## La idea del lápiz

La idea de "dibujar sin levantar el lápiz" ayuda a imaginar la continuidad, pero no es una definición matemática y puede fallar en gráficas complicadas. En un punto $a$, una función es continua cuando se cumplen **las tres condiciones** siguientes:

1. Existe $f(a)$.
2. Existe $\lim_{x\to a}f(x)$; por tanto, los dos límites laterales coinciden.
3. Ambos valores son iguales: $\lim_{x\to a}f(x)=f(a)$.

Si falla cualquiera de las tres, la función es discontinua en $a$.

> [!IMPORTANT]
> Para demostrar continuidad en $a$ hay que comprobar las tres condiciones. Que el límite exista no basta si $f(a)$ no existe o tiene otro valor.

### Ejemplos mentales

- La gráfica de una recta ($f(x)=2x+1$): la puedes dibujar de un tirón, sin levantar el lápiz. Es continua en todos los puntos.
- La gráfica de $f(x)=\dfrac{1}{x}$: cuando te acercas a $x=0$, la línea se dispara hacia arriba por un lado y hacia abajo por el otro. Tienes que levantar el lápiz para "saltar" de un lado al otro. **No es continua en $x=0$**.

---

## ¿Cuándo es continuo un polinomio?

**Siempre.** Los polinomios (como $3x^2-5x+4$, o $x^3+2x-1$) son continuos en **todos** los números reales. No tienen saltos, ni agujeros, ni se disparan al infinito en ningún punto. Por eso, para un polinomio, siempre puedes calcular el límite **sustituyendo directamente**:

$$
\lim_{x\to a}P(x)=P(a)
$$

---

## ¿Cuándo es continua una función racional?

Una función racional (una fracción de polinomios) es continua **en todos los puntos excepto donde el denominador se anula** (vale 0).

Ejemplo: $f(x)=\dfrac{1}{x-2}$ es continua en todos los números **excepto** en $x=2$, porque ahí el denominador se hace 0 y la función "se dispara" hacia el infinito (o directamente no existe).

---

## Relación entre continuidad y sustitución directa

Si sabes que una función es continua en un punto $a$, entonces puedes calcular el límite **simplemente sustituyendo**:

$$
\lim_{x\to a}f(x)=f(a)
$$

Pero si la función **no** es continua en $a$ (por ejemplo, porque el denominador se anula ahí), sustituir directamente no funciona, y hay que investigar más (factorizar, estudiar límites laterales, etc.) — que es justo lo que se hace en los Ejercicios 2, 3, 6 y 7 del examen.

---

## Un ejemplo que parece continuo pero tiene un "agujero"

$$
f(x)=\frac{x^2-9}{x-3}
$$

Esta función **no está definida** en $x=3$ (el denominador se anula ahí), así que técnicamente hay un "agujero" en la gráfica justo en ese punto.

Sin embargo, si simplificamos:

$$
f(x)=\frac{(x-3)(x+3)}{x-3}=x+3 \quad (\text{para } x\neq3)
$$

vemos que, muy cerca de $x=3$, la función se comporta exactamente como la recta $x+3$, que en $x=3$ valdría 6. Es decir: **el límite existe y vale 6**, aunque la función no esté definida en $x=3$ (solo hay un "agujerito" en ese único punto, pero alrededor todo funciona perfectamente).

Esto ilustra que **el límite habla de los alrededores de un punto, no del punto en sí**. La discontinuidad es **removible**: bastaría definir $f(3)=6$ para rellenar el agujero y hacer continua la función en $3$.

| Tipo de discontinuidad | Qué ocurre cerca del punto | ¿Puede repararse definiendo un solo valor? |
|---|---|---|
| Removible | El límite existe, pero falta $f(a)$ o tiene otro valor | Sí |
| De salto | Los límites laterales son finitos pero distintos | No |
| Infinita | Algún límite lateral es infinito | No |

![Diferencia entre el valor aislado f(3) y el límite](../animaciones/AcercamientoAlLimite.gif)

---

## 🧠 Por qué importa esto para los límites

Entender la continuidad te permite decidir, en cuestión de segundos, **si puedes sustituir directamente** (cuando la función es continua ahí, como en el Ejercicio 1) o si **tienes que investigar más** (cuando hay una discontinuidad, como en los Ejercicios 2, 3, 6 y 7). También te ayuda a entender por qué el límite puede existir en un punto aunque la función no esté definida ahí (Ejercicio 8).

---

## Comprueba lo aprendido

**1. ¿Es continua $f(x)=x^2+1$ en $x=3$?**

<details>
<summary>Comprobar respuesta</summary>

Sí. Es un polinomio y, por tanto, es continuo en todo número real. Además, $\lim_{x\to3}f(x)=f(3)=10$.

</details>

**2. Si $\lim_{x\to a}f(x)=5$ pero $f(a)=2$, ¿es continua en $a$?**

<details>
<summary>Comprobar respuesta</summary>

No. Existen el límite y el valor de la función, pero no coinciden. Es una discontinuidad removible: redefinir $f(a)=5$ la repararía.

</details>

**3. Si los límites laterales valen $2$ y $7$, ¿existe el límite bilateral?**

<details>
<summary>Comprobar respuesta</summary>

No. Para que exista el límite bilateral, ambos límites laterales deben existir y ser iguales.

</details>
