from days.day_090.files.helpers import *


def day_090():
    title("PDF TO AUDIOBOOK")
    import PyPDF2
    import pyttsx3
    import os
    from PyPDF2.errors import PdfReadError

    def extract_text_from_pdf(pdf_path):
        # Open the PDF file
        with open(pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
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

    def text_to_speech(text, rate=200):
        # Initialize the pyttsx3 engine
        engine = pyttsx3.init()
        # Set the speech rate (default is 200 words per minute)
        engine.setProperty("rate", rate)
        # Convert the text to speech
        engine.say(text)
        # Wait for the speech to complete
        engine.runAndWait()

    if __name__ == "days.day_090.main":
        # Replace 'example.pdf' with your PDF file path
        pdf_path = os.path.join(os.path.dirname(__file__), "files", "example.pdf")

        # Extract text from PDF
        nls("Extracting text from PDF...")
        pdf_text = extract_text_from_pdf(pdf_path)

        # Convert text to speech
        nls("Converting text to speech...")
        text_to_speech(pdf_text, 300)
        nls("Done!")
