def parse_line(graph, line):
    a, _, b, _, distance = line.split()
    if a not in graph:
        graph[a] = {}
    if b not in graph:
        graph[b] = {}
    graph[a][b] = int(distance)
    graph[b][a] = int(distance)


def traverse(graph, all_locations):
    for a in graph:
        yield from _traverse(graph, all_locations, (a,), a, 0)


def _traverse(graph, all_locations, visited, a, total_distance):
    if len(visited) == len(all_locations):
        yield visited, total_distance

    for b, distance in graph[a].items():
        if b not in visited:
            yield from _traverse(
                graph,
                all_locations,
                visited + (b,),
                b,
                total_distance + distance,
            )


def get_all_locations(graph):
    locations = set()
    for a, bs in graph.items():
        locations.add(a)
        for b in bs:
            locations.add(b)
    return locations


def make_graph(lines):
    graph = {}
    for line in lines:
        parse_line(graph, line)
    return graph


if __name__ == '__main__':
    with open('input.txt') as f:
        graph = make_graph(f.read().splitlines())

    sorted_routes = sorted(
        traverse(graph, get_all_locations(graph)),
        key=lambda x: x[1]
    )
    print(sorted_routes[0][1])

