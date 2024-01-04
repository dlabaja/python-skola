from game_objects import *

black = "\u001b[30m"
red = "\u001b[1;31m"
green = "\u001b[1;92m"
yellow = "\u001b[1;93m"
blue = "\u001b[34m"
gray = "\u001b[38;2;87;85;85m"
bold = "\u001b[1m"
reset_style = "\u001b[0m"

def print_map(fields, players, row_count):
    map = ""
    column_count = len(fields) // row_count
    for i in range(row_count):
        map += generate_row(fields[-column_count:], players)
        fields = fields[:len(fields) - column_count]

    print(format_map(map))

def generate_row(fields, players):
    map = ""
    generated_fields = []
    for field in fields:
        generated_fields.append(generate_field(field, players))

    for i in range(len(generated_fields[0])):
        for array in generated_fields:
            map += array[i]
        map += "\n"

    return map

def format_map(map):
    #  jednoduché ohraničení sloupců místo dvojitého
    map = map.replace("╋╋", "╋")
    map = map.replace("┃┃", "┃")

    lines = map.split('\n')

    # replace top line
    lines[0] = lines[0].replace("╋", "┳")

    # replace top corners
    chars = list(lines[0])
    chars[0] = "┏"
    chars[len(chars) - 1] = "┓"
    lines[0] = "".join(chars)

    # add and modify bottom line
    lines[-1] = lines[0]
    lines[-1] = lines[-1].replace("┳", "┻")

    # replace bottom corners
    chars = list(lines[-1])
    chars[0] = "┗"
    chars[len(chars) - 1] = "┛"
    lines[-1] = "".join(chars)

    map = '\n'.join(lines)

    # replace vertical connectors on map edges
    map = map.replace("╋\n", "┫\n")
    map = map.replace("┃\n╋", "┃\n┣")

    return map

def generate_field(field: Field, players):
    rendered_index = '{:<3}'.format(field.index + 1)
    rendered_teleport_index = '{:<3}'.format(field.teleport_index + 1)
    field_type = " "

    if rendered_index == rendered_teleport_index:
        rendered_teleport_index = "   "
    else:
        if type(field) == Ladder:
            field_type = f"{bold}{green}L{reset_style}"
        elif type(field) == Snake:
            field_type = f"{bold}{red}S{reset_style}"

    rendered_players = ""
    for player in players:
        if player.position == field.index:
            rendered_players += player.name[0].upper()

    return ["╋━━━━━━━╋", f"┃{yellow}{'{:<7}'.format(rendered_players)}{reset_style}┃",
            f"┃{rendered_index}{field_type}{rendered_teleport_index}┃"]
