from collections import defaultdict
from decimal import Decimal

from random import choice
from model.refeicao import Refeicao
from model.receita import Receita
from model.receita_produto import ReceitaProduto
from model.refeicao_receita import RefeicaoReceita
from model.produto import Produto
from model.unidade import Unidade

class Carrinho:

    separador = '-' * 25

    @classmethod
    def gerar_carrinho(cls, session):
        '''
        Gera um carrinho de compras com receitas aleatórias. O usuário informa a quantidade de refeições que deseja e o sistema gera um carrinho com receitas aleatórias.

        As receitas geradas são: Carne moída, Frango guisado, Frango guisado.

        -------------------------
        Resumo das compras:
        - Arroz: 3.0kg
        - Sal: 0.50kg
        - Alho: 0.50g
        - Carne moída: 0.4kg
        - Frango: 3.15kg
        - Batata: 0.9kg
        - Cenoura: 0.9kg

        -------------------------
        Detalhes das receitas:
        * Carne moída (1x)
        - Arroz
            | Arroz (0.3kg)
            | Sal (0.05kg)
            | Alho (0.05g)


        E retorna o caminho do arquivo.
        '''

        qtd_refeicoes = int(input('Digite a quantidade de refeições: '))

        refeicoes = session.query(Refeicao).all()
        if not refeicoes:
            print('Vocês não tem refeições pra mostrar!')
            return

        carrinho = defaultdict(int)
        for _ in range(qtd_refeicoes):
            refeicao = choice(refeicoes)
            carrinho[refeicao] += 1

        path = 'carrinho.txt'
        resumo_das_receitas = [f'As receitas geradas são: {", ".join([refeicao.nome.capitalize() for refeicao in carrinho.keys()])}.']
        resumo_das_compras = ['Resumo das compras:']
        detalhes_das_receitas = ['Detalhes das receitas:']
        soma_dos_produtos = defaultdict(int)
        for refeicao, quantidade_dessa_refeicao in carrinho.items():
            nome_da_refeicao = refeicao.nome.capitalize()
            detalhes_das_receitas.append(f'* {nome_da_refeicao} ({quantidade_dessa_refeicao}x)')
            receitas = session.query(Receita).join(RefeicaoReceita).filter(RefeicaoReceita.idRefeicao == refeicao.id).all()

            for receita in receitas:
                detalhes_das_receitas.append(f'  - {receita.nome.capitalize()}')
                receita_produtos = session.query(ReceitaProduto).filter_by(idReceita=receita.id).all()

                for receita_produto in receita_produtos:
                    produto = session.query(Produto).filter_by(id=receita_produto.idProduto).one()
                    unidade = session.query(Unidade).filter_by(id=produto.idUnidade).one()
                    quantidade = receita_produto.quantidadeProduto
                    detalhes_das_receitas.append(f'    | {produto.nome.capitalize()} ({quantidade}{unidade.abreviatura})')
                    soma_dos_produtos[(produto.nome, unidade.abreviatura)] += Decimal(str(quantidade)) * Decimal(str(quantidade_dessa_refeicao))
                detalhes_das_receitas.append('')

        detalhes_das_receitas.append('')
        for (produto, unidade), quantidade in soma_dos_produtos.items():
            resumo_das_compras.append(f'- {produto.capitalize()}: {quantidade}{unidade}')

        with open(path, 'w', encoding='utf-8') as carrinho_saida:
            carrinho_saida.write(cls.join_lines(resumo_das_receitas))
            carrinho_saida.write('\n')
            carrinho_saida.write(cls.separador)
            carrinho_saida.write('\n')
            carrinho_saida.write(cls.join_lines(resumo_das_compras))
            carrinho_saida.write('\n')
            carrinho_saida.write(cls.separador)
            carrinho_saida.write('\n')
            carrinho_saida.write(cls.join_lines(detalhes_das_receitas, end_line=''))

        return path

    @classmethod
    def join_lines(cls, lines, end_line='\n'):
        """
        Junta as linhas com uma quebra de linha no final.

        Args:
            lines (list): Lista de linhas.
            end_line (str): Quebra de linha no final.

        Returns:
            str: Linhas juntas.
        """
        return '\n'.join(lines) + end_line
