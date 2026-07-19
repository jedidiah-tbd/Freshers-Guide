from bs4 import BeautifulSoup
import os
import re

# ==========================
# LOCATION OF HTML FILES
# ==========================

TEMPLATE_FOLDER = "templates"

# Pages to search
PAGES = [
    "index.html",
    "fees.html",
    "screening.html",
    "four-files.html",
    "course-reg.html",
    "roadmap.html"
]

# ==========================
# READ HTML PAGE
# ==========================

def read_page(filename):

    path = os.path.join(TEMPLATE_FOLDER, filename)

    if not os.path.exists(path):
        return ""

    with open(path, "r", encoding="utf-8") as file:

        soup = BeautifulSoup(file, "html.parser")

        # Remove unwanted tags
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()

        text = soup.get_text(separator=" ")

        text = re.sub(r"\s+", " ", text)

        return text.strip()


# ==========================
# LOAD ALL PAGES
# ==========================

def load_website():

    pages = {}

    for page in PAGES:

        pages[page] = read_page(page)

    return pages


# ==========================
# SIMPLE SEARCH
# ==========================

def search_website(question):

    question = question.lower()

    pages = load_website()

    best_page = None

    best_score = 0

    best_text = ""

    keywords = question.split()

    for page, text in pages.items():

        lower = text.lower()

        score = 0

        for word in keywords:

            if word in lower:
                score += 1

        if score > best_score:

            best_score = score
            best_page = page
            best_text = text

    if best_score == 0:

        return None

    return {

        "page": best_page,

        "content": best_text

    }


# ==========================
# TEST
# ==========================

if __name__ == "__main__":

    result = search_website(
        "What documents are needed for screening?"
    )

    if result:

        print("Found in:", result["page"])
        print(result["content"][:700])

    else:

        print("Nothing found.")