import matplotlib.pyplot as plt

# Data organized by category
ants_data = {
    10: [26104.4, 26218.4],
    50: [26133.75, 26146.5],
    100: [26128.466666666667, 26161.0]
}

# Extracting ACO and Elitist data
ants_labels = ['ACO = 10', 'Elitist = 10', 'ACO = 50', 'Elitist = 50', 'ACO = 100', 'Elitist = 100']
aco_values = [value[0] for value in ants_data.values()]
elitist_values = [value[1] for value in ants_data.values()]

# Plotting
fig, axes = plt.subplots(3, 1, figsize=(10, 15))

# Plot for number of ants
for i, (key, value) in enumerate(ants_data.items()):
    axes[0].plot([key] * len(value), value, 'o', label=ants_labels[i % len(ants_labels)])
axes[0].set_title('Average Best Total Cost - Number of Ants')
axes[0].set_xlabel('Number of Ants')
axes[0].set_ylabel('Average Best Total Cost')
axes[0].legend()

# Data organized by category
rho_data = {
    0.1: [26138.975, 26170.075],
    0.2: [26138.2, 26189.04],
    0.3: [26140.766666666666, 26192.366666666665],
    0.4: [26142.614285714284, 26190.371428571427],
    0.5: [26133.7125, 26190.125],
    0.6: [26142.4, 26188.17777777778],
    0.7: [26142.8, 26180.35],
    0.8: [26145.645454545454, 26173.454545454544],
    0.9: [26142.733333333334, 26166.325],
    1.0: [24181.984615384616, 24213.115384615383]
}

# Plot for Rho
rho_labels = [
'0.1', 
'0.2', 
'0.3', 
'0.4', 
'0.5', 
'0.6', 
'0.7', 
'0.8', 
'0.9', 
'1', 
]

for i, (key, value) in enumerate(rho_data.items()):
    axes[1].plot([key] * len(value), value, 'o', label=rho_labels[i % len(rho_labels)])
axes[1].set_title('Average Best Total Cost - Rho')
axes[1].set_xlabel('Rho')
axes[1].set_ylabel('Average Best Total Cost')
axes[1].legend()

# Data organized by category
q_data = {
    0.5: [24323.72857142857, 24349.014285714286],
    1.0: [24446.31333333333, 24465.593333333334],
    2.0: [24552.7375, 24574.09375],
    5.0: [24648.74705882353, 24669.717647058824],
    10.0: [24730.994444444445]
}

# Plot for Q
q_labels = ['ACO', 'Elitist']
for i, (key, value) in enumerate(q_data.items()):
    axes[2].plot([key] * len(value), value, 'o', label=q_labels[i % len(q_labels)])
axes[2].set_title('Average Best Total Cost - Q')
axes[2].set_xlabel('Q')
axes[2].set_ylabel('Average Best Total Cost')
axes[2].legend()

plt.tight_layout()
plt.show()

