import tkinter as tk
from PIL import ImageTk, Image

# Load Images
DIM = 25
p_img = Image.open("converter/GGST Moves/P.png").resize((DIM, DIM), Image.LANCZOS)
k_img = Image.open("converter/GGST Moves/K.png").resize((DIM, DIM), Image.LANCZOS)
s_img = Image.open("converter/GGST Moves/S.png").resize((DIM, DIM), Image.LANCZOS)
h_img = Image.open("converter/GGST Moves/H.png").resize((DIM, DIM), Image.LANCZOS)
d_img = Image.open("converter/GGST Moves/D.png").resize((DIM, DIM), Image.LANCZOS)

one_img = Image.open("converter/GGST Moves/one.png").resize((DIM, DIM), Image.LANCZOS)
two_img = Image.open("converter/GGST Moves/two.png").resize((DIM, DIM), Image.LANCZOS)
three_img = Image.open("converter/GGST Moves/three.png").resize((DIM, DIM), Image.LANCZOS)
four_img = Image.open("converter/GGST Moves/four.png").resize((DIM, DIM), Image.LANCZOS)
six_img = Image.open("converter/GGST Moves/six.png").resize((DIM, DIM), Image.LANCZOS)
seven_img = Image.open("converter/GGST Moves/seven.png").resize((DIM, DIM), Image.LANCZOS)
eight_img = Image.open("converter/GGST Moves/eight.png").resize((DIM, DIM), Image.LANCZOS)
nine_img = Image.open("converter/GGST Moves/nine.png").resize((DIM, DIM), Image.LANCZOS)


# create helper function to convert move strings to images
def move_to_img(move_string, canvas):
    # define images as global
    global p_img, k_img, s_img, h_img, d_img, \
        one_img, two_img, three_img, four_img, six_img, seven_img, eight_img, nine_img

    # Load images to tkinter window
    p_img_F = ImageTk.PhotoImage(p_img, master=canvas)
    k_img_F = ImageTk.PhotoImage(k_img, master=canvas)
    s_img_F = ImageTk.PhotoImage(s_img, master=canvas)
    h_img_F = ImageTk.PhotoImage(h_img, master=canvas)
    d_img_F = ImageTk.PhotoImage(d_img, master=canvas)

    one_img_F = ImageTk.PhotoImage(one_img, master=canvas)
    two_img_F = ImageTk.PhotoImage(two_img, master=canvas)
    three_img_F = ImageTk.PhotoImage(three_img, master=canvas)
    four_img_F = ImageTk.PhotoImage(four_img, master=canvas)
    six_img_F = ImageTk.PhotoImage(six_img, master=canvas)
    seven_img_F = ImageTk.PhotoImage(seven_img, master=canvas)
    eight_img_F = ImageTk.PhotoImage(eight_img, master=canvas)
    nine_img_F = ImageTk.PhotoImage(nine_img, master=canvas)

    # use dictionaries to translate moves to images
    attack_to_img = {"P": p_img_F, "K": k_img_F, "S": s_img_F, "H": h_img_F, "D": d_img_F}

    num_to_img = {"1": one_img_F, "2": two_img_F, "3": three_img_F, "4": four_img_F, "6": six_img_F,
                  "7": seven_img_F, "j": eight_img_F, "9": nine_img_F}

    col_no = 0

    for letter in move_string:
        panel = None
        if letter in num_to_img:
            panel = tk.Label(canvas, image=num_to_img[letter])
            panel.image = num_to_img[letter]
        elif letter in attack_to_img:
            panel = tk.Label(canvas, image=attack_to_img[letter])
            panel.image = attack_to_img[letter]
        elif letter == "/":
            panel = tk.Label(canvas, text="/")
        elif letter == "]":
            panel = tk.Label(canvas, text="(Hold)")
        elif letter == "c":
            panel = tk.Label(canvas, text="(Close)")
        elif letter == "f":
            panel = tk.Label(canvas, text="(Far)")
        else:
            panel = tk.Label(canvas, text=letter)

        panel.pack(padx=5, pady=5, side="left")
        col_no += 1
    return
