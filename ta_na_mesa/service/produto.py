from service import Service
from model.unidade import Unidade

class ProdutoService(Service):
    @classmethod
    def coleta_requisitos(cls, model, instance = None, session = None):
        columns = cls.getColumnNames(model, ['id'])
        requisitos = {}
        for column in columns:
            tip = f' ({instance.__dict__[column]})' if instance else ''
            if column.lower() == 'idunidade':
                cls.listar(session, Unidade, [])
            requisitos[column] = input(f'{column.capitalize()}{tip}: ')
        return model(**requisitos, id = instance.id if instance else None)
