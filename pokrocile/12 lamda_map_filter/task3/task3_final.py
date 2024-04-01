def add_initials(people):
    add_initials_to_person = lambda person: {**person, "initials": person["name"][:1] + person["surname"][:1]}
    people_with_initials = map(add_initials_to_person, people)

    return list(people_with_initials)
