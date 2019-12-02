class VerticeInvalidoException(Exception):
    pass


class ArestaInvalidaException(Exception):
    pass


class MatrizInvalidaException(Exception):
    pass


class Grafo:
    QTDE_MAX_SEPARADOR = 1
    SEPARADOR_ARESTA = '-'
    __maior_vertice = 0

    def __init__(self, V=None, A=None):
        '''
        Constrói um objeto do tipo Grafo. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param V: Uma lista dos vértices (ou nodos) do grafo.
        :param V: Uma matriz de adjacência que guarda as arestas do grafo. Cada entrada da matriz tem um inteiro que indica a quantidade de arestas que ligam aqueles vértices
        '''

        if V == None:
            V = list()
        if A == None:
            A = dict()

        for v in V:
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

        self.N = list(V)
        M = []

        for k in range(len(V)):
            M.append(list())
            for l in range(len(V)):
                cond = False
                for j in A.values():
                    if j[0][0] == V[k] and j[0][-1] == V[l]:
                        try:
                            if M[k][l] > j[1]:
                                M[k][l] = j[1]
                        except:
                            M[k].append(j[1])
                        cond = True
                if not cond:
                    M[k].append(0)
        self.M = M

        if len(M) != len(V):
            raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for c in M:
            if len(c) != len(V):
                raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for i in range(len(V)):
            for j in range(len(V)):
                '''
                Verifica se os índices passados como parâmetro representam um elemento da matriz abaixo da diagonal principal.
                Além disso, verifica se o referido elemento é um traço "-". Isso indica que a matriz é não direcionada e foi construída corretamente.
                '''
                # if i>j and not(M[i][j] == '-'):
                #     raise MatrizInvalidaException('A matriz não representa uma matriz não direcionada')

                aresta = V[i] + Grafo.SEPARADOR_ARESTA + V[j]

        self.M = M
        self.len = len(self.N)
        self.A = A

    def __str__(self):
        '''
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato padrão.
        :return: Uma string que representa o grafo
        '''

        # Dá o espaçamento correto de acordo com o tamanho do string do maior vértice

        return self.tostring(self.M)

    def dfsAux(self, d, lista, arestasv, matriz):
        aux = self.arestas_sobre_vertice(d, matriz)
        for aresta in aux:
            if aresta[-1] not in lista:
                lista.append(aresta[-1])
                self.dfsAux(aresta[-1], lista, arestasv, matriz)

    def dfs(self, d, matriz):
        lista = [d]
        self.dfsAux(d, lista, [], matriz)
        return lista

    def conexo(self, inicio, matriz):
        a = self.dfs(inicio, matriz)
        for i in self.N:
            if i not in a:
                return False
        return True

    def copy(self, m):
        aux = []
        for i in range(self.len):
            aux.append([])
            for p in range(self.len):
                aux[i].append(m[i][p])
        return aux

    def arestas_sobre_vertice(self, d, matriz):
        lista = []
        aux = self.N.index(d)
        for i in range(self.len):
            if self.M[aux][i] > 0:
                lista.append("%s-%s" % (d, self.N[i]))

        return lista

    def tostring(self, matriz):
        # Dá o espaçamento correto de acordo com o tamanho do string do maior vértice
        espaco = ' ' * (self.__maior_vertice)

        grafo_str = espaco + ' '

        for v in range(self.len):
            grafo_str += self.N[v]
            if v < (self.len - 1):  # Só coloca o espaço se não for o último vértice
                grafo_str += ' '

        grafo_str += '\n'

        for l in range(self.len):
            grafo_str += self.N[l] + ' '
            for c in range(self.len):
                grafo_str += str(matriz[l][c]) + ' '
            grafo_str += '\n'
        return grafo_str

    def grau(self, d):
        aux = self.N.index(d)
        soma = 0
        for i in range(self.len):
            if i > aux:
                soma += self.M[aux][i]
            elif i <= aux:
                soma += self.M[i][aux]
        return soma

    # ======================================================================================================================
    #                                                       ROTEIRO 8
    # ======================================================================================================================

    def verticeNaArvore(self, ind, matriz):

        cond = True
        for i in range(self.len):
            if matriz[i][self.N.index(ind)] > 0 or matriz[self.N.index(ind)][i] > 0:
                cond = False
        return cond

    def adicionarAresta(self, inicio, fim, matriz):

        matriz[self.N.index(inicio)][self.N.index(fim)] = self.M[self.N.index(inicio)][self.N.index(fim)]

    def prim_recurcivo(self, u, matriz):

        for i in self.arestas_sobre_vertice(u, matriz):
            if self.verticeNaArvore(i[-1], matriz):
                self.adicionarAresta(u, i[-1], matriz)
                self.prim_recurcivo(i[-1], matriz)

    def Prim(self, inicio):

        # Função que inicia e implanta as variaveis necessarias para a recursividade de prim

        Matriz_temp = []
        for i in range(self.len):
            Matriz_temp.append([])
            for p in range(self.len):
                Matriz_temp[i].append(0)

        self.prim_recurcivo(inicio, Matriz_temp)
        return self.tostring(Matriz_temp)

    def ModifiedPrim(self):
        # Prim começando do vertice com menor peso
        menorEdge = ''
        menorgrau = float("inf")
        for i in self.N:
            a = self.grau(i)
            if a < menorgrau:
                menorEdge = i
                menorgrau = a

        if menorgrau == 0:
            return "Nao a spanning tree"

        return self.Prim(menorEdge)

    def kruskall(self):

        Matriz_temp = []
        for i in range(self.len):
            Matriz_temp.append([])
            for p in range(self.len):
                Matriz_temp[i].append(0)

        # separação e sort das arestas
        lista = []
        while len(lista) < len(self.A.values()):
            maior = float("inf")
            tmaior = []
            for i in self.A.values():
                if i[1] < maior and list(i) not in lista:
                    maior = i[1]
                    tmaior = list(i)

            lista.append(tmaior)

        # Raizes das arvores
        Arvores = []
        for i in self.N:
            Arvores.append([i])

        for i in lista:

            for o in range(len(Arvores)):

                if i[0][0] in Arvores[o]:
                    break

            for p in range(len(Arvores)):
                if i[0][-1] in Arvores[p]:
                    break

            if o == p:
                continue

            for j in Arvores[p]:
                Arvores[o].append(j)
            Arvores[o].append(i)

            del Arvores[p]

        arestas = []
        for i in Arvores[0]:

            if len(i) > 1:
                self.adicionarAresta(i[0][0], i[0][-1], Matriz_temp)

        return self.tostring(Matriz_temp)


# ======================================================================================================================
#                                                       Teste
# ======================================================================================================================


# grafo = Grafo(
#     ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X',
#      'W', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g'],
#     {'a0': 'A-B', 'a1': 'A-C', 'a2': 'A-D', 'a3': 'B-C', 'a4': 'B-E', 'a5': 'C-F', 'a6': 'D-H', 'a7': 'D-L',
#      'a8': 'E-I', 'a9': 'E-F', 'a10': 'F-G', 'a11': 'F-J', 'a12': 'F-K', 'a13': 'G-K', 'a14': 'G-D',
#      'a15': 'H-G', 'a16': 'I-M', 'a17': 'J-N', 'a18': 'K-L', 'a19': 'K-O', 'a20': 'L-P', 'a21': 'M-Q',
#      'a22': 'N-R', 'a23': 'O-R', 'a24': 'O-Q', 'a25': 'O-S', 'a26': 'P-R', 'a27': 'P-T', 'a28': 'R-U',
#      'a29': 'R-S', 'a30': 'S-W', 'a31': 'S-T', 'a32': 'T-X', 'a33': 'U-Y', 'a34': 'U-Z', 'a35': 'V-R',
#      'a36': 'W-V', 'a37': 'W-a', 'a38': 'W-b', 'a39': 'X-b', 'a40': 'X-c', 'a41': 'Z-e', 'a42': 'c-f',
#      'a43': 'f-e', 'a44': 'e-d', 'a45': 'e-g'},{'A-B':2, 'F-G':3, 'L-P':2, 'I-M':2, 'R-U':4, 'D-H':2, 'J-N':2)
#
# inicio = 'A'
#
# grafo.Prim(inicio)

g_p = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'],
            {'a1': ('J-C', 1), 'a2': ('C-E', 2), 'a3': ('C-E', 3), 'a4': ('C-P', 1), 'a5': ('C-P', 2),
             'a6': ('C-M', 3), 'a7': ('C-T', 2), 'a8': ('M-T', 1), 'a9': ('T-Z', 1)})

print(g_p.kruskall())
