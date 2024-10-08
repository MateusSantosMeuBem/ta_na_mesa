from service import Service
from model.refeicao_receita import RefeicaoReceita

class RefeicaoService(Service):
    @classmethod
    def adicionar_receita(cls, session, model, model_receita):
        refeicoes = session.query(model).all()
        if not refeicoes:
            print(f'Vocês não tem {model.__name__} pra mostrar!')
            return

        print('[TODAS AS REFEIÇÕES]')
        for refeicao in refeicoes:
            print(f'[{refeicao.id}] {refeicao.nome}')
        refeicao_id = input('Digite o ID da refeição que deseja adicionar receita: ')

        refeicao = session.query(model).filter_by(id=refeicao_id).one()
        receitas = session.query(model_receita).all()
        if not receitas:
            print(f'Vocês não tem {model_receita.__name__} pra mostrar!')
            return

        print('[TODAS AS RECEITAS]')
        for receita in receitas:
            print(f'[{receita.id}] {receita.nome}')
        receita_id = input('Digite o ID da receita que deseja adicionar a refeição: ')

        receita = session.query(model_receita).filter_by(id=receita_id).one()
        refeicao_receita = RefeicaoReceita(idRefeicao = refeicao.id, idReceita = receita.id)
        session.add(refeicao_receita)
        session.commit()