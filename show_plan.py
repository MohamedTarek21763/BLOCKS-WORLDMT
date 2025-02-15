# Read the plan output from pyperplan
with open("plan_output.txt", "r") as file:
    plan_steps = file.readlines()

# Print each step with clear formatting
print("\n### Block Stacking Plan ###\n")
for i, step in enumerate(plan_steps, start=1):
    step = step.strip()
    if step:
        print(f"Step {i}: {step}")

print("\n### End of Plan ###\n")
