import wikipediaapi

def get_formatted_lines(page_title):
    wiki_wiki = wikipediaapi.Wikipedia('en',
                                       extract_format=wikipediaapi.ExtractFormat.WIKI,
                                       user_agent="YourApp/1.0 (https://yourapp.com)")
    page = wiki_wiki.page(page_title)

    if not page.exists():
        print("Page not found.")
        return []

    formatted_lines = []

    for section in page.sections:
        for line in section.text.split('\n'):
            if line.strip():
                formatted_lines.append(line.strip())

    return formatted_lines

if __name__ == "__main__":
    page_title = "Python (programming language)"
    lines = get_formatted_lines(page_title)
    
    for line in lines:
        print(line)
