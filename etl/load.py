import os
import logging
from urllib.parse import quote_plus
from sqlalchemy import create_engine, text

# ---------- DATABASE CONFIG ----------
MYSQL_USER = "root"
MYSQL_PASSWORD = quote_plus(os.getenv("MYSQL_PASSWORD"))
MYSQL_HOST = "localhost"
MYSQL_DB = "ecommerce_dw"

engine = create_engine(
    f"mysql+mysqldb://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}",
    pool_pre_ping=True
)

# ---------- LOGGING CONFIG ----------
logging.basicConfig(
    filename="logs/etl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -----------------------------------

def get_last_order_id():
    query = text("SELECT COALESCE(MAX(order_id), 0) FROM orders_fact")
    with engine.connect() as conn:
        last_id = conn.execute(query).scalar()
    logging.info(f"Last order_id in DB: {last_id}")
    return last_id


def load_data(df):
    if df.empty:
        logging.info("No new records to load")
        print("No new records found")
        return

    df.to_sql(
        "orders_fact",
        con=engine,
        if_exists="append",
        index=False,
        chunksize=1000
    )

    logging.info(f"Loaded {len(df)} new records")
    print(f"Loaded {len(df)} new records")
