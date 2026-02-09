import os

folder_path = 'Incoming'

# 1. Get all names, then 2. convert to lower, then 3. keep if they end with .pdf
pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]

print(f"Found {len(pdf_files)} PDF files.")
