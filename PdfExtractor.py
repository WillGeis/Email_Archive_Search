import os
import extract_msg

def extract_pdfs_from_msg_files(root_directory, pdf_archive_directory):
    # Create the pdf archive directory if it doesn't exist
    if not os.path.exists(pdf_archive_directory):
        os.makedirs(pdf_archive_directory)

    # Walk through the directory tree
    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename.endswith('.msg'):
                msg_path = os.path.join(dirpath, filename)
                msg = extract_msg.Message(msg_path)
                # Iterate through all attachments in the .msg file
                for attachment in msg.attachments:
                    if attachment.longFilename and attachment.longFilename.endswith('.pdf'):
                        pdf_path = os.path.join(pdf_archive_directory, attachment.longFilename)
                        # Save the PDF attachment to the pdf archive directory
                        with open(pdf_path, 'wb') as pdf_file:
                            pdf_file.write(attachment.data)
                        print(f"Extracted {attachment.longFilename} to {pdf_archive_directory}")

if __name__ == "__main__":
    root_directory = r'C:\\Users\\u235211\\OneDrive - Trane Technologies\\Desktop\\Stuff\\CustOnbMDMS\\####EMAIL BACKUPS'
    pdf_archive_directory = r'C:\\Users\\u235211\\Documents\\Email_Archive_Search\\pdf_archive'
    extract_pdfs_from_msg_files(root_directory, pdf_archive_directory)