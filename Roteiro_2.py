class VerticeInvalidoException(Exception):
    pass

class ArestaInvalidaException(Exception):
    pass

class Grafo:

    QTDE_MAX_SEPARADOR = 1
    SEPARADOR_ARESTA = '-'

    def __init__(self, N=[], A={}):
        '''
        Constrói um objeto do tipo Grafo. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param N: Uma lista dos vértices (ou nodos) do grafo.
        :param V: Uma dicionário que guarda as arestas do grafo. A chave representa o nome da aresta e o valor é uma string que contém dois vértices separados por um traço.
        '''
        for v in N:
            if not(Grafo.verticeValido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

        self.N = N

        for a in A:
            if not(self.arestaValida(A[a])):
                raise ArestaInvalidaException('A aresta ' + A[a] + ' é inválida')

        self.A = A

    def arestaValida(self, aresta=''):
        '''
        Verifica se uma aresta passada como parâmetro está dentro do padrão estabelecido.
        Uma aresta é representada por um string com o formato a-b, onde:
        a é um substring de aresta que é o nome de um vértice adjacente à aresta.
        - é um caractere separador. Uma aresta só pode ter um único caractere como esse.
        b é um substring de aresta que é o nome do outro vértice adjacente à aresta.
        Além disso, uma aresta só é válida se conectar dois vértices existentes no grafo.
        :param aresta: A aresta que se quer verificar se está no formato correto.
        :return: Um valor booleano que indica se a aresta está no formato correto.
        '''

        # Não pode haver mais de um caractere separador
        if aresta.count(Grafo.SEPARADOR_ARESTA) != Grafo.QTDE_MAX_SEPARADOR:
            return False

        # Índice do elemento separador
        i_traco = aresta.index(Grafo.SEPARADOR_ARESTA)

        # O caractere separador não pode ser o primeiro ou o último caractere da aresta
        if i_traco == 0 or aresta[-1] == Grafo.SEPARADOR_ARESTA:
            return False

        # Verifica se as arestas antes de depois do elemento separador existem no Grafo
        if not(self.existeVertice(aresta[:i_traco])) or not(self.existeVertice(aresta[i_traco+1:])):
            return False

        return True

    @classmethod
    def verticeValido(self, vertice=''):
        '''
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        '''
        return vertice != '' and vertice.count(Grafo.SEPARADOR_ARESTA) == 0

    def existeVertice(self, vertice=''):
        '''
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        '''
        return Grafo.verticeValido(vertice) and self.N.count(vertice) > 0

    def existeAresta(self, aresta=''):
        '''
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        '''
        existe = False
        if Grafo.arestaValida(self, aresta):
            for k in self.A:
                if aresta == self.A[k]:
                    existe = True

        return existe

    def adicionaVertice(self, v):
        '''
        Adiciona um vértice no Grafo caso o vértice seja válido e não exista outro vértice com o mesmo nome
        :param v: O vértice a ser adicionado
        :raises: VerticeInvalidoException se o vértice passado como parâmetro não puder ser adicionado
        '''
        if self.verticeValido(v) and not self.existeVertice(v):
            self.N.append(v)
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adicionaAresta(self, nome, a):
        '''
        Adiciona uma aresta no Grafo caso a aresta seja válida e não exista outra aresta com o mesmo nome
        :param v: A aresta a ser adicionada
        :raises: ArestaInvalidaException se a aresta passada como parâmetro não puder ser adicionada
        '''
        if self.arestaValida(a):
            self.A[nome] = a
        else:
            ArestaInvalidaException('A aresta ' + self.A[a] + ' é inválida')


# =======================================================================================================================
#                                            Funções auxiliares
# =======================================================================================================================


    def seleciona_arestas(self, vetor):

        """
        Função auxiliar que seleciona as arestas que incidem em um determinado vertice.
        :param vetor: Vetor sendo analisado;
        :return: Um Dicionario contendo as aresta que incidem no vertice.
        """

        aux = {}
        for i in self.A.keys():
            if vetor in self.A[i]:
                if vetor == self.A[i][-1]:
                    aux[i] = self.A[i][::-1]
                else:
                    aux[i] = self.A[i]
        return aux



    def seleciona_arestas(self, vetor):

        """
        Função auxiliar que seleciona as arestas que incidem em um determinado vertice.
        :param vetor: Vetor sendo analisado;
        :return: Um Dicionario contendo as aresta que incidem no vertice.
        """

        aux = {}
        for i in self.A.keys():
            if vetor in self.A[i]:
                if vetor == self.A[i][-1]:
                    aux[i] = self.A[i][::-1]
                else:
                    aux[i] = self.A[i]
        return aux


#=======================================================================================================================
#                                                       ROTEIRO 2
#=======================================================================================================================


    def controle(self, d, lista):

        """
        Função auxiliar para a função *DFS*.
        :param d: Vertice sendo atualmente processado;
        :param lista: Lista resultante para o DFS;
        """

        aux = self.seleciona_arestas(d)
        for aresta in aux.keys():
            if aux[aresta][-1] not in lista:
                lista.append(aresta)
                lista.append(aux[aresta][-1])
                self.controle(aux[aresta][-1], lista)

    def DFS(self, vertice):

        """
        Função para gerar o DFS do grafo.
        :param vertice: Vertice que o usuario deseja iniciar o caminho;
        :return: Lista contendo o DFS
        """


        lista = [vertice]
        self.controle(vertice, lista)

        return lista


g_p = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'],
                 {'a1':'J-C', 'a2':'C-E', 'a3':'C-E', 'a4':'C-P', 'a5':'C-P', 'a6':'C-M', 'a8':'M-T', 'a9':'T-Z'})

Ze = Grafo(['A', 'B', 'C', 'D', 'E', 'F', 'H', 'G'], {'a1':'A-E', 'a2' : 'A-F', 'a3':'F-H', 'a4':'H-G', 'a5' : 'G-F', 'a6':'A-B', 'a7':'B-C', 'a8':'B-D', 'a9':'G-C'})


g_p_sem_paralelas = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'], {'a1': 'J-C', 'a3': 'C-E', 'a4': 'C-P', 'a6': 'C-M','a8': 'M-T', 'a9': 'T-Z'})


grafo = Grafo(['A','B','C','D','E','F','G','H','I','J','K'],
              {'1':'A-B', '2':'A-G','3':'A-J','4':'G-K','5':'K-J',
              '6':'J-G','7':'J-I','8':'I-G', '9':'G-H','10':'H-F',
              '11':'F-B','12':'B-G','13':'B-C','14':'C-D','15':'D-E',
              '16':'D-B','17':'B-E'})

print("DFS grafo A-K")
print(grafo.DFS("A"))

print("ze DFS")
print(Ze.DFS("A"))

print("DFS grafo normal da paraiba")
print(g_p.DFS("Z"))

print("DFS grafo paraiba sem paralelas")
print(g_p_sem_paralelas.DFS("J"))