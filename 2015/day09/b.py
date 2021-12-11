from a import make_graph, get_all_locations, traverse


if __name__ == '__main__':
    with open('input.txt') as f:
        graph = make_graph(f.read().splitlines())

    sorted_routes = sorted(
        traverse(graph, get_all_locations(graph)),
        key=lambda x: x[1]
    )
    print(sorted_routes[-1][1])

