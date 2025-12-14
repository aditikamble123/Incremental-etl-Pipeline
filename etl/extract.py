import pandas as pd

def extract_data(csv_path):
    """
    Extract data from CSV file.
    """
    df = pd.read_csv(csv_path)
    return df
