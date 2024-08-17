from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from model import Base

class Unidade(Base):
    __tablename__ = 'unidade'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    abreviatura = Column(String, nullable=False)

    produtos = relationship('Produto', back_populates='unidade')
