from a import generate_routes, make_graph


def can_visit(visited, node):
    if node == 'start':
        return False
    if node not in visited or node.isupper():
        return True
    small_nodes = [_node for _node in visited if _node.islower()]
    if len(set(small_nodes)) == len(small_nodes):
        return True
    return False


if __name__ == '__main__':
    with open('input.txt') as f:
        graph = make_graph(f.read().splitlines())

    print(len(list(generate_routes(graph, can_visit))))

