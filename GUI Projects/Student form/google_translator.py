from deep_translator import GoogleTranslator
import tkinter as tk
from tkinter import messagebox

class GoogleTranslatorGUI:
    def _init_(self):
        self.window = tk.Tk()
        self.window.title("Kirti's Translator")
        self.window.geometry("930x900")
        self.window.config(bg="#FF1493")

        self.lang1 = tk.StringVar()
        self.lang2 = tk.StringVar()
        self.lang1.set("en")
        self.lang2.set("hi")

        self.label1 = tk.Label(self.window, text="Language 1:", bg="#FFB6C1", font=("Georgia",30,"bold"))
        self.label1.grid(row=0, column=0, padx=30, pady=25,)

        self.option1 = tk.OptionMenu(self.window, self.lang1, "en", "hi", "bn", "ta", "te", "mr", "gu", "kn" )
        self.option1.config(font="Georgia", width=9)
        self.option1.grid(row=0, column=1, padx=30, pady=30)

        self.label2 = tk.Label(self.window, text="Language 2:", bg="#FFB6C1", font=("Georgia", 30,"bold"))
        self.label2.grid(row=1, column=0, padx=50, pady=25)

        self.option2 = tk.OptionMenu(self.window, self.lang2,"en", "hi", "bn", "ta", "te", "mr", "gu", "kn" )
        self.option2.config(font="Georgia", width=9)
        self.option2.grid(row=1, column=1,padx=50, pady=30,)

        self.text1 = tk.Text(self.window, height=15, width=40, font=("Times New Roman", 15),relief="solid")
        self.text1.grid(row=2, column=0, padx=25, pady=30,)

        self.text2 = tk.Text(self.window, height=15, width=40, font=("Times New Roman", 15),relief="solid")
        self.text2.grid(row=2, column=1, padx=25, pady=30)

        self.translate_button = tk.Button(self.window, text="Translate", command=self.translate, bg="#4CAF50", fg="#fff", font=("Georgia",20))
        self.translate_button.grid(row=3, column=0, columnspan=2, padx=50, pady=30)

        self.clear_button = tk.Button(self.window, text="Clear", command=self.clear, bg="#e74c3c", fg="#fff", font=("Georgia", 15))
        self.clear_button.grid(row=4, column=0, columnspan=2, padx=120, pady=10)

    def translate(self):
        try:
            translator = GoogleTranslator(source=self.lang1.get(), target=self.lang2.get())
            text = self.text1.get("1.0", tk.END)
            result = translator.translate(text)
            self.text2.delete("1.0", tk.END)
            self.text2.insert(tk.END, result)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear(self):
        self.text1.delete("1.0", tk.END)
        self.text2.delete("1.0", tk.END)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = GoogleTranslatorGUI()
    app.run()