import json

def convert(json_file="blocks_problem.json", pddl_file="blocks_problem.pddl"):
    with open(json_file) as f:
        problem = json.load(f)
    
    init = []
    # Add size predicates
    for b in problem["blocks"]:
        init.append(f"({b['size']} {b['name']})")
    # Add initial state
    for item in problem["initial"]["ontable"]:
        init.append(f"(ontable {item})")
    for item in problem["initial"]["clear"]:
        init.append(f"(clear {item})")
    init.append("(handempty)")

    # Build goal
    goal = [f"(on {pair[0]} {pair[1]})" for pair in problem["goal"]["on"]]

    pddl = f"""(define (problem blocks-problem)
  (:domain blocks)
  (:objects {" ".join(b["name"] for b in problem["blocks"])} - block)
  (:init {" ".join(init)})
  (:goal (and {" ".join(goal)}))
)"""

    with open(pddl_file, "w") as f:
        f.write(pddl)

if __name__ == "__main__":
    convert()