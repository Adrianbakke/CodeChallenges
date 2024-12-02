import networkx as nx

def parse_input(input_text):
    G = nx.Graph()
    for line in input_text.strip().split('\n'):
        if not line.strip():
            continue
        node, neighbors_str = line.strip().split(':')
        node = node.strip()
        neighbors = neighbors_str.strip().split()
        for neighbor in neighbors:
            G.add_edge(node, neighbor)


    return G

def main():
    input_text = """
    jqt: rhn xhk nvd
    rsh: frs pzl lsr
    xhk: hfx
    cmg: qnr nvd lhk bvb
    rhn: xhk bvb hfx
    bvb: xhk hfx
    pzl: lsr hfx nvd
    qnr: nvd
    ntq: jqt hfx bvb xhk
    nvd: lhk
    lsr: lhk
    rzs: qnr cmg lsr rsh
    frs: qnr lhk lsr
    """
    #input_text = open("input.txt", "r").read()
    G = parse_input(input_text)

    # Find the minimum edge cut
    min_cut_edges = nx.minimum_edge_cut(G)
    min_cut_size = len(min_cut_edges)
    print(f"Minimum edge cut size: {min_cut_size}")
    print(f"Edges to disconnect: {min_cut_edges}")

    # Since we need to disconnect the graph by removing exactly 3 edges
    if min_cut_size == 3:
        G_copy = G.copy()
        G_copy.remove_edges_from(min_cut_edges)
        components = list(nx.connected_components(G_copy))
        if len(components) == 2:
            sizes = [len(component) for component in components]
            product = sizes[0] * sizes[1]
            print(f"The product of the sizes of the two components is: {product}")
        else:
            print("Graph is not divided into exactly two components after removing the edges.")
    else:
        print("Could not find a cut of size 3.")

if __name__ == "__main__":
    main()
