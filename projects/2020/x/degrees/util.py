class Node():
    def __init__(self, artist, movie, parent = None):
        self.artist = artist
        self.parent = parent
        self.action = movie


class Search():
    def __init__(self, source):
        self.frontier = [Node(source, None)]
        self.explored = set()

    def add(self, node):
        self.frontier.append(node)

    def is_empty(self):
        return len(self.frontier) == 0

class BFS(Search):
    def remove(self):
        return self.frontier.pop()

class DFS(Search):

    def remove(self):
        return self.frontier.pop(0)
