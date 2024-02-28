import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image
import os

input_path = ""
output_path = ""

def convert_image(input_path, output_path, output_format):
    try:
        # Open the image file
        with Image.open(input_path) as img:
            # Convert and save the image in the specified format
            img.save(output_path, format=output_format)
            print(f"Conversion successful: {output_path}")
    except Exception as e:
        print(f"Error during conversion: {e}")

def select_file(input_label):
    global input_path

    root = tk.Tk()
    root.withdraw()

    # Ask the user to select a file
    input_path = filedialog.askopenfilename(
        title="Select an image file",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.webp")]
    )
    input_label.config(text=f"Input File: {os.path.basename(input_path)}")


def select_output_path(output_label):
    global output_path

    root = tk.Tk()
    root.withdraw()

    # Ask the user to select a folder for output
    output_path = filedialog.askdirectory(title="Select output folder")
    output_label.config(text=f"Output Folder: {output_path}")
    

def convert_button_click(output_format, output_label):
    global input_path
    global output_path

    if not input_path:
        output_label.config(text="No file selected.")
        return

    if not output_path:
        output_label.config(text="No output folder selected.")
        return

    output_file = os.path.join(output_path, f"{os.path.splitext(os.path.basename(input_path))[0]}.{output_format.lower()}")

    convert_image(input_path, output_file, output_format)

def create_gui():
    # Create the main window
    main_window = tk.Tk()
    main_window.title("Image Converter")

    # Set window size and position in the center
    window_width = 600
    window_height = 400

    screen_width = main_window.winfo_screenwidth()
    screen_height = main_window.winfo_screenheight()

    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2

    main_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Apply ttk theme
    ttk_style = ttk.Style()
    ttk_style.theme_use('clam')  # Change 'clam' to other available themes if desired

    
    # Function to handle the conversion button click
    input_label = ttk.Label(main_window, text="Select Input File:")
    input_label.pack(pady=5)

    select_file_button = ttk.Button(main_window, text="Browse", command=lambda: select_file(input_label))
    select_file_button.pack(pady=5)
    

    # Output folder button
    output_label = ttk.Label(main_window, text="Output Folder: [not selected]")
    output_label.pack(pady=5)

    select_output_button = ttk.Button(main_window, text="Select Output Folder", command=lambda: select_output_path(output_label))
    select_output_button.pack(pady=5)

    output_label.config(text=f"Conversion successful: {output_path}")

    # Dropdown for selecting the output format
    format_var = tk.StringVar(main_window)
    format_var.set("PNG")  # Default format

    format_label = ttk.Label(main_window, text="Select Output Format:")
    format_label.pack(pady=5)

    format_dropdown = ttk.Combobox(main_window, textvariable=format_var, values=["PNG", "JPEG", "GIF"])
    format_dropdown.pack(pady=5)

    # Convert button
    convert_button = ttk.Button(main_window, text="Convert", command=lambda: convert_button_click(format_var.get(), output_label))
    convert_button.pack(pady=5)

    # Start the GUI event loop
    main_window.mainloop()

if __name__ == "__main__":
    # Run the GUI
    create_gui()
