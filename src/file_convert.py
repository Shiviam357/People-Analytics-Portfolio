import pdfplumber

def get_pdf_text(file_path):
    """
    Opens a PDF and bundles all text into a single string.
    """
    all_text = ""
    
    with pdfplumber.open(file_path) as pdf:
        # Loop through every page in the PDF
        for page in pdf.pages:
            # Extract the text
            page_content = page.extract_text()
            
            # If text exists, add it to our master string
            if page_content:
                all_text += page_content + "\n"
                
    return all_text
