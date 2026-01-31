full_dot = '●'
empty_dot = '○'


def create_character(character_name, strength, intelligence, charisma):

stats = (strength, intelligence, charisma)

    character_name.str = 

if not character_name:
    print("The Character should have a name")
    return None 

if len(character_name) > 10:
print("The character name is too long")
return None 

if ' ' in character_name:
    print("The character name should not contain spaces")
    return None

strength = int(strength)
intelligence = int(intelligence)
charisma = int(charisma)

if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
    return None

if not all(x <= 4 for x in [strength, intelligence, charisma]):
    return None

if not all(x == 7 for x in stats):
    return None
else None
