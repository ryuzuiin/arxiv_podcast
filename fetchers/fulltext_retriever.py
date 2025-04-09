import requests

def retrieve_fulltext(article_id: str) -> str:
    url = f"https://www.ncbi.nlm.nih.gov/pmc/articles/{article_id}/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to retrieve article: {url}")