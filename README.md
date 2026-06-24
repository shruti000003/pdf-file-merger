
## Markdown# 📄 PDF Merger (Python)

A simple and efficient Python script to **merge multiple PDF files** into a single PDF using the [`PyPDF2`](https://pypi.org/project/PyPDF2/) library.

---

## 🚀 Features
- Merge multiple PDF files into one.
- Preserve the original page order.
- Works on **Windows, macOS, and Linux**.
- Lightweight and easy to use.

---

##Install dependencies

Bashpip install PyPDF2


🛠 Usage
1️⃣ Place your PDF files
Put all the PDF files you want to merge in the pdfs/ folder (or any folder you choose).
2️⃣ Run the script
Bashpython merge_pdfs.py

3️⃣ Output
The merged PDF will be saved as:
merged_output.pdf


📜 Example Code (merge_pdfs.py)
Pythonimport os
from PyPDF2 import PdfMerger

def merge_pdfs(input_folder, output_file):
    merger = PdfMerger()

    # Get all PDF files in the folder
    pdf_files = [f for f in os.listdir(input_folder) if f.lower().endswith(".pdf")]
    pdf_files.sort()  # Sort alphabetically to maintain order

    if not pdf_files:
        print("❌ No PDF files found in the folder.")
        return

    for pdf in pdf_files:
        file_path = os.path.join(input_folder, pdf)
        try:
            merger.append(file_path)
            print(f"✅ Added: {pdf}")
        except Exception as e:
            print(f"⚠️ Could not add {pdf}: {e}")

    merger.write(output_file)
    merger.close()
    print(f"\n🎉 Merged PDF saved as: {output_file}")

if __name__ == "__main__":
    merge_pdfs("pdfs", "merged_output.pdf")
