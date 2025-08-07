import PdfExtractor
import KeyWordSearch
from tkinter import *

## Head window for selecting PDF extraction or email search
def selection_window():
    ## Opening new windows for PDF extraction and email search
    def on_pdf_extractor():
        master.destroy()
        extractor_window()
    def on_email_search():
        master.destroy()
        search_window()
        
    ## Main selection window params
    master = Tk()
    master.title("Selection Window")
    master.geometry("800x600")
    
    ## Menu bar
    menu = Menu(master)
    master.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='Placeholder1')
    filemenu.add_command(label='Placeholder2')
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=master.quit)
    helpmenu = Menu(menu)
    menu.add_cascade(label='Help', menu=helpmenu)
    helpmenu.add_command(label='About', command=help_menu)
    
    ## Instructions message
    instructions_message = 'This is part of an Email Archive Search and Categorization Tool. Please select one of the following options to proceed:'
    messageVar = Message(master, text=instructions_message, width=400)
    messageVar.config(bg='lightblue', font=('Arial', 12))
    messageVar.grid(row=0, columnspan=2, pady=10)
    
    ## Buttons for PDF extraction and email search
    Button(master, text='PDF Extractor', command=on_pdf_extractor, width=50).grid(row=1, column=0, pady=5)
    Button(master, text='Email Search', command=on_email_search, width=50).grid(row=2, column=0, pady=5)
    
    ## Run the main loop
    master.mainloop()

## Extractor window for PDF extraction
def extractor_window():
    ## Call the PDF extractor function from PdfExtractor.py
    def call_pdf_extractor():
        if e1.get() == '' or e2.get() == '':
            error_window(1)
            return
        PdfExtractor.extract_pdfs_from_msg_files(e1.get(), e2.get())
        completed_window()
        
    ## window params
    extractor = Tk()
    extractor.title("Extractor Window")
    extractor.geometry("800x600")
    instructions_message_extractor = 'This is the PDF extractor portion of this program, please route to the correct directories below:'
    messageVar = Message(extractor, text=instructions_message_extractor, width=400)
    messageVar.config(bg='lightblue', font=('Arial', 12))
    messageVar.grid(row=0, columnspan=2, pady=10)
    Label(extractor, text='Path/to/email/archive/directory').grid(row=1)
    Label(extractor, text='Path/to/desired/pdf/archive').grid(row=2)
    Button(extractor, text='Go', command=call_pdf_extractor, width=50).grid(row=3, column=0, pady=5)
    e1 = Entry(extractor)
    e2 = Entry(extractor)
    e1.grid(row=1, column=1)
    e2.grid(row=2, column=1)
    extractor.mainloop()

def search_window():
    search = Tk()
    search.title("Search Window")
    Label(search, text='First Name').grid(row=0)
    Label(search, text='Last Name').grid(row=1)
    e1 = Entry(search)
    e2 = Entry(search)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    search.mainloop()

def help_menu():
    print("Help menu not implemented yet.")

def error_window(error_code):
    error = Tk()
    match error_code:
        case 1:
            error.title("Error Window")
            Label(error, text='Error: Invalid Directory').grid(row=0)
            Button(error, text='Ok', command=error.destroy, width=50).grid(row=1, column=0, pady=5)
        case 2:
            error.title("Error Window")
            Label(error, text='Error: No PDFs Found').grid(row=0)
            Button(error, text='Ok', command=error.destroy, width=50).grid(row=1, column=0, pady=5)
        case _:
            error.title("Error Window")
            Label(error, text='Error: Unknown Error').grid(row=0)
            Button(error, text='Ok', command=error.destroy, width=50).grid(row=1, column=0, pady=5)

def completed_window():
    completed = Tk()
    completed.title("Completed Window")
    Label(completed, text='Command Successfully Run!').grid(row=0)
    completed.mainloop()

if __name__ == "__main__":
    selection_window()
