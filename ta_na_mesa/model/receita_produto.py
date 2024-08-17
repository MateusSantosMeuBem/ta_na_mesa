from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from model import Base

class ReceitaProduto(Base):
    __tablename__ = 'receita_produto'

    id = Column(Integer, primary_key=True)
    idReceita = Column(Integer, ForeignKey('receita.id'))
    idProduto = Column(Integer, ForeignKey('produto.id'))
    quantidadeProduto = Column(Float, nullable=False)

    receita = relationship('Receita')
    produto = relationship('Produto')
