import pandas as pd
from database.db_utils import get_db_connection

def load_csv_to_db(csv_path, table_name):
    df = pd.read_csv(csv_path)
    conn = get_db_connection()
    cursor = conn.cursor()
    for _, row in df.iterrows():
        # Construct your INSERT statement dynamically based on table_name and row
        pass
    conn.commit()
    conn.close()

if __name__ == "__main__":
    load_csv_to_db('data/experiment_metadata.csv', 'Experiment')