from functools import partial

from sqlalchemy.orm import sessionmaker
from model import engine

from service.carrinho import Carrinho
from model.receita import Receita
from model.refeicao import Refeicao
from model.produto import Produto
from model.unidade import Unidade
from service.produto import ProdutoService
from service.receita import ReceitaService
from service.refeicao import RefeicaoService
from service.unidade import UnidadeService

# Criar a sessão
Session = sessionmaker(bind=engine)
session = Session()

class Menu:
    opcoes = {
        'refeição': {
            'adicionar': partial(RefeicaoService.adicionar, session, Refeicao),
            'listar': partial(RefeicaoService.listar, session, Refeicao),
            'editar': partial(RefeicaoService.editar, session, Refeicao),
            'adicionar receita': partial(RefeicaoService.adicionar_receita, session, Refeicao, Receita),
        },
        'receita': {
            'adicionar': partial(ReceitaService.adicionar, session, Receita),
            'listar': partial(ReceitaService.listar, session, Receita),
            'editar': partial(ReceitaService.editar, session, Receita),
            'adicionar produto': partial(ReceitaService.adicionar_produto, session, Receita, Produto),
        },
        'produto': {
            'adicionar': partial(ProdutoService.adicionar, session, Produto),
            'listar': partial(ProdutoService.listar, session, Produto),
            'editar': partial(ProdutoService.editar, session, Produto),
        },
        'unidade': {
            'adicionar': partial(UnidadeService.adicionar, session, Unidade),
            'listar': partial(UnidadeService.listar, session, Unidade),
            'editar': partial(UnidadeService.editar, session, Unidade),
        },
        'carrinho': {
            'gerar': partial(Carrinho.gerar_carrinho, session),
        },
    }

    @classmethod
    def run(cls):
        cls.clear_terminal()
        while True:
            print('\n--- Menu Principal ---')
            for i, (item, _) in enumerate(cls.opcoes.items(), start=1):
                print(f'{i}. {item.capitalize()}: ')

            print(f'{i+1}. Sair')

            escolha = input('Escolha uma opção: ')

            if escolha == str(i+1):
                print('Saindo...')
                break
            elif escolha.isdigit() and int(escolha) in range(1, i+1):
                cls.clear_terminal()
                categoria = list(cls.opcoes.keys())[int(escolha)-1]
                print(f'\n--- Menu {categoria.capitalize()} ---')
                sub_opcoes = cls.opcoes[categoria]
                for i, (item, _) in enumerate(sub_opcoes.items(), start=1):
                    print(f'{i}. {item.capitalize()}')

                escolha = input('Escolha uma opção: ')
                if escolha.isdigit() and int(escolha) in range(1, i+1):
                    sub_opcao = list(sub_opcoes.keys())[int(escolha)-1]
                    sub_opcoes[sub_opcao]()
                else:
                    print('Opção inválida. Tente novamente.')
            else:
                print('Opção inválida. Tente novamente.')

    @staticmethod
    def clear_terminal():
        import os
        os.system('cls' if os.name == 'nt' else 'clear')