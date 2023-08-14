
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import numpy as np

# df_merge = pd.read_csv('Human_del.csv')

# # Define the color map
# color_map = {
#     'BREAKDANCER': 'peru',
#     'clever': 'gold',
#     'grom': 'forestgreen',
#     'DELLY': 'mediumorchid',
#     'gasv': 'firebrick',
#     'tardis': 'lime',
#     'popdel': 'navy',
#     'rdxplorer': 'darkgray',
#     'smoove': 'orangered',
#     'crest': 'red',
#     'GENOMESTRIP': 'pink',
#     'manta': 'aqua',
#     'deepvariant': 'rosybrown',
#     'octopus': 'coral',
#     'svpred': 'black',
#     'surv': 'purple',
#     'jasmine': 'lightblue',
#     'parl': 'magenta'
# }

# caller_order = ['crest','gasv','smoove','GENOMESTRIP','BREAKDANCER','tardis','rdxplorer','popdel','clever',
#        'grom','deepvariant','octopus','DELLY','manta','jasmine','surv','parl','svpred']

# tools = ['crest','gasv','smoove','GENOMESTRIP','BREAKDANCER','tardis','rdxplorer','popdel','clever',
#        'grom','deepvariant','octopus','DELLY','manta','jasmine','surv','parl','svpred']
# labels = ['CREST','GASV','LUMPY','GenomeSTRiP','BreakDancer','Tardis','RDXplorer','PopDel','CLEVER',
#           'GROM','Deepvariant','Octopus','DELLY','Manta','Jasmine*','SURVIVOR*','Parliament2*','VISTA*']

# thresholds = df_merge['threshold'].unique()

# fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# # Calculate the angles for the lines in the circular plot
# angles = np.linspace(0, 2 * np.pi, len(tools), endpoint=False)

# # Create a dictionary to store each caller's precision for each threshold
# caller_precision_dict = {}

# for threshold in thresholds:
#     data = df_merge[df_merge['threshold'] == threshold]
    
#     data = data.sort_values(by='precision')

#     # Store the sorted caller names and precision values
#     sorted_callers = data['tool'].tolist()
#     sorted_precisions = data['precision'].tolist()
    
#     # Draw lines for each threshold
#     ax.plot(angles, data['precision'], marker='o', label=f'Threshold: {threshold} (bp)')
    

# # Set the radial ticks and labels
# ax.set_xticks(angles)
# ax.set_xticklabels(labels, ha='center')  # Using labels instead of tools
# ax.set_rlabel_position(0)  # Move radial labels outside
# ax.set_yticklabels([])  # Hide radial tick labels for better visibility

# # Add legend outside the circular plot
# ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1))

# plt.title('Precision for Deletion')
# plt.tight_layout()
# plt.show()

# plt.savefig("circle_HG_del.png", bbox_inches='tight')
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import numpy as np

# df_merge = pd.read_csv('Human_del.csv')

# # Define the color map
# color_map = {
#     'BREAKDANCER': 'peru',
#     'clever': 'gold',
#     'grom': 'forestgreen',
#     'DELLY': 'mediumorchid',
#     'gasv': 'firebrick',
#     'tardis': 'lime',
#     'popdel': 'navy',
#     'rdxplorer': 'darkgray',
#     'smoove': 'orangered',
#     'crest': 'red',
#     'GENOMESTRIP': 'pink',
#     'manta': 'aqua',
#     'deepvariant': 'rosybrown',
#     'octopus': 'coral',
#     'svpred': 'black',
#     'surv': 'purple',
#     'jasmine': 'lightblue',
#     'parl': 'magenta'
# }

# tools = ['crest','gasv','smoove','GENOMESTRIP','BREAKDANCER','tardis','rdxplorer','popdel','clever',
#        'grom','deepvariant','octopus','DELLY','manta','jasmine','surv','parl','svpred']
# labels = ['CREST','GASV','LUMPY','GenomeSTRiP','BreakDancer','Tardis','RDXplorer','PopDel','CLEVER',
#           'GROM','Deepvariant','Octopus','DELLY','Manta','Jasmine*','SURVIVOR*','Parliament2*','VISTA*']

# thresholds = df_merge['threshold'].unique()

# fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# # Calculate the angles for the lines in the circular plot
# angles = np.linspace(0, 2 * np.pi, len(tools), endpoint=False)

# # Create a dictionary to store each caller's precision for each threshold
# caller_precision_dict = {}

# threshold_colors = plt.cm.copper(np.linspace(0, 1, len(thresholds)))

# for i, threshold in enumerate(thresholds):
#     data = df_merge[df_merge['threshold'] == threshold]
    
#     # Sort the data based on precision in ascending order
#     data = data.sort_values(by='precision')
    
#     # Update the labels to match the sorted order
#     labels_sorted = [labels[tools.index(tool)] for tool in data['tool']]
    
#     # Store the caller precision values in the dictionary
#     caller_precision_dict[threshold] = {caller: precision for caller, precision in zip(labels_sorted, data['precision'])}
#     color = threshold_colors[i]
#     # Draw lines for each threshold
#     ax.plot(angles, data['precision'], marker='o', label=f'Threshold: {threshold} (bp)', color=color, linewidth=0.7, markersize=5)

# # Set the radial ticks and labels
# ax.set_xticks(angles)
# ax.set_xticklabels(labels_sorted, ha='center')  # Using updated labels
# ax.set_rlabel_position(0)  # Move radial labels outside
# ax.set_yticklabels([])  # Hide radial tick labels for better visibility

# # Add legend outside the circular plot
# ax.legend(loc='upper right', bbox_to_anchor=(1.5, 1))

# plt.title('Precision for Deletion', y= 1.1)
# plt.tight_layout()
# plt.show()

# plt.savefig("circle_HG_del.png", bbox_inches='tight')

# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import numpy as np

# df_merge = pd.read_csv('Human_del.csv')

# # Define the color map
# color_map = {
#     'BREAKDANCER': 'peru',
#     'clever': 'gold',
#     'grom': 'forestgreen',
#     'DELLY': 'mediumorchid',
#     'gasv': 'firebrick',
#     'tardis': 'lime',
#     'popdel': 'navy',
#     'rdxplorer': 'darkgray',
#     'smoove': 'orangered',
#     'crest': 'red',
#     'GENOMESTRIP': 'pink',
#     'manta': 'aqua',
#     'deepvariant': 'rosybrown',
#     'octopus': 'coral',
#     'svpred': 'black',
#     'surv': 'purple',
#     'jasmine': 'lightblue',
#     'parl': 'magenta'
# }

# tools = ['crest','gasv','smoove','GENOMESTRIP','BREAKDANCER','tardis','rdxplorer','popdel','clever',
#        'grom','deepvariant','octopus','DELLY','manta','jasmine','surv','parl','svpred']
# labels = ['CREST','GASV','LUMPY','GenomeSTRiP','BreakDancer','Tardis','RDXplorer','PopDel','CLEVER',
#           'GROM','Deepvariant','Octopus','DELLY','Manta','Jasmine*','SURVIVOR*','Parliament2*','VISTA*']

# thresholds = df_merge['threshold'].unique()

# fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# # Calculate the angles for the lines in the circular plot
# angles = np.linspace(0, 2 * np.pi, len(tools), endpoint=False)

# # Create a dictionary to store each caller's precision for each threshold
# caller_precision_dict = {}

# threshold_colors = plt.cm.copper(np.linspace(0, 1, len(thresholds)))

# for i, threshold in enumerate(thresholds):
#     data = df_merge[df_merge['threshold'] == threshold]
    
#     # Sort the data based on precision in ascending order
#     data = data.sort_values(by='sensitivity')
    
#     # Update the labels to match the sorted order
#     labels_sorted = [labels[tools.index(tool)] for tool in data['tool']]
    
#     # Store the caller precision values in the dictionary
#     caller_precision_dict[threshold] = {caller: precision for caller, precision in zip(labels_sorted, data['sensitivity'])}
#     color = threshold_colors[i]
#     # Draw lines for each threshold
#     ax.plot(angles, data['sensitivity'], marker='o', label=f'Threshold: {threshold} (bp)', color=color, linewidth=0.7, markersize=5)

# # Set the radial ticks and labels
# ax.set_xticks(angles)
# ax.set_xticklabels([])  # Hide original radial tick labels
# ax.set_yticklabels([0.2, 0.4, 0.6, 0.8, 1])


# # Place the tool labels outside the circle
# for angle, label in zip(angles, labels_sorted):
#     ax.text(angle, ax.get_ylim()[1] + 0.18, label, ha='center', va='center')

# # Add legend outside the circular plot
# ax.legend(loc='upper right', bbox_to_anchor=(1.55, 1))

# plt.title('Sensitivity for Deletion', y= 1.18)
# plt.tight_layout()
# plt.subplots_adjust(right=0.9)
# plt.show()

# plt.savefig("circle_HG_del.png", bbox_inches='tight')
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df_merge = pd.read_csv('Human_del.csv')

# Define the color map
color_map = {
    'BREAKDANCER': 'peru',
    'clever': 'gold',
    'grom': 'forestgreen',
    'DELLY': 'mediumorchid',
    'gasv': 'firebrick',
    'tardis': 'lime',
    'popdel': 'navy',
    'rdxplorer': 'darkgray',
    'smoove': 'orangered',
    'crest': 'red',
    'GENOMESTRIP': 'pink',
    'manta': 'aqua',
    'deepvariant': 'rosybrown',
    'octopus': 'coral',
    'svpred': 'black',
    'surv': 'purple',
    'jasmine': 'lightblue',
    'parl': 'magenta'
}

tools = ['crest','gasv','smoove','GENOMESTRIP','BREAKDANCER','tardis','rdxplorer','popdel','clever',
       'grom','deepvariant','octopus','DELLY','manta','jasmine','surv','parl','svpred']
labels = ['CREST','GASV','LUMPY','GenomeSTRiP','BreakDancer','Tardis','RDXplorer','PopDel','CLEVER',
          'GROM','Deepvariant','Octopus','DELLY','Manta','Jasmine*','SURVIVOR*','Parliament2*','VISTA*']

thresholds = df_merge['threshold'].unique()

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

angles = np.linspace(0, 2 * np.pi, len(tools), endpoint=False)

caller_precision_dict = {}

threshold_colors = plt.cm.RdBu(np.linspace(0, 1, len(thresholds)))

data_10000 = df_merge[df_merge['threshold'] == 10000]
data_10000 = data_10000.sort_values(by='sensitivity')

labels_sorted = [labels[tools.index(tool)] for tool in data_10000['tool']]

for i, threshold in enumerate(thresholds):
    data = df_merge[df_merge['threshold'] == threshold]
    
    data = data.set_index('tool').loc[data_10000['tool']].reset_index()
    
    caller_precision_dict[threshold] = {caller: precision for caller, precision in zip(labels_sorted, data['precision'])}
    
    color = threshold_colors[i]
    
    ax.plot(angles, data['sensitivity'], marker='o', label=f'Threshold: {threshold} (bp)', color=color, linewidth=0.7, markersize=5)

ax.set_xticks(angles)
ax.set_xticklabels([])  # Hide original radial tick labels
# ax.set_yticklabels([0.2, 0.4, 0.6, 0.8, 1])

for angle, label in zip(angles, labels_sorted):
    ax.text(angle, ax.get_ylim()[1] + 0.18, label, ha='center', va='center')

# ax.legend(loc='upper right', bbox_to_anchor=(1.55, 1))

plt.title('Sensitivity', y= 1.18)
plt.tight_layout()
plt.subplots_adjust(right=0.9)
plt.show()

plt.savefig("circle_HG_del.png", bbox_inches='tight',dpi=500)
