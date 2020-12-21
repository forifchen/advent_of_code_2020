import sys
import re
from maxflow import Graph

def solve():
    dishes = fetch_dishes()
    matrix_graph, ingredient_inverse_map, allergen_inverse_map = build_graph(dishes)
    maxflow_graph = Graph(matrix_graph) 
    source, sink = 0, 1
    maxflow_graph.FordFulkerson(source, sink)

    matching = dict()
    for ingredient_id, is_present in enumerate(maxflow_graph.graph[sink]):
        if is_present:
            for allergen_id, is_matching_allergen in enumerate(maxflow_graph.graph[ingredient_id]):
                if is_matching_allergen:
                    matching[ingredient_inverse_map[ingredient_id]] = allergen_inverse_map[allergen_id]
                    break


    sorted_ingredients = sorted(matching.keys(), key=lambda ingredient: matching[ingredient])
    return ",".join(sorted_ingredients)

def build_graph(dishes):
    ingredient_map = dict()
    allergen_map = dict()
    ingredient_id = 0
    allergen_id = 0
    for ingredient_list, allergen_list in dishes:
        for ingredient in ingredient_list:
            if ingredient not in ingredient_map:
                ingredient_map[ingredient] = ingredient_id
                ingredient_id += 1

        for allergen in allergen_list:
            if allergen not in allergen_map:
                allergen_map[allergen] = allergen_id
                allergen_id += 1

    source = 0
    sink = 1
    ingredient_count = ingredient_id
    allergen_count = allergen_id
    graph = [[] for _ in range(ingredient_count + allergen_count + 2)]
    for allergen in allergen_map.keys():
        allergen_map[allergen] += 2
        graph[source].append(allergen_map[allergen])
    for ingredient in ingredient_map.keys():
        ingredient_map[ingredient] += 2 + allergen_count
        graph[ingredient_map[ingredient]].append(sink)

    for allergen in allergen_map.keys():
        candidates = []
        for ingredient_list, allergen_list in dishes:
            if allergen in allergen_list:
                candidates.append(ingredient_list) 
        for ingredient in ingredient_map.keys():
            is_on_intersection = True
            for ingredient_list in candidates:
                if ingredient not in ingredient_list:
                    is_on_intersection = False
            if is_on_intersection:
                u = allergen_map[allergen]
                v = ingredient_map[ingredient]
                graph[u].append(v)

    matrix_graph = [[0 for _ in range(len(graph))] for _ in range(len(graph))]
    for row_id, row in enumerate(graph):
        for col_id in row:
            matrix_graph[row_id][col_id] = 1
    return matrix_graph, build_inverse_map(ingredient_map), build_inverse_map(allergen_map)

def build_inverse_map(generic_map):
    inverse_map = dict()
    for key, value in generic_map.items():
        inverse_map[value] = key
    return inverse_map

def fetch_dishes():
    lines = read_lines()
    return [build_dish(line.strip()) for line in lines]

def build_dish(line):
    match = re.search("^(.*) \(contains (.*)\)$", line)
    ingredients = match.group(1).split(" ")
    allergens = match.group(2).split(", ")
    return [ingredients, allergens]


def read_lines():
    filename = "simple_input.txt" if sys.argv[1] == "simple" else "input.txt"
    with open(filename, "r") as file:
        return file.readlines()

print(solve())

