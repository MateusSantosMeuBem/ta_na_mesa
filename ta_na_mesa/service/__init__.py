class Service: 
    @classmethod
    def coleta_requisitos(cls, model, instance = None, session = None):
        columns = cls.getColumnNames(model, ['id'])
        requisitos = {}
        for column in columns:
            tip = f' ({instance.__dict__[column]})' if instance else ''
            requisitos[column] = input(f'{column.capitalize()}{tip}: ')
        return model(**requisitos, id = instance.id if instance else None)

    def criar_novo(self, session, item):
        session.add(item)
        session.commit()

    @classmethod
    def adicionar(cls, session, model):
        servico = cls()
        novo_item = servico.coleta_requisitos(model, instance=None, session=session)
        servico.criar_novo(session, novo_item)

    @classmethod
    def listar(cls, session, model, columns_to_ignore = ['id']):
        items = session.query(model).all()
        if items:
            columns = cls.getColumnNames(model, columns_to_ignore)
            print('\n[TODOS OS ITEMS]')

        for item in items:
            for column in columns:
                if 'id' in column.lower():
                    print(f'[{getattr(item, column)}]', end='')
                    continue
                print(f' | {getattr(item, column):<20}', end='')
            print()

    @staticmethod
    def getColumnNames(model, ignore_columns = []):
        return [
            column.name for column in model.__table__.columns
            if column.name not in ignore_columns
        ]

    @classmethod
    def editar(cls, session, model):
        do_not_edit = ['id']
        items = session.query(model).all()
        if not items:
            print(f'Vocês não tem {model.__name__} pra mostrar!')
            return

        columns = cls.getColumnNames(model, do_not_edit)
        print('\n[TODOS OS ITEMS]')
        for item in items:
            print(f'[{item.id}]', end='')
            for column in columns:
                print(f' | {getattr(item, column)}')
        item_id = input('Digite o ID do item que deseja editar: ')

        item = session.query(model).filter_by(id=item_id).one()

        if not item:
            print('Item não encontrado')
            return

        requisitos = cls.coleta_requisitos(model, item)
        item.nome = item.nome
        for key, value in requisitos.__dict__.items():
            print(key, value, type(value))
            if key not in do_not_edit:
                setattr(item, key, value)
        session.commit()
        print('Item editado com sucesso!')
