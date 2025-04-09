from bs4 import BeautifulSoup

def extract_html_main_text(html: str) -> str:
    soup = BeautifulSoup(html, "lxml")
    main = soup.find("main") or soup.body
    return main.get_text(separator="\n") if main else soup.get_text()