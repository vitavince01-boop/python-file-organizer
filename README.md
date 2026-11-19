# Python File Organizer

A small Python program that automatically sorts files in your Downloads folder into category folders—such as Images, Documents, Audio, Videos, Archives, Programs, Code, and Other.

## Features

- Sorts existing files when you start the program.
- Watches for new files and sorts them automatically.
- Creates category folders when needed.
- Avoids overwriting files with the same name by adding a number.

## Requirements

- Python 3
- The `watchdog` Python package

## Setup on Windows

1. Open **Command Prompt** in the folder containing `organizer.py`.
   - In File Explorer, open that folder.
   - Click the address bar, type `cmd`, and press **Enter**.
2. Install the required package:

   ```cmd
   py -m pip install watchdog
   ```

3. Start the organizer:

   ```cmd
   py organizer.py
   ```

Keep the Command Prompt window open while it runs. Press **Ctrl+C** to stop it.

## Folder to organize

By default, the script watches your Downloads folder. To choose another folder, edit `SOURCE_FOLDER` near the top of `organizer.py`.

For example:

```python
SOURCE_FOLDER = Path.home() / "Downloads"
```

The program moves files into category folders inside the selected folder. Try it with a few test files first, and make sure important files are backed up.

## Customize file categories

Edit the `CATEGORIES` section in `organizer.py` to add or remove file extensions. For example, add `".heic"` to the Images list to sort HEIC photos there.

## Current progress

- [x] Sort files into folders by file type
- [x] Watch for newly added files
- [x] Prevent overwriting files with duplicate names
- [ ] Add more file types and categories
- [ ] Add configurable folder selection

## License

Choose a license if you plan to share or reuse this project publicly.
