import PySimpleGUI as sg
from PIL import Image

def main():
    layout = [
        [sg.Text("Select WEBP files to convert:")],
        [sg.InputText("", key="-FILES-", disabled=True), sg.FileBrowse(file_types=(("WEBP Files", "*.webp"),))],
        [sg.Text("Select destination folder:")],
        [sg.InputText("", key="-FOLDER-", disabled=True), sg.FolderBrowse()],
        [sg.Button("Convert to PNG"), sg.Button("Exit")],
        [sg.Text("", size=(50, 1), key="-OUTPUT-")],
    ]

    window = sg.Window("WEBP to PNG Converter", layout, finalize=True)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Exit":
            break
        elif event == "Convert to PNG":
            files = values["-FILES-"].split(";")
            folder = values["-FOLDER-"]

            for file_path in files:
                img = Image.open(file_path)
                new_path = f"{folder}/{file_path.split('/')[-1].split('.')[0]}.png"
                img.save(new_path, "PNG")
                window["-OUTPUT-"].update(f"Converted {file_path} to {new_path}")

    window.close()

if __name__ == "__main__":
    main()
