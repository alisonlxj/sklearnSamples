# ==========================
# PART1 普通读取数据库
# ==========================
print("===PART1 普通读取数据库===")

import pymysql

USER = "waimai_dq"
PW = "iadCfu8C5xnHcl"
DB_HOST = "10.189.181.21"
DB_PORT = 5002
DB_NAME = "waimai_data_query"
db = pymysql.connect(user=USER, password=PW, host=DB_HOST, port=DB_PORT, db=DB_NAME)
cursor = db.cursor()
sql_cmd_01 = "select distinct crt_time from appkey_time_combination_cache_data"
cursor.execute(sql_cmd_01)
data = cursor.fetchall()

print(type(data))
print(data)

db.close()

# ==========================
# PART2 pandas读取数据库
# ==========================
print("===PART2 pandas读取数据库===")

import pandas as pd
from sqlalchemy import create_engine

# 用 sqlalchemy 构建数据库连接
connect_info = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(USER, PW, DB_HOST, DB_PORT, DB_NAME)
print(connect_info)
engine = create_engine(connect_info)

# select id, name, git, octo_app_key, bds_mode, plus_id, plus_name, business
sql_cmd_02 = "select id, name, git, octo_app_key, bds_mode, plus_id, plus_name, business from job where octo_app_key != '' limit 10"

print(sql_cmd_02)
df = pd.read_sql(sql=sql_cmd_02, con=engine, columns=['name', 'octo_app_key', 'bds_mode'])
print(df)

