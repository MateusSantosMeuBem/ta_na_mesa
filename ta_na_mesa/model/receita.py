from sqlalchemy import Column, Integer, String

from model import Base

class Receita(Base):
    __tablename__ = 'receita'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)