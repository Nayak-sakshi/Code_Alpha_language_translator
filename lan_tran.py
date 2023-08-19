from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox



root = Tk()
root.title('language translator')
root.geometry("852x300")

def translate_it():
    # Delete any Previous Translations
    translated_text.delete(1.0, END)
    try:
        #lets get the languages from the dictonary keys
        # Get that from language key
        for key, value in languages.items():
            if(value == original_combo.get()):
                from_language_key = key


        # Get the to Language Key
        for key, value in languages.items():
            if(value == translated_combo.get()):
                to_language_key = key

        # Trun Original Text into a textBLob
        words = textblob.TextBlob(original_text.get(1.0, END))

        #Translate Text
        words = words.translate(from_lang=from_language_key , to=to_language_key)
        

        # Output translated text to screen
        translated_text.insert(1.0 , words)


    except Exception as e:
        messagebox.showerror("Translator" , e)



    


def clear():
    #clear the text boxes
    original_text.delete(0.1,END)
    translated_text.delete(0.1,END)

# language_list = (1,2,3,4,5,6,7,8,9,0,1,1,1,1,1,1,1,1,1,8,4,5,7,6,4,6,6,7,5,2,4,8,3,4)

# Grab Language LIst From GoogleTrnas
languages = googletrans.LANGUAGES

#Convert to List
language_list = list(languages.values())



# Text boxes
original_text = Text(root, height=10 , width=40)
original_text.grid(row=0 , column=0, pady=20, padx=10)

translate_button = Button(root, text="Translate!", font=("Helvetica" , 20) , command=translate_it)
translate_button.grid(row=0, column=1, padx=10)

translated_text = Text(root, height=10 , width=40)
translated_text.grid(row=0 , column=2, pady=20, padx=10)

#combo boxes
original_combo = ttk.Combobox(root, width=50 , value=language_list)
original_combo.current(21)
original_combo.grid(row=1 , column=0)

translated_combo = ttk.Combobox(root, width=50 , value=language_list)
translated_combo.current(26)
translated_combo.grid(row=1 , column=2)

#Clear button
clear_button = Button(root, text="clear", command=clear)
clear_button.grid(row=2, column=1)
root.mainloop()