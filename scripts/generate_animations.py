"""Genera animaciones GIF educativas con Manim.

Uso desde la raiz del repositorio:
    .venv/bin/python scripts/generate_animations.py

Los GIF finales se guardan en ``calculo1/limites/animaciones``. Los archivos
intermedios de Manim se escriben en ``.manim-media`` (ignorado por Git).
"""

from __future__ import annotations

import math
import os
from pathlib import Path
import shutil
import subprocess
import sys

from manim import (
    Axes,
    BLUE_C,
    Circle,
    Create,
    DashedLine,
    Dot,
    DOWN,
    FadeIn,
    FadeOut,
    GREEN_C,
    GREY_A,
    LEFT,
    Line,
    PI,
    RED_C,
    RIGHT,
    Scene,
    Text,
    Transform,
    UP,
    ValueTracker,
    VGroup,
    WHITE,
    YELLOW,
    always_redraw,
    linear,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "calculo1" / "limites" / "animaciones"
MEDIA_DIR = ROOT / ".manim-media"
SCENES = (
    "AcercamientoAlLimite",
    "FactorizacionYAgujero",
    "LimitesLaterales",
    "GradosEnElInfinito",
    "TangenteCercaDePiMedios",
)


def heading(text: str) -> Text:
    return Text(text, font_size=34, weight="BOLD", color=WHITE).to_edge(UP)


def caption(text: str, color=GREY_A) -> Text:
    return Text(text, font_size=24, color=color)


class AcercamientoAlLimite(Scene):
    """Distingue el comportamiento cercano del valor aislado f(3)."""

    def construct(self):
        title = heading("El límite mira alrededor del punto")
        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 9, 1],
            x_length=7.2,
            y_length=4.2,
            axis_config={"include_numbers": False},
        ).shift(DOWN * 0.35)
        graph = axes.plot(lambda x: x + 3, x_range=[0.2, 5.8], color=BLUE_C)
        hole = Dot(axes.c2p(3, 6), radius=0.11, color=YELLOW).set_fill(opacity=0)
        actual = Dot(axes.c2p(3, 2), radius=0.09, color=RED_C)
        actual_label = caption("f(3) = 2", RED_C).next_to(actual, RIGHT, buff=0.2)
        limit_label = caption("aunque f(3) sea distinto,  f(x) → 6", YELLOW).to_edge(DOWN)

        left_x = ValueTracker(0.8)
        right_x = ValueTracker(5.2)
        left_dot = always_redraw(
            lambda: Dot(axes.c2p(left_x.get_value(), left_x.get_value() + 3), color=GREEN_C)
        )
        right_dot = always_redraw(
            lambda: Dot(axes.c2p(right_x.get_value(), right_x.get_value() + 3), color=GREEN_C)
        )

        self.add(title)
        self.play(Create(axes), Create(graph), run_time=1.2)
        self.play(FadeIn(hole), FadeIn(actual), FadeIn(actual_label))
        self.add(left_dot, right_dot)
        self.play(
            left_x.animate.set_value(2.92),
            right_x.animate.set_value(3.08),
            FadeIn(limit_label),
            run_time=2.8,
            rate_func=linear,
        )
        self.wait(1.2)


class FactorizacionYAgujero(Scene):
    """Muestra qué se cancela y por qué permanece un agujero en x=3."""

    def construct(self):
        title = heading("Resolver 0/0: factorizar antes de sustituir")
        original = Text("(x² − 9) / (x − 3)", font_size=42, color=WHITE)
        factored = Text("(x − 3)(x + 3) / (x − 3)", font_size=42, color=WHITE)
        simplified = Text("x + 3,   solo si x ≠ 3", font_size=42, color=GREEN_C)
        warning = caption("Se cancelan factores completos; no términos de una suma.", YELLOW)
        warning.to_edge(DOWN)

        self.add(title, original)
        self.wait(0.5)
        self.play(Transform(original, factored), run_time=1.2)
        strike_1 = Line(LEFT * 2.9 + UP * 0.11, LEFT * 1.45 + DOWN * 0.11, color=RED_C)
        strike_2 = Line(RIGHT * 1.23 + UP * 0.11, RIGHT * 2.62 + DOWN * 0.11, color=RED_C)
        self.play(Create(strike_1), Create(strike_2), FadeIn(warning), run_time=0.8)
        self.wait(0.5)
        self.play(
            FadeOut(strike_1),
            FadeOut(strike_2),
            Transform(original, simplified),
            run_time=1.1,
        )
        conclusion = VGroup(
            caption("Cerca de 3:  x + 3 → 6", BLUE_C),
            caption("La restricción x ≠ 3 deja un agujero en (3, 6).", YELLOW),
        ).arrange(DOWN, buff=0.35).next_to(original, DOWN, buff=0.65)
        self.play(FadeIn(conclusion))
        self.wait(1.3)


class LimitesLaterales(Scene):
    """Visualiza los signos opuestos de 1/(x-2) por cada lado."""

    def construct(self):
        title = heading("Una asíntota: dos comportamientos laterales")
        axes = Axes(
            x_range=[-1, 5, 1],
            y_range=[-8, 8, 2],
            x_length=7.2,
            y_length=4.5,
            axis_config={"include_numbers": False},
        ).shift(DOWN * 0.25)
        left_graph = axes.plot(lambda x: 1 / (x - 2), x_range=[-0.8, 1.86], color=BLUE_C)
        right_graph = axes.plot(lambda x: 1 / (x - 2), x_range=[2.14, 4.8], color=BLUE_C)
        asymptote = DashedLine(axes.c2p(2, -8), axes.c2p(2, 8), color=RED_C)

        lx = ValueTracker(0.2)
        rx = ValueTracker(4.2)
        left_dot = always_redraw(
            lambda: Dot(axes.c2p(lx.get_value(), 1 / (lx.get_value() - 2)), color=YELLOW)
        )
        right_dot = always_redraw(
            lambda: Dot(axes.c2p(rx.get_value(), 1 / (rx.get_value() - 2)), color=GREEN_C)
        )
        labels = VGroup(
            caption("x → 2⁻  ⇒  f(x) → −∞", YELLOW),
            caption("x → 2⁺  ⇒  f(x) → +∞", GREEN_C),
        ).arrange(RIGHT, buff=1.0).to_edge(DOWN)

        self.add(title)
        self.play(Create(axes), Create(left_graph), Create(right_graph), Create(asymptote), run_time=1.2)
        self.add(left_dot, right_dot)
        self.play(
            lx.animate.set_value(1.86),
            rx.animate.set_value(2.14),
            FadeIn(labels),
            run_time=3,
            rate_func=linear,
        )
        self.wait(1.2)


class GradosEnElInfinito(Scene):
    """Compara numéricamente dos cocientes cuando x crece."""

    def construct(self):
        title = heading("En el infinito dominan los términos de mayor grado")
        x = ValueTracker(2)

        top_formula = Text("(4x² − 3x + 1) / (2x² + 5x − 7)", font_size=30)
        bottom_formula = Text("(3x + 2) / (x² − 1)", font_size=30)
        top_formula.move_to(UP * 1.3 + LEFT * 1.2)
        bottom_formula.move_to(DOWN * 1.2 + LEFT * 1.2)

        x_label = Text("x =", font_size=30).to_edge(LEFT).shift(UP * 2.15)
        x_value = always_redraw(
            lambda: Text(f"{x.get_value():.0f}", font_size=30, color=YELLOW).next_to(x_label, RIGHT)
        )

        equal_top = Text("→", font_size=38).next_to(top_formula, RIGHT, buff=0.35)
        equal_bottom = Text("→", font_size=38).next_to(bottom_formula, RIGHT, buff=0.35)
        top_value = always_redraw(
            lambda: Text(
                f"{(4 * x.get_value() ** 2 - 3 * x.get_value() + 1) / (2 * x.get_value() ** 2 + 5 * x.get_value() - 7):.4f}",
                font_size=34,
                color=GREEN_C,
            ).next_to(equal_top, RIGHT)
        )
        bottom_value = always_redraw(
            lambda: Text(
                f"{(3 * x.get_value() + 2) / (x.get_value() ** 2 - 1):.4f}",
                font_size=34,
                color=BLUE_C,
            ).next_to(equal_bottom, RIGHT)
        )
        limits = VGroup(
            caption("mismo grado  ⇒  cociente → 4/2 = 2", GREEN_C),
            caption("grado inferior arriba  ⇒  cociente → 0", BLUE_C),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).to_edge(DOWN)

        self.add(title, x_label, x_value, top_formula, bottom_formula, equal_top, equal_bottom)
        self.add(top_value, bottom_value)
        self.play(x.animate.set_value(10000), FadeIn(limits), run_time=3.5, rate_func=linear)
        self.wait(1.3)


class TangenteCercaDePiMedios(Scene):
    """Relaciona el círculo unidad con los signos de la tangente."""

    def construct(self):
        title = heading("Tangente cerca de π/2: el coseno cambia de signo")
        center = LEFT * 3.4 + DOWN * 0.1
        radius = 1.45
        circle = Circle(radius=radius, color=GREY_A).move_to(center)
        h_axis = Line(center + LEFT * 1.7, center + RIGHT * 1.7, color=GREY_A)
        v_axis = Line(center + DOWN * 1.7, center + UP * 1.7, color=GREY_A)

        axes = Axes(
            x_range=[0, math.pi, math.pi / 2],
            y_range=[-5, 5, 2.5],
            x_length=5.3,
            y_length=3.5,
            axis_config={"include_numbers": False},
        ).shift(RIGHT * 2.0 + DOWN * 0.15)
        x_labels = VGroup(
            caption("0").next_to(axes.c2p(0, 0), DOWN, buff=0.15),
            caption("π/2").next_to(axes.c2p(math.pi / 2, 0), DOWN, buff=0.15),
            caption("π").next_to(axes.c2p(math.pi, 0), DOWN, buff=0.15),
        )
        tan_left = axes.plot(math.tan, x_range=[0.05, 1.37], color=YELLOW)
        tan_right = axes.plot(math.tan, x_range=[1.77, math.pi - 0.05], color=GREEN_C)
        asymptote = DashedLine(axes.c2p(math.pi / 2, -5), axes.c2p(math.pi / 2, 5), color=RED_C)

        left_angle = ValueTracker(0.35)
        right_angle = ValueTracker(math.pi - 0.35)
        circle_left = always_redraw(
            lambda: Dot(
                center
                + radius
                * (math.cos(left_angle.get_value()) * RIGHT + math.sin(left_angle.get_value()) * UP),
                color=YELLOW,
            )
        )
        circle_right = always_redraw(
            lambda: Dot(
                center
                + radius
                * (math.cos(right_angle.get_value()) * RIGHT + math.sin(right_angle.get_value()) * UP),
                color=GREEN_C,
            )
        )
        ray_left = always_redraw(lambda: Line(center, circle_left.get_center(), color=YELLOW))
        ray_right = always_redraw(lambda: Line(center, circle_right.get_center(), color=GREEN_C))
        graph_left = always_redraw(
            lambda: Dot(axes.c2p(left_angle.get_value(), math.tan(left_angle.get_value())), color=YELLOW)
        )
        graph_right = always_redraw(
            lambda: Dot(axes.c2p(right_angle.get_value(), math.tan(right_angle.get_value())), color=GREEN_C)
        )
        labels = VGroup(
            caption("desde la izquierda: cos x → 0⁺, tan x → +∞", YELLOW),
            caption("desde la derecha: cos x → 0⁻, tan x → −∞", GREEN_C),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).to_edge(DOWN)

        self.add(title)
        self.play(
            Create(circle), Create(h_axis), Create(v_axis), Create(axes),
            Create(tan_left), Create(tan_right), Create(asymptote), FadeIn(x_labels),
            run_time=1.3,
        )
        self.add(ray_left, ray_right, circle_left, circle_right, graph_left, graph_right)
        self.play(
            left_angle.animate.set_value(1.37),
            right_angle.animate.set_value(1.77),
            FadeIn(labels),
            run_time=3,
            rate_func=linear,
        )
        self.wait(1.2)


def render_all() -> None:
    """Renderiza todas las escenas y copia solo los GIF finales."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env["MANIM_RENDERING"] = "1"
    command = [
        sys.executable,
        "-m",
        "manim",
        "render",
        "-ql",
        "--format=gif",
        "--disable_caching",
        f"--media_dir={MEDIA_DIR}",
        str(Path(__file__).resolve()),
        *SCENES,
    ]
    subprocess.run(command, cwd=ROOT, env=env, check=True)

    for scene in SCENES:
        matches = list(MEDIA_DIR.glob(f"videos/**/{scene}*.gif"))
        if not matches:
            raise FileNotFoundError(f"Manim no generó el GIF de {scene}")
        destination = OUTPUT_DIR / f"{scene}.gif"
        shutil.copy2(matches[0], destination)
        print(f"guardado {destination.relative_to(ROOT)}")


if __name__ == "__main__" and os.environ.get("MANIM_RENDERING") != "1":
    render_all()
