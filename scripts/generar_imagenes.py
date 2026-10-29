"""Genera las portadas de ejemplo, la foto provisoria y el favicon del sitio.

Uso (desde la carpeta del sitio):  python scripts/generar_imagenes.py
Cuando tengas tu foto real, guardala como img/foto.png (cuadrada, mínimo 400x400).
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

RAIZ = Path(__file__).resolve().parent.parent
PAPEL, TINTA, SUAVE, ACENTO, ALERTA = "#1a2028", "#f3f2ee", "#5d6874", "#4fb3a9", "#e07a4f"


def lienzo(ancho=8, alto=4.5):
    fig, ax = plt.subplots(figsize=(ancho, alto), dpi=150)
    fig.patch.set_facecolor(PAPEL)
    ax.set_facecolor(PAPEL)
    ax.set_axis_off()
    return fig, ax


def guardar(fig, ruta):
    if ruta.exists():  # nunca pisa una imagen que ya está (por ejemplo, tu foto real)
        plt.close(fig)
        return
    ruta.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(ruta, facecolor=fig.get_facecolor(), bbox_inches="tight", pad_inches=0)
    plt.close(fig)


def portada_empiezo():
    """Una serie que arranca: puntos que se van ordenando en una línea."""
    rng = np.random.default_rng(3)
    fig, ax = lienzo()
    x = np.linspace(0, 10, 60)
    ruido = rng.normal(0, 1, 60) * np.linspace(1.6, 0.05, 60)
    y = 0.35 * x + ruido
    ax.scatter(x, y, s=np.linspace(10, 70, 60), color=ACENTO, alpha=0.85)
    ax.plot(x, 0.35 * x, color=TINTA, lw=1, alpha=0.35)
    ax.set_xlim(-0.5, 10.5)
    guardar(fig, RAIZ / "posts/2026-11-01-empiezo/portada.png")


def portada_promedio():
    """Muchos puntos juntos y uno lejos: la media se va, la mediana se queda."""
    rng = np.random.default_rng(42)
    fig, ax = lienzo()
    datos = rng.normal(100, 12, 30)
    ax.scatter(datos, rng.uniform(-0.15, 0.15, 30), s=60, color=SUAVE)
    ax.scatter([300], [0], s=110, color=ALERTA)
    ax.axvline(np.median(datos), color=ACENTO, lw=3)
    ax.axvline(np.append(datos, 300).mean(), color=ALERTA, lw=3, ls="--")
    ax.set_ylim(-0.6, 0.6)
    ax.set_xlim(55, 320)
    guardar(fig, RAIZ / "posts/2026-11-15-cuando-el-promedio-miente/portada.png")


def portada_proyecto():
    """Barras apiladas por día de la semana."""
    rng = np.random.default_rng(7)
    fig, ax = lienzo()
    base = np.array([0.9, 0.85, 0.9, 0.95, 1.1, 1.35, 1.0])
    abajo = np.zeros(7)
    for color, (lo, hi) in zip([ACENTO, "#7fb3ad", "#c9a227"], [(0.35, 0.5), (0.25, 0.35), (0.2, 0.35)]):
        alto = base * rng.uniform(lo, hi, 7)
        ax.bar(range(7), alto, bottom=abajo, color=color, width=0.62)
        abajo += alto
    guardar(fig, RAIZ / "proyectos/plantilla-proyecto/portada.png")


def foto_provisoria():
    fig, ax = plt.subplots(figsize=(4, 4), dpi=150)
    fig.patch.set_facecolor(ACENTO)
    ax.set_axis_off()
    ax.text(0.5, 0.5, "MB", ha="center", va="center", fontsize=90, color=PAPEL,
            fontweight="bold", transform=ax.transAxes)
    guardar(fig, RAIZ / "img/foto.png")


def favicon():
    fig, ax = plt.subplots(figsize=(1, 1), dpi=64)
    fig.patch.set_facecolor(ACENTO)
    ax.set_axis_off()
    ax.text(0.5, 0.45, "x̄", ha="center", va="center", fontsize=38, color=PAPEL, transform=ax.transAxes)
    guardar(fig, RAIZ / "img/favicon.png")


if __name__ == "__main__":
    portada_empiezo()
    portada_promedio()
    portada_proyecto()
    foto_provisoria()
    favicon()
    print("Imágenes generadas.")
