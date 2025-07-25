# Practices and Challenges of Retrospective Meetings in Agile Teams: Insights from a Rapid Review

This project contains the scripts and data used in the analysis for the research paper on retrospective meetings in remote agile software development teams.

## Summary

This study conducted a rapid review to investigate challenges and practices related to retrospective meetings in remote agile software development teams. Through the analysis of selected articles, categories such as "Retrospective Format", "Action Plan Generation", "Communication Difficulties", and "Retrospective as Continuous Improvement" were identified. The results highlight the importance of structuring retrospectives to produce tangible actions, diversifying formats to increase engagement in remote environments, and promoting an inclusive environment that facilitates communication. The analysis resulted in a set of best practices organized into categories such as methodological conduction, participant engagement, action follow-up, and inclusion of underrepresented voices. These practices offer directly applicable recommendations for agile teams and facilitators working in remote contexts.

## How to Use

### Prerequisites

- Python 3.x
- Libraries listed in the `requirements.txt` file

### Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <directory-name>
   ```

2. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Scripts

1.  **Generate Category Analysis**:
    This script processes the input data file and generates the analysis output file, which aggregates and consolidates the data.

    ```bash
    python gerar_analise_categorias.py
    ```

2.  **Generate Charts**:
    This script uses the input data file to generate analysis charts, saving them in the `graficos_gerados/` directory.

    ```bash
    python gerador_graficos.py
    ```

## Project Structure

- `analise_categorias.csv`: Output from the analysis script.
- `gerador_graficos.py`: Script to generate charts.
- `gerar_analise_categorias.py`: Script to process and analyze data.
- `graficos_gerados/`: Directory where generated charts are saved.
- `input_data.csv`: Raw data used as input.
- `README.md`: This file.
- `requirements.txt`: Python dependencies list.
