import pandas as pd

def remove_outliers(df, columns):
    """
    Removes outliers from specified columns in a DataFrame using the IQR method.
    
    Parameters:
        df (pd.DataFrame): The DataFrame from which to remove outliers.
        columns (list): A list of column names to check for outliers.
        
    Returns:
        pd.DataFrame: The DataFrame with outliers removed from the specified columns.
    """
    for column in columns:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1

        # Define the lower and upper bounds for outliers
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        # Filter out outliers
        df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    
    return df

# Example usage:
# Create a sample DataFrame
data = {
    'value1': [10, 12, 14, 15, 15, 17, 18, 19, 100, 150, 200],
    'value2': [5, 6, 7, 8, 9, 10, 11, 12, 1000, 1500, 2000]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Remove outliers from the 'value1' and 'value2' columns
df_no_outliers = remove_outliers(df, ['value1', 'value2'])

print("\nDataFrame after removing outliers:")
print(df_no_outliers)
