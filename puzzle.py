### Author: ŁJ
### Version 1.1
### Date: 05.09.2019

"""
BIBLIOTEKI
"""

from PIL import Image, ImageTk
from random import randint
import sounddevice as sd
import soundfile as sf
from time import sleep
import tkinter as tk


"""
ZMIENNE
"""

comment = 0 # Wyświetlać komunikaty? 0-nie / 1-tak
        
file1 = "Sounds\szur.wav"
file2 = "Sounds\klik.wav"
data1, fs1 = sf.read(file1, dtype = "float32")
data2, fs2 = sf.read(file2, dtype = "float32")


areas_3x3 = [(0, 0, 100, 100), (100, 0, 200, 100), (200, 0, 300, 100),
             (0, 100, 100, 200), (100, 100, 200, 200), (200, 100, 300, 200),
             (0, 200, 100, 300), (100, 200, 200, 300), (200, 200, 300, 300)] # wyznaczamy fragmenty, które będą kawałkami obrazka dla poziomu łatwy

areas_4x4 = [(0, 0, 100, 100), (100, 0, 200, 100), (200, 0, 300, 100), (300, 0, 400, 100),
             (0, 100, 100, 200), (100, 100, 200, 200), (200, 100, 300, 200), (300, 100, 400, 200),
             (0, 200, 100, 300), (100, 200, 200, 300), (200, 200, 300, 300), (300, 200, 400, 300),
             (0, 300, 100, 400), (100, 300, 200, 400), (200, 300, 300, 400), (300, 300, 400, 400)]

areas_5x5 = [(0, 0, 100, 100), (100, 0, 200, 100), (200, 0, 300, 100), (300, 0, 400, 100), (400, 0, 500, 100),
             (0, 100, 100, 200), (100, 100, 200, 200), (200, 100, 300, 200), (300, 100, 400, 200), (400, 100, 500, 200),
             (0, 200, 100, 300), (100, 200, 200, 300), (200, 200, 300, 300), (300, 200, 400, 300), (400, 200, 500, 300),
             (0, 300, 100, 400), (100, 300, 200, 400), (200, 300, 300, 400), (300, 300, 400, 400), (400, 300, 500, 400),
             (0, 400, 100, 500), (100, 400, 200, 500), (200, 400, 300, 500), (300, 400, 400, 500), (400, 400, 500, 500)] # wyznaczamy fragmenty, które będą kawałkami obrazka dla poziomu trudny

"""
DEFINICJE
"""


def sounds(name):
    if TheGame.sound_mode == True:
        if name == "change": sd.play(data1, fs1)
        else: sd.play(data2, fs2)

def sound():
    if TheGame.sound_mode == True:
        if comment: print("wylaczam dzwiek")
        TheGame.sound_mode = False
        for button in [button_sound_menu, button_sound_e, button_sound_m]:
            button["image"] = sound_off_gif
    else:
        if comment: print("wlaczam dzwiek")
        TheGame.sound_mode = True
        for button in [button_sound_menu, button_sound_e, button_sound_m]:
            button["image"] = sound_on_gif
    
    
def start_game(random_table, buttons, lvl):
    if comment: print("definicja start_game")
    sounds(None)
    TheGame.level = lvl
    if comment: print("klawisz START naciśnięty")
    if lvl == "easy":
        random_table = random(random_table, TheGame.ordered_table, 9)
        button_start.grid_remove()
        for i in range(9):
            buttons[i]["state"] = "normal"
            buttons[i]["image"] = random_table[i]
        steps_counter.grid(row = 4, column = 1, pady = (30, 0))
        
    elif lvl == "medium":
        random_table = random(random_table, TheGame.ordered_table, 16)
        button_start_m.grid_remove()
        for i in range(16):
            buttons[i]["state"] = "normal"
            buttons[i]["image"] = random_table[i]
        steps_counter_m.grid(row = 5, column = 1, columnspan = 2, pady = (50, 0))
        
    elif lvl == "hard":
        random_table = random(random_table, TheGame.ordered_table, 25)
        button_start_h.grid_remove()
        for i in range(25):
            buttons[i]["state"] = "normal"
            buttons[i]["image"] = random_table[i]
        steps_counter_h.grid(row = 6, column = 2, pady = (10, 0))

def open_easy(): # Ustawia grę pod tryb łatwy
    sounds(None)
    if comment: print("definicja open_easy")
    TheGame.ordered_table, TheGame.picture = filling(areas_3x3)
    TheGame.buttons = [b0, b1, b2, b3, b4, b5, b6, b7, b8]
    steps_counter.grid_remove()
    for i in range(9):
        TheGame.buttons[i]["image"] = TheGame.ordered_table[i]
        TheGame.buttons[i]["state"] = "disable"
    if comment: print("wlaczam tryb latwy")
    raise_frame(easy)

def open_medium(): # Ustawia grę pod tryb średni
    sounds(None)
    if comment: print("definicja open_medium")
    TheGame.ordered_table, TheGame.picture = filling(areas_4x4)
    TheGame.buttons = [bm0, bm1, bm2, bm3, bm4, bm5, bm6, bm7, bm8, bm9, bm10, bm11, bm12, bm13, bm14, bm15]
    steps_counter_m.grid_remove()
    for i in range(16):
        TheGame.buttons[i]["image"] = TheGame.ordered_table[i]
        TheGame.buttons[i]["state"] = "disable"
    if comment: print("wlaczam tryb latwy")
    raise_frame(medium)

def open_hard(): # Ustawia grę pod tryb trudny
    sounds(None)
    if comment: print("definicja open_hard")
    TheGame.ordered_table, TheGame.picture = filling(areas_5x5)
    TheGame.buttons = [bh0, bh1, bh2, bh3, bh4, bh5, bh6, bh7, bh8, bh9, bh10, bh11, bh12, bh13, bh14, bh15, bh16, bh17, bh18, bh19, bh20, bh21, bh22, bh23, bh24]
    steps_counter_h.grid_remove()
    for i in range(25):
        TheGame.buttons[i]["image"] = TheGame.ordered_table[i]
        TheGame.buttons[i]["state"] = "disable"
    if comment: print("wlaczam tryb trudny")
    raise_frame(hard)

# img = ImageTk.PhotoImage(Image.open("tree.gif")) # <- Tak się wgrywa zdjęcie do guzika, żeby guzik działał

def filling(area_mode):
    if comment: print("definicja filling")
    ordered_table = []
    if area_mode == areas_3x3: picture = "Pictures/tree.gif"
    elif area_mode == areas_4x4: picture = "Pictures/bird.gif"
    elif area_mode == areas_5x5: picture = "Pictures/apples.gif"
    TheGame.img = Image.open(picture) # ustawiamy "img" jako nasz obrazek
    for area in area_mode: # pętla która potnie obrazek i wrzuci kawałki do tabeli
        cropped_img = TheGame.img.crop(area)
        image = ImageTk.PhotoImage(cropped_img)
        ordered_table.append(image)
    if area_mode == areas_3x3:
        pass
    while len(ordered_table) != 25:
        ordered_table.append(empty)
    return ordered_table, picture

def reset(frame): # Resetuje wszystko, aby można było grać od nowa
    sounds(None)
    if comment: print("definicja reset")
    TheGame.steps = 0
    TheGame.random_table = []
    TheGame.ordered_table = []
    if comment: print("resetuje gre")
    TheGame.steps_msg_h.set("Ruchy: " + str(TheGame.steps))
    TheGame.steps_msg.set("Ruchy: " + str(TheGame.steps))
    if frame == "easy" or frame == None: button_start.grid(row = 4, column = 0, columnspan = 3, sticky = "news")
    elif frame == "medium" or frame == None: button_start_m.grid(row = 5, column = 0, columnspan = 4, sticky = "news")
    elif frame == "hard" or frame == None: button_start_h.grid(row = 6, column = 0, columnspan = 5, sticky = "news")
    raise_frame(menu)
    
def ifwin(): # sprawdzanie czy doszło do wygranej
    if comment: print("definicja ifwin")
    if TheGame.level == "easy":   limit = 9
    if TheGame.level == "medium": limit = 16
    if TheGame.level == "hard":   limit = 25
    count = 0
    for i in range(limit):
        if str(TheGame.buttons[i]["image"]) == str(TheGame.ordered_table[i]): count += 1
    if count == limit: return 1

def button(pressed_button): # pętla sprawdzająca, które klawisze z obrazkami zostały naciśnięte
    if comment: print("definicja button")
    TheGame.pressed.append(pressed_button)
    pressed_button["bg"] = "red"
    if len(TheGame.pressed) == 2:
        change()

def change(): # definicja zamieniające kliknięte klawisze miejscami
    if comment: print("definicja change")
    if TheGame.pressed[0] != TheGame.pressed[1]:
        sounds("change")
        TheGame.steps += 1
        if TheGame.level == "easy": TheGame.steps_msg.set("Ruchy: " + str(TheGame.steps))
        if TheGame.level == "medium": TheGame.steps_msg_m.set("Ruchy: " + str(TheGame.steps))
        if TheGame.level == "hard": TheGame.steps_msg_h.set("Ruchy: " + str(TheGame.steps))
        TheGame.pressed[0]["image"], TheGame.pressed[1]["image"] = TheGame.pressed[1]["image"], TheGame.pressed[0]["image"]
        TheGame.pressed[0]["bg"] = "white"
        TheGame.pressed[1]["bg"] = "white"
        TheGame.pressed = []
        if ifwin():
            win_steps()
            raise_frame(win)
    else:
        TheGame.pressed[0]["bg"] = "white"
        TheGame.pressed = []
    
def random(random_table, ordered_table, limit): # definicja mieszająca obrazek
    if comment: print("definicja random")
    numbers = []
    while len(numbers) != limit:
        random_nr = randint(0,limit-1)
        if not random_nr in numbers:
            numbers.append(random_nr)
            random_table.append(ordered_table[random_nr])
    return random_table

def raise_frame(frame):
    if comment: print("definicja raise_frame")
    frame.tkraise()

root = tk.Tk() # Tworzenie okna w TK
root.title("Puzzle")
root.resizable(0, 0)
window = "530x890+" + str(root.winfo_screenwidth()//2-270) + "+0"# + str(root.winfo_screenheight()//2-445)
root.geometry(window)
root.iconbitmap("Graphics/ico.ico")

menu =   tk.Frame(root) # wybór poziomu trudności
easy =   tk.Frame(root) # poziom łatwy
medium = tk.Frame(root) # poziom średni
hard =   tk.Frame(root) # poziom trudny
win =    tk.Frame(root) # wygranie gry

sound_on_gif = ImageTk.PhotoImage(Image.open("Graphics/sound_on.gif"))
sound_off_gif = ImageTk.PhotoImage(Image.open("Graphics/sound_off.gif"))

img = Image.open("Pictures/test.gif")

for frame in (menu, easy, medium, hard, win):
    frame.grid(row = 0, column = 0, sticky = "news")

empty = ImageTk.PhotoImage(Image.open("Graphics/puste.gif"))

class game():
    def __init__(self):
        self.pressed = [] # lista wciśniętych klawiszy z obrazkami
        self.random_table = [] # Tabela z wymieszanymi kawałkami obrazka
        self.buttons = [] 
        self.ordered_table = [] # Tabela, dodamy do niej kawałki obrazka w poprawnym porządku
        self.level = None # informacja o tym, na jakim poziomie trudności ktoś będzie grał
        self.sound_mode = True
        self.img = Image.open("Pictures/test.gif")

        self.steps = 0 # ilość ruchów przy układaniu obrazka
        self.steps_msg = tk.StringVar()
        self.steps_msg_m = tk.StringVar()
        self.steps_msg_h = tk.StringVar()
        
        while len(self.ordered_table) != 25:
            self.ordered_table.append(empty)
        self.empty_table = self.ordered_table[:]

TheGame = game()

"""
MENU
"""

options_info_gif = ImageTk.PhotoImage(Image.open("Graphics/info.gif"))
options_info = tk.Label(menu, image = options_info_gif)
options_info.grid(row = 0, padx = (110, 10), pady = 25)

option_1_gif = ImageTk.PhotoImage(Image.open("Graphics/opcja1.gif"))
option_1 = tk.Button(menu, image = option_1_gif, command = lambda: open_easy(), relief = "flat")
option_1.grid(row = 1, padx = (110, 10), pady = 5)

option_2_gif = ImageTk.PhotoImage(Image.open("Graphics/opcja2.gif"))
option_2 = tk.Button(menu, image = option_2_gif, command = lambda: open_medium(), relief = "flat")
option_2.grid(row = 2, padx = (110, 10), pady = 5)

option_3_gif = ImageTk.PhotoImage(Image.open("Graphics/opcja3.gif"))
option_3 = tk.Button(menu, image = option_3_gif, command = lambda: open_hard(), relief = "flat")
option_3.grid(row = 3, padx = (110, 10), pady = 5)

exit_game_image = ImageTk.PhotoImage(Image.open("Graphics/exit.gif"))
exit_game = tk.Button(menu, image = exit_game_image, command = lambda: root.destroy(), relief = "flat")
exit_game.grid(row = 4, padx = (110, 10), pady = (25, 0))

button_sound_menu = tk.Button(menu, image = sound_on_gif, command = sound)
button_sound_menu.grid(row = 4, column = 1, pady = (20, 0))

"""
EASY
"""

give_up_gif = ImageTk.PhotoImage(Image.open("Graphics/poddanie.gif"))
give_up_e = tk.Button(easy, image = give_up_gif, command = lambda: reset("easy"), relief = "flat")
give_up_e.grid(row = 0, column = 0, columnspan = 3, padx = (100, 0), pady = (30, 30))

b0 = tk.Button(easy, image = TheGame.ordered_table[0], command = lambda: button(b0), state = "disabled")
b0.grid(row = 1, column = 0, padx = (82, 0))

b1 = tk.Button(easy, image = TheGame.ordered_table[1], command = lambda: button(b1), state = "disabled")
b1.grid(row = 1, column = 1)

b2 = tk.Button(easy, image = TheGame.ordered_table[2], command = lambda: button(b2), state = "disabled")
b2.grid(row = 1, column = 2)

b3 = tk.Button(easy, image = TheGame.ordered_table[3], command = lambda: button(b3), state = "disabled")
b3.grid(row = 2, column = 0, padx = (82, 0))

b4 = tk.Button(easy, image = TheGame.ordered_table[4], command = lambda: button(b4), state = "disabled")
b4.grid(row = 2, column = 1)

b5 = tk.Button(easy, image = TheGame.ordered_table[5], command = lambda: button(b5), state = "disabled")
b5.grid(row = 2, column = 2)

b6 = tk.Button(easy, image = TheGame.ordered_table[6], command = lambda: button(b6), state = "disabled")
b6.grid(row = 3, column = 0, padx = (82, 0), pady = (0, 50))

b7 = tk.Button(easy, image = TheGame.ordered_table[7], command = lambda: button(b7), state = "disabled")
b7.grid(row = 3, column = 1, pady = (0, 50))

b8 = tk.Button(easy, image = TheGame.ordered_table[8], command = lambda: button(b8), state = "disabled")
b8.grid(row = 3, column = 2, pady = (0, 50))

button_start_gif = ImageTk.PhotoImage(Image.open("Graphics/start.gif"))
button_start = tk.Button(easy, image = button_start_gif, command = lambda: start_game(TheGame.random_table, TheGame.buttons, "easy"), relief = "flat")
button_start.grid(row = 4, column = 0, columnspan = 3, padx = (100, 0), sticky = "news")

button_sound_e = tk.Button(easy, image = sound_on_gif, command = sound)
button_sound_e.grid(row = 4, column = 3, padx = (30, 0))

steps_counter = tk.Label(easy, textvariable = TheGame.steps_msg, font = ("Comic Sans MS", 14))
TheGame.steps_msg.set("Ruchy: " + str(TheGame.steps)) # info o ruchach dla poziomu easy

"""
MEDIUM
"""

give_up_m = tk.Button(medium, image = give_up_gif, command = lambda: reset("medium"), relief = "flat")
give_up_m.grid(row = 0, column = 0, columnspan = 5, padx = (45, 0), pady = (15, 15))

bm0 = tk.Button(medium, image = TheGame.ordered_table[0], command = lambda: button(bm0), state = "disabled")
bm0.grid(row = 1, column = 0, padx = (55, 0))

bm1 = tk.Button(medium, image = TheGame.ordered_table[1], command = lambda: button(bm1), state = "disabled")
bm1.grid(row = 1, column = 1)

bm2 = tk.Button(medium, image = TheGame.ordered_table[2], command = lambda: button(bm2), state = "disabled")
bm2.grid(row = 1, column = 2)

bm3 = tk.Button(medium, image = TheGame.ordered_table[3], command = lambda: button(bm3), state = "disabled")
bm3.grid(row = 1, column = 3)

bm4 = tk.Button(medium, image = TheGame.ordered_table[4], command = lambda: button(bm4), state = "disabled")
bm4.grid(row = 2, column = 0, padx = (55, 0))

bm5 = tk.Button(medium, image = TheGame.ordered_table[5], command = lambda: button(bm5), state = "disabled")
bm5.grid(row = 2, column = 1)

bm6 = tk.Button(medium, image = TheGame.ordered_table[6], command = lambda: button(bm6), state = "disabled")
bm6.grid(row = 2, column = 2)

bm7 = tk.Button(medium, image = TheGame.ordered_table[7], command = lambda: button(bm7), state = "disabled")
bm7.grid(row = 2, column = 3)

bm8 = tk.Button(medium, image = TheGame.ordered_table[8], command = lambda: button(bm8), state = "disabled")
bm8.grid(row = 3, column = 0, padx = (55, 0))

bm9 = tk.Button(medium, image = TheGame.ordered_table[9], command = lambda: button(bm9), state = "disabled")
bm9.grid(row = 3, column = 1)

bm10 = tk.Button(medium, image = TheGame.ordered_table[10], command = lambda: button(bm10), state = "disabled")
bm10.grid(row = 3, column = 2)

bm11 = tk.Button(medium, image = TheGame.ordered_table[11], command = lambda: button(bm11), state = "disabled")
bm11.grid(row = 3, column = 3)

bm12 = tk.Button(medium, image = TheGame.ordered_table[12], command = lambda: button(bm12), state = "disabled")
bm12.grid(row = 4, column = 0, padx = (55, 0))

bm13 = tk.Button(medium, image = TheGame.ordered_table[13], command = lambda: button(bm13), state = "disabled")
bm13.grid(row = 4, column = 1)

bm14 = tk.Button(medium, image = TheGame.ordered_table[14], command = lambda: button(bm14), state = "disabled")
bm14.grid(row = 4, column = 2)

bm15 = tk.Button(medium, image = TheGame.ordered_table[15], command = lambda: button(bm15), state = "disabled")
bm15.grid(row = 4, column = 3)

button_start_m = tk.Button(medium, image = button_start_gif, command = lambda: start_game(TheGame.random_table, TheGame.buttons, "medium"), relief = "flat")
button_start_m.grid(row = 5, column = 0, columnspan = 5, padx = (50, 0), pady = (30, 0), sticky = "news")

button_sound_m = tk.Button(medium, image = sound_on_gif, command = sound)
button_sound_m.grid(row = 5, column = 3, padx = (40, 0), pady = (25, 0))

steps_counter_m = tk.Label(medium, textvariable = TheGame.steps_msg_m, font = ("Comic Sans MS", 14))
TheGame.steps_msg_m.set("Ruchy: " + str(TheGame.steps)) # info o ruchach dla poziomu medium

"""
HARD
"""

give_up_h = tk.Button(hard, image = give_up_gif, command = lambda: reset("hard"), relief = "flat")
give_up_h.grid(row = 0, column = 0, columnspan = 5, pady = (10, 10))

bh0 = tk.Button(hard, image = TheGame.ordered_table[0], command = lambda: button(bh0), state = "disabled")
bh0.grid(row = 1, column = 0)

bh1 = tk.Button(hard, image = TheGame.ordered_table[1], command = lambda: button(bh1), state = "disabled")
bh1.grid(row = 1, column = 1)

bh2 = tk.Button(hard, image = TheGame.ordered_table[2], command = lambda: button(bh2), state = "disabled")
bh2.grid(row = 1, column = 2)

bh3 = tk.Button(hard, image = TheGame.ordered_table[3], command = lambda: button(bh3), state = "disabled")
bh3.grid(row = 1, column = 3)

bh4 = tk.Button(hard, image = TheGame.ordered_table[4], command = lambda: button(bh4), state = "disabled")
bh4.grid(row = 1, column = 4)

bh5 = tk.Button(hard, image = TheGame.ordered_table[5], command = lambda: button(bh5), state = "disabled")
bh5.grid(row = 2, column = 0)

bh6 = tk.Button(hard, image = TheGame.ordered_table[6], command = lambda: button(bh6), state = "disabled")
bh6.grid(row = 2, column = 1)

bh7 = tk.Button(hard, image = TheGame.ordered_table[7], command = lambda: button(bh7), state = "disabled")
bh7.grid(row = 2, column = 2)

bh8 = tk.Button(hard, image = TheGame.ordered_table[8], command = lambda: button(bh8), state = "disabled")
bh8.grid(row = 2, column = 3)

bh9 = tk.Button(hard, image = TheGame.ordered_table[9], command = lambda: button(bh9), state = "disabled")
bh9.grid(row = 2, column = 4)

bh10 = tk.Button(hard, image = TheGame.ordered_table[10], command = lambda: button(bh10), state = "disabled")
bh10.grid(row = 3, column = 0)

bh11 = tk.Button(hard, image = TheGame.ordered_table[11], command = lambda: button(bh11), state = "disabled")
bh11.grid(row = 3, column = 1)

bh12 = tk.Button(hard, image = TheGame.ordered_table[12], command = lambda: button(bh12), state = "disabled")
bh12.grid(row = 3, column = 2)

bh13 = tk.Button(hard, image = TheGame.ordered_table[13], command = lambda: button(bh13), state = "disabled")
bh13.grid(row = 3, column = 3)

bh14 = tk.Button(hard, image = TheGame.ordered_table[14], command = lambda: button(bh14), state = "disabled")
bh14.grid(row = 3, column = 4)

bh15 = tk.Button(hard, image = TheGame.ordered_table[15], command = lambda: button(bh15), state = "disabled")
bh15.grid(row = 4, column = 0)

bh16 = tk.Button(hard, image = TheGame.ordered_table[16], command = lambda: button(bh16), state = "disabled")
bh16.grid(row = 4, column = 1)

bh17 = tk.Button(hard, image = TheGame.ordered_table[17], command = lambda: button(bh17), state = "disabled")
bh17.grid(row = 4, column = 2)

bh18 = tk.Button(hard, image = TheGame.ordered_table[18], command = lambda: button(bh18), state = "disabled")
bh18.grid(row = 4, column = 3)

bh19 = tk.Button(hard, image = TheGame.ordered_table[19], command = lambda: button(bh19), state = "disabled")
bh19.grid(row = 4, column = 4)

bh20 = tk.Button(hard, image = TheGame.ordered_table[20], command = lambda: button(bh20), state = "disabled")
bh20.grid(row = 5, column = 0, pady = (0, 10))

bh21 = tk.Button(hard, image = TheGame.ordered_table[21], command = lambda: button(bh21), state = "disabled")
bh21.grid(row = 5, column = 1, pady = (0, 10))

bh22 = tk.Button(hard, image = TheGame.ordered_table[22], command = lambda: button(bh22), state = "disabled")
bh22.grid(row = 5, column = 2, pady = (0, 10))

bh23 = tk.Button(hard, image = TheGame.ordered_table[23], command = lambda: button(bh23), state = "disabled")
bh23.grid(row = 5, column = 3, pady = (0, 10))

bh24 = tk.Button(hard, image = TheGame.ordered_table[24], command = lambda: button(bh24), state = "disabled")
bh24.grid(row = 5, column = 4, pady = (0, 10))

button_start_h = tk.Button(hard, image = button_start_gif, command = lambda: start_game(TheGame.random_table, TheGame.buttons, "hard"), relief = "flat")
button_start_h.grid(row = 6, column = 0, columnspan = 5, sticky = "news")

steps_counter_h = tk.Label(hard, textvariable = TheGame.steps_msg_h, font = ("Comic Sans MS", 14))
TheGame.steps_msg_h.set("Ruchy: " + str(TheGame.steps)) # info o ruchach dla poziomu hard

"""
WIN
"""

image_win_info = ImageTk.PhotoImage(Image.open("Graphics/win_info.gif")) # Grafika "Wygrałeś!"
win_info = tk.Label(win, image = image_win_info).grid(row = 0, padx = (20, 10), pady = (10, 5)) # Przypisanie grafiki "Wygrałeś!" do etykiety

TheGame.image_ready = ImageTk.PhotoImage(TheGame.img) # grafika próbna do etykiety o zakończonej grze
TheGame.ready_image = tk.Label(win, image = TheGame.image_ready) # etykieta o zakończonej grzew

def win_steps():
    TheGame.ready_image.destroy() # Niszczenie etykiety o zakończonej grze
    TheGame.image_ready = ImageTk.PhotoImage(TheGame.img) # grafika z ułożonym obrazkiem
    TheGame.ready_image = tk.Label(win, image = TheGame.image_ready) # etykieta z grafiką z ułożonym obrazkiem
    
    TheGame.ready_image.grid(row = 1, padx = (15, 0), pady = 10)

    steps_info = tk.Label(win, text = "Wykonane ruchy: " + str(TheGame.steps), font = ("Comics Sans", 14))
    steps_info.grid(row = 2)

continue_game_image = ImageTk.PhotoImage(Image.open("Graphics/kontynuuj.gif"))
continue_game = tk.Button(win, image = continue_game_image, command = lambda: reset(None), relief = "flat")
continue_game.grid(row = 3)

exit_game = tk.Button(win, image = exit_game_image, command = lambda: root.destroy(), relief = "flat")
exit_game.grid(row = 4, padx = 100)

"""
ODPALANIE PROGRAMU
"""

raise_frame(menu)

root.mainloop()


"""
Do zrobienia:
 - zmiana obrazków, zapis czasu
"""
