import requests
from bs4 import BeautifulSoup
import time
import os

base_url = "https://www.azlyrics.com"
artist_url = "https://www.azlyrics.com/e/eminem.html"

headers = {
    "User-Agent": "Mozilla/5.0"
}

def get_song_links(artist_url):
    response = requests.get(artist_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    links = []

    # All song links are in divs with class 'listalbum-item'
    for div in soup.find_all("div", class_="listalbum-item"):
        a_tag = div.find("a")
        if a_tag and a_tag['href'].startswith("../lyrics/eminem"):
            full_link = base_url + a_tag['href'][2:]  # remove '../' from path
            links.append(full_link)
    return links

def scrape_lyrics(song_url):
    try:
        response = requests.get(song_url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # Lyrics are inside a <div> with no attributes 
        divs = soup.find_all("div", class_=False, id=False)
        for div in divs:
            text = div.get_text(strip=True)
            if len(text) > 200:  # simple heuristic to filter
                return div.get_text(separator="\n").strip()
    except Exception as e:
        print(f"Error scraping {song_url}: {e}")
    return None

def main():
    links = get_song_links(artist_url)
    print(f"Found {len(links)} songs.")

    if not os.path.exists("eminem_lyrics"):
        os.makedirs("eminem_lyrics")

    for i, link in enumerate(links):
        print(f"[{i+1}/{len(links)}] Scraping {link}")
        lyrics = scrape_lyrics(link)
        if lyrics:
            title = link.split("/")[-1].replace(".html", "")
            with open(f"eminem_lyrics/{title}.txt", "w", encoding="utf-8") as f:
                f.write(lyrics)
        else:
            print("No lyrics found.")
        time.sleep(1.5)

if __name__ == "__main__":
    main()
