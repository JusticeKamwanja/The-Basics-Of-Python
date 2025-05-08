def pet_description(animal_type, pet_name):
    if (animal_type[0].lower() == 'a' or
        animal_type[0].lower() == 'e' or
        animal_type[0].lower() == 'i' or
        animal_type[0].lower() == 'o' or
        animal_type[0].lower() == 'u'):
        article  = 'an'
    else:
        article = 'a'

    print(f'I have {article} {animal_type.lower()}.')
    print(f"My {animal_type.lower()}'s name is {pet_name.title()}. \n")

print('sfdgssf')
pet_description('hamster', 'michael')
pet_description('armadillo', 'maria')
pet_description(pet_name= 'peter', animal_type= 'weasel' )