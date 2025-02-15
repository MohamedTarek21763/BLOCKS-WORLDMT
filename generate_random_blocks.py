import random
import json

def generate_random_blocks():
    blocks = ['a', 'b', 'c', 'd', 'x', 'y', 'z']
    sizes = ['big', 'small']
    random.shuffle(blocks)

    state = {
        "blocks": {},   # Stores size of each block
        "init": [],     # Initial state conditions
        "goal": []      # Goal state conditions
    }

    # Assign each block a random size
    for block in blocks:
        state["blocks"][block] = random.choice(sizes)

    # Randomly arrange blocks: some on the table, some stacked
    on_table = set(blocks)  # Initially, assume all are on the table
    clear_blocks = set(blocks)  # Initially, all are clear

    stack_probability = 0.5  # 50% chance a block is stacked
    for block in blocks:
        if random.random() < stack_probability and len(on_table) > 1:
            below = random.choice(list(on_table - {block}))  # Pick another block
            state["init"].append({"on": [block, below]})  # block is on below
            on_table.discard(block)  # It’s no longer on the table
            clear_blocks.discard(below)  # The below block is no longer clear

    # Mark remaining blocks as on-table
    for block in on_table:
        state["init"].append({"on-table": block})

    # Mark remaining clear blocks
    for block in clear_blocks:
        state["init"].append({"clear": block})

    # Assign random goal state (two stacked blocks)
    goal_blocks = random.sample(blocks, 2)
    state["goal"].append({"on": goal_blocks})

    return state

# Generate and save the JSON
random_state = generate_random_blocks()
with open('random_blocks.json', 'w') as f:
    json.dump(random_state, f, indent=4)

print("✅ Random blocks JSON generated!")
