full_dot = '●'
empty_dot = '○'


def create_character(create_character, strength, intelligence, charisma):

    stats = (strength, intelligence, charisma)
    
    if not isinstance(create_character, str):
        return "The character name should be a string"
        
    if ' ' in create_character:
        return "The character name should not contain spaces"

    if not create_character:
        return "The character should have a name"

    if len(create_character) > 10:
        return "The character name is too long"
    
    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return "All stats should be integers"
    
    if not all(x <= 4 for x in [strength, intelligence, charisma]):
        return None
    
    if not all(x == 7 for x in stats):
        return None
    else: 
        print(create_character, "\n", "STR", "\n", "INT", "\n", "CHA")
