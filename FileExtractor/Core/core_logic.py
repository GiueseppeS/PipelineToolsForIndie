import os
import re
import shutil


SOURCE_DIR : str = "C:\\Testing\\SOURCE_FOLDER"
DEST_DIR : str = "C:\\Testing\\DESTINATION_FOLDER"

shot_pattern = re.compile(r"Shot_\d{4}")
render_pattern = re.compile(r"Mamma\\Renders")

os.makedirs(DEST_DIR, exist_ok=True)


def find_shot_folders(directory_name: str, pattern) -> list[str]:
    shot_folders = []

    for folder in os.listdir(directory_name):
        full_path = os.path.join(directory_name, folder)

        if os.path.isdir(full_path) and pattern.match(folder):
            shot_folders.append(os.path.join(full_path))

    return shot_folders



def find_render_folders(shot_folders : list[str], pattern) -> list[str]:
    render_folders = []

    for folder in shot_folders:
        render_folder = find_shot_folders(folder, pattern)
        render_folders.extend(render_folder)
        #print(f"Found {len(render_folder)} render folders.")

    return render_folders



def find_latest_version(render_folders_list: list[str]) -> str:
    version_pattern = re.compile(r"v(\d{3})")
    latest_version = -1
    latest_folder = None

    latest_render_folders = []

    for render_folder in render_folders_list:
        if not render_folder:
            continue
        for folder in os.listdir(render_folder):
            full_path = os.path.join(render_folder, folder)
            #print(f"Checking folder: {full_path}")
            match = version_pattern.search(folder)
            if match:
                current_version = int(match.group(1))
                if current_version > latest_version:
                    latest_version = current_version
                    latest_folder = full_path

        latest_render_folders.append(latest_folder)
        latest_version = -1  # Reset for next render folder
            #print(f"Checking folder: {full_path}")
    return latest_render_folders



def copy_latest_versions(latest_folders: list[str], destination: str):
    for folder in latest_folders:
        if folder is None:
            continue
        dest_path = os.path.join(destination, os.path.basename(folder))
        if not os.path.exists(dest_path):
            shutil.copytree(folder, dest_path)
            print(f"Copied {folder} to {dest_path}")



def main():
    first_folders  : list[str] = find_shot_folders(SOURCE_DIR, shot_pattern)
    print(f"Found {len(first_folders)} shot folders.")

    render_folders = find_render_folders(first_folders, render_pattern)
    a = find_latest_version(render_folders)
    copy_latest_versions(a, DEST_DIR)



if __name__ == "__main__":
    main()