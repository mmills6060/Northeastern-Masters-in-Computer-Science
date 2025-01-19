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
    sns.countplot(data=df, x='make')


    # Step 7: Visualize the data
    plt.xlabel('Make')
    plt.ylabel('Count')
    plt.title('Bar Plot of Make')
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
    
    # Create a larger figure for better readability
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

if __name__ == '__main__':
    main()