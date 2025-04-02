from contextlib import contextmanager
import pymysql
from config import settings

@contextmanager
def get_db_connection():
    conn = pymysql.connect(
        host=settings.MYSQL_HOST,
        user=settings.MYSQL_USER,
        password=settings.MYSQL_PASSWORD,
        db=settings.MYSQL_DB,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        yield conn
    finally:
        conn.close()

def batch_insert(table_name, data_list, batch_size=100):
    """批量插入数据优化"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        try:
            for i in range(0, len(data_list), batch_size):
                batch = data_list[i:i+batch_size]
                placeholders = ', '.join(['%s'] * len(batch[0]))
                columns = ', '.join(batch[0].keys())
                sql = f"INSERT IGNORE INTO {table_name} ({columns}) VALUES ({placeholders})"
                cursor.executemany(sql, [tuple(item.values()) for item in batch])
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e