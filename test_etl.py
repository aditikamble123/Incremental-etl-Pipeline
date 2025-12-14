from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import get_last_order_id, load_data

def run_etl():
    df = extract_data("data/ecommerce_orders_10k_updated.csv")

    last_order_id = get_last_order_id()
    print(f"Last order_id in DB: {last_order_id}")

    df_new = transform_data(df, last_order_id)
    load_data(df_new)

    print("Incremental ETL completed")

if __name__ == "__main__":
    run_etl()
