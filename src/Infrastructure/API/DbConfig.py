import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pyodbc



from urllib.parse import quote_plus

DATABASE_URL = f"mssql+pyodbc://sa:{quote_plus('Gy1ok37%9')}@localhost:1433/master?driver=ODBC+Driver+18+for+SQL+Server"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


connection_string = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=localhost,1433;"
    "DATABASE=master2;"
    "UID=sa;"
    "PWD=Gy1ok37%9;"
)

try:
    conn = pyodbc.connect(connection_string, timeout=5)
    print("✅ Bağlantı başarılı!")
except Exception as e:
    print(f"❌ Bağlantı hatası: {e}")
finally:
    if 'conn' in locals():
        conn.close()