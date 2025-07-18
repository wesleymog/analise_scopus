import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import warnings
import os

warnings.filterwarnings('ignore')

def configurar_estilo_grafico():
    """Configura o estilo visual padrão para todos os gráficos."""
    plt.style.use('seaborn-v0_8-whitegrid')
    sns.set_palette("viridis")
    plt.rcParams.update({
        'figure.figsize': (14, 8),
        'font.size': 12,
        'axes.titlesize': 16,
        'axes.labelsize': 14,
        'xtick.labelsize': 12,
        'ytick.labelsize': 12,
        'axes.formatter.useoffset': False,
        'axes.formatter.limits': (-3, 3),
        'figure.autolayout': True
    })

def configurar_eixos_inteiros(ax, axis='y'):
    """Configura os eixos para exibir apenas números inteiros."""
    if axis in ['x', 'both']:
        ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))
    if axis in ['y', 'both']:
        ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True))

def adicionar_rotulos_barras(bars, ax, horizontal=False):
    """Adiciona rótulos de dados às barras de um gráfico."""
    for bar in bars:
        if horizontal:
            x_val = bar.get_width()
            y_val = bar.get_y() + bar.get_height() / 2
            ax.text(x_val + 0.1, y_val, f'{int(x_val)}', va='center', ha='left', fontsize=12)
        else:
            x_val = bar.get_x() + bar.get_width() / 2
            y_val = bar.get_height()
            ax.text(x_val, y_val, f'{int(y_val)}', ha='center', va='bottom', fontsize=12, fontweight='bold')

# --- Funções de Geração de Gráficos ---

def gerar_distribuicao_categorias_rq1(df, output_dir):
    """Gera e salva o gráfico de distribuição de categorias para RQ1."""
    print("Gerando gráfico: Distribuição das Categorias para RQ1...")
    rq1_data = df[df['categoria_rq1'].notna() & (df['categoria_rq1'] != '')]
    categoria_counts = rq1_data['categoria_rq1'].value_counts()
    
    fig, ax = plt.subplots(figsize=(12, 8))
    colors = sns.color_palette("viridis", len(categoria_counts))
    
    bars = ax.barh(categoria_counts.index, categoria_counts.values, color=colors)
    ax.set_title('Distribuição das Categorias para RQ1 (Como são feitas)', fontweight='bold')
    ax.set_xlabel('Número de Códigos')
    ax.invert_yaxis()  # Categorias mais frequentes no topo
    configurar_eixos_inteiros(ax, 'x')
    adicionar_rotulos_barras(bars, ax, horizontal=True)

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'distribuicao_categorias_rq1.png'), dpi=300)
    plt.close(fig)
    print("Gráfico 'distribuicao_categorias_rq1.png' salvo.")

def gerar_categorias_bardin_rq2(df, output_dir):
    """Gera e salva o gráfico de categorias de Bardin para RQ2."""
    print("Gerando gráfico: Categorias de Bardin para RQ2...")
    rq2_data = df[df['categoria_rq2'].notna() & (df['categoria_rq2'] != '')]
    categoria_counts = rq2_data['categoria_rq2'].value_counts()
    
    fig, ax = plt.subplots(figsize=(12, 8))
    colors = sns.color_palette("viridis_r", len(categoria_counts))
    
    bars = ax.barh(categoria_counts.index, categoria_counts.values, color=colors)
    ax.set_title('Categorias de Bardin para RQ2 (Desafios)', fontweight='bold')
    ax.set_xlabel('Número de Códigos')
    ax.invert_yaxis()
    configurar_eixos_inteiros(ax, 'x')
    adicionar_rotulos_barras(bars, ax, horizontal=True)

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'categorias_bardin_por_rq2.png'), dpi=300)
    plt.close(fig)
    print("Gráfico 'categorias_bardin_por_rq2.png' salvo.")

def gerar_artigos_mais_citados(df, output_dir):
    """Gera e salva os gráficos de artigos mais citados para RQ1 e RQ2."""
    print("Gerando gráfico: Artigos mais citados...")
    
    rq1_data = df[df['rqs'].str.contains('1', na=False)]
    rq2_data = df[df['rqs'].str.contains('2', na=False)]

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 16), sharex=True)
    
    # Gráfico para RQ1
    artigo_counts_rq1 = rq1_data['artigo'].value_counts().nlargest(8)
    colors_rq1 = sns.color_palette("viridis", len(artigo_counts_rq1))
    bars1 = ax1.barh(artigo_counts_rq1.index, artigo_counts_rq1.values, color=colors_rq1)
    ax1.set_title('RQ1: Artigos mais Citados', fontweight='bold')
    configurar_eixos_inteiros(ax1, 'x')
    adicionar_rotulos_barras(bars1, ax1, horizontal=True)

    # Gráfico para RQ2
    artigo_counts_rq2 = rq2_data['artigo'].value_counts().nlargest(8)
    colors_rq2 = sns.color_palette("viridis_r", len(artigo_counts_rq2))
    bars2 = ax2.barh(artigo_counts_rq2.index, artigo_counts_rq2.values, color=colors_rq2)
    ax2.set_title('RQ2: Artigos mais Citados', fontweight='bold')
    ax2.set_xlabel('Número de Códigos')
    configurar_eixos_inteiros(ax2, 'x')
    adicionar_rotulos_barras(bars2, ax2, horizontal=True)

    plt.tight_layout(pad=3.0)
    plt.savefig(os.path.join(output_dir, 'artigos_mais_citados.png'), dpi=300)
    plt.close(fig)
    print("Gráfico 'artigos_mais_citados.png' salvo.")

# --- Função Principal ---

def main():
    """Função principal para carregar dados e gerar gráficos."""
    # Carregar dados
    input_csv = 'scopus_categorias_atualizadas_rq1_final.csv'
    try:
        df = pd.read_csv(input_csv)
        print(f"Arquivo '{input_csv}' carregado com sucesso com {len(df)} linhas.")
    except FileNotFoundError:
        print(f"Erro: Arquivo '{input_csv}' não encontrado.")
        return

    # Criar diretório para salvar os gráficos
    output_dir = 'graficos_gerados'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Diretório '{output_dir}' criado.")

    # Configurar estilo e gerar gráficos
    configurar_estilo_grafico()
    
    gerar_distribuicao_categorias_rq1(df, output_dir)
    gerar_categorias_bardin_rq2(df, output_dir)
    gerar_artigos_mais_citados(df, output_dir)

    print("\nTodos os gráficos foram gerados e salvos com sucesso!")

if __name__ == '__main__':
    main() 