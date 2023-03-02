import configparser
import pathlib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


file_config = pathlib.Path(__file__).parent.joinpath('config.ini')
config = configparser.ConfigParser()
config.read(file_config)
db_url = config.get('DB', 'URL_STRING')

engine = create_engine(db_url, echo=True, pool_size=5)
session = sessionmaker(bind=engine, autoflush=False)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()