# Step 1: Importing the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# matplotlib.use('TkAgg')  # Set the backend before importing pyplot

def main():
    # Step 2: Load your data
    df = pd.read_csv("vehicles.csv")

    # Step 3: Examine the Data
    print(df.head())

    
    # Step 4: Summarize the Data
    print(df.describe())

    # Step 5: Handle Missing Values
    print(df.isnull().sum())

    plt.hist(df['barrels08'], bins=20)
    plt.xlabel('Barrels08')
    plt.ylabel('Frequency')
    plt.title('Histogram of Barrels08')
    plt.show()

    # Step 6: Explore Cateegorical Variables
    sns.countplot(data=df, x='drive')


    # Step 7: Visualize the data
    plt.xlabel('Drive')
    plt.ylabel('Count')
    plt.title('Bar Plot of Drive')
    plt.xticks(rotation=45)
    plt.show()


    sns.pairplot(df[['barrels08', 'charge120', 'city08']])
    plt.show()

    # Step 8: Identify Outliers
    plt.boxplot(df['barrels08'])
    plt.xlabel('Barrels08')
    plt.title('Box Plot of Barrels08')
    plt.show()


    # Step 9: Explore Relationships
    # Select only numeric columns for correlation
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    correlation_matrix = df[numeric_columns].corr()
    
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Heatmap (Numeric Variables Only)')
    plt.xticks(rotation=45)
    plt.yticks(rotation=45)
    plt.tight_layout()  # Adjust layout to prevent label cutoff
    plt.show()


    plt.scatter(df['barrels08'], df['displ'])
    plt.xlabel('Barrels08')
    plt.ylabel('Displ')
    plt.title('Scatter Plot of Barrels08 and Displ')
    plt.show()

    # Plots for dependent variable (UCity)
    plt.figure(figsize=(10, 6))
    plt.hist(df['UCity'], bins=30)
    plt.xlabel('Urban MPG (UCity)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Urban Fuel Economy')
    plt.show()

    # Box plot for UCity by vehicle class
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='VClass', y='UCity', data=df)
    plt.xticks(rotation=45)
    plt.xlabel('Vehicle Class')
    plt.ylabel('Urban MPG (UCity)')
    plt.title('Urban Fuel Economy by Vehicle Class')
    plt.tight_layout()
    plt.show()

    # Scatter plot of UCity vs engine displacement
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='displ', y='UCity', hue='fuelType1', data=df)
    plt.xlabel('Engine Displacement')
    plt.ylabel('Urban MPG (UCity)')
    plt.title('Urban Fuel Economy vs Engine Displacement by Fuel Type')
    plt.show()

    # Expanded numeric variables analysis (15 variables)
    numeric_vars = ['displ', 'cylinders', 'barrels08', 'city08', 'highway08', 
                   'comb08', 'charge120', 'charge240', 'co2TailpipeGpm',
                   'fuelCost08', 'ghgScore', 'highway08U', 'hlv', 
                   'hpv', 'lv2']
    
    plt.figure(figsize=(12, 8))
    sns.heatmap(df[numeric_vars[:8]].corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix of Numeric Variables (Part 1)')
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(12, 8))
    sns.heatmap(df[numeric_vars[8:]].corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix of Numeric Variables (Part 2)')
    plt.tight_layout()
    plt.show()

    # Expanded categorical variables analysis (7 variables)
    categorical_vars = ['make', 'model', 'VClass', 'drive', 'fuelType1', 
                       'trans_dscr', 'sCharger']
    
    # Create two rows of subplots for categorical variables
    fig, axes = plt.subplots(4, 2, figsize=(15, 20))
    axes = axes.flatten()
    
    for idx, var in enumerate(categorical_vars):
        if idx < len(axes):
            sns.countplot(data=df, y=var, ax=axes[idx], 
                         order=df[var].value_counts().index[:10])
            axes[idx].set_title(f'Top 10 {var} Categories')
    
    # Remove empty subplot if any
    if len(categorical_vars) < len(axes):
        fig.delaxes(axes[-1])
    
    plt.tight_layout()
    plt.show()

    # Additional interesting aspects
    # 1. Fuel economy trends by manufacturer
    plt.figure(figsize=(15, 8))
    top_makes = df['make'].value_counts().head(10).index
    make_year_avg = df[df['make'].isin(top_makes)].groupby(['year', 'make'])['UCity'].mean().unstack()
    sns.lineplot(data=make_year_avg)
    plt.xlabel('Year')
    plt.ylabel('Average Urban MPG')
    plt.title('Urban Fuel Economy Trends by Top Manufacturers')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

    # 2. Technology adoption over time
    tech_cols = ['sCharger', 'tCharger', 'atvType']
    yearly_tech = df.groupby('year')[tech_cols].sum()
    
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=yearly_tech)
    plt.xlabel('Year')
    plt.ylabel('Count')
    plt.title('Technology Adoption Trends Over Time')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()