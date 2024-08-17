from model import Base, engine
from model.receita import Receita
from model.receita_produto import ReceitaProduto
from model.refeicao import Refeicao
from model.refeicao_receita import RefeicaoReceita
from model.produto import Produto
from model.unidade import Unidade
from service.menu import Menu


# Executar o CLI
if __name__ == '__main__':
    # Criar as tabelas no banco de dados apenas se elas não existirem
    Base.metadata.create_all(engine)

    Menu.run()
