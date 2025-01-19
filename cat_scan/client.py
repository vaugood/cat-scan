from io import StringIO
from io import TextIOWrapper

from .core import get_document

class CatScan:
    def __init__(self, urls_txt:TextIOWrapper=None):
        if not urls_txt:
            raise ValueError("urls_txt received None. Expected text file object.")
        
        self.documents = None
        
        # Parse urls.txt and store urls in a list
        file_lines = urls_txt.readlines()
        self.urls = [
            line[:-1].strip() for line in file_lines if line[0] != "#" and line != "\n"
        ]

    def get_documents(self):
        docs = {}
        for url in self.urls:
            # Create file object for document
            document = StringIO()

            # Fetch document contents and store as a variable
            contents = get_document(url)

            # If contents exist
            if contents:
                # Write contents to document instance
                document.write(contents)
                # Update the docs dictionary
                docs.update({url:document})
                
        self.documents = docs