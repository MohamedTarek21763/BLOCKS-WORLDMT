# Initialize world state
world_state = {
    "table": {"A": "on table", "B": "on table", "C": "on table"},  # Blocks on the table as a dictionary
    "agent1": {"holding": None},  # Agent1 is not holding any block initially
    "agent2": {"holding": None}   # Agent2 is not holding any block initially
}

# Function to print the world state
def print_world_state(world_state):
    print("Current world state:")
    
    # Iterate over the blocks on the table (which is now a dictionary)
    for block, position in world_state["table"].items():
        print(f"Block {block}: {position}")
    
    # Display agents' current holding state
    print(f"Agent1 holding: {world_state['agent1']['holding']}")
    print(f"Agent2 holding: {world_state['agent2']['holding']}")
    print("-" * 30)

# Function to simulate an agent picking up a block
def pick_up(agent, block, world_state):
    if world_state["table"].get(block) == "on table" and world_state[agent]["holding"] is None:
        # The block is on the table, and the agent is not holding anything
        world_state["table"][block] = f"{block} picked up"
        world_state[agent]["holding"] = block
        print(f"{agent} picks up {block}")
        print_world_state(world_state)

# Function to simulate an agent stacking a block on another block
def stack(agent, block, target_block, world_state):
    if world_state[agent]["holding"] == block:
        # The agent is holding the block, and the target block is on the table
        if world_state["table"].get(target_block) == "on table":
            # Stack the block onto the target block
            world_state[agent]["holding"] = None
            world_state["table"][block] = f"{block} on {target_block}"
            print(f"{agent} stacks {block} on {target_block}")
            print_world_state(world_state)

# Simulating the actions
print("Initial world state:")
print_world_state(world_state)

# Simulate Agent1 picking up block A
pick_up("agent1", "A", world_state)

# Simulate Agent1 stacking block A on B
stack("agent1", "A", "B", world_state)

# Simulate Agent2 picking up block C
pick_up("agent2", "C", world_state)

# Simulate Agent2 stacking block C on A
stack("agent2", "C", "A", world_state)
