import nx as nx
import networkx as nx
import matplotlib.pyplot as plt

class Graph():
    v = {}
    visual=[]



    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)

    #  self.v.setdefault(a,[]).append(b)


        # In visualize function G is an object of
        # class Graph given by networkx G.add_edges_from(visual)
        # creates a graph with a given list
        # nx.draw_networkx(G) - plots the graph
        # plt.show() - displays the graph

    def visualize(self):
        G = nx.DiGraph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()
        plt.draw()



    # visits all the nodes of a graph (connected component) using BFS
    def bfsTraverse(self, start):
        # keep track of all visited nodes
        explored = []
        # keep track of nodes to be checked
        queue = [start]

        # keep looping until there are nodes still to be checked
        while queue:
            # pop shallowest node (first node) from queue
            node = queue.pop(0)
            if node not in explored:
                # add node to list of checked nodes
                explored.append(node)
                neighbours = self.v.setdefault(node,[])


                # add neighbours of node to queue
                for neighbour in neighbours:
                    queue.append(neighbour)
        return explored

    def bfsShortestPath(self, start, goal):
        # keep track of explored nodes
        explored = []
        # keep track of all the paths to be checked
        queue = [[start]]

        # return path if start is goal
        if start == goal:
            return "That was easy! Start = goal"

        # keeps looping until all possible paths have been checked
        while queue:
            # pop the first path from the queue
            path = queue.pop(0)
            # get the last node from the path
            node = path[-1]
            if node not in explored:
                neighbours = self.v.setdefault(node,[])
                # go through all neighbour nodes, construct a new path and
                # push it into the queue
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
                    # return path if neighbour is goal
                    if neighbour == goal:
                        return new_path

                # mark node as explored
                explored.append(node)

        # in case there's no path between the 2 nodes
        return "So sorry, but a connecting path doesn't exist :("

    #DFS ADHAM
    def DFS(self, start, goal, explored, path_so_far):
        """ Returns path from v to goal in g as a string (Hack) """
        explored.add(start)
        if start == goal:
            return path_so_far + start
        for w in self.v.setdefault(start,[]):
            if w not in explored:
                p = self.DFS(w, goal, explored, path_so_far + start)
                if p:
                    return p

        return ""