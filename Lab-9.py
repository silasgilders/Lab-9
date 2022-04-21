from tkinter import *
from tkinter import ttk
from pokeapi import get_poke_list, get_poke_image
from library1 import download_image_from_url, set_desktop_background_image
import os 
import sys
import ctypes

def main():
    
    script_dir = sys.path[0]
    image_dir = os.path.join(script_dir, 'images')
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)
    root = Tk()
    #I named this after a Segment on the Pokemon show which played before and after commercials
    root.title("Who's that Pokemon?!")

    #Generally creates the rules for where the Button and Combo Box goes when you resize
    myappid = "Pokedex"
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    root.iconbitmap(os.path.join(script_dir, 'Pokedex.ico'))
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    #This makes it so that you can't collapse the window in to the point that the image is obscured
    root.minsize(500, 600)

    #This creates our initial frame, and sets us up so that the image stays centered
    frm = ttk.Frame(root)
    frm.grid(sticky=(N,S,E,W))
    frm.rowconfigure(0, weight=1)
    frm.columnconfigure(0, weight=1)

    img_poke = PhotoImage(file=os.path.join(script_dir, 'pokeball.png'))
    lbl_image = ttk.Label(frm, image=img_poke)
    lbl_image.grid(row=0, column=0, padx=10, pady=10)

    #Gets our list of pokemon, and puts them in a Combo Box, that like the Window, I named after a segment in the show 
    pokemon_list= get_poke_list()
    pokemon_list.sort()
    pokemon_list= [p.capitalize() for p in pokemon_list]
    cbo_pokemon = ttk.Combobox(frm, values=pokemon_list, state='readonly')
    cbo_pokemon.set("Who's that Pokemon!")
    cbo_pokemon.grid(row=1, column=0, padx=10, pady=10)


    def handle_poke_select(event):
        """Handles getting the image, and stopping the user 
            from pressing the button to set it as a desktop background until they've picked a Pokemon."""
        pokemon_name = cbo_pokemon.get()
        image_url = get_poke_image(pokemon_name)
        image_path = os.path.join(image_dir, pokemon_name + ".png")
        download_image_from_url(image_url, image_path)
        img_poke['file'] = image_path
        btn_set_desktop.state(['!disabled'])
        

    #Sets up for something to happen when the event happens, in this case, selecting an option
    cbo_pokemon.bind('<<ComboboxSelected>>', handle_poke_select)
    def handle_btn_set_desktop():
        pokemon_name = cbo_pokemon.get()
        image_path = os.path.join(image_dir, pokemon_name + ".png")
        set_desktop_background_image(image_path)


    btn_set_desktop = ttk.Button(frm, text="Set as Desktop Image", command=handle_btn_set_desktop)
    btn_set_desktop.state(['disabled'])
    btn_set_desktop.grid(row=2, column=0, padx=10, pady=10)



    root.mainloop()



main()

