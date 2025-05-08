# Start with some designs that need to be printed.
unprinted_designs = ['iPhone case', 'Robot pendant', 'Chair', 'Dodecahedron']
completed_models = []

# Simulate printing each design, until none is left.
# Move each design to completed_models after printing.

while unprinted_designs:
    current_design = unprinted_designs.pop()

    # Simulate creating a 3D model from the design.
    print(f'\nPrinting model: {current_design}')
    completed_models.append (current_design)

print('\n')

# Design all completed models.
print('\nThe following models have been printed: \n')
model_number = 0
for completed_model in completed_models:
    model_number += 1
    print(f'\t{model_number}. {completed_model}')
print('\n')