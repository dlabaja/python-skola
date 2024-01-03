import re
from game_objects import *

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
    map = map.replace("╂╂", "╂")
    map = map.replace("┃┃", "┃")

    map += map.partition("\n")[0]  # přidá spodní ohraničení

    return map

def generate_field(field: Field, players):
    rendered_index = '{:<3}'.format(field.index + 1)
    rendered_teleport_index = '{:<3}'.format(field.teleport_index + 1)
    if rendered_index == rendered_teleport_index:
        rendered_teleport_index = "   "

    field_type = ' '
    if type(field) == Ladder:
        field_type = 'L'
    elif type(field) == Snake:
        field_type = 'S'

    rendered_players = ""
    for player in players:
        if player.position == field.index:
            rendered_players += player.name[0].upper()

    return ["╂━━━━━━━╂", f"┃{'{:<7}'.format(rendered_players)}┃",
            f"┃{rendered_index}{field_type}{rendered_teleport_index}┃"]
