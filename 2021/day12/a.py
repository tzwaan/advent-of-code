def make_graph(lines):
    graph = {}

    for line in lines:
        a, b = line.split('-')
        if a not in graph:
            graph[a] = set()
        if b not in graph:
            graph[b] = set()
        graph[a].add(b)
        graph[b].add(a)

    return graph


def generate_routes(graph, can_visit):
    yield from _generate_routes(graph, ['start'], can_visit)


def _generate_routes(graph, visited, can_visit):
    node = visited[-1]
    if node == 'end':
        yield visited
    else:
        if node in graph:
            for target in sorted(graph[node]):
                if not can_visit(visited, target):
                    continue
                yield from _generate_routes(
                    graph, visited + [target], can_visit,
                )


def can_visit(visited, node):
    if node.islower() and node in visited:
        return False
    return True


if __name__ == '__main__':
    with open('input.txt') as f:
        graph = make_graph(f.read().splitlines())

    print(len(list(generate_routes(graph, can_visit))))

