class Avaliacao:
    
    def __init__(self, nome, disciplina, nota = 0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota


    #Criando Atributo Validável
    @property
    def nota(self):         # Método getter
        return self._nota

    @nota.setter
    def nota(self, nota):   # Método setter
        if 0 <= nota <= 10:
            self._nota = nota
        else:
            print("Nota inválida!")