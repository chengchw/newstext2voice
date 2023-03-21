import docx2txt
import langid

class LanguageDetector:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def extract_text(self):
        # Extract text from Word document
        text = docx2txt.process(self.file_path)
        # Split text into paragraphs
        paragraphs = text.split('\n\n')
        # Detect language of each paragraph
        lang_paragraphs = [(p, langid.classify(p)[0]) for p in paragraphs]
        return lang_paragraphs