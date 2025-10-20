from pdf2image import convert_from_path
import easyocr
import os
import shutil

def OCR_folder(folder_path):
    if not os.path.isdir(folder_path):
        raise NotADirectoryError(f"Directory not found: {folder_path}")

    # Output folders
    output_txt = os.path.join(folder_path, "##txtfiles")
    print(f"txt folder made")
    output_named_pdf = os.path.join(folder_path, "##namedPdf")
    print(f"named pdf folder made")
    output_non_W9_pdf = os.path.join(folder_path, "##non-W9Pdf")
    print(f"non w9 pdf folder made")

    os.makedirs(output_txt, exist_ok=True)
    os.makedirs(output_named_pdf, exist_ok=True)
    os.makedirs(output_non_W9_pdf, exist_ok=True)

    poppler_path = os.path.join(os.getcwd(), "poppler", "poppler-25.07.0", "Library", "bin")
    reader = easyocr.Reader(['en'])

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)
            print(f"\nProcessing: {filename}")

            # Convert PDF pages to images
            images = convert_from_path(pdf_path, poppler_path=poppler_path)
            full_text_lines = []

            for i, image in enumerate(images):
                image_path = os.path.join(output_txt, f"temp_page_{i+1}.jpg")
                image.save(image_path, "JPEG")
                text_lines = reader.readtext(image_path, detail=0)
                full_text_lines.extend(text_lines)
                os.remove(image_path)

            # Save OCR as txt file
            txt_filename = os.path.splitext(filename)[0] + ".txt"
            txt_path = os.path.join(output_txt, txt_filename)
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write("\n".join(full_text_lines))
            print(f"Saved OCR text to: {txt_path}")

            name_line = None
            dba_line = None
            for idx, line in enumerate(full_text_lines):
                cleaned_line = line.lower().replace(" ", "")
                if "businessname" in cleaned_line:
                    # Take the line above as name
                    if idx > 0:
                        name_line = full_text_lines[idx - 1].strip().replace("\n", " ")
                    # Take the line below as DBA
                    if idx + 1 < len(full_text_lines):
                        dba_line = full_text_lines[idx + 1].strip().replace("\n", " ")
                    break

            # Copy PDF to appropriate folder
            if name_line and dba_line:
                if "ifdifferentfromabove" in dba_line.lower().replace(" ", ""):
                    new_pdf_name = f"{name_line}.pdf"
                else:
                    new_pdf_name = f"{name_line} DBA {dba_line}.pdf"

                # Sanitize filename
                new_pdf_name = new_pdf_name.replace("/", "-").replace("\\", "-")
                dest_path = os.path.join(output_named_pdf, new_pdf_name)
                shutil.copy(pdf_path, dest_path)
                print(f"Renamed PDF saved: {dest_path}")
            else:
                dest_path = os.path.join(output_non_W9_pdf, filename)
                shutil.copy(pdf_path, dest_path)
                print(f"No business name found, PDF moved: {dest_path}")

    print("\nOCR and PDF categorization complete.")
