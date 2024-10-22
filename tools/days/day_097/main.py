from days.day_097.files.helpers import *


def day_097():
    """
    A tkinter program that takes in a png image and pixelates it.
    """
    title("PIXELATOR")
    global processed_image, selected_file_path, pixel_size
    processed_image = None
    selected_file_path = None
    pixel_size = 10  # Default pixel size

    def select_image():
        """Open a file dialog to select an image file and handle processing."""
        global selected_file_path
        filetypes = (("Image files", "*.jpeg *.jpg *.png"), ("All files", "*.*"))
        selected_file_path = filedialog.askopenfilename(
            title="Select an image", filetypes=filetypes
        )

        if selected_file_path:
            if selected_file_path.lower().endswith((".png", ".jpg", ".jpeg")):
                process_image(selected_file_path)
            else:
                messagebox.showerror(
                    "Invalid File", "Please select a valid JPEG or PNG image."
                )

    def process_image(filepath):
        """Load the image and call the pixelation function."""
        global processed_image
        try:
            image = Image.open(filepath)
            processed_image = pixelate_image(image, pixel_size=pixel_size)
            display_image(processed_image)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to process image: {e}")

    def pixelate_image(image, pixel_size=10):
        """Pixelate the given image by reducing its resolution."""
        original_size = image.size

        # If the image is PNG, preserve transparency by using RGBA
        if image.mode != "RGBA":
            image = image.convert("RGBA")

        # Reduce the size by the pixel size
        small_image = image.resize(
            (original_size[0] // pixel_size, original_size[1] // pixel_size),
            Image.NEAREST,
        )

        # Scale it back up to original size
        pixelated_image = small_image.resize(original_size, Image.NEAREST)

        return pixelated_image

    def display_image(image):
        """Display the pixelated image in the Tkinter window."""
        tk_image = ImageTk.PhotoImage(image)

        # Clear the previous image
        label_img.config(image=tk_image)
        label_img.image = tk_image

        # Enable the save button after the image is processed
        save_button.config(state=tk.NORMAL)

    def save_image():
        """Open a file dialog to save the processed image to the chosen location."""
        global processed_image
        if processed_image is None:
            messagebox.showerror("Error", "No image to save!")
            return

        save_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")],
        )

        if save_path:
            try:
                # Save the image based on the selected file extension
                processed_image.save(save_path)
                messagebox.showinfo(
                    "Success", f"Image saved successfully at {save_path}"
                )
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save the image: {e}")

    def set_pixel_size(selection):
        """Set the pixel size based on the user's selection."""
        global pixel_size
        pixel_map = {"Favicon": 5, "2D Game": 20, "High Pixelation": 50}
        pixel_size = pixel_map[selection]
        if selected_file_path:
            process_image(selected_file_path)

    def create_window():
        """Set up the Tkinter window."""
        window = tk.Tk()
        window.title("PIXELATOR")
        window.geometry("500x600")

        # Add a button to upload the image
        button = tk.Button(window, text="Select Image", command=select_image)
        button.pack(pady=20)

        # Add dropdown (OptionMenu) for pixelation levels
        tk.Label(window, text="Pixelation Level:").pack()

        # Dropdown values
        options = ["Favicon", "2D Game", "High Pixelation"]
        selected_option = tk.StringVar(window)
        selected_option.set(options[0])  # Default option

        dropdown = tk.OptionMenu(
            window, selected_option, *options, command=set_pixel_size
        )
        dropdown.pack(pady=10)

        # Add a save button (initially disabled)
        global save_button
        save_button = tk.Button(
            window, text="Save Image", command=save_image, state=tk.DISABLED
        )
        save_button.pack(pady=10)

        global label_img
        label_img = tk.Label(window)
        label_img.pack()

        window.mainloop()

    if __name__ == "days.day_097.main":
        create_window()
