# Dependencies and Setup
%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats, integrate
# Hide warning messages in notebook
import warnings
warnings.filterwarnings('ignore')

# File to Load (Remember to Change These)
mouse_csv = "data/mouse_drug_data.csv"
clinical_csv = "data/clinicaltrial_data.csv"

# Read the Mouse and Drug Data and the Clinical Trial Data
mouse_data = pd.read_csv(mouse_csv)
clinical_data = pd.read_csv(clinical_csv)
mouse_data.head()


# Combine the data into a single dataset
data_merge = pd.merge(mouse_data, clinical_data, how="inner", on="Mouse ID")

# Display the data table for preview
data_merge.head()



# Store the Mean Tumor Volume Data Grouped by Drug and Timepoint 
drug_sort = data_merge.groupby(['Drug'])['Drug'].unique()
data_merge_by_drug = data_merge.groupby(['Drug','Timepoint']).mean()

#Store data into a pivot table 
drug_pivot = pd.pivot_table(data_merge, values=['Tumor Volume (mm3)'], index=['Timepoint'], columns=['Drug'], aggfunc=np.mean)

# Preview DataFrame
drug_pivot.(head)



# Create Tumor response scatter plot.

y_axis = list(drug_pivot['Tumor Volume (mm3)']['Capomulin'].values)
x_axis = list(drug_pivot['Tumor Volume (mm3)']['Capomulin'].index)
Capomulin = plt.errorbar(x_axis,  y_axis, marker="^", color='red', alpha=1.0)


y_axis = list(drug_pivot['Tumor Volume (mm3)']['Infubinol'].values)
x_axis = list(drug_pivot['Tumor Volume (mm3)']['Infubinol'].index)
Infubinol = plt.errorbar(x_axis,  y_axis, marker="d",  color='blue', alpha=1.0)


y_axis = list(drug_pivot['Tumor Volume (mm3)']['Ketapril'].values)
x_axis = list(drug_pivot['Tumor Volume (mm3)']['Ketapril'].index)
Ketapril = plt.errorbar(x_axis,  y_axis, marker="o",  color='green', alpha=1.0)


y_axis = list(drug_pivot['Tumor Volume (mm3)']['Placebo'].values)
x_axis = list(drug_pivot['Tumor Volume (mm3)']['Placebo'].index)
Placebo = plt.errorbar(x_axis,  y_axis, marker="x",  color='black', alpha=1.0)


plt.legend(('Capomulin', 'Infubinol', 'Ketapril', 'Placebo'),
           scatterpoints=1,
           loc='upper left',
           ncol=2,
           fontsize=10)



plt.xlabel("Time (Days)", fontsize=10, color='black')
plt.ylabel("Tumor Volume (mm3)", fontsize=10, color='black')
plt.title("Tumor Response to Treatment", fontsize=14, color='black')
plt.grid()

      
plt.ylim(30, 75.0)
plt.xlim(0, 50.0)
plt.show()

# Metastatic Response to Treatment

# Create metastatic pivot table.
metastatic_pivot = pd.pivot_table(data_merge, values=['Metastatic Sites'], index=['Timepoint'], columns=['Drug'], aggfunc=np.mean)
metastatic_pivot

#Preview the pivot table
metastatic_pivot.head()

# Create Metastatic Response to treatment plot

y_axis = list(metastatic_pivot['Metastatic Sites']['Capomulin'].values)
x_axis = list(metastatic_pivot['Metastatic Sites']['Capomulin'].index)
Capomulin = plt.errorbar(x_axis,  y_axis, marker="^", color='red', alpha=1.0)


y_axis = list(metastatic_pivot['Metastatic Sites']['Infubinol'].values)
x_axis = list(metastatic_pivot['Metastatic Sites']['Infubinol'].index)
Infubinol = plt.errorbar(x_axis,  y_axis, marker="d",  color='blue', alpha=1.0)


y_axis = list(metastatic_pivot['Metastatic Sites']['Ketapril'].values)
x_axis = list(metastatic_pivot['Metastatic Sites']['Ketapril'].index)
Ketapril = plt.errorbar(x_axis,  y_axis, marker="o",  color='green', alpha=1.0)


y_axis = list(metastatic_pivot['Metastatic Sites']['Placebo'].values)
x_axis = list(metastatic_pivot['Metastatic Sites']['Placebo'].index)
Placebo = plt.errorbar(x_axis,  y_axis, marker="x",  color='black', alpha=1.0)


# Set our legend to where the chart thinks is best
#plt.legend(handles=[Capomulin, Infubinol], loc="best")

plt.legend(('Capomulin', 'Infubinol', 'Ketapril', 'Placebo'),
           scatterpoints=1,
           loc='upper left',
           ncol=2,
           fontsize=10)



plt.xlabel("Time (Days)", fontsize=10, color='black')
plt.ylabel("Tumor Volume (mm3)", fontsize=10, color='black')
plt.title("Metastatic Response to Treatment", fontsize=14, color='black')
plt.grid()

      
plt.ylim(0, 5.0)
plt.xlim(0, 50.0)
plt.show()


# Survival Rates

# Store the Count of Mice Grouped by Drug and Timepoint.
data_merge_by_drug['Mouse Count'] = data_merge.groupby(['Drug', 'Timepoint'])['Mouse ID'].count()
data_merge_by_drug.head()

# Covert into a pivot table
mouse_pivot = pd.pivot_table(data_merge_by_drug, values=['Mouse Count'], index=['Timepoint'], columns=['Drug'])

# Preview the data
mouse_pivot

# Create mouse survival rate plot
y_axis = list(mouse_pivot['Mouse Count']['Capomulin'].values)
x_axis = list(mouse_pivot['Mouse Count']['Capomulin'].index)
Capomulin = plt.errorbar(x_axis,  y_axis, marker="o", color='red', alpha=1.0)


y_axis = list(mouse_pivot['Mouse Count']['Infubinol'].values)
x_axis = list(mouse_pivot['Mouse Count']['Infubinol'].index)
Infubinol = plt.errorbar(x_axis,  y_axis, marker="o",  color='blue', alpha=1.0)


y_axis = list(mouse_pivot['Mouse Count']['Ketapril'].values)
x_axis = list(mouse_pivot['Mouse Count']['Ketapril'].index)
Ketapril = plt.errorbar(x_axis,  y_axis, marker="o",  color='green', alpha=1.0)


y_axis = list(mouse_pivot['Mouse Count']['Placebo'].values)
x_axis = list(mouse_pivot['Mouse Count']['Placebo'].index)
Placebo = plt.errorbar(x_axis,  y_axis, marker="o",  color='black', alpha=1.0)



plt.legend(('Capomulin', 'Infubinol', 'Ketapril', 'Placebo'),
           scatterpoints=1,
           loc='lower left',
           ncol=2,
           fontsize=10)



plt.xlabel("Time (Days)", fontsize=10, color='black')
plt.ylabel("Number of Mice Alive", fontsize=10, color='black')
plt.title("Mouse Survival Rate over Drug Treatment", fontsize=14, color='black')
plt.grid()

      
plt.ylim(0, 30)
plt.xlim(0, 50.0)
plt.show()


# Summary Bar Graph

# Calculate the percent changes for each drug
y_axis = []
y_axis.append(100*(drug_pivot['Tumor Volume (mm3)']['Capomulin'].iloc[-1] - drug_pivot['Tumor Volume (mm3)']['Capomulin'].iloc[0])/drug_pivot['Tumor Volume (mm3)']['Capomulin'].iloc[0])
y_axis.append(100*(drug_pivot['Tumor Volume (mm3)']['Infubinol'].iloc[-1] - drug_pivot['Tumor Volume (mm3)']['Infubinol'].iloc[0])/drug_pivot['Tumor Volume (mm3)']['Capomulin'].iloc[0])
y_axis.append(100*(drug_pivot['Tumor Volume (mm3)']['Ketapril'].iloc[-1] - drug_pivot['Tumor Volume (mm3)']['Ketapril'].iloc[0])/drug_pivot['Tumor Volume (mm3)']['Capomulin'].iloc[0])
y_axis.append(100*(drug_pivot['Tumor Volume (mm3)']['Placebo'].iloc[-1] - drug_pivot['Tumor Volume (mm3)']['Placebo'].iloc[0])/drug_pivot['Tumor Volume (mm3)']['Capomulin'].iloc[0])

x_axis = [0,1,2,3]
x=0
print(y_axis)

# Plot Bar chart

plt.bar(0, y_axis[0], facecolor='green', alpha=1.0, align="center",width=1.0)
plt.bar(1, y_axis[1], facecolor='red', alpha=1.0, align="center",width=1.0)
plt.bar(2, y_axis[2], facecolor='red', alpha=1.0, align="center",width=1.0)
plt.bar(3, y_axis[3], facecolor='red', alpha=1.0, align="center",width=1.0)
tick_locations = [value+0.1 for value in x_axis]
plt.xticks(tick_locations, ["Capomulin", "Infubinol", "Ketapril", "Placebo"], fontsize=10, color='blue')


plt.xlim(0, 3.5)
plt.ylim(min(y_axis)-10, max(y_axis)+10)

plt.title("Tumor Percentage Change Over Treatment", fontsize=14, color='black')
plt.xlabel("Drug SChedule", fontsize=10, color='black')
plt.ylabel("% Tumor Volume Change", fontsize=10, color='black')
plt.tight_layout(pad=0.4, w_pad=0.01, h_pad=1.0)
plt.grid()
plt.hline(0,0,3),alpha=0.6)
plt.show()

