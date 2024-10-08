from service import Service
from model.receita_produto import ReceitaProduto

class ReceitaService(Service):
    @classmethod
    def adicionar_produto(cls, session, model, model_produto):
        receitas = session.query(model).all()
        if not receitas:
            print(f'Vocês não tem {model.__name__} pra mostrar!')
            return

        print('[TODAS AS RECEITAS]')
        for receita in receitas:
            print(f'[{receita.id}] {receita.nome}')
        receita_id = input('Digite o ID da receita que deseja adicionar produto: ')

        receita = session.query(model).filter_by(id=receita_id).one()
        produtos = session.query(model_produto).all()
        if not produtos:
            print(f'Vocês não tem {model_produto.__name__} pra mostrar!')
            return

        print('[TODOS OS PRODUTOS]')
        for produto in produtos:
            print(f'[{produto.id}] {produto.nome}')
        produto_id = input('Digite o ID do produto que deseja adicionar a receita: ')

        produto = session.query(model_produto).filter_by(id=produto_id).one()
        quantidade = input('Digite a quantidade do produto: ')
        receita_produto = ReceitaProduto(idReceita = receita.id, idProduto = produto.id, quantidadeProduto = quantidade)
        session.add(receita_produto)
        session.commit()
