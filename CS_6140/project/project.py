import os
import pandas as pd
import matplotlib.pyplot as plt
from zipfile import ZipFile
import glob


def load_dataset():
    """
    Load the Ookla Internet Speed dataset from a local file
    """
    # Use a relative path starting from the current directory
    file_path = "dataset/2019-q1/2019-01-01_performance_fixed_tiles.parquet"

    # Handle absolute path as well (in case the relative path doesn't work)
    if not os.path.exists(file_path):
        # Try searching in a few different places
        possible_paths = [
            file_path,
            os.path.join(os.getcwd(), file_path),
            os.path.join(os.getcwd(), "CS_6140", "project", file_path),
            os.path.join(os.getcwd(), "CS_6140", file_path),
        ]

        # Find the first path that exists
        for path in possible_paths:
            if os.path.exists(path):
                file_path = path
                break

    print(f"Attempting to load dataset from: {file_path}")

    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            print(f"Error: File not found at {file_path}")
            print(
                "Please ensure the Ookla dataset is downloaded and provide the correct path.")
            print(
                "The expected structure is: archive/2019-q1/2019-01-01_performance_fixed_tiles.parquet")
            return None

        # If it's a zip file, extract it first
        if file_path.endswith('.zip'):
            print("Extracting zip file...")
            extract_dir = os.path.join(os.path.dirname(file_path), 'extracted')
            os.makedirs(extract_dir, exist_ok=True)

            with ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(extract_dir)

            print(f"Files extracted to: {extract_dir}")

            # Find all potential data files in the extracted directory
            csv_files = glob.glob(os.path.join(
                extract_dir, '**', '*.csv'), recursive=True)
            parquet_files = glob.glob(os.path.join(
                extract_dir, '**', '*.parquet'), recursive=True)
            excel_files = glob.glob(os.path.join(extract_dir, '**', '*.xlsx'), recursive=True) + \
                glob.glob(os.path.join(
                    extract_dir, '**', '*.xls'), recursive=True)

            # Prioritize files to load
            data_files = csv_files + parquet_files + excel_files

            if not data_files:
                print("No data files found in the extracted directory.")
                shp_files = glob.glob(os.path.join(
                    extract_dir, '**', '*.shp'), recursive=True)
                if shp_files:
                    print(f"Found {
                          len(shp_files)} shapefile(s). To load these, install geopandas and use:")
                    print("import geopandas as gpd")
                    print(f"gdf = gpd.read_file('{shp_files[0]}')")
                return None

            file_path = data_files[0]
            print(f"Loading data from: {file_path}")

        # Load the file based on its extension
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith('.parquet'):
            try:
                # Try with pyarrow engine first
                df = pd.read_parquet(file_path, engine='pyarrow')
            except Exception as e:
                print(f"Error with pyarrow: {e}")
                try:
                    # Try with fastparquet engine
                    df = pd.read_parquet(file_path, engine='fastparquet')
                except Exception as e2:
                    print(f"Error with fastparquet: {e2}")
                    print(
                        "\nTo read parquet files, you need to install the required packages:")
                    print("pip install pyarrow fastparquet")
                    return None
        elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
            df = pd.read_excel(file_path)
        else:
            print(f"Unsupported file format: {file_path}")
            return None

        print("\nDataset loaded successfully!")
        print(f"Shape: {df.shape}")
        return df

    except Exception as e:
        print(f"Error loading dataset: {e}")
        print("\nTry installing necessary dependencies:")
        print("pip install pandas pyarrow fastparquet matplotlib")
        return None


def analyze_data(df):
    """
    Perform basic analysis and visualization on the dataset
    """
    if df is None:
        return None

    # Basic information
    print("\nDataset Information:")
    print(f"Number of records: {len(df)}")
    print(f"Columns: {df.columns.tolist()}")

    # Display a few rows
    print("\nFirst 5 rows:")
    print(df.head())

    # Summary statistics
    print("\nSummary Statistics:")
    numeric_columns = df.select_dtypes(include=['number']).columns
    if not numeric_columns.empty:
        print(df[numeric_columns].describe())

    # Plot basic visualizations if possible
    os.makedirs('CS_6140/project/output', exist_ok=True)

    # Try to create a simple visualization based on available columns
    try:
        # If there's a numeric column, create a histogram
        if len(numeric_columns) > 0:
            plt.figure(figsize=(10, 6))
            df[numeric_columns[0]].hist(bins=30)
            plt.title(f'Distribution of {numeric_columns[0]}')
            plt.xlabel(numeric_columns[0])
            plt.ylabel('Frequency')
            plt.savefig(os.path.join(
                'CS_6140/project/output', 'histogram.png'))
            plt.close()
            print(f"Saved histogram of {
                  numeric_columns[0]} to CS_6140/project/output/histogram.png")
    except Exception as e:
        print(f"Error creating visualization: {e}")

    return df


def main():
    # Load the dataset
    df = load_dataset()

    # Analyze and visualize the data
    if df is not None:
        df = analyze_data(df)
        print("\nData loading and analysis complete!")

    return df


if __name__ == "__main__":
    df = main()
