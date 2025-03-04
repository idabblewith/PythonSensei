from days.day_090.files.helpers import *


def day_090():
    title("PDF TO AUDIOBOOK")
    from gtts import gTTS
    import os
    from pypdf import PdfReader
    from pypdf.errors import PdfReadError
    import tempfile
    import platform
    import subprocess

    def extract_text_from_pdf(pdf_path):
        # Open the PDF file
        with open(pdf_path, "rb") as f:
            reader = PdfReader(f)
            text = ""

            # Check if the PDF is encrypted
            if reader.is_encrypted:
                try:
                    # Attempt to decrypt with an empty password or a known password
                    reader.decrypt("")
                except PdfReadError:
                    return "The PDF file is encrypted and requires a password."

            # Read each page in the PDF
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text()
        return text

    def text_to_speech(text, speed=1.0):
        # Create a temporary file for the audio
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        temp_file.close()

        # Convert text to speech using gTTS
        tts = gTTS(text=text, lang="en", slow=False)
        tts.save(temp_file.name)

        # Play the audio file using the appropriate command based on the OS
        if platform.system() == "Darwin":  # macOS
            subprocess.call(["afplay", temp_file.name])
        elif platform.system() == "Linux":
            subprocess.call(["mpg321", temp_file.name])
        elif platform.system() == "Windows":
            subprocess.call(["start", temp_file.name], shell=True)

        # Note: The speed parameter isn't directly supported by gTTS
        # Speed would need to be handled by the player or by pre-processing the audio

        # Clean up the temporary file after playing (or handle as needed)
        os.unlink(temp_file.name)

    if __name__ == "days.day_090.main":
        # Replace 'example.pdf' with your PDF file path
        pdf_path = os.path.join(os.path.dirname(__file__), "files", "example.pdf")

        # Extract text from PDF
        nls("Extracting text from PDF...")
        pdf_text = extract_text_from_pdf(pdf_path)

        # Convert text to speech
        nls("Converting text to speech...")
        text_to_speech(pdf_text)
        nls("Done!")
