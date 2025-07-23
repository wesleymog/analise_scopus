import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import warnings
import os
import textwrap

warnings.filterwarnings('ignore')

def translate_categories(df):
    """Translate Portuguese categories and subcategories to English."""
    
    # Translation dictionary for categories - using exact names from main.tex
    category_translations = {
        # RQ1 Categories - exact names from main.tex
        'Metodologia e Condução': 'Conduction Methodology',
        'Definição e Propósito': 'Definition and Purpose',
        'Estrutura e Organizacao': 'Structure and Organization',
        'Fatores Contextuais': 'Contextual Factors',
        'Desafios e problemas': 'Challenges and Problems',
        'Facilitação': 'Facilitation',
        
        # RQ2 Categories - exact names from main.tex
        'Desafios de Participação': 'Participation Challenges',
        'Desafios de Eficácia': 'Effectiveness Challenges',
        'Desafios de Implementação': 'Implementation Challenges',
        'Desafios de Comunicação': 'Communication Challenges',
        'Desafios de Foco': 'Focus Challenges',
        'Estrutura Organizacional': 'Organizational Structure',
        'Fatores Contextuais': 'Contextual Factors',
        'Metodologia de Condução': 'Conduction Methodology',
        'Padrões Negativos': 'Negative Patterns',
        
        # Categories with leading spaces (data cleaning issues)
        ' Padrões Negativos': 'Negative Patterns',
        ' Desafios de Implementação': 'Implementation Challenges',
        ' Desafios de Participação': 'Participation Challenges',
        ' Desafios de Eficácia': 'Effectiveness Challenges',
        ' Metodologia de Condução': 'Conduction Methodology'
    }
    
    # Translation dictionary for subcategories
    subcategory_translations = {
        # RQ1 Subcategories
        'Técnicas de Facilitação': 'Facilitation Techniques and Activities',
        'Acompanhamento': 'Follow-up and Monitoring',
        'Modalidade de Reunião': 'Meeting Format and Modality',
        'Estrutura de Questões': 'Question Framework and Structure',
        'Estrutura Padrão': 'Standard Meeting Format',
        'Duração': 'Meeting Duration and Timing',
        'Resultados Esperados': 'Expected Outcomes and Deliverables',
        'Conteúdo da Discussão': 'Discussion Topics and Content',
        'Melhoria Contínua': 'Continuous Process Improvement',
        'Timing': 'Meeting Scheduling and Frequency',
        'Reflexão e Aprendizado': 'Reflection and Learning Processes',
        'Inspeção e Melhoria': 'Inspection and Improvement Cycles',
        'Organização de Aprendi': 'Learning Organization Principles',
        'Histórico': 'Historical Context and Evolution',
        'Estrutura Hierárquica': 'Hierarchical Meeting Structure',
        'Seleção de Problemas': 'Problem Identification and Selection',
        'Priorização': 'Issue Prioritization and Ranking',
        
        # RQ2 Subcategories
        'Engajamento': 'Team Engagement and Motivation',
        'Percepção de Valor': 'Value Perception and Meeting Utility',
        'Falta de Resultados': 'Lack of Tangible Outcomes',
        'Falta de Implementação': 'Lack of Action Implementation',
        'Formato Alternativo': 'Alternative Meeting Formats',
        'Qualidade vs Quantidade': 'Quality vs Quantity of Participation',
        'Pressão Temporal': 'Time Pressure and Constraints',
        'Tamanho do Grupo': 'Group Size and Dynamics',
        'Maturidade do Time': 'Team Maturity and Experience',
        'Priorização de Conteúdo': 'Content Prioritization and Focus',
        'Restrições de Tempo': 'Time Constraints and Limitations',
        'Monotonia': 'Meeting Monotony and Repetitiveness',
        'Complexidade dos Problemas': 'Problem Complexity and Scope',
        'Falta de Estrutura': 'Lack of Meeting Structure',
        'Comportamento Negativo': 'Negative Team Behaviors',
        'Distribuição de Participação': 'Uneven Participation Distribution',
        'Resistência': 'Team Resistance and Reluctance',
        'Repetição': 'Repetitive Issues and Discussions',
        'Conteúdo Insuficiente': 'Insufficient Discussion Content',
        'Gestão de Tempo': 'Time Management and Efficiency',
        'Comunicação': 'Communication Barriers and Issues',
        'Priorização': 'Issue Prioritization Challenges',
        'Barreiras Organizacionais': 'Organizational Barriers and Constraints',
        'Padrões Negativos': 'Dysfunctional Meeting Patterns',
        'Falta de Preparação': 'Lack of Meeting Preparation',
        'Qualidade da Implementação': 'Implementation Quality Issues',
        'Pressão Organizacional': 'Organizational Pressure and Stress',
        'Eficácia das Técnicas': 'Technique Effectiveness and Impact',
        'Limitações do Estudo': 'Study Limitations'
    }
    
    # Create a copy of the dataframe to avoid modifying the original
    df_translated = df.copy()
    
    # Clean data by removing leading/trailing spaces
    if 'categoria_rq1' in df_translated.columns:
        df_translated['categoria_rq1'] = df_translated['categoria_rq1'].str.strip()
    if 'categoria_rq2' in df_translated.columns:
        df_translated['categoria_rq2'] = df_translated['categoria_rq2'].str.strip()
    if 'subcategoria' in df_translated.columns:
        df_translated['subcategoria'] = df_translated['subcategoria'].str.strip()
    
    # Translate RQ1 categories
    if 'categoria_rq1' in df_translated.columns:
        df_translated['categoria_rq1'] = df_translated['categoria_rq1'].map(
            category_translations).fillna(df_translated['categoria_rq1'])
    
    # Translate RQ2 categories
    if 'categoria_rq2' in df_translated.columns:
        df_translated['categoria_rq2'] = df_translated['categoria_rq2'].map(
            category_translations).fillna(df_translated['categoria_rq2'])
    
    # Translate subcategories
    if 'subcategoria' in df_translated.columns:
        df_translated['subcategoria'] = df_translated['subcategoria'].map(
            subcategory_translations).fillna(df_translated['subcategoria'])
    
    return df_translated

def configure_graph_style():
    """Configure the default visual style for all graphs."""
    plt.style.use('seaborn-v0_8-whitegrid')
    sns.set_palette("viridis")
    plt.rcParams.update({
        'figure.figsize': (12, 8),  # Default figure size
        'font.size': 14,            # Increased from 12 to 14
        'axes.titlesize': 18,       # Increased from 16 to 18
        'axes.labelsize': 16,       # Increased from 14 to 16
        'xtick.labelsize': 14,      # Increased from 12 to 14
        'ytick.labelsize': 14,      # Increased from 12 to 14
        'axes.formatter.useoffset': False,
        'axes.formatter.limits': (-3, 3),
        'figure.autolayout': True
    })

def configure_integer_axes(ax, axis='y'):
    """Configure axes to display only integer numbers."""
    if axis in ['x', 'both']:
        ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))
    if axis in ['y', 'both']:
        ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True))

def add_bar_labels(bars, ax, horizontal=False):
    """Add data labels to bars in a graph."""
    for bar in bars:
        if horizontal:
            x_val = bar.get_width()
            y_val = bar.get_y() + bar.get_height() / 2
            ax.text(x_val + 0.1, y_val, f'{int(x_val)}', va='center', ha='left', fontsize=14)
        else:
            x_val = bar.get_x() + bar.get_width() / 2
            y_val = bar.get_height()
            ax.text(x_val, y_val, f'{int(y_val)}', ha='center', va='bottom', fontsize=14, fontweight='bold')

# --- Graph Generation Functions ---

def generate_rq1_category_distribution(df, output_dir):
    """Generate and save the category distribution graph for RQ1."""
    print("Generating graph: Category Distribution for RQ1...")
    rq1_data = df[df['categoria_rq1'].notna() & (df['categoria_rq1'] != '')]
    category_counts = rq1_data['categoria_rq1'].value_counts()
    
    fig, ax = plt.subplots(figsize=(10, 7))
    colors = sns.color_palette("viridis", len(category_counts))
    
    bars = ax.barh(category_counts.index, category_counts.values, color=colors, height=0.6)
    ax.set_title('Distribution of Categories by Codes for RQ1', fontweight='bold')
    ax.set_xlabel('Number of Codes')
    ax.invert_yaxis()  # Most frequent categories at the top
    configure_integer_axes(ax, 'x')
    add_bar_labels(bars, ax, horizontal=True)

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'category_distribution_rq1.png'), dpi=300)
    plt.close(fig)
    print("Graph 'category_distribution_rq1.png' saved.")

def generate_rq2_category_distribution(df, output_dir):
    """Generate and save the category distribution graph for RQ2."""
    print("Generating graph: Category Distribution for RQ2...")
    rq2_data = df[df['categoria_rq2'].notna() & (df['categoria_rq2'] != '')]
    category_counts = rq2_data['categoria_rq2'].value_counts()
    
    fig, ax = plt.subplots(figsize=(10, 7))
    colors = sns.color_palette("viridis_r", len(category_counts))
    
    bars = ax.barh(category_counts.index, category_counts.values, color=colors, height=0.6)
    ax.set_title('Distribution of Categories by Codes for RQ2', fontweight='bold')
    ax.set_xlabel('Number of Codes')
    ax.invert_yaxis()
    configure_integer_axes(ax, 'x')
    add_bar_labels(bars, ax, horizontal=True)

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'category_distribution_rq2.png'), dpi=300)
    plt.close(fig)
    print("Graph 'category_distribution_rq2.png' saved.")

def generate_most_cited_articles(df, output_dir):
    """Generate and save the most cited articles graphs for RQ1 and RQ2 in separate images."""
    print("Generating most cited articles graphs...")
    
    rq1_data = df[df['rqs'].str.contains('1', na=False)]
    rq2_data = df[df['rqs'].str.contains('2', na=False)]

    # Graph for RQ1
    fig1, ax1 = plt.subplots(figsize=(12, 7))
    article_counts_rq1 = rq1_data['artigo'].value_counts().nlargest(8)
    labels_rq1 = [textwrap.fill(label, width=70) for label in article_counts_rq1.index]
    colors_rq1 = sns.color_palette("viridis", len(article_counts_rq1))
    bars1 = ax1.barh(article_counts_rq1.index, article_counts_rq1.values, color=colors_rq1, height=0.6)
    ax1.set_yticklabels(labels_rq1, fontsize=16)
    ax1.set_title('Articles by Number of Codes for RQ1', fontweight='bold')
    ax1.set_xlabel('Number of Codes')
    configure_integer_axes(ax1, 'x')
    add_bar_labels(bars1, ax1, horizontal=True)
    ax1.invert_yaxis()

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'most_cited_articles_rq1.png'), dpi=300)
    plt.close(fig1)
    print("Graph 'most_cited_articles_rq1.png' saved.")

    # Graph for RQ2
    fig2, ax2 = plt.subplots(figsize=(12, 7))
    article_counts_rq2 = rq2_data['artigo'].value_counts().nlargest(8)
    labels_rq2 = [textwrap.fill(label, width=70) for label in article_counts_rq2.index]
    colors_rq2 = sns.color_palette("viridis_r", len(article_counts_rq2))
    bars2 = ax2.barh(article_counts_rq2.index, article_counts_rq2.values, color=colors_rq2, height=0.6)
    ax2.set_yticklabels(labels_rq2, fontsize=16)
    ax2.set_title('Articles by Number of Codes for RQ2', fontweight='bold')
    ax2.set_xlabel('Number of Codes')
    configure_integer_axes(ax2, 'x')
    add_bar_labels(bars2, ax2, horizontal=True)
    ax2.invert_yaxis()

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'most_cited_articles_rq2.png'), dpi=300)
    plt.close(fig2)
    print("Graph 'most_cited_articles_rq2.png' saved.")

# --- Main Function ---

def main():
    """Main function to load data and generate graphs."""
    # Load data
    input_csv = 'scopus_categorias_atualizadas_rq1_final.csv'
    try:
        df = pd.read_csv(input_csv)
        print(f"File '{input_csv}' loaded successfully with {len(df)} rows.")
    except FileNotFoundError:
        print(f"Error: File '{input_csv}' not found.")
        return

    # Translate categories from Portuguese to English
    print("Translating categories from Portuguese to English...")
    df_translated = translate_categories(df)
    print("Translation completed.")

    # Create directory to save graphs
    output_dir = 'Association_for_Computing_Machinery__ACM____SIG_Proceedings_Template'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Directory '{output_dir}' created.")

    # Configure style and generate graphs
    configure_graph_style()
    
    generate_rq1_category_distribution(df_translated, output_dir)
    generate_rq2_category_distribution(df_translated, output_dir)
    generate_most_cited_articles(df_translated, output_dir)

    print("\nAll graphs were generated and saved successfully!")

if __name__ == '__main__':
    main() 