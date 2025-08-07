import os
import glob
import shutil
import extract_msg

def search_keywords_in_msg(file_path, keywords):
    try:
        msg = extract_msg.Message(file_path)
        msg_body = msg.body.lower()
        msg_subject = msg.subject.lower()
        msg_sender = msg.sender.lower()
        
        for keyword in keywords:
            if keyword in msg_body or keyword in msg_subject or keyword in msg_sender:
                return True
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return False

def main():
    base_dir = r"C:\\Users\\u235211\\Documents\\####EMAIL BACKUPS"
    temp_dir = os.path.join(os.path.dirname(__file__), '.temp')
    
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    
    keywords = input("Enter keywords separated by commas: ").lower().split(',')
    keywords = [keyword.strip() for keyword in keywords]
    
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.msg'):
                file_path = os.path.join(root, file)
                if search_keywords_in_msg(file_path, keywords):
                    shutil.copy(file_path, temp_dir)
                    print(f"Copied: {file_path}")

if __name__ == "__main__":
    main()
