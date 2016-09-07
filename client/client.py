import tkinter as tk;

class Application(tk.Frame):
    """
    The main application behind the graphical interface.
    """

    def __init__(self, master=None):
        super(Application, self).__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        """
        Include all your widgets here.
        """
        pass


root = tk.Tk()
app = Application(master=root)
app.mainloop()
