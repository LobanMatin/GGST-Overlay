from converter.converter import move_to_img


def combo_to_img(combo_string, canvas):
    combo = combo_string.split(" > ")

    for move in combo:
        move_to_img(move, canvas)
