from tkinter import *
from langdetect import *
from iso639 import languages
root = Tk()
root.title("Language Detector")
root.geometry("400x480")
def language_detection():
	text = T.get("1.0", 'end-1c')
	language_code = languages.get(alpha2=detect(text))
	l_d.config(text="Language Detected: "+language_code.name)
T = Text(root)
T.pack()
l_d = Label(root, text="Language Detected: ")
l_d.pack(pady=10)
Button(root, text='Detect Language', command=language_detection).pack(pady=10)
root.mainloop()
