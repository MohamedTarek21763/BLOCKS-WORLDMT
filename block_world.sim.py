class Agent:
    def __init__(self, name):
        self.name = name
        self.holding = None

    def pick_up(self, block, world_state):
        if block in world_state["table"]:
            self.holding = block
            world_state["table"].remove(block)
            print(f"{self.name} picks up {block}")
        else:
            print(f"{self.name} cannot pick up {block} (not on the table)")

    def stack(self, block, target, world_state):
        if self.holding == block:
            world_state["table"].remove(target)
            world_state["table"].append(block)
            self.holding = None
            print(f"{self.name} stacks {block} on {target}")
        else:
            print(f"{self.name} cannot stack {block} (not holding it)")

    def __str__(self):
        return f"{self.name} holding: {self.holding}"

def print_world_state(world_state):
    print("\nCurrent world state:")
    for block, position in world_state["table"].items():
        print(f"Block {block} is on {position}")
    print(f"Agent1 holding: {agent1.holding}")
    print(f"Agent2 holding: {agent2.holding}")
    print("------------------------------")

# Initial world state and agent setup
world_state = {
    "table": ["A", "B", "C"]
}

agent1 = Agent("Agent1")
agent2 = Agent("Agent2")

# Run actions
agent1.pick_up("A", world_state)
print_world_state(world_state)

agent1.stack("A", "B", world_state)
print_world_state(world_state)

agent2.pick_up("C", world_state)
print_world_state(world_state)

agent2.stack("C", "A", world_state)
print_world_state(world_state)