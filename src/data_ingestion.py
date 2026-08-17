import pandas as pd
import numpy as np
import logging
import os

log_dir = 'log'
os.makedirs(log_dir, exist_ok=True)

logger = logging.getLogger('Data_ingestion')
logger.setLevel('DEBUG')

consoler = logging.StreamHandler()
consoler.setLevel('DEBUG')

file_path = os.path.join(log_dir, 'Data_ingestion.log')
file_handle = logging.FileHandler(file_path)
file_handle.setLevel("DEBUG")

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
consoler.setFormatter(formatter)
file_handle.setFormatter(formatter)

logger.addHandler(consoler)
logger.addHandler(file_handle)


def load_data(data_path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(data_path , engine='pyarrow')
        logger.debug(f"Data loaded successfully from {data_path}. Shape: {df.shape}")
        return df
    except Exception as e:
        logger.error(f"Unable to load data from {data_path}. Error: {e}")
        raise


def save_data(df: pd.DataFrame, path_save: str, filename: str) -> None:
    try:
        raw_data_path = os.path.join(path_save, 'raw')
        os.makedirs(raw_data_path, exist_ok=True)
        # Parquet: much smaller + faster to read/write than CSV, keeps dtypes intact
        out_path = os.path.join(raw_data_path, f"{filename}.parquet")
        df.to_parquet(out_path, index=False, compression='snappy')
        logger.debug(f"Data saved successfully to {out_path}. Shape: {df.shape}")
    except Exception as e:
        logger.error(f"Unable to save data to {filename}. Error: {e}")
        raise


def main():
    try:
        logger.debug("Main function started now.")

        base = r"C:\Users\devan\Downloads\Project_data\ieee-fraud-detection"
        tr_tran_path = os.path.join(base, "train_transaction.csv")
        tr_id_path = os.path.join(base, "train_identity.csv")
        test_tr_path = os.path.join(base, "test_transaction.csv")
        test_id_path = os.path.join(base, "test_identity.csv")

        train_transaction = load_data(tr_tran_path)
        train_identity = load_data(tr_id_path)
        test_transaction = load_data(test_tr_path)
        test_identity = load_data(test_id_path)

        save_data(train_transaction, './data', 'train_transaction')
        save_data(train_identity, './data', 'train_identity')
        save_data(test_transaction, './data', 'test_transaction')
        save_data(test_identity, './data', 'test_identity')

        logger.debug("Data ingestion process completed successfully.")
    except Exception as e:
        logger.error(f"Data ingestion process is unsuccessful. Error: {e}")
        raise


if __name__ == '__main__':
    main()