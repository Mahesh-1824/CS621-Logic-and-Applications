from z3 import *

def read_input(file_path):
    with open(file_path, 'r') as input_file:
        return [line.split() for line in input_file]

def solve_scheduling(data):
    dlen=len(data)
    persons = []
    for i in range(len(data)):
        persons.append(f'{i}')
    timeslots = {}
    for i in persons:
        timeslots[i] = Int(i)
    solver = Solver()


    for i in range(len(persons)):
        solver.add(And(timeslots[persons[i]] >= 0, timeslots[persons[i]] < len(data)))

        for j in range(dlen):
            if data[i][j] == '0':
                solver.add(timeslots[persons[i]] != j)

    for i in persons:
        for j in persons:
            if i != j:
                solver.add(timeslots[i] != timeslots[j])

    unique_solutions = set()

    while solver.check() == sat:
        model = solver.model()
        assign = {}
        for i in persons:
            assign[i] = model[timeslots[i]].as_long()


        unique_solutions.add(tuple(sorted([(i, assign[i]) for i in persons])))

        solver.add(Or([timeslots[i] != assign[i] for i in assign]))

    return unique_solutions

if __name__ == "__main__":
    input_file_path = "3.txt"
    data = read_input(input_file_path)
    solutions = solve_scheduling(data)

    for index, solution in enumerate(solutions):
        print(f"Schedule {index + 1}:")
        for (i, j) in solution:
            print(f"Time Slot {i} -> person {j}")
        print()
    print(f"Number of possible schedules: {len(solutions)}")
