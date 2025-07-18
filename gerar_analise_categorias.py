import pandas as pd

def aggregate_rqs(series):
    """
    Agrega uma série de RQs, tratando valores múltiplos e garantindo saídas únicas e ordenadas.
    Exemplo: uma série contendo ['1', '2', '1, 2'] se tornará '1, 2'.
    """
    all_rqs = set()
    # Itera sobre cada item na série de RQs (ex: '1', '1, 2')
    for item in series.dropna():
        # Divide o item por vírgula para lidar com strings como '1, 2'
        rq_list = str(item).split(',')
        for rq in rq_list:
            # Adiciona o número da RQ ao set, removendo espaços
            all_rqs.add(rq.strip())
    
    # Remove quaisquer valores vazios que possam ter sido adicionados
    all_rqs.discard('')
    
    # Converte para inteiros para ordenação numérica correta e depois de volta para string
    sorted_rqs = sorted([int(r) for r in all_rqs if r.isdigit()])
    return ', '.join(map(str, sorted_rqs))

# Carregar o arquivo CSV
df = pd.read_csv('scopus_categorias_atualizadas_rq1_final.csv')

# Renomear colunas para consistência
df.rename(columns={
    'codigos': 'Codigos',
    'artigo': 'Artigo',
    'rqs': 'RQs',
    'referenciaDentroDoArtigo': 'Citacoes',
    'pagina': 'Pagina',
    'categoria_rq2': 'Categoria_RQ2',
    'subcategoria': 'Subcategoria',
    'categoria_rq1': 'Categoria_RQ1'
}, inplace=True)

# Unificar as colunas de categoria
id_vars = ['Codigos', 'Artigo', 'RQs', 'Citacoes', 'Pagina', 'Subcategoria']
value_vars = ['Categoria_RQ1', 'Categoria_RQ2']
df_melted = df.melt(id_vars=id_vars, value_vars=value_vars, var_name='Fonte_Categoria', value_name='Categoria')

# Limpar categorias vazias ou nulas
df_melted.dropna(subset=['Categoria'], inplace=True)
df_melted = df_melted[df_melted['Categoria'].str.strip() != '']

# Agrupar por 'Categoria' e agregar os dados
df_agg = df_melted.groupby('Categoria').agg(
    Numero_de_Artigos=('Artigo', 'nunique'),
    RQs=('RQs', aggregate_rqs),
    Artigos=('Artigo', lambda x: ', '.join(sorted(x.unique()))),
    Citacoes=('Citacoes', lambda x: ' | '.join(x.unique())),
    Numero_de_Citacoes=('Citacoes', 'count')
).reset_index()

# Renomear as colunas para o formato final
df_agg.rename(columns={
    'Numero_de_Artigos': 'Número de Artigos',
    'Citacoes': 'Citações',
    'Numero_de_Citacoes': 'Número de Citações'
}, inplace=True)

# Reordenar as colunas
df_agg = df_agg[[
    'Categoria',
    'Número de Artigos',
    'RQs',
    'Artigos',
    'Citações',
    'Número de Citações'
]]

# Salvar o resultado
df_agg.to_csv('analise_categorias.csv', index=False)

print("Arquivo 'analise_categorias.csv' gerado com sucesso, com RQs corrigidas e agregadas.") 