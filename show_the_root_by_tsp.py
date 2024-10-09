import random
import networkx as nx
import matplotlib.pyplot as plt

def generate_graph(num_nodes):
    G= nx.complete_graph(num_nodes)
    n=num_nodes
    for u,v in G.edges():
        print(u,"and",v)
        weight=int(input())
        G.edges[u,v]['weight']=weight

    return G

def plot_graph_step(G,delivery,curr_node,pos):
    plt.clf()
    nx.draw(G,pos,with_labels=True,node_color="blue",node_size=500)
    path_edges=list(zip(delivery,delivery[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
    nx.draw_networkx_nodes(G, pos, nodelist=[curr_node], node_color='green', node_size=500)

    edge_level=nx.get_edge_attributes(G, name='weights')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_level)

    plt.pause(5)

def calculate_delivery_cost(G,delivery):
    return sum(G[delivery[i]][delivery[i+1]]['weight'] for i in range(len(delivery)-1))

def nearest_neighbor_tsp(G,start_node):
    pos=nx.spring_layout(G)
    plt.ion()
    plt.show()

    unvisited=set(G.nodes)
    unvisited.remove(start_node)
    delivery=[start_node]
    curr_node=start_node

    plot_graph_step(G,delivery,curr_node,pos)

    while unvisited:
        next_node=min(unvisited,key=lambda node:G[curr_node][node]['weight'])
        unvisited.remove(next_node)
        delivery.append(next_node)
        curr_node=next_node
        plot_graph_step(G,delivery,curr_node,pos)
    
    delivery.append(start_node)
    plot_graph_step(G,delivery,curr_node,pos)
    print(delivery)
    delivery_cost=calculate_delivery_cost(G,delivery)
    print(f'Heuristic delivery cost:{delivery_cost}')
    plt.ioff()
    plt.show()

if __name__== '__main__':
    n=int(input("Enter number of delivery point:"))
    G=generate_graph(n)
    start_node=int(input("Enter starting delivery point:"))
    nearest_neighbor_tsp(G,start_node)
