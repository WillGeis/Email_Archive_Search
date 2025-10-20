import os
import extract_msg

def extract_pdfs_from_msg_files(root_directory, pdf_archive_directory):
    if not os.path.exists(pdf_archive_directory):
        os.makedirs(pdf_archive_directory)

    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename.endswith('.msg'):
                msg_path = os.path.join(dirpath, filename)
                msg = extract_msg.Message(msg_path)
                for attachment in msg.attachments:
                    if attachment.longFilename and attachment.longFilename.endswith('.pdf'):
                        pdf_path = os.path.join(pdf_archive_directory, attachment.longFilename)
                        with open(pdf_path, 'wb') as pdf_file:
                            pdf_file.write(attachment.data)
                        print(f"Extracted {attachment.longFilename} to {pdf_archive_directory}")