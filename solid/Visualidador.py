class Visualizador:
    def verEntidades(self, entidades):
        if not entidades:
            print("Nenhuma entidade cadastrada.")
            return

        for entidade in entidades:
            print(entidade)