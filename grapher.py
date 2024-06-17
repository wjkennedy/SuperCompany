import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV files
persona_table = pd.read_csv('persona_table.csv', delimiter='|')
rasci_table = pd.read_csv('rasci_table.csv', delimiter='|')
interaction_details_df = pd.read_csv('interaction_details.csv', delimiter='|')

# Convert interaction details DataFrame to a dictionary
interaction_details = interaction_details_df.set_index('Persona').T.to_dict()

# Fill NaN values in the 'Values' column with an empty string
persona_table['Values'] = persona_table['Values'].fillna('')

# Normalize the 'Values' column to ensure all rows have the same number of values
max_values_length = persona_table['Values'].str.split(', ').apply(len).max()
persona_table['Values'] = persona_table['Values'].apply(lambda x: ', '.join(x.split(', ') + [''] * (max_values_length - len(x.split(', ')))))

# Define DMAIC phases
dmaic_phases = ["Define", "Measure", "Analyze", "Improve", "Control"]

# Define personas involved in each DMAIC phase
dmaic_personas = {
    "Define": ["CEO", "COO", "Product Manager", "Marketing Manager"],
    "Measure": ["CTO", "CFO", "QA Engineer", "HR Manager"],
    "Analyze": ["CTO", "Engineering Manager", "QA Engineer", "Data Analyst"],
    "Improve": ["Product Manager", "Engineering Manager", "Software Engineer", "QA Engineer"],
    "Control": ["COO", "QA Engineer", "IT Support", "HR Manager"]
}

# Create a directed graph
G = nx.DiGraph()

# Add nodes for DMAIC phases
for phase in dmaic_phases:
    G.add_node(phase, type="phase")

# Add transitions between DMAIC phases to form a cycle
for i in range(len(dmaic_phases)):
    G.add_edge(dmaic_phases[i], dmaic_phases[(i + 1) % len(dmaic_phases)])

# Add nodes and edges for personas involved in each DMAIC phase
for phase, personas in dmaic_personas.items():
    for persona in personas:
        G.add_node(persona, type="persona")
        G.add_edge(persona, phase)

# Define positions for nodes
pos = {}
for i, phase in enumerate(dmaic_phases):
    angle = 2 * 3.14159 * i / len(dmaic_phases)
    pos[phase] = (3 * np.cos(angle), 3 * np.sin(angle))

for persona in G.nodes:
    if G.nodes[persona]['type'] == "persona":
        phase = next(iter(G[persona]))
        angle = np.arctan2(pos[phase][1], pos[phase][0])
        radius = np.sqrt(pos[phase][0]**2 + pos[phase][1]**2) + 1
        pos[persona] = (radius * np.cos(angle), radius * np.sin(angle))

# Draw the graph
plt.figure(figsize=(14, 10))

# Draw phases
phase_nodes = [node for node, data in G.nodes(data=True) if data['type'] == 'phase']
nx.draw_networkx_nodes(G, pos, nodelist=phase_nodes, node_size=3000, node_color='lightblue', node_shape='s', label="Phases")

# Draw personas
persona_nodes = [node for node, data in G.nodes(data=True) if data['type'] == 'persona']
nx.draw_networkx_nodes(G, pos, nodelist=persona_nodes, node_size=2000, node_color='lightgreen', node_shape='o', label="Personas")

# Draw edges
edges = G.edges()
nx.draw_networkx_edges(G, pos, edgelist=edges, arrowstyle='->', arrowsize=15, edge_color='gray')

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

# Add legend
plt.legend(scatterpoints=1, loc='upper left', fontsize=12)

plt.title("Cyclical DMAIC Process Emphasizing Continuous Improvement")
plt.show()