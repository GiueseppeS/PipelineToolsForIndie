from kivy.config import Config
Config.set('graphics', 'resizable', '0') # 0 being False
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '420')


import sys
import os

# Add the script's own directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder

#! Don't remove, otherwise doesn't recognise the pattern
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from modules.inputfield import InputField

from Core.core_logic import process_shot_folders, copy_latest_versions
import webbrowser
import threading
import time
from kivy.clock import Clock



kv_path = os.path.join(os.path.dirname(__file__), 'modules', 'inputfield.kv')
Builder.load_file(kv_path)

# Config.set('graphics', 'resizable', False)
# Window.size = (800, 300)
Window.clearcolor = (16/255, 24/255, 39/255, 1)



def process_shot_folders_with_progress(source_path, dest_path, render_path, shot_pattern_text, progress_callback):
    # Simulate processing time
    last_render_folders = process_shot_folders(source_path, render_path, shot_pattern_text)

    print(f"last_render_folders in main: {last_render_folders}")

    #items_to_process = list(range(last_render_folders))
    total_items = len(last_render_folders)
    print(f"last_render_folders in main: {last_render_folders}")
    print(f"dest_path in main: {dest_path}")
    for i, item in enumerate(last_render_folders):
        copy_latest_versions(item, dest_path)

        progress = (i + 1) / total_items * 100
        text=f'Processing item {i + 1} of {total_items}'
        progress_callback(progress, text)

    print(f"Total items to process: {total_items}")

    return total_items  # Return the total number of items processed

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

        if not source_path or not dest_path or not render_path or not shot_pattern_text:
            self.update_progress(0, "Please fill in all fields.")
            return

        self.ids.process_button.disabled = True

        thread = threading.Thread(target=self.processing_thread, args=(source_path, dest_path, render_path, shot_pattern_text))
        thread.start()

        # process_shot_folders(source_path, dest_path, render_path, shot_pattern_text)

    def processing_thread(self, source_path, dest_path, render_path, shot_pattern_text):
        try:
            total_folders = process_shot_folders_with_progress(source_path, dest_path, render_path, shot_pattern_text, self.schedule_progress_update)
            Clock.schedule_once(lambda dt: self.update_progress(100, f"Completed processing {total_folders} folders."))

        except Exception as e:
            print(f"Error occurred: {e}")
            Clock.schedule_once(lambda dt: self.update_progress(0, f"Error: {e}"))



    def schedule_progress_update(self, progress, message):
        Clock.schedule_once(lambda dt: self.update_progress(progress, message))


    def update_progress(self, progress, message):
        # Update the progress bar and message label
        self.ids.progress_bar.value = progress
        self.ids.progress_label.text = message
        if progress == 100:
            self.ids.process_button.disabled = False


class CopyApp(App):
    def build(self):
        self.title = "Magic Copy v0.1"
        return MainLayout()
   
    def open_link(self, url):
        webbrowser.open(url)
 

    def open_about_popup(self):
            # Create an instance of the popup and open it
            the_popup = AboutPopup()
            the_popup.open()



if __name__ == "__main__":
    CopyApp().run()