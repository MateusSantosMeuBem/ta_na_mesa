from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from model import Base

class RefeicaoReceita(Base):
    __tablename__ = 'refeicao_receita'

    id = Column(Integer, primary_key=True)
    idRefeicao = Column(Integer, ForeignKey('refeicao.id'))
    idReceita = Column(Integer, ForeignKey('receita.id'))

    refeicao = relationship('Refeicao')
    receita = relationship('Receita')
