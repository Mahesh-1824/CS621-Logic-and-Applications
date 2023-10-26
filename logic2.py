from z3 import *

def create_coloring_solver(vertices, edges, num_colors):
    solver = Solver()
    colors = {v: Int(f"{v}_color") for v in vertices}
    
    for v in vertices:
        solver.add(And(colors[v] >= 1, colors[v] <= num_colors))
    
    for u, v in edges:
        solver.add(colors[u] != colors[v])
    
    return solver, colors

def find_graph_coloring(vertices, edges):
    num_vertices = len(vertices)
    num_colors_used = 1
    soln = None
    
    while not soln:
        solver, colors = create_coloring_solver(vertices, edges, num_colors_used)
        if solver.check() == sat:
            model = solver.model()
            num_colors = {v: model[colors[v]].as_long() for v in vertices}
            min_colors_used = len(set(num_colors.values()))
            if min_colors_used <= num_colors_used:
                soln = num_colors
        else:
            num_colors_used += 1
            if num_colors_used > num_vertices:
                break
    
    return soln

def main(input_file):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()
            vertices = lines[0].split()
            edges = [tuple(line.split()) for line in lines[1:]]
    except FileNotFoundError:
        print(f"Input file '{input_file}' not found.")
        return

    coloring = find_graph_coloring(vertices, edges)
    
    if coloring:
        print(f"Total number of colors required in a valid coloring of G: {max(coloring.values())}")
        print("A valid assignment of colors to all vertices in V:")
        for v, color in coloring.items():
            print(f"{v} : {color}")
    else:
        print("No valid coloring exists.")

if __name__ == "__main__":
    input_file = "2.txt" 
    main(input_file)
