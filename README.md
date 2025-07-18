# Resultados Iniciais de uma Rapid Review sobre Reuniões de Retrospectiva em Times Ágeis Remotos

Este projeto contém os scripts e dados utilizados na análise para o artigo "Resultados Iniciais de uma Rapid Review sobre Reuniões de Retrospectiva em Times Ágeis Remotos".

## Autores

- Wesley M. de O. Gomes
- Rafael de Mello
- Juliana S. F. França

## Resumo

Este estudo realizou uma rapid review para investigar os desafios e práticas relacionados às reuniões de retrospectiva em times ágeis remotos de desenvolvimento de software. A partir da análise de oito artigos selecionados, foram identificadas categorias como "Formato das Retrospectivas", "Gerar planos de ação", "Dificuldade de se expressar" e "Retrospectiva como melhoria contínua". Os resultados destacam a importância de estruturar as retrospectivas para produzir ações tangíveis, diversificar os formatos para aumentar o engajamento em ambientes remotos e promover um ambiente inclusivo que facilite a comunicação. A análise resultou em um conjunto de boas práticas organizadas em categorias como condução metodológica, engajamento de participantes, acompanhamento de ações e inclusão de vozes sub-representadas. Essas práticas oferecem recomendações diretamente aplicáveis para equipes ágeis e facilitadores que atuam em contextos remotos.

## Como usar

### Pré-requisitos

- Python 3.x
- Bibliotecas listadas no arquivo `requirements.txt`

### Instalação

1. Clone o repositório:

   ```bash
   git clone <url-do-repositorio>
   cd <nome-do-diretorio>
   ```

2. Crie e ative um ambiente virtual (recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

### Executando os Scripts

1.  **Gerar Análise de Categorias**:
    Este script processa o arquivo `scopus_categorias_atualizadas_rq1_final.csv` e gera o arquivo `analise_categorias.csv`, que agrega e consolida os dados.

    ```bash
    python gerar_analise_categorias.py
    ```

2.  **Gerar Gráficos**:
    Este script utiliza o arquivo `scopus_categorias_atualizadas_rq1_final.csv` para gerar os gráficos da análise, salvando-os no diretório `graficos_gerados/`.

    ```bash
    python gerador_graficos.py
    ```

## Estrutura do Projeto

- `analise_categorias.csv`: Saída do script de análise.
- `gerador_graficos.py`: Script para gerar os gráficos.
- `gerar_analise_categorias.py`: Script para processar e analisar os dados.
- `graficos_gerados/`: Diretório onde os gráficos gerados são salvos.
- `scopus_categorias_atualizadas_rq1_final.csv`: Dados brutos utilizados como entrada.
- `README.md`: Este arquivo.
- `requirements.txt`: Lista de dependências Python.
