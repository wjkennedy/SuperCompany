# Persona-Driven GPT Generation

Welcome to the Persona-Driven GPT Generation project! This repository is designed to help you generate detailed personas and their respective areas of responsibility within a corporate structure. These personas are tailored for use with GPTs (Generative Pre-trained Transformers), equipped with custom knowledge files and actions that suit their areas of expertise.

## Project Overview

This project leverages the power of GPT-4 to automate the creation and organization of corporate personas, providing them with detailed knowledge files and specific actions to enhance their effectiveness. Each persona is aligned with corporate goals, ensuring a cohesive and strategic approach to business development and operational efficiency.

## Tetrix Prism (ELICEO)

The generation process is guided by the **Tetrix Prism** framework—a fractal model where **Strategy**, **Culture**, and **Execution** form a balanced triad. This approach, sometimes referred to as **ELICEO**, emphasizes how small strategic shifts cascade cleanly through the organization while preserving autonomy at every layer. Viewing the company through this prism simplifies communication and highlights how customer-facing work connects back to internal teams.

### Key Features

- **Automated Persona Generation**: Generate detailed personas with specific responsibilities and knowledge areas.
- **Custom Knowledge Files**: Equip each persona with tailored knowledge files to enhance their GPT capabilities.
- **Organizational Alignment**: Align personas with corporate goals and principles, ensuring strategic consistency.
- **Continuous Improvement Focus**: Incorporate Six Sigma DMAIC principles to emphasize continuous improvement and operational excellence.
- **Visual Representations**: Create detailed Directed Acyclic Graphs (DAGs) to visualize persona interactions and strategic planning phases.

## Project Structure

The repository is organized as follows:

- **CSV Files**: Contains data files (`persona_table.csv`, `interaction_details.csv`, `persona_knowledge.csv`) used for persona generation.
- **Python Scripts**: Scripts to read data, generate personas, create directories, and populate them with detailed prompts and knowledge files.
- **Visualization**: Scripts to create and display DAGs for various planning and review phases, highlighting continuous improvement and Six Sigma principles.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- Pandas
- NetworkX
- Matplotlib
- NumPy

Install the required packages using pip:

```bash
pip install pandas networkx matplotlib numpy
```

### Running the Scripts

1. **Prepare Your Data**: Ensure your CSV files (`persona_table.csv`, `interaction_details.csv`, `persona_knowledge.csv`) are correctly formatted and located in the same directory as your scripts.

2. **Generate Personas**: Run the main script to generate detailed personas and populate the directories:

   ```bash
   python promptbuilder.py
   ```

3. **Visualize Planning Phases**: Run the visualization script to create and display the DAGs for strategic planning and review phases:

   ```bash
   python visualize_dag.py
   ```

## Project Files

### `persona_table.csv`

Defines the basic details of each persona, including their roles, responsibilities, and core values.

### `interaction_details.csv`

Details the interactions between personas, highlighting key points of collaboration and specific actions.

### `persona_knowledge.csv`

Provides detailed knowledge areas, skills, tools, and responsibilities for each persona, enhancing their GPT capabilities.

### `promptbuilder.py`

The main script to generate personas, create directories, and populate them with detailed prompts and knowledge files.

### `visualize_dag.py`

Script to create and display DAGs for various strategic planning and review phases, emphasizing continuous improvement and Six Sigma principles.

## About

This project was generated with the assistance of GPT-4 by William Kennedy/A9 Consulting Group, an Atlassian Silver Partner. The goal is to streamline corporate persona creation and enhance their effectiveness using GPT capabilities.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- GPT-4 by OpenAI for assisting in the project generation.
- Pandas, NetworkX, Matplotlib, and NumPy for their powerful data processing and visualization capabilities.
- Atlassian for their comprehensive Partner program and tools that inspired this project.

---

**William Kennedy**  
*A9 Consulting Group*  
*Atlassian Silver Partner*

For more information, visit [A9 Consulting Group](https://www.a9consultinggroup.com).

---

Happy coding!

