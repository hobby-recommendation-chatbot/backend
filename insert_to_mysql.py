# 필요한 패키지 설치:
# pip install pandas sqlalchemy pymysql cryptography
import pandas as pd
from sqlalchemy import create_engine

# MySQL 연결 설정
DB_USER = 'ssafy'      
DB_PASSWORD = 'ssafy' 
DB_HOST = 'localhost'
DB_PORT = '3306'
DB_NAME = 'ssafydb'   

engine = create_engine(f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4')


# CSV 파일 불러오기
user_df = pd.read_csv('C:/Users/SSAFY/Downloads/user_hobbies_data - user_hobbies_data.csv')
hobby_df = pd.read_csv('C:/Users/SSAFY/Downloads/hobbies_data - hobbies_data.csv')

# MySQL에 INSERT
hobby_df.to_sql(name='hobbies', con=engine, if_exists='append', index=False)
user_df.to_sql(name='users', con=engine, if_exists='append', index=False)

print("데이터 삽입 완료")
