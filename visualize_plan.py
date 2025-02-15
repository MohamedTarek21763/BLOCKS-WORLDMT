import re

# Initialize block positions
stacks = {}  # Tracks stacks (e.g., {1: ['A', 'B'], 2: ['C']})
on_table = set()  # Tracks blocks on the table
holding = None  # Tracks the block being moved

# Function to print the current state
def print_state():
    max_height = max(len(stack) for stack in stacks.values()) if stacks else 0
    for level in range(max_height, 0, -1):
        for stack in sorted(stacks.keys()):
            if len(stacks[stack]) >= level:
                print(f" {stacks[stack][level - 1]} ", end=" ")
            else:
                print("   ", end=" ")
        print()
    print("===" * len(stacks))
    print(" ".join([str(stack) for stack in sorted(stacks.keys())]), "\n")

# Read plan output
with open("plan_output.txt", "r") as file:
    plan_steps = file.readlines()

# Parse each step
for step in plan_steps:
    step = step.strip().lower()
    if step.startswith("(") and step.endswith(")"):
        tokens = re.findall(r"\w+", step)  # Extract words
        action = tokens[0]

        if action == "pickup":
            block = tokens[1].upper()
            holding = block
            for stack in stacks:
                if block in stacks[stack]:
                    stacks[stack].remove(block)
                    if not stacks[stack]:
                        del stacks[stack]
                    break

        elif action == "putdown":
            block = tokens[1].upper()
            holding = None
            new_stack = max(stacks.keys(), default=0) + 1
            stacks[new_stack] = [block]

        elif action == "stack":
            block = tokens[1].upper()
            target = tokens[2].upper()
            holding = None
            for stack in stacks:
                if stacks[stack][-1] == target:
                    stacks[stack].append(block)
                    break

        elif action == "unstack":
            block = tokens[1].upper()
            target = tokens[2].upper()
            holding = block
            for stack in stacks:
                if stacks[stack][-1] == block:
                    stacks[stack].remove(block)
                    if not stacks[stack]:
                        del stacks[stack]
                    break

        # Print the updated stacks after each move
        print(f"Action: {step.upper()}")
        print_state()
