def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none is left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simulate creating a 3D print from the design.
        print(f'Printing Model: {current_design}')
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all models that were printed"""
    print('\nThe following models have been printed: \n')
    model_number = 0
    for completed_model in completed_models:
        model_number += 1
        print(f'{model_number}. {completed_model}.')

unprinted_designs = ['iPhone case', 'Robot Pendant', 'Chair', 'Dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)