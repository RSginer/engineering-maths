# Matemáticas para Ingeniería Informática

Repositorio con material de estudio de matemáticas para Ingeniería Informática:
exámenes, soluciones paso a paso, teoría y prerrequisitos. Las gráficas
estáticas y las animaciones con Manim conectan el cálculo simbólico con el
comportamiento visual de las funciones.

El repositorio va creciendo por bloques temáticos (asignaturas/temas). Por
ahora contiene **Cálculo I**, empezando por el tema de **Límites**; con el
tiempo se irán añadiendo más asignaturas y temas.

## Índice

### Cálculo I

- [calculo1/limites/](calculo1/limites/) — Bloque de **Límites**
  - [examen-limites-1.md](calculo1/limites/examen-limites-1.md) — Examen (8 ejercicios, 10 puntos)
  - [soluciones-examen-limites-1.md](calculo1/limites/soluciones-examen-limites-1.md) — Soluciones resueltas paso a paso
  - [teoria-limites.md](calculo1/limites/teoria-limites.md) — Teoría necesaria para resolver el examen
  - [laboratorio-limites.ipynb](calculo1/limites/laboratorio-limites.ipynb) — Exploración numérica opcional con Python
  - [pre-saberes/indice.md](calculo1/limites/pre-saberes/indice.md) — Prerrequisitos matemáticos antes de límites
    - [01-aritmetica.md](calculo1/limites/pre-saberes/01-aritmetica.md)
    - [02-algebra.md](calculo1/limites/pre-saberes/02-algebra.md)
    - [03-racionalizacion.md](calculo1/limites/pre-saberes/03-racionalizacion.md)
    - [04-funciones.md](calculo1/limites/pre-saberes/04-funciones.md)
    - [05-grado-polinomio.md](calculo1/limites/pre-saberes/05-grado-polinomio.md)
    - [06-estudio-signos.md](calculo1/limites/pre-saberes/06-estudio-signos.md)
    - [07-trigonometria.md](calculo1/limites/pre-saberes/07-trigonometria.md)
    - [08-infinito-acercarse.md](calculo1/limites/pre-saberes/08-infinito-acercarse.md)
    - [09-continuidad.md](calculo1/limites/pre-saberes/09-continuidad.md)
    - [10-notacion.md](calculo1/limites/pre-saberes/10-notacion.md)

## Convenciones del repositorio

Este repo sigue una serie de convenciones (notación matemática en Markdown,
cómo generar gráficas, etc.) documentadas para agentes de IA en
[AGENTS.md](AGENTS.md) (también válido para Claude Code vía [CLAUDE.md](CLAUDE.md)).
Si vas a editar o añadir contenido, revisa ese archivo primero.

## Ejecutar los laboratorios

Los laboratorios son cuadernos de Jupyter (`.ipynb`) que permiten modificar
valores, ejecutar cálculos y generar gráficas. Los siguientes comandos deben
ejecutarse desde la raíz del repositorio.

La primera vez, crea el entorno virtual e instala las dependencias:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

Después, abre el laboratorio de límites con:

```bash
.venv/bin/jupyter lab calculo1/limites/laboratorio-limites.ipynb
```

JupyterLab se abrirá en el navegador. Para ejecutar el cuaderno completo,
selecciona **Run → Run All Cells**. También puedes ejecutar una celda cada vez
con `Shift + Enter`, lo que resulta útil para cambiar un valor y observar cómo
varían las tablas o las gráficas.

Para cerrar JupyterLab, vuelve a la terminal, pulsa `Ctrl + C` y confirma la
detención si se solicita.

> [!TIP]
> No es necesario activar el entorno virtual: utilizar `.venv/bin/jupyter`
> garantiza que se ejecute la versión instalada para este repositorio.

## Regenerar el material visual

Las dependencias de Python están en `requirements.txt`. En macOS, Manim necesita además Cairo, Pango y FFmpeg:

```bash
brew install cairo pango ffmpeg
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

Después se pueden regenerar por separado las gráficas y las animaciones:

```bash
.venv/bin/python scripts/generate_graphs.py
.venv/bin/python scripts/generate_animations.py
```

Los PNG se guardan en las carpetas `img/` y los GIF en `calculo1/limites/animaciones/`.
