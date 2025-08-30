from kivy.config import Config
Config.set('graphics', 'resizable', '0') # 0 being False
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '300')


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder

from modules.inputfield import InputField  #! Don't remove, otherwise doesn't recognise the pattern
from kivy.uix.label import Label
from kivy.uix.popup import Popup


from Core.core_logic import process_shot_folders




Builder.load_file('modules/inputfield.kv')



# Config.set('graphics', 'resizable', False)
# Window.size = (800, 300)
Window.clearcolor = (16/255, 24/255, 39/255, 1)


class AboutPopup(Popup):
    pass

class PatternBoxLayout(BoxLayout):
    pass

class MainLayout(BoxLayout):

    def process_data(self):
        input_field_widget = self.ids.input_field
        source_path = input_field_widget.source_path
        dest_path = input_field_widget.dest_path
        render_path = input_field_widget.render_path
        shot_pattern_box = self.ids.pattern_box_layout_id
        shot_pattern_text = shot_pattern_box.ids.shot_pattern_id.text
        print(f"Source: {source_path}, Destination: {dest_path}, Render: {render_path}, Pattern: {shot_pattern_text}")




class CopyApp(App):
    def build(self):
        self.title = "Magic Copy v0.1"
        return MainLayout()
    

    def open_about_popup(self):
            # Create an instance of the popup and open it
            the_popup = AboutPopup()
            the_popup.open()



if __name__ == "__main__":
    CopyApp().run()