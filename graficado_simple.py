"""
    GRAFICADO SIMPLE

Bokeh permite construir gráficas complejas de manera
rápida y con comandos simples.
Permite exportar varios fromatos como html, notebooks, imágenes, etc.
"""
from bokeh.plotting import figure, output_file, show
import random

if __name__ == '__main__':
    output_file('graficado_simple.html')
    fig = figure()
    
    total_vals = int(input('Cuantos valores quieres graficar?'))
    x_vals = list(range(total_vals))
    y_vals = list(random.random() for i in range(len(x_vals)))

    fig.line(x_vals, y_vals, line_width=2)
    show(fig)