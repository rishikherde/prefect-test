from prefect import flow, task
import pandas as pd
import os

@task
def read_csv(file_path: str) -> pd.DataFrame:
    print(f"Reading file: {file_path}")
    return pd.read_csv(file_path)

@task
def process_data(df: pd.DataFrame) -> pd.DataFrame:
    return df.applymap(lambda x: x.upper() if isinstance(x, str) else x)

@task
def write_csv(df: pd.DataFrame, output_path: str):
    print(f"Writing file: {output_path}")
    df.to_csv(output_path, index=False)

@flow
def data_pipeline(input_file: str, output_file: str):
    print(f"Current working directory: {os.getcwd()}")
    df = read_csv(file_path=input_file)
    transformed_df = process_data(df)
    write_csv(transformed_df, output_path=output_file)

if __name__ == "__main__":
    pass  # Remove local execution.