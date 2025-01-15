class Visualizador:
    def ver_entidades(self, entidades):
        if not entidades:
            print("Nenhuma entidade cadastrada.")
            return

        for entidade in entidades:
            print(entidade)