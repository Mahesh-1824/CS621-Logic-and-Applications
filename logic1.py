from collections import deque

# Define the jug capacities and the goal
max_x = 8
max_y = 5
max_z = 3
goal = (4, 4, 0)

# Define possible transitions
def transitions(x, y, z):
    next_states = []

    # Pour from x to y
    if x > 0 and y < max_y:
        pour = min(x, max_y - y)
        next_states.append((x - pour, y + pour, z, f"transfer from A to B: {pour}"))

    # Pour from x to z
    if x > 0 and z < max_z:
        pour = min(x, max_z - z)
        next_states.append((x - pour, y, z + pour, f"transfer from A to C: {pour}"))

    # Pour from y to x
    if y > 0 and x < max_x:
        pour = min(y, max_x - x)
        next_states.append((x + pour, y - pour, z, f"transfer from B to A: {pour}"))

    # Pour from y to z
    if y > 0 and z < max_z:
        pour = min(y, max_z - z)
        next_states.append((x, y - pour, z + pour, f"transfer from B to C: {pour}"))

    # Pour from z to x
    if z > 0 and x < max_x:
        pour = min(z, max_x - x)
        next_states.append((x + pour, y, z - pour, f"transfer from C to A: {pour}"))

    # Pour from z to y
    if z > 0 and y < max_y:
        pour = min(z, max_y - y)
        next_states.append((x, y + pour, z - pour, f"transfer from C to B: {pour}"))

    return next_states

# Print the state in the desired format
def print_state(step, state, transfer_info):
    a, b, c, transfer = state
    print(f"step {step}: A:{a} B:{b} C:{c}")
    if transfer:
        print(transfer)

# BFS for state space exploration
def bfs():
    visited = set()
    queue = deque()

    initial_state = (8, 0, 0, "")
    queue.append((initial_state, [initial_state]))

    step = 0

    while queue:
        current_state, steps = queue.popleft()
        x, y, z, transfer_info = current_state

        if (x, y, z) == goal:
            for state in steps:
                print_state(step, state, transfer_info)
                step += 1
            return len(steps) - 1

        for next_state in transitions(x, y, z):
            if next_state[:3] not in visited:
                visited.add(next_state[:3])
                new_steps = steps + [next_state]
                queue.append((next_state, new_steps))

    return -1  # If no solution

if __name__ == "__main__":
    print("Minimum steps to reach the goal:", bfs())
