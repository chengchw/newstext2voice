import textconvertor as txct

tx = txct.LanguageDetector("SanFrancisco.docx")
arr = tx.extract_text()
print(arr)
