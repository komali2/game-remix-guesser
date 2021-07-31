import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

username = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_ROOT_PASSWORD')
# MYSQL_HOST is known internally by the MySQL container
# When containers connect to eachother over a network they use the container name as host
host = "game-remix-guesser_mysqldbgame_1" # os.getenv('MYSQL_HOST')
port = os.getenv('MYSQL_PORT')
DB_NAME = os.getenv('MYSQL_DB')

print(username)
print(password)
print(host)
print(port)
SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{username}:{password}@{host}:{port}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={'auth_plugin': 'mysql_native_password'}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()