from sqlalchemy import Column, Integer, String

from model import Base

class Refeicao(Base):
    __tablename__ = 'refeicao'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
