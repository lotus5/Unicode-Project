import requests

def fetch_published_doc_text():
    published_url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
    text_export_url = published_url.replace("/pub", "/export?format=txt")
    
    response = requests.get(published_url)
    response.raise_for_status()
    
    return response.text

# Example usage
print(fetch_published_doc_text())