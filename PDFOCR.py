from pdf2image import convert_from_path
import easyocr
import os

# Path to your Poppler bin folder (relative or absolute)
poppler_path = os.path.join(os.getcwd(), "poppler", "poppler-24.08.0", "bin")

# Path to your PDF
pdf_path = "input.pdf"

# Convert PDF pages to images (JPG)
images = convert_from_path(pdf_path, poppler_path=poppler_path)

reader = easyocr.Reader(['en'])
full_text = ""

for i, image in enumerate(images):
    image_path = f"page_{i+1}.jpg"
    image.save(image_path, "JPEG")
    text = reader.readtext(image_path, detail=0)
    full_text += "\n".join(text) + "\n"

print(full_text)
