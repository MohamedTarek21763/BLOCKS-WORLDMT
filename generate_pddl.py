import json

# Load JSON file
with open("random_blocks.json", "r") as f:
    data = json.load(f)

# Extract block objects
blocks = list(data["blocks"].keys())

# Create domain PDDL
domain_pddl = f"""(define (domain blocks)
  (:requirements :strips :typing)
  (:types block)
  (:predicates
    (on ?x ?y - block)
    (on-table ?x - block)
    (clear ?x - block)
    (big ?x - block)
    (small ?x - block)
  )
  (:action stack
    :parameters (?x ?y - block)
    :precondition (and (clear ?x) (clear ?y) (on-table ?x))
    :effect (and (not (clear ?x)) (not (on-table ?x)) (on ?x ?y) (clear ?y))
  )
  (:action unstack
    :parameters (?x ?y - block)
    :precondition (and (on ?x ?y) (clear ?x))
    :effect (and (clear ?y) (on-table ?x) (not (on ?x ?y)) (not (clear ?x)))
  )
)
"""

# Create problem PDDL
problem_pddl = f"""(define (problem blocks-problem)
  (:domain blocks)
  (:objects {" ".join(blocks)} - block)
  (:init
"""

# Add block properties (big, small)
for block, size in data["blocks"].items():
    problem_pddl += f"    ({size} {block})\n"

# Add relationships
for condition in data["init"]:
    for key, value in condition.items():
        if isinstance(value, list):
            problem_pddl += f"    ({key} {value[0]} {value[1]})\n"
        else:
            problem_pddl += f"    ({key} {value})\n"

problem_pddl += "  )\n  (:goal (and\n"

# Add goal conditions
for condition in data["goal"]:
    for key, value in condition.items():
        if isinstance(value, list):
            problem_pddl += f"    ({key} {value[0]} {value[1]})\n"
        else:
            problem_pddl += f"    ({key} {value})\n"

problem_pddl += "  ))\n)"

# Save files
with open("blocks_domain.pddl", "w") as f:
    f.write(domain_pddl)

with open("blocks_problem.pddl", "w") as f:
    f.write(problem_pddl)

print("✅ PDDL files generated successfully!")
