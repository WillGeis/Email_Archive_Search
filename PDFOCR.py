from pdf2image import convert_from_path
import pytesseract

pdf_path = r'C:\Users\u235211\Documents\Email_Archive_Search\W9_GF Operations LLC_10.2023.pdf'

# Convert PDF pages to images
images = convert_from_path(pdf_path, dpi=300)

# Run OCR on each image
for i, image in enumerate(images):
    text = pytesseract.image_to_string(image)
    print(f"Text from page {i+1}:\n{text}\n")