import pandas as pd
import os
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV files
persona_table = pd.read_csv('persona_table.csv', delimiter='|')
rasci_table = pd.read_csv('rasci_table.csv', delimiter='|')
interaction_details_df = pd.read_csv('interaction_details.csv', delimiter='|')
# Load optional persona knowledge if available
if os.path.exists('persona_knowledge.csv'):
    persona_knowledge = pd.read_csv('persona_knowledge.csv', delimiter='|')
    persona_knowledge_dict = persona_knowledge.set_index('persona').T.to_dict()
else:
    persona_knowledge_dict = {}

# Debugging: Print the column names to ensure they match
print("Interaction Details Columns: ", interaction_details_df.columns)

# Ensure the column names are lowercase and without leading/trailing spaces
interaction_details_df.columns = interaction_details_df.columns.str.strip().str.lower()

# Convert interaction details DataFrame to a dictionary
interaction_details = interaction_details_df.set_index('persona').T.to_dict()

# Fill NaN values in the 'values' column with an empty string
persona_table['values'] = persona_table['values'].fillna('')

# Normalize the 'values' column to ensure all rows have the same number of values
max_values_length = persona_table['values'].str.split(', ').apply(len).max()
persona_table['values'] = persona_table['values'].apply(lambda x: ', '.join(x.split(', ') + [''] * (max_values_length - len(x.split(', ')))))

# persona_knowledge_dict is populated above if the optional file exists

# Print the columns and the first few rows of the DataFrame for debugging
print("Persona Table Columns: ", persona_table.columns)
print("First few rows of the Persona Table:")
print(persona_table.head())

# Define the template for the prompts
template = """As a {persona}, you operate within the Tetrix Prism model where Strategy, Culture, and Execution form a balanced triad. You are responsible for {resourcing} and ensuring {key_metrics}. Your capacity is {capacity}. Company goals: {company_goals}. Core values: {values}. Key tools: {tools}.

When interacting with {relevant_roles}, highlight {key_points_of_interaction_and_collaboration}. Ensure that {specific_actions_or_behaviors}. This framework mirrors a fractal pyramid so changes at the strategic level cascade cleanly through execution."""

# Generate prompts based on the template and interaction details
def generate_prompt(row):
    persona = row.persona
    details = interaction_details.get(persona, {})
    knowledge = persona_knowledge_dict.get(persona, {})
    tools = knowledge.get('tools', 'N/A')
    return template.format(
        persona=row.persona,
        resourcing=row.resourcing,
        capacity=row.capacity,
        key_metrics=row.key_metrics,
        company_goals=row.company_goals,
        values=row.values,
        tools=tools,
        relevant_roles=details.get('relevant_roles', 'N/A'),
        key_points_of_interaction_and_collaboration=details.get('key_points_of_interaction_and_collaboration', 'N/A'),
        specific_actions_or_behaviors=details.get('specific_actions_or_behaviors', 'N/A')
    )

# Create directory structure and files for each persona
def create_persona_directory(persona, prompt, rasci_table, output_dir='persona_prompts'):
    persona_dir = os.path.join(output_dir, persona.replace(' ', '_'))
    print(f"Creating directory for persona: {persona}")  # Debugging statement
    os.makedirs(persona_dir, exist_ok=True)
    
    # Save the prompt to a file
    with open(os.path.join(persona_dir, 'prompt.txt'), 'w') as f:
        f.write(prompt)
    
    # Save the RASCI table to a CSV file
    rasci_table.to_csv(os.path.join(persona_dir, 'rasci_table.csv'), index=False)
    
    # Save the persona details to a file
    with open(os.path.join(persona_dir, 'persona.txt'), 'w') as f:
        f.write(f"Persona: {persona}\n\nPrompt:\n{prompt}\n")

# Iterate over the DataFrame rows as namedtuples
output_dir = 'persona_prompts'
for row in persona_table.itertuples(index=False, name='Persona'):
    persona = row.persona
    prompt = generate_prompt(row)
    print(f"Processing persona: {persona}")  # Debugging statement
    create_persona_directory(persona, prompt, rasci_table, output_dir)

print(f"Directories and files have been created in the '{output_dir}' directory.")

# Display the persona_table dataframe
print(persona_table)
