"""Generate Cartesian-plane graphs (PNG) for calculo1 markdown docs.

Run inside the repo venv:
    source .venv/bin/activate && python3 scripts/generate_graphs.py
"""
import numpy as np
import matplotlib.pyplot as plt

LIMITES_IMG = "calculo1/limites/img"
PRESABERES_IMG = "calculo1/limites/pre-saberes/img"


def new_axes(xlim, ylim, title):
    fig, ax = plt.subplots(figsize=(6, 5), dpi=150)
    ax.axhline(0, color="black", linewidth=1)
    ax.axvline(0, color="black", linewidth=1)
    ax.grid(True, linestyle="--", alpha=0.4)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title(title)
    return fig, ax


def save(fig, path):
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)
    print("saved", path)


# ---------------------------------------------------------------------------
# Ejercicio 1: f(x) = 3x^2 - 5x + 4 (parabola, continua, sustitucion directa)
# ---------------------------------------------------------------------------
x = np.linspace(-2, 4, 400)
y = 3 * x ** 2 - 5 * x + 4
fig, ax = new_axes((-2, 4), (0, 40), "Ejercicio 1: f(x) = 3x² - 5x + 4")
ax.plot(x, y, color="tab:blue")
ax.plot(2, 3 * 2 ** 2 - 5 * 2 + 4, "o", color="tab:red")
ax.annotate("x=2 → f(2)=6", (2, 6), textcoords="offset points", xytext=(10, -15))
save(fig, f"{LIMITES_IMG}/ejercicio1.png")

# ---------------------------------------------------------------------------
# Ejercicio 2: f(x) = (x^2-9)/(x-3) = x+3, con un "agujero" en x=3
# ---------------------------------------------------------------------------
x = np.linspace(-2, 8, 400)
x = x[np.abs(x - 3) > 0.001]
y = x + 3
fig, ax = new_axes((-2, 8), (-2, 12), "Ejercicio 2: f(x) = (x²-9)/(x-3)")
ax.plot(x, y, color="tab:blue")
ax.plot(3, 6, "o", markerfacecolor="white", markeredgecolor="tab:red", markersize=8)
ax.annotate("agujero en x=3\n(límite = 6)", (3, 6), textcoords="offset points", xytext=(10, -25))
save(fig, f"{LIMITES_IMG}/ejercicio2.png")

# ---------------------------------------------------------------------------
# Ejercicio 3: f(x) = (x^2+x+2)/(x+1), asintota vertical en x=-1
# ---------------------------------------------------------------------------
def f3(x):
    return (x ** 2 + x + 2) / (x + 1)

fig, ax = new_axes((-6, 4), (-20, 20), "Ejercicio 3: f(x) = (x²+x+2)/(x+1)")
for lo, hi in [(-6, -1.02), (-0.98, 4)]:
    x = np.linspace(lo, hi, 400)
    ax.plot(x, f3(x), color="tab:blue")
ax.axvline(-1, color="tab:red", linestyle="--")
ax.annotate("asíntota vertical x=-1", (-1, 15), textcoords="offset points", xytext=(10, 0))
save(fig, f"{LIMITES_IMG}/ejercicio3.png")

# ---------------------------------------------------------------------------
# Ejercicio 4: f(x) = (4x^2-3x+1)/(2x^2+5x-7), asintota horizontal y=2
# ---------------------------------------------------------------------------
def f4(x):
    return (4 * x ** 2 - 3 * x + 1) / (2 * x ** 2 + 5 * x - 7)

fig, ax = new_axes((-15, 15), (-4, 8), "Ejercicio 4: f(x) = (4x²-3x+1)/(2x²+5x-7)")
roots = [1, -3.5]  # 2x^2+5x-7 = 0 -> x=1, x=-3.5
bounds = sorted([-15] + roots + [15])
for i in range(len(bounds) - 1):
    lo, hi = bounds[i] + 0.05, bounds[i + 1] - 0.05
    if hi <= lo:
        continue
    x = np.linspace(lo, hi, 400)
    ax.plot(x, f4(x), color="tab:blue")
ax.axhline(2, color="tab:green", linestyle="--")
ax.annotate("asíntota horizontal y=2", (-14, 2.3))
save(fig, f"{LIMITES_IMG}/ejercicio4.png")

# ---------------------------------------------------------------------------
# Ejercicio 5: f(x) = (3x+2)/(x^2-1), asintota horizontal y=0
# ---------------------------------------------------------------------------
def f5(x):
    return (3 * x + 2) / (x ** 2 - 1)

fig, ax = new_axes((-10, 10), (-6, 6), "Ejercicio 5: f(x) = (3x+2)/(x²-1)")
bounds = sorted([-10, -1, 1, 10])
for i in range(len(bounds) - 1):
    lo, hi = bounds[i] + 0.05, bounds[i + 1] - 0.05
    x = np.linspace(lo, hi, 400)
    ax.plot(x, f5(x), color="tab:blue")
ax.axhline(0, color="tab:green", linestyle="--")
ax.annotate("asíntota horizontal y=0", (-9, 0.6))
save(fig, f"{LIMITES_IMG}/ejercicio5.png")

# ---------------------------------------------------------------------------
# Ejercicio 6: f(x) = 1/(x-2), asintota vertical en x=2
# ---------------------------------------------------------------------------
def f6(x):
    return 1 / (x - 2)

fig, ax = new_axes((-2, 6), (-10, 10), "Ejercicio 6: f(x) = 1/(x-2)")
for lo, hi in [(-2, 1.9), (2.1, 6)]:
    x = np.linspace(lo, hi, 400)
    ax.plot(x, f6(x), color="tab:blue")
ax.axvline(2, color="tab:red", linestyle="--")
ax.annotate("asíntota vertical x=2", (2.2, 8))
save(fig, f"{LIMITES_IMG}/ejercicio6.png")

# ---------------------------------------------------------------------------
# Ejercicio 7: f(x) = tan(x), asintotas en pi/2 + k*pi
# ---------------------------------------------------------------------------
fig, ax = new_axes((-np.pi, 2 * np.pi), (-10, 10), "Ejercicio 7: f(x) = tan(x)")
for k in range(-1, 2):
    center = np.pi / 2 + k * np.pi
    x = np.linspace(center - np.pi / 2 + 0.05, center + np.pi / 2 - 0.05, 400)
    ax.plot(x, np.tan(x), color="tab:blue")
    ax.axvline(center, color="tab:red", linestyle="--")
ax.set_xticks([-np.pi / 2, 0, np.pi / 2, np.pi, 3 * np.pi / 2])
ax.set_xticklabels(["-π/2", "0", "π/2", "π", "3π/2"])
save(fig, f"{LIMITES_IMG}/ejercicio7.png")

# ---------------------------------------------------------------------------
# Pre-saberes 04: tipos de funciones basicas
# ---------------------------------------------------------------------------
x = np.linspace(-5, 5, 400)
fig, ax = new_axes((-5, 5), (-10, 10), "Función lineal: f(x) = 2x + 1")
ax.plot(x, 2 * x + 1, color="tab:blue")
save(fig, f"{PRESABERES_IMG}/lineal.png")

fig, ax = new_axes((-4, 4), (-1, 16), "Función cuadrática: f(x) = x²")
ax.plot(x, x ** 2, color="tab:blue")
save(fig, f"{PRESABERES_IMG}/cuadratica.png")

fig, ax = new_axes((-4, 4), (-2, 2), "Función raíz: f(x) = √x")
xr = np.linspace(0, 5, 200)
ax.plot(xr, np.sqrt(xr), color="tab:blue")
save(fig, f"{PRESABERES_IMG}/raiz.png")

fig, ax = new_axes((-4, 4), (-10, 10), "Función racional: f(x) = 1/(x-2)")
for lo, hi in [(-4, 1.9), (2.1, 4)]:
    xx = np.linspace(lo, hi, 300)
    ax.plot(xx, 1 / (xx - 2), color="tab:blue")
ax.axvline(2, color="tab:red", linestyle="--")
save(fig, f"{PRESABERES_IMG}/racional.png")

print("Todas las gráficas generadas correctamente.")
