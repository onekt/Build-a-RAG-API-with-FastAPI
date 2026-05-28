from pypdf import PdfReader

def load_pdf(file_path):
    reader = PdfReader(file_path)
    text=""
    
    for page in reader.pages:
        text += page.extract_text()
        return text
    
if __name__=="__main__":
    text = load_pdf("documents/doc.pdf")
    print (text)