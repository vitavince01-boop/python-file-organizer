from pathlib import Path
from shutil import move
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Change these paths
SOURCE_FOLDER = Path.home() / "Downloads"

CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".xlsx", ".xls", ".ppt", ".pptx", ".csv"},
    "Audio": {".mp3", ".wav", ".aac", ".flac", ".m4a"},
    "Videos": {".mp4", ".mov", ".avi", ".mkv", ".wmv"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Programs": {".exe", ".msi", ".apk", ".dmg"},
    "Code": {".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".json"},
}


def organize_file(file_path: Path):
    if not file_path.is_file():
        return

    extension = file_path.suffix.lower()

    destination_folder = SOURCE_FOLDER / "Other"
    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            destination_folder = SOURCE_FOLDER / category
            break

    destination_folder.mkdir(parents=True, exist_ok=True)
    destination = destination_folder / file_path.name

    # Avoid overwriting existing files
    counter = 1
    while destination.exists():
        destination = destination_folder / (
            f"{file_path.stem}_{counter}{file_path.suffix}"
        )
        counter += 1

    try:
        move(str(file_path), str(destination))
        print(f"Moved: {file_path.name} -> {destination}")
    except Exception as error:
        print(f"Could not move {file_path}: {error}")


def organize_existing_files():
    for item in SOURCE_FOLDER.iterdir():
        if item.is_file():
            organize_file(item)


class DownloadHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            time.sleep(1)
            organize_file(Path(event.src_path))

    def on_moved(self, event):
        if not event.is_directory:
            time.sleep(1)
            organize_file(Path(event.dest_path))


if __name__ == "__main__":
    SOURCE_FOLDER.mkdir(parents=True, exist_ok=True)

    organize_existing_files()

    observer = Observer()
    observer.schedule(
        DownloadHandler(),
        str(SOURCE_FOLDER),
        recursive=False,
    )
    observer.start()

    print(f"Organizing files in: {SOURCE_FOLDER}")
    print("Press Ctrl+C to stop.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

    
