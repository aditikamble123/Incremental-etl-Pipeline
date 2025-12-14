def transform_data(df, last_order_id):
    """
    Filter only new records based on order_id.
    """
    df_new = df[df["order_id"] > last_order_id].copy()

    if df_new.empty:
        return df_new

    df_new["total_price"] = df_new["qty"] * df_new["price"]
    return df_new
