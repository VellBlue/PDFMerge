import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader, PdfWriter


def select_files():
    file_paths = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    selected_files.delete(0, tk.END)  # Pulisce la lista dei file selezionati
    for file_path in file_paths:
        selected_files.insert(tk.END, file_path)


def merge_pdfs():
    file_paths_to_merge = list(selected_files.get(0, tk.END))
    output_pdf_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])

    if file_paths_to_merge and output_pdf_path:
        pdf_writer = PdfWriter()

        for filepath in file_paths_to_merge:
            pdf_reader = PdfReader(filepath)
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)

        with open(output_pdf_path, 'wb') as output_file:
            pdf_writer.write(output_file)
            info_label.config(text=f"Il PDF è stato creato con successo in:\n{output_pdf_path}")


# Creazione dell'interfaccia grafica
root = tk.Tk()
root.title("Unisci PDF")

select_button = tk.Button(root, text="Seleziona file", command=select_files)
select_button.pack(pady=10)

selected_files = tk.Listbox(root, width=50, height=10)
selected_files.pack()

merge_button = tk.Button(root, text="Unisci PDF", command=merge_pdfs)
merge_button.pack(pady=10)

info_label = tk.Label(root, text="", wraplength=300)
info_label.pack(pady=10)

root.mainloop()
