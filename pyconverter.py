import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image
import os

def convert_image(input_path, output_path, output_format):
    try:
        # Open the image file
        with Image.open(input_path) as img:
            # Convert and save the image in the specified format
            img.save(output_path, format=output_format)
            print(f"Conversion successful: {output_path}")
    except Exception as e:
        print(f"Error during conversion: {e}")

def select_file():
    root = tk.Tk()
    root.withdraw()

    # Ask the user to select a file
    file_path = filedialog.askopenfilename(
        title="Select an image file",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")]
    )

    return file_path

def select_output_path(output_label):
    root = tk.Tk()
    root.withdraw()

    # Ask the user to select a folder for output
    output_path = filedialog.askdirectory(title="Select output folder")
    
    # Update the label with the selected output folder
    output_label.config(text=r"Output Folder: {}".format(output_path))

    return output_path

def create_gui():
    # Create the main window
    main_window = tk.Tk()
    main_window.title("Image Converter")

    # Set window size and position in the center
    window_width = 400
    window_height = 200

    screen_width = main_window.winfo_screenwidth()
    screen_height = main_window.winfo_screenheight()

    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2

    main_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Apply ttk theme
    ttk_style = ttk.Style()
    ttk_style.theme_use('clam')  # Change 'clam' to other available themes if desired

    # Function to handle the conversion button click
    def convert_button_click():
        input_file = select_file()

        if not input_file:
            output_label.config(text="No file selected.")
            return

        output_folder = output_label.cget("text")[15:]  # Extract the output folder from the label text

        if not output_folder:
            output_label.config(text="No output folder selected.")
            return

        output_format = format_var.get()
        output_file = os.path.join(output_folder, r"{}.{}".format(os.path.splitext(os.path.basename(input_file))[0], output_format.lower()))

        convert_image(input_file, output_file, output_format)
        output_label.config(text=r"Conversion successful: {}".format(output_file))

   

    # Output folder button
    output_label = ttk.Label(main_window, text=r"Output Folder: [not selected]")
    output_label.pack()

    def output_folder_button_click():
        output_path = select_output_path(output_label)
    
    output_folder_button = ttk.Button(main_window, text="Select Output Folder", command=output_folder_button_click)
    output_folder_button.pack()

    input_label = ttk.Label(main_window, text="Select Input File:")
    input_label.pack()

    convert_button = ttk.Button(main_window, text="Convert", command=convert_button_click)
    convert_button.pack()
    # Dropdown for selecting the output format
    format_var = tk.StringVar(main_window)
    format_var.set("PNG")  # Default format

    format_label = ttk.Label(main_window, text="Select Output Format:")
    format_label.pack()

    format_dropdown = ttk.Combobox(main_window, textvariable=format_var, values=["PNG", "JPEG", "GIF"])
    format_dropdown.pack()

    # Start the GUI event loop
    main_window.mainloop()

if __name__ == "__main__":
    # Run the GUI
    create_gui()
