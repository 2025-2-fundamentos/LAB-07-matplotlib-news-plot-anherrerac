"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import pandas as pd
import matplotlib.pyplot as plt
import os
import glob

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    ruta_base = "files/input/news.csv"
    ruta_final = "files/plots"
    
    if os.path.exists(ruta_final):
        for file in glob.glob(f"{ruta_final}/*"):
            os.remove(file)
        os.rmdir(ruta_final)
    os.makedirs(ruta_final)
    
    plt.Figure()
    
    colors = {
        "Television" : "dimgray",
        "Newspaper" : "grey",
        "Internet" : "tab:blue",
        "Radio" : "lightgrey",
    }
    
    zorder = {
        "Television" : 1,
        "Newspaper" : 1,
        "Internet" : 2,
        "Radio" : 1,
    }
    
    linewidths = {
        "Television" : 2,
        "Newspaper" : 2,
        "Internet" : 4,
        "Radio" : 2,
    }
    
    df = pd.read_csv(ruta_base, index_col=0)
    for col in df.columns:
        plt.plot(df[col], color=colors[col], label=col, zorder=zorder[col], linewidth=linewidths[col])   
    
    plt.title("How people get their news", fontsize=16)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)
    
    for col in df.columns:
        firt_year = df.index[0]
        plt.scatter(x=firt_year, y=df[col][firt_year],color=colors[col],zorder=zorder[col])
        plt.text(firt_year - 0.2, df[col][firt_year], col + " " + str(df[col][firt_year]) + "%", ha="right", va="center", color=colors[col])
    
        last_year = df.index[-1]
        plt.scatter(x=last_year, y=df[col][last_year],color=colors[col],zorder=zorder[col])
        plt.text(last_year + 0.2, df[col][last_year], str(df[col][last_year]) + "%", ha="left", va="center", color=colors[col])
    
    plt.xticks(ticks=df.index, label=df.index, ha="center")
    
    plt.tight_layout()
    plt.savefig(f"{ruta_final}/news.png")