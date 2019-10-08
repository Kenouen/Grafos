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


# ======================================================================================================================
#                                                       ROTEIRO 1
#=======================================================================================================================


    def vertices_nao_adjacentes(self):

        '''
        Resposta da A da Segunda questão pro primeiro roteiro " Encontre todos os pares de vértices não adjacentes."
        '''

        lista = []
        for i in self.N:
            for o in self.N:
                a = i + self.SEPARADOR_ARESTA + o
                b = o + self.SEPARADOR_ARESTA + i
                if a not in self.A.values() and b not in self.A.values():
                    lista.append(a)
        return lista

    def ha_laco(self):

        '''
        Resposta da B da Segunda questão pro primeiro roteiro " Há algum vértice adjacente a ele mesmo? (Retorne True ou False)"
        '''

        for i in self.A.values():
            a, b = i.split(self.SEPARADOR_ARESTA)
            if a == b:
                return True
        return False

    def ha_paralelas(self):

        '''
        Resposta da C da Segunda questão pro primeiro roteiro " Há arestas paralelas? (Retorne True ou False)"
        '''

        for i in self.A.values():
            cont = -1
            for o in self.A.values():
                aux = i[::-1]
                if i == o or aux == o:
                    cont += 1
            if cont >= 1:
                return True
        return False

    def grau(self, x):

        '''
        Resposta da D da Segunda questão pro primeiro roteiro " Qual o grau de um vértice arbitrário?"
        '''

        cont = 0
        for i in self.A.values():
            if x in i:
                cont += 1
        return cont

    def arestas_sobre_vertice(self, x):

        '''
        Resposta da E da Segunda questão pro primeiro roteiro " Quais arestas incidem sobre um vértice N arbitrário?"
        '''

        arestas = []
        for i in self.A.keys():
            if x in self.A[i]:
                arestas.append(i)
        return arestas

    def eh_completo(self):

        '''
        Resposta da F da Segunda questão pro primeiro roteiro "Esse grafo é completo?"
        '''
        cond = True
        for i in self.N:
            cont = 0
            if cond:
                for p in self.N:
                    if p != i:
                        a = i + self.SEPARADOR_ARESTA + p
                        b = p + self.SEPARADOR_ARESTA + i
                        if a not in self.A.values() and b not in self.A.values():
                            cond = False
                            break
            else:
                break
        return cond


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


# =======================================================================================================================
#                                                       ROTEIRO 3
# =======================================================================================================================


    def ha_ciclo(self):

        """
        Função para achar ciclos no grafo.
        :return: O ciclo em forma de lista, ou False caso não haja ciclos.
        """

        for i in self.N:
            INICIO = 0 #indice do primeiro vertice a ser processado

            cicla = [i]
            arestasverificadas = []
            lista = self.verifica_ciclo(i, cicla, arestasverificadas)

            if lista != False:
                return lista
        return False

    def verifica_ciclo(self, atual, ciclo, arestasVerificadas):

        """
        Função auxiliar da função *ha_ciclo*, com intuito de gerar recursivamente a lista de ciclo. Caso a mesma exista;
        :param atual: Vertice sendo verificado;
        :param ciclo: Lista para alocar o ciclo;
        :param arestasVerificadas: Lista de arestas já verificadas;
        :return: Retorna uma lista contendo o caminho do ciclo, ou False caso o mesmo nao exista;
        """

        aux = self.seleciona_arestas(atual)
        for i in aux.keys():
            if i not in arestasVerificadas:
                if aux[i][-1] in ciclo:
                    ciclo = ciclo[ciclo.index(aux[i][-1]):]
                    ciclo.append(i)
                    ciclo.append(aux[i][-1])
                    return ciclo
                else:
                    arestasVerificadas.append(i)
                    ciclo.append(i)
                    ciclo.append(aux[i][-1])
                    return self.verifica_ciclo(aux[i][-1], ciclo, arestasVerificadas)
        ciclo = ciclo[0:-2]
        if len(ciclo) == 1:
            return False
        else:
            return self.verifica_ciclo(aux[i][-1], ciclo, arestasVerificadas)

    def recursivaCaminho(self, d, lista, arestasverificadas, cont, n):
        """
        Função auxiliar da Função *caminho*, para processar recursivamente o vertice passado.
        :param d: Vertice sendo processado;
        :param lista: Lista final com o caminho;
        :param arestasverificadas: lista de arestas ja verificadas pelo programa;
        :param cont: contador para conferir quantas arestas ja estão no caminho;
        :param n: Tamanho do caminho desejado;
        :return: Retorna o maior caminho possivel achado.
        """
        aux = self.seleciona_arestas(d)
        for i in aux.keys():
            if i not in arestasverificadas:
                if aux[i][-1] not in lista:
                    lista.append(i)
                    lista.append(aux[i][-1])
                    arestasverificadas.append(i)
                    cont +=1
                    return self.recursivaCaminho(aux[i][-1], lista, arestasverificadas, cont, n)
                else:
                    arestasverificadas.append(i)

        if cont >= n:
            return lista
        if len(lista) == 0:
            return False
        else:
            if len(arestasverificadas) == len(self.A.keys()):
                return False
            cont -= 1
            lista = lista[:-2]
            return self.recursivaCaminho(aux[i][-1], lista, arestasverificadas, cont, n)

    def caminho(self, n):
        """
        Função para descobrir um caminho de tamanho n.
        :param n: Tamanho desejado do caminho;
        :return: Lista contendo o caminho de tamanho n.
        """
        for i in self.N:
            aux = [i]
            av = []
            cont = 0
            f = self.recursivaCaminho(i, aux, av, cont, n)
            if f != False:
                return f[:n+(n+1)]
        return False

    def conexo(self):
        """
        Função para verificar se o grafo é conexo.
        :return:
        """
        aux = self.DFS(self.N[0])
        cond = True
        for i in self.N:
            if i not in aux:
                cond = False
        return cond

    def to_string(self):
        print("Ciclo:")
        print(self.ha_ciclo())
        print("Caminho de tamanho %d" % (int(len(self.A.keys())/2)))
        print(self.caminho(int(len(self.A.keys())/2)))
        print("conexo:")
        print(self.conexo())


# =======================================================================================================================
#                                                       Testes
# =======================================================================================================================


g_p = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'],
                 {'a1':'J-C', 'a2':'C-E', 'a3':'C-E', 'a4':'C-P', 'a5':'C-P', 'a6':'C-M', 'a8':'M-T', 'a9':'T-Z'})

Ze = Grafo(['A', 'B', 'C', 'D', 'E', 'F', 'H', 'G'], {'a1':'A-E', 'a2' : 'A-F', 'a3':'F-H', 'a4':'H-G', 'a5' : 'G-F', 'a6':'A-B', 'a7':'B-C', 'a8':'B-D', 'a9':'G-C'})


g_p_sem_paralelas = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'], {'a1': 'J-C', 'a3': 'C-E', 'a4': 'C-P', 'a6': 'C-M','a7': 'C-T', 'a8': 'M-T', 'a9': 'T-Z'})


grafo = Grafo(['A','B','C','D','E','F','G','H','I','J','K'],
              {'1':'A-B', '2':'A-G','3':'A-J','4':'G-K','5':'K-J',
              '6':'J-G','7':'J-I','8':'I-G', '9':'G-H','10':'H-F',
              '11':'F-B','12':'B-G','13':'B-C','14':'C-D','15':'D-E',
              '16':'D-B','17':'B-E'})

g_p.to_string()
g_p_sem_paralelas.to_string()
Ze.to_string()
grafo.to_string()
