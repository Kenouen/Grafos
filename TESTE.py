from grafoPC import *

g_p = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'],
                 {'a1':'J-C', 'a2':'C-E', 'a3':'C-E', 'a4':'C-P', 'a5':'C-P', 'a6':'C-M', 'a7':'C-T', 'a8':'M-T', 'a9':'T-Z'})

print(g_p.DFS('J'))

grafo = Grafo(['A','B','C','D','E','F','G','H','I','J','K'],
              {'1':'A-B', '2':'A-G','3':'A-J','4':'G-K','5':'K-J',
              '6':'J-G','7':'J-I','8':'I-G', '9':'G-H','10':'H-F',
              '11':'F-B','12':'B-G','13':'B-C','14':'C-D','15':'D-E',
              '16':'D-B','17':'B-E'})

print(grafo.DFS("K"))