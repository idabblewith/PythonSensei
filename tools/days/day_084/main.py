from days.day_084.files.helpers import *


def day_084():
    title("IMAGE WATERMARKING")

    import os, subprocess, platform
    import numpy as np
    from tkinter import Tk, Label, Button, Entry, filedialog, Canvas
    from PIL import Image, ImageTk, ImageDraw, ImageFont

    class WatermarkApp:
        def __init__(self, master):
            self.master = master
            master.title("Image Watermarking App")

            self.label = Label(master, text="Choose an image to watermark:")
            self.label.pack()

            self.upload_button = Button(
                master, text="Upload Image", command=self.upload_image
            )
            self.upload_button.pack()

            self.label = Label(master, text="Enter watermark text:")
            self.label.pack()

            self.watermark_text = Entry(master)
            self.watermark_text.pack()

            self.watermark_button = Button(
                master, text="Add Watermark", command=self.add_watermark
            )
            self.watermark_button.pack()

            self.canvas = Canvas(master, width=500, height=500)
            self.canvas.pack()

            self.image_path = None
            self.image = None
            self.photo_image = None

        def upload_image(self):
            self.image_path = filedialog.askopenfilename(
                filetypes=[("Image files", "*.jpg *.jpeg *.png")]
            )
            if self.image_path:
                self.image = Image.open(self.image_path)
                self.image.thumbnail((500, 500))
                self.photo_image = ImageTk.PhotoImage(self.image)
                self.canvas.create_image(250, 250, image=self.photo_image)

        def open_image(self, file_path):
            if platform.system() == "Windows":
                os.startfile(file_path)
            elif platform.system() == "Darwin":  # macOS
                subprocess.call(["open", file_path])
            else:  # Linux variants
                subprocess.call(["xdg-open", file_path])

        def add_watermark(self):
            if self.image_path and self.watermark_text.get():
                # Load image and convert to NumPy array
                image = Image.open(self.image_path).convert("RGBA")
                np_image = np.array(image)

                # Create watermark image
                watermark_text = self.watermark_text.get()
                width, height = image.size
                watermark_image = Image.new("RGBA", (width, height), (255, 255, 255, 0))
                draw = ImageDraw.Draw(watermark_image)
                font = ImageFont.truetype("arial.ttf", 36)
                # Use textbbox to calculate text dimensions
                textbbox = draw.textbbox((0, 0), watermark_text, font=font)
                textwidth, textheight = (
                    textbbox[2] - textbbox[0],
                    textbbox[3] - textbbox[1],
                )
                x = width - textwidth - 10
                y = height - textheight - 10
                draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))

                # Convert watermark image to NumPy array
                np_watermark = np.array(watermark_image)

                # Combine original image with watermark
                combined = np_image.copy()
                mask = np_watermark[:, :, 3] > 0
                combined[mask] = np_watermark[mask]

                # Convert combined image back to PIL and save
                combined_image = Image.fromarray(combined)
                watermarked_image_path = os.path.join(
                    os.path.dirname(self.image_path), "watermarked_image.png"
                )
                combined_image.save(watermarked_image_path)

                self.image = combined_image
                self.image.thumbnail((500, 500))
                self.photo_image = ImageTk.PhotoImage(self.image)
                self.canvas.create_image(250, 250, image=self.photo_image)
                self.label.config(
                    text=f"Watermark added! Saved as {watermarked_image_path}"
                )
                # Open the saved watermarked image
                self.open_image(watermarked_image_path)

    root = Tk()
    my_app = WatermarkApp(root)
    root.mainloop()
