import os
import pandas as pd

dataframes = {}
data_folder = 'data/raw'

for file in os.listdir(data_folder):
#goes through every file within the raw data folder.
    if file.endswith('.csv'):
        
        #Load CSV into a DataFrame
        df_name = file.replace('.csv', '')
        df = pd.read_csv(os.path.join(data_folder, file), low_memory=False)
        df = df.drop_duplicates()

        for column in df.columns: 
            print(column, df[column].dtype)
            if pd.api.types.is_numeric_dtype(df[column]):
                df[column]=df[column].fillna(df[column].mean())
            else:
                df[column]=df[column].fillna(df[column].mode()[0])

        cleaned_folder ='data/cleaned'
        os.makedirs(cleaned_folder, exist_ok=True)
        cleaned_file_path = os.path.join(cleaned_folder, f"cleaned_{file}")
        df.to_csv(cleaned_file_path, index=False)

        dataframes[df_name] = df 

    print(f"📂 Cleaning file: {file}")
    print(f"✅ Saved cleaned file: {cleaned_file_path}\n")