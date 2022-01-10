
from typing import List

class Actions():

    up = 1

class Node:
    '''
    Implementação de um único estado do problema que mantêm controle
    do passo anterior que o gerou

    Atributos:
    ------------
    state: Any
        Recebe um estado do problema.

    parent: None | Node
        O Nó que deu origem à este nó. Se for um nó inicial, seu valor é None.

    action: Actions
        A ação aplicada em pai que deu origem à este nó.

    cost: float | int | None
        Um número que indica o custo do caminho até este nó.
    '''

    def __init__(self, state, parent = None, action = None, cost:float | int | None = None):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost


class Search:

    def __init__(self, inicial):
        self.frontier = [Node(inicial)]
        self.exploration = set()

    def is_empty(self):
        return bool(self.frontier)
    
    def expand(self):

    
class BFS(Search):

    def expand(self):
        node = self.frontier.pop()
        for 