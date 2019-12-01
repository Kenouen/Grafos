import unittest


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
            if not (Grafo.verticeValido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

        self.N = N

        for a in A:
            if not (self.arestaValida(A[a])):
                raise ArestaInvalidaException('A aresta ' + A[a] + ' é inválida')
        self.len = len(N)
        self.A = A

    def arestaValida(self, aresta=''):
        '''
        Verifica se uma aresta passada como parâmetro está dentro do padrão estabelecido.
        Uma aresta é representada por um string com o formato a-b, onde:
        a é um substring de aresta que é o nome de um vértice adjacente �  aresta.
        - é um caractere separador. Uma aresta só pode ter um único caractere como esse.
        b é um substring de aresta que é o nome do outro vértice adjacente �  aresta.
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
        if not (self.existeVertice(aresta[:i_traco])) or not (self.existeVertice(aresta[i_traco + 1:])):
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

    def arestas_sobre_vertice(self, d, lista):

        '''
        Resposta da E da Segunda questão pro primeiro roteiro " Quais arestas incidem sobre um vértice N arbitrário?"
        '''

        arestas = []
        for i in lista:
            if d in i:
                if d == i[0]:
                    arestas.append(i)
                else:
                    arestas.append(i[::-1])
        return arestas

# ======================================================================================================================
#                                                       ROTEIRO 7
# ======================================================================================================================

    def remove_parallel(self):
        temp = []
        for i in self.A.values():
            if i not in temp and i[0] != i[-1] and i[::-1] not in temp:
                temp.append(i)
        return temp

    def DijkstraHead(self):
        temp = self.remove_parallel()
        mapa = {}
        for i in self.N:
            arestas = self.arestas_sobre_vertice(i, temp)
            mapa[i] = [arestas, False, len(self.A.values()) + 1, '', 0]
        return mapa

    def Dijkstra(self, w, v, gasosa, postos):
        u = w
        dados = self.DijkstraHead()
        # dados[vertice] = [arestas, Fi, Beta, pi, energy, limite de energia]

        fis = []
        # fi de u vira 1
        dados[u][1] = True

        # Beta de u = 0
        dados[u][2] = 0
        dados[u][4] = gasosa
        while u != v and len(fis) < self.len:

            # Para todos os outros vértices 𝞫(r) ⇽ ∞, 𝞿(r) ⇽ 0, 𝞹(r) ⇽ 0 e w ⇽ u
            for i in dados[u][0]:
                if dados[i[-1]][2] > dados[u][2] + 1:
                    dados[i[-1]][2] = dados[u][2] + 1
                    dados[i[-1]][3] = u
                    dados[i[-1]][4] = dados[i[0]][4] - 1

            # Ache um vértice r* tal que 𝞿(r*)=0, 𝞫(r*)<∞ e 𝞫(r*)=min𝞿(r) = 0(𝞫(r))
            menorcaminho = len(self.A.values()) + 1
            menorvertice = ''

            for p in dados.keys():
                if p in postos:
                    dados[p][4] = 5
                aux = dados[p]
                if aux[1] == False and aux[2] < menorcaminho and aux[4]-1 >= 0:
                    menorcaminho = aux[2]
                    menorvertice = p

            # Se r* não existe, não há caminho u-v e o algoritmo deve parar
            if menorvertice == '':
                break
            # Faça 𝞿(r*) = 1 e w = r*

            dados[menorvertice][1] = True
            u = menorvertice
            if u in postos:
                dados[u][4] = 5


        aux = []
        aux.append(v)
        while v != w:
            if v == '':
                print("Nao a caminho possivel :(")
                return False
            t = dados[v][3]
            aux.append(t)
            v = t

        for i in aux[::-1]:
            print(i, end=' ')
            if (i != u):
                print("-", end=' ')
        print()

# ======================================================================================================================
#                                                       TESTE
# ======================================================================================================================


grafo = Grafo(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','W','Y','Z','a','b','c','d','e','f','g'],
              {'a0': 'A-B', 'a1': 'A-C', 'a2': 'A-D', 'a3': 'B-C', 'a4': 'B-E', 'a5': 'C-F', 'a6': 'D-H', 'a7': 'D-L',
               'a8': 'E-I', 'a9': 'E-F', 'a10': 'F-G', 'a11': 'F-J', 'a12': 'F-K', 'a13': 'G-K', 'a14': 'G-D',
               'a15': 'H-G', 'a16': 'I-M', 'a17': 'J-N', 'a18': 'K-L', 'a19': 'K-O', 'a20': 'L-P', 'a21': 'M-Q',
               'a22': 'N-R', 'a23': 'O-R', 'a24': 'O-Q', 'a25': 'O-S', 'a26': 'P-R', 'a27': 'P-T', 'a28': 'R-U',
               'a29': 'R-S', 'a30': 'S-W', 'a31': 'S-T', 'a32': 'T-X', 'a33': 'U-Y', 'a34': 'U-Z', 'a35': 'V-R',
               'a36': 'W-V', 'a37': 'W-a', 'a38': 'W-b', 'a39': 'X-b', 'a40': 'X-c', 'a41': 'Z-e', 'a42': 'c-f',
               'a43': 'f-e', 'a44': 'e-d', 'a45': 'e-g'})


inicio = 'A'

fim = 'd'

pontos_de_recarga = ['I', 'R', 'X', 'f']

energia_inicial = 3

grafo.Dijkstra(inicio, fim, energia_inicial, pontos_de_recarga)