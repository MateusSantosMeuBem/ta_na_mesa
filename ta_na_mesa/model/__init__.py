from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

# Conexão com o banco de dados (SQLite neste exemplo)
engine = create_engine('sqlite:///meu_banco.db', echo=True)

# Base para as classes
Base = declarative_base()