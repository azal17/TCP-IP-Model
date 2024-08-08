import networkx as nx
import matplotlib.pyplot as plt

def build_network_topology():

    G = nx.Graph()


    G.add_nodes_from(['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'H1', 'H2', 'S'])


    G.add_edges_from([('D1', 'H1'), ('D2', 'H1'), ('D3', 'H1'), ('D4', 'H1'), ('D5', 'H1'),
                      ('D6', 'H2'), ('D7', 'H2'), ('D8', 'H2'), ('D9', 'H2'), ('D10', 'H2'),
                      ('H1', 'S'), ('H2', 'S')])

    return G

def transmit_messages(G):
    N = int(input("Enter the number of queries: "))
    print("There are 4 collision domains and 2 broadcast domains for this topology")
    node_addresses = {}


    G.nodes['H1']['address'] = 100
    j = 1
    for neighbor in G.neighbors('H1'):
        if neighbor != 'S':
            G.nodes[neighbor]['address'] = 100 + j
            j += 1

    G.nodes['H2']['address'] = 200
    j = 1
    for neighbor in G.neighbors('H2'):
        if neighbor != 'S':
            G.nodes[neighbor]['address'] = 200 + j
            j += 1

    for i in range(N):
        sender, receiver = input("Enter the sender and receiver: ").split()
        if i == 0:
            print(f"Message broadcasted in both domains at address {node_addresses.get(sender, 'Unknown')} and {node_addresses.get(receiver, 'Unknown')}")
            node_addresses['H1'] = G.nodes['H1']['address']
            node_addresses['H2'] = G.nodes['H2']['address']
        elif G.has_edge(sender, 'H1') and G.has_edge(receiver, 'H1'):
            print(f"Message broadcasted in H1 domain at address {node_addresses.get('H1', 'Unknown')} and {node_addresses.get('H1', 'Unknown')}")
            print("There are 2 collision domains and 1 broadcast domain for this topology")
        elif G.has_edge(sender, 'H2') and G.has_edge(receiver, 'H2'):
            print(f"Message broadcasted in H2 domain at address {node_addresses.get('H2', 'Unknown')} and {node_addresses.get('H2', 'Unknown')}")
            print("There are 2 collision domains and 1 broadcast domain for this topology")
        elif G.has_edge(sender, 'H1') and G.has_edge(receiver, 'H2'):
            print(f"Message broadcasted in H1 domain at address {node_addresses.get('H1', 'Unknown')} and in H2 domain at address {node_addresses.get('H2', 'Unknown')}")
            print("There are 4 collision domains and 2 broadcast domains for this topology")
        elif G.has_edge(sender, 'H2') and G.has_edge(receiver, 'H1'):
            print(f"Message broadcasted in H2 domain at address {node_addresses.get('H2', 'Unknown')} and in H1 domain at address {node_addresses.get('H1', 'Unknown')}")
            print("There are 4 collision domains and 2 broadcast domains for this topology")

def visualize_topology(G):
    nx.draw(G, with_labels=True)
    plt.show()

def main():
    G = build_network_topology()
    transmit_messages(G)
    visualize_topology(G)

if __name__ == "__main__":
    main()
