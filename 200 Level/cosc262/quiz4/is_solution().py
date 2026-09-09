def permutations(s):
    solutions = []
    dfs_backtrack((), s, solutions)
    return solutions


def dfs_backtrack(candidate, input_data, output_data):
    if should_prune(candidate):
        return
    if is_solution(candidate, input_data):
        add_to_output(candidate, output_data)
    else:
        for child_candidate in children(candidate, input_data):
            dfs_backtrack(child_candidate, input_data, output_data)

    
def add_to_output(candidate, output_data):
    output_data.append(candidate)

    
def should_prune(candidate):
    return False

def all_paths(adj_list, source, destination):
    solutions = []
    dfs_backtrack((source,), adj_list, destination, solutions)
    return solutions


def dfs_backtrack(candidate, adj_list, destination, output):
    if is_solution(candidate, destination):
        output.append(candidate)
    else:
        for child in children(candidate, adj_list):
            dfs_backtrack(child, adj_list, destination, output)


def is_solution(candidate, destination):
    return candidate[-1] == destination


def children(candidate, adj_list):
    last = candidate[-1]
    return [candidate + (v,) for v, *_ in adj_list[last] if v not in candidate]