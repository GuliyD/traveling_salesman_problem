import math
from collections import deque


class Graph:
    def __init__(self):
        self.graph = []
        self.path = None
        self.distance = 0

    def count_metric_distance_for_all(self):
        for i in range(len(self.graph)):
            self.graph[i]['distances'] = {}
            for j in self.graph[i]['links']:
                coordinatesI = self.graph[i]['coordinates']
                coordinatesJ = self.graph[j]['coordinates']
                x = coordinatesI[0] - coordinatesJ[0]
                y = coordinatesI[1] - coordinatesJ[1]
                distance = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
                self.graph[i]['distances'][j] = distance

    def add_point_metric(self, x, y):
        self.graph.append({'coordinates': [x, y]})

    def add_links_to_all(self):
        for i in range(len(self.graph)):
            self.graph[i]['links'] = []
            for j in range(len(self.graph)):
                self.graph[i]['links'].append(j)
            del self.graph[i]['links'][i]

    def build_minimum_spanning_tree(self, index_of_start_point):
        points = [index_of_start_point]
        edges = []
        while not len(points) == len(self.graph):
            min_edge_distance = None
            for point in points:
                for link in self.graph[point]['links']:
                    if link in points:
                        continue
                    if not min_edge_distance:
                        min_edge_distance = self.graph[point]['distances'][link]
                        min_point = point
                        min_link = link
                    elif self.graph[point]['distances'][link] < min_edge_distance:
                        min_edge_distance = self.graph[point]['distances'][link]
                        min_point = point
                        min_link = link
            edges.append([min_point, min_link])
            points.append(min_link)
        for point in self.graph:
            point['links'] = []
        for edge in edges:
            self.graph[edge[0]]['links'].append(edge[1])
            self.graph[edge[1]]['links'].append(edge[0])



    def deep_first_search_for_path_for_sales_man(self, start_index):
        path = [start_index]
        queue = deque([start_index])
        while not len(path) == len(self.graph):
            can_go = []

            for link in self.graph[queue[-1]]['links']:
                if not link in path:
                    can_go.append(link)
            if can_go:
                min_go = self.graph[queue[-1]]['distances'][can_go[0]]
                index_to_go = can_go[0]
                for go in can_go:
                    if self.graph[queue[-1]]['distances'][go] < min_go:
                        min_go = self.graph[queue[-1]]['distances'][go]
                        index_to_go = go

                queue.append(index_to_go)
                path.append(index_to_go)


            else:
                queue.pop()
        path.append(start_index)
        self.path = path

    def find_distance(self):
        distance = 0
        for i in range(len(self.path)-1):
            distance += self.graph[self.path[i]]['distances'][self.path[i+1]]
        self.distance = distance


    def documentation(self):
        print(f"{self.graph[self.path[0]]['coordinates']} ", end='')
        for i in range(len(self.path)-1):
            print(f"> {self.graph[self.path[i+1]]['coordinates']} ", end='')

        [print() for i in range(2)]

        print(f'{self.distance} = ', end='')
        for i in range(len(self.path)-2):
            print(f"{self.graph[self.path[i]]['distances'][self.path[i+1]]} +", end='')
            j = i
        print(f"{self.graph[self.path[j+1]]['distances'][self.path[j+2]]}")


if __name__ == '__main__':
    while 1:
        g = Graph()
        how_many_nodes = int(input('How many nodes will be in graph>>>'))
        if how_many_nodes < 2:
            print("error: can't be less that 2 nodes")
            continue
        print('Syntax for input node:x y. Like>>>2 1')
        for i in range(how_many_nodes):
            node = input('Input please node>>>').split()
            g.add_point_metric(float(node[0]), float(node[1]))
        g.add_links_to_all()
        g.count_metric_distance_for_all()
        print('Where to start?')
        index = 1
        for i in g.graph:
            print(f"{index}: {i['coordinates']}")
            index+=1
        start = int(input('>>>'))-1
        g.build_minimum_spanning_tree(start)
        g.deep_first_search_for_path_for_sales_man(start)
        g.find_distance()
        g.documentation()
        print('end')
        [print() for i in range(2)]