import tkinter as tk
import convert
import dis


class Main:
    def __init__(self):
        # Create the main window
        self.root = tk.Tk()

        # Set the window title
        self.root.title("Python-MIPS Translator")

        # Make the window fullscreen
        self.root.attributes("-fullscreen", True)

        # Configure rows and columns to expand and fill available space
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

        # Create a label for the Python text box
        py_label = tk.Label(self.root, text="Python", font=("Arial", 14))
        py_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        # Create the Python text box
        self.py_text = tk.Text(self.root, width=40, height=20)
        self.py_text.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        # Create a line separator
        line = tk.Canvas(self.root, width=1, height=600, bg="gray")
        line.grid(row=0, column=1, rowspan=3, padx=5, pady=5, sticky="ns")

        # Create a label for the MIPS output box
        mips_label = tk.Label(self.root, text="MIPS", font=("Arial", 14))
        mips_label.grid(row=0, column=2, padx=5, pady=5, sticky="w")

        # Create the MIPS output box
        self.mips_text = tk.Text(self.root, width=40, height=20, state=tk.DISABLED)
        self.mips_text.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")

        # Bind the Return key to the translate function
        self.root.bind("<Return>", self.translate)

        # Start the main event loop
        self.root.mainloop()


    def translate(self, event):
        # Clear the MIPS output box
        self.mips_text.configure(state=tk.NORMAL)
        self.mips_text.delete("1.0", tk.END)
        self.mips_text.configure(state=tk.DISABLED)

        # Get the Python code from the text box
        py_code = self.py_text.get("1.0", tk.END)

        # Translate the Python code to MIPS assembly
        mips_code = translate_python_to_mips(py_code)

        # Display the MIPS code in the output box
        self.mips_text.configure(state=tk.NORMAL)
        self.mips_text.insert(tk.END, mips_code)
        self.mips_text.configure(state=tk.DISABLED)

# Gonna create a class here
def translate_python_to_mips(py_code):
    def translator():
        py_code

    bytecode = dis.Bytecode(translator)
    mips_code = "Translated to MIPS:\n\n" + convert.convert_bytecode_to_mips(bytecode)
    return mips_code



app = Main()

