from days.day_091.files.helpers import *


def day_091():
    title("COLOR-PAL GEN")
    from flask import Flask, render_template, request
    from PIL import Image
    import io
    import numpy as np
    from collections import Counter
    import os

    template_folder_path = os.path.join(os.path.dirname(__file__), "files", "templates")
    app = Flask(
        __name__,
        template_folder=template_folder_path,
    )

    # Function to extract colors from an Image object
    def extract_colors(image, num_colors=10):
        image = image.resize((150, 150))  # Resize to speed up processing time
        # Extract RGB values
        pixels = np.array(image)
        pixels = pixels.reshape(-1, 3)

        # Count frequencies of each color
        counter = Counter([tuple(color) for color in pixels])

        # Sort colors by frequency
        most_common = counter.most_common(num_colors)

        # Convert RGB to hex and return
        colors = []
        for rgb, _ in most_common:
            hex_color = "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])
            colors.append(hex_color)

        return colors

    # Route to upload an image file and display most common colors
    @app.route("/", methods=["GET", "POST"])
    def upload_file():
        if request.method == "POST":
            # Check if the post request has the file part
            if "file" not in request.files:
                return render_template("upload.html", error="No file part")

            file = request.files["file"]

            # If user does not select file, browser also submit an empty part without filename
            if file.filename == "":
                return render_template("upload.html", error="No selected file")

            # Verify if the file is an image based on its mimetype
            if file and file.mimetype.startswith("image/"):
                try:
                    # Rewind the file to the beginning
                    file.seek(0)

                    # Read image file
                    image = Image.open(
                        file.stream
                    )  # Use file.stream to open the file directly

                    # Get most common colors
                    colors = extract_colors(image)

                    return render_template(
                        "result.html", colors=colors, image_file=file
                    )

                except Exception as e:
                    return render_template(
                        "upload.html", error=f"Error processing image: {str(e)}"
                    )
            else:
                return render_template(
                    "upload.html", error="Uploaded file is not an image."
                )

        return render_template("upload.html")

    if __name__ == "days.day_091.main":
        app.run(debug=True, use_reloader=False)
