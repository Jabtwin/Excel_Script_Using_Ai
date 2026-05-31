import polars as pl

def read_data(file_path_or_buffer, file_type: str) -> pl.DataFrame:
    """
    Đọc dữ liệu từ file csv hoặc excel sử dụng Polars
    """
    try:
        if file_type == "csv":
            df = pl.read_csv(file_path_or_buffer)
        elif file_type == "excel" or file_type == "xlsx":
            df = pl.read_excel(file_path_or_buffer)
        else:
            raise ValueError("Định dạng file không được hỗ trợ")
        return df
    except Exception as e:
        raise Exception(f"Lỗi khi đọc dữ liệu: {str(e)}")

def get_data_info(df: pl.DataFrame) -> str:
    """
    Lấy thông tin cơ bản của dữ liệu (schema, số dòng)
    """
    schema = df.schema
    n_rows = df.height
    info = f"Dữ liệu có {n_rows} dòng.\nCấu trúc các cột:\n"
    for col_name, col_type in schema.items():
        info += f"- {col_name}: {col_type}\n"
    return info
