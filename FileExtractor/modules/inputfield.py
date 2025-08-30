import tkinter as tk
from tkinter import filedialog
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

root = tk.Tk()
root.withdraw()



class InputField(BoxLayout):
    source_path = StringProperty("")
    dest_path = StringProperty("")
    render_path = StringProperty("")
    

    def browse_source(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.source_path = folder_selected

    def browse_dest(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.dest_path = folder_selected

    def browse_render(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.render_path = folder_selected