import file_magic
import file_convert
import info_extract

# This will hold all our "Candidate" dictionaries
hr_database = []

for filename in file_magic.pdf_files:
    # Get the text
    path = f"Incoming/{filename}"
    raw_text = file_convert.get_pdf_text(path)
    
    # Extract info
    email = info_extract.find_email(raw_text)
    phone = info_extract.find_phone(raw_text)
    
    # Create a 'Row' (Dictionary)
    candidate_row = {
        "File": filename,
        "Email": email,
        "Phone": phone
    }
    
   # 2. Package into a Dictionary
    candidate_info = {
        "File": filename,
        "Email": email,
        "Phone": phone
    }
    
    # 3. Store in the big list
    hr_database.append(candidate_info)
