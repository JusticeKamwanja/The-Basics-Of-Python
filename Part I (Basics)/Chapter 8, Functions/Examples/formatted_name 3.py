def build_person(first_name, last_name, age = ''):
    """Return a dictionary of informaton about somebody"""
    if age:
        person = {'first': first_name.title(), 'last': last_name.title(), 'age': age}
    else:
        person = {'first': first_name.title(), 'last': last_name.title()}

    return person

person_details = build_person('justice', 'kamwanja', 22)
print('\n', person_details, '\n')