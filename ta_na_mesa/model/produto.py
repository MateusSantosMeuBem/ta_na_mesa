from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from model import Base

class Produto(Base):
    __tablename__ = 'produto'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    preco = Column(Float, nullable=False)
    idUnidade = Column(Integer, ForeignKey('unidade.id'))

    unidade = relationship('Unidade', back_populates='produtos')
