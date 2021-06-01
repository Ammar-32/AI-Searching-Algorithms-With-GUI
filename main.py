
import nx as nx
import networkx as nx
import pylab
from Graph import Graph

from tkinter import *
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from WeightedGraph import WeightedGraph

G = Graph()
WG = WeightedGraph()


def main():
    root = Tk()
    gui = Window(root)
    gui.root.mainloop()
    return None


class Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Graph searching algorithms - AI Project ASU")
        self.root.geometry('600x550')



        # node 1
        Label(self.root, text="Node 1").grid(row=0, column=0)
        self.node1Entry = Entry(self.root, width=5)
        self.node1Entry.grid(row=0, column=1)

        # node 2
        Label(self.root, text="Node 2").grid(row=1, column=0)
        self.node2Entry = Entry(self.root, width=5)
        self.node2Entry.grid(row=1, column=1)

        # Cost
        Label(self.root, text="Cost").grid(row=0, column=2)
        self.costEntry = Entry(self.root, width=5)
        self.costEntry.grid(row=0, column=3)

        # Heauristic
        Label(self.root, text="Heuristic").grid(row=0, column=4)
        self.heuristicEntry = Entry(self.root, width=5)
        self.heuristicEntry.grid(row=0, column=5)

        # Heauristic node
        Label(self.root, text="Node").grid(row=0, column=6)
        self.heuristicNodeEntry = Entry(self.root, width=5)
        self.heuristicNodeEntry.grid(row=0, column=7)

        # Heuristic Button
        button7 = Button(self.root, text="Add Heuristic", command=self.Heuristicbtn)
        button7.grid(row=4, column=7)
        self.root.bind("<Return>", self.Heuristicbtn)

        # Start BFS
        Label(self.root, text="Start").grid(row=7, column=0)
        self.startBFSentry = Entry(self.root, width=5)
        self.startBFSentry.grid(row=7, column=1)

        # Goal BFS
        Label(self.root, text="Goal").grid(row=7, column=2)
        self.goalBFSentry = Entry(self.root, width=5)
        self.goalBFSentry.grid(row=7, column=3)

        # Output BFS
        self.my_string_var_BFS = StringVar()
        self.my_string_var_BFS.set("")
        self.outputBFS = Label(self.root, textvariable=self.my_string_var_BFS).grid(row=7, column=7)

        # Output ASTAR
        self.my_string_var_ASTAR = StringVar()
        self.my_string_var_ASTAR.set("")
        self.outputASTAR = Label(self.root, textvariable=self.my_string_var_ASTAR).grid(row=9, column=7)

        # Output GREEDY
        self.my_string_var_GREEDY = StringVar()
        self.my_string_var_GREEDY.set("")
        self.outputGREEDY = Label(self.root, textvariable=self.my_string_var_GREEDY).grid(row=10, column=7)

        # Start DFS
        Label(self.root, text="Start").grid(row=8, column=0)
        self.startDFSentry = Entry(self.root, width=5)
        self.startDFSentry.grid(row=8, column=1)

        # Goal DFS
        Label(self.root, text="Goal").grid(row=8, column=2)
        self.goalDFSentry = Entry(self.root, width=5)
        self.goalDFSentry.grid(row=8, column=3)

        # Output DFS
        self.my_string_var_DFS = StringVar()
        self.my_string_var_DFS.set("")
        self.outputDFS = Label(self.root, textvariable=self.my_string_var_DFS).grid(row=8, column=7)

        # Start A*
        Label(self.root, text="Start").grid(row=9, column=0)
        self.startASTARentry = Entry(self.root, width=5)
        self.startASTARentry.grid(row=9, column=1)

        # Goal A*
        Label(self.root, text="Goal").grid(row=9, column=2)
        self.goalASTARentry = Entry(self.root, width=5)
        self.goalASTARentry.grid(row=9, column=3)

        # Start GREEDY
        Label(self.root, text="Start").grid(row=10, column=0)
        self.startGREEDYentry = Entry(self.root, width=5)
        self.startGREEDYentry.grid(row=10, column=1)

        # Goal GREEDY
        Label(self.root, text="Goal").grid(row=10, column=2)
        self.goalGREEDYentry = Entry(self.root, width=5)
        self.goalGREEDYentry.grid(row=10, column=3)


        # Add Edge Button
        button1 = Button(self.root, text="Add Edge", command=self.addEdgebtn)
        button1.grid(row=4, column=1)
        self.root.bind("<Return>", self.addEdgebtn)

        # Add Weighted Edge Button
        button5 = Button(self.root, text="Add Weighted Edge", command=self.addWeightedEdge)
        button5.grid(row=4, column=3)
        self.root.bind("<Return>", self.addWeightedEdge)


        #BFS Button
        button2 = Button(self.root, text="BFS", command=self.BFSbtn)
        button2.grid(row=7, column=4)
        self.root.bind("<Return>", self.BFSbtn)


        #DFS Button
        button3 = Button(self.root, text="DFS", command=self.DFSbtn)
        button3.grid(row=8, column=4)
        self.root.bind("<Return>", self.DFSbtn)

        # ASTAR Button
        button6 = Button(self.root, text="A STAR", command=self.ASTARbtn)
        button6.grid(row=9, column=4)
        self.root.bind("<Return>", self.ASTARbtn)

        # GREEDY Button
        button7 = Button(self.root, text="GREEDY", command=self.GREEDYbtn)
        button7.grid(row=10, column=4)
        self.root.bind("<Return>", self.GREEDYbtn)


        # clear  Button
        button4 = Button(self.root, text="Clear", command=self.clearGraph)
        button4.grid(row=4, column= 5)
        self.root.bind("<Return>", self.clearGraph)


        pass

    def addEdgebtn(self, event=None):
        self.node1 = self.node1Entry.get()
        self.node2 = self.node2Entry.get()
        G.v.setdefault(self.node1, []).append(self.node2)
        G.addEdge(self.node1, self.node2)
        print(G.v)
        G.visualize()

    def clearGraph(self):
        G.visual=[]
        G.v={}
        WG.adjacency_list={}
        WG.heuristic = {}
        G.visualize()

    def BFSbtn(self):
        bfsTraversal = G.bfsTraverse(self.startBFSentry.get())
        str1 = ''.join(str(e) for e in bfsTraversal)
        bfsPath = G.bfsShortestPath(self.startBFSentry.get(), self.goalBFSentry.get())
        str2 = ''.join(str(e) for e in bfsPath)
        self.my_string_var_BFS.set("Traversing path : " + str1 + " Returned Path : " + str2)


    def DFSbtn(self):
       dfsPath = G.DFS(self.startDFSentry.get(), self.goalDFSentry.get(),set(), "")
       output= "             Returned Path : " + dfsPath

       self.my_string_var_DFS.set(output)

    def ASTARbtn(self):
        ASTARPATH = WG.a_star_algorithm(self.startASTARentry.get(), self.goalASTARentry.get())
        str1 = ''.join(str(e) for e in ASTARPATH)
        output = "             Returned Path : " + str1
        self.my_string_var_ASTAR.set(output)

    def addWeightedEdge(self):
        self.node1 = self.node1Entry.get()
        self.node2 = self.node2Entry.get()
        self.cost = self.costEntry.get()
        WG.adjacency_list.setdefault(self.node1,[]).append((self.node2, int(self.cost)))
        G.addEdge(self.node1, self.node2)
        G.visualize()
        print(WG.adjacency_list)

    def GREEDYbtn(self):
        GREEDYPATH = WG.GREEDY(self.startGREEDYentry.get(), self.goalGREEDYentry.get())
        str1 = ''.join(str(e) for e in GREEDYPATH)
        output = "             Returned Path : " + str1
        self.my_string_var_GREEDY.set(output)

    def Heuristicbtn(self):
        self.heuristicValue= int(self.heuristicEntry.get())
        self.heuristicNode = self.heuristicNodeEntry.get()
        WG.heuristic[self.heuristicNode] = self.heuristicValue
        print(WG.heuristic)





pass


main()