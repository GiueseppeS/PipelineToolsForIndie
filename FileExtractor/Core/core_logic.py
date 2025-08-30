from ast import main
import os
import re
import shutil


# SOURCE_DIR : str = "C:\\Testing\\SOURCE_FOLDER"
# DEST_DIR : str = "C:\\Testing\\DESTINATION_FOLDER"
# full_render_path : str = "C:\\Testing\\SOURCE_FOLDER\\Shot_0010\\Mamma\\Renders"
# shot_folder_name : str = "Shot_0010"


#shot_pattern = re.compile(r"Shot_\d{4}")

#os.makedirs(DEST_DIR, exist_ok=True)


def find_shot_folders(directory_name: str, pattern) -> list[str]:
    shot_folders = []

    for folder in os.listdir(directory_name):
        full_path = os.path.join(directory_name, folder)

        if os.path.isdir(full_path) and pattern.match(folder):
            shot_folders.extend([os.path.join(full_path)])

    return shot_folders



def return_render_folder_path(_shot_folders, _full_render_path):
    render_path = os.path.relpath(_full_render_path, start= _shot_folders)
    print(f"Render path: {render_path}")
    return render_path



def find_latest_version(_shot_folders_ : list[str], _shot_render_folder_relative_path: str) -> list[str]:
    version_pattern = re.compile(r"v(\d{3})")
    latest_version = -1
    latest_folder = None

    latest_render_folders = []

    print(_shot_folders_)
    for folder in _shot_folders_:
        if not folder:
            continue
        render_folder = os.path.join(folder, _shot_render_folder_relative_path)
        if os.path.exists(render_folder):
            for renders in os.listdir(render_folder):
                match = version_pattern.search(renders)
                print(f"found version: {match.group(1)}" if match else "No version found")
                if match:
                    current_version = int(match.group(1))
                    if current_version > latest_version:
                        latest_version = current_version
                        latest_folder = os.path.join(render_folder, renders)

            latest_render_folders.append(latest_folder)
            latest_version = -1  # Reset for next render folder
            print(f"Latest render folder found: {latest_folder}")

    return latest_render_folders



def find_shot_pattern(_shot_folder) -> str:
    first_pattern = []
    for letter in _shot_folder:
        if not letter.isdigit():
            first_pattern.append(letter)
    first_pattern = ''.join(first_pattern)
    last_pattern = ''.join([letter for letter in _shot_folder if letter.isdigit()])
    return first_pattern, last_pattern


def copy_latest_versions(folder: list[str], destination: str):

    if folder is None:
        return
    dest_path = os.path.join(destination, os.path.basename(folder))

    if not os.path.exists(dest_path):
        shutil.copytree(folder, dest_path)
        print(f"Copied {folder} to {dest_path}")

    if not os.path.exists(folder):
        print(f"Folder does not exist: {folder}")




def get_shot_number_count(_shot_pattern : str) -> int:
    # This function will return the count of shot numbers in the given pattern
    #for match in re.finditer(r"(\d+)", _shot_pattern):
    text_part = None
    number_length = None
    match = re.search(r"([A-Za-z_]+)(\d+)", _shot_pattern)

    if match:
        text_part = match.group(1)
        number_length = len(match.group(2))
        print(f"Text part: {text_part}, Number length: {number_length}")
    return re.compile(rf"{text_part}(\d{{{number_length}}})")


def process_shot_folders(SOURCE_DIR, RENDER_PATH, SHOT_PATTERN):

    pattern = get_shot_number_count(SHOT_PATTERN)
    print(pattern)
    shot_folders  : list[str] = find_shot_folders(SOURCE_DIR, pattern)
    last_render_folders : list[str] = []



    relative_render_folder_path = return_render_folder_path(shot_folders[0], RENDER_PATH)
    print(f"Relative render folder path: {relative_render_folder_path}")
    last_render_folder = find_latest_version(shot_folders, relative_render_folder_path)
    print(f"Last render folder: {last_render_folder}")
    
    return last_render_folder
    # print(f"Last render folder: {last_render_folder}")
    # copy_latest_versions(last_render_folder, DEST_DIR)

# if __name__ == "__main__":
#     process_shot_folders(SOURCE_DIR, DEST_DIR, RENDER_PATH, SHOT_PATTERN)

