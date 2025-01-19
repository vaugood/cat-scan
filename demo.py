from datetime import datetime
import os
from urllib.parse import urlparse

import cat_scan.client


def main():
    # Open urls.txt
    urls_txt = open('urls.txt','r')

    # Create a scan instance and pass in the urls_txt text file object
    scan = cat_scan.client.CatScan(urls_txt)
    # Get documents
    scan.get_documents()

    # Make output folder if it doesn't exist
    if not os.path.exists("output"):
        os.makedirs("output")

    # Save documents to the outputs folder
    for d in scan.documents:
        # Parse URL and use the URL parts for the file name
        document_url_parsed = urlparse(d)
        base_url = document_url_parsed.netloc
        last_url_part = document_url_parsed.path.split("/")[-1].split(".")[0]

        file_name = f"{base_url}-{last_url_part}-{datetime.now().timestamp()}.html"

        # Stage the document file for saving
        document = open(f"output/{file_name}","w")
        # Write the document contents to the document file
        document.write(scan.documents.get(d).getvalue())

if __name__ == "__main__":
    main()