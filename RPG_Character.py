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

    if any(x < 1 for x in stats):
        return "All stats should be no less than 1"
        
    if not all(x <= 4 for x in stats):
        return "All stats should be no more than 4"

    if sum(stats) != 7:
        return "The character should start with 7 points"
        
    else:
        return f"{create_character}\nSTR {full_dot * strength + empty_dot * (10 - strength)}\nINT {full_dot * intelligence + empty_dot * (10 - intelligence)}\nCHA {full_dot * charisma + empty_dot * (10 - charisma)}"

create_character("Maincoon", 3, 2, 2)
    if not all(x == 7 for x in stats):
        return None
    else: 
        print(create_character, "\n", "STR", "\n", "INT", "\n", "CHA")
