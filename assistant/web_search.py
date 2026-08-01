import webbrowser
import urllib.parse


def search_web(query):
    """
    Search Google for the given query.
    """

    encoded_query = urllib.parse.quote(query)

    url = f"https://www.google.com/search?q={encoded_query}"

    webbrowser.open(url)

    return f"Searching Google for {query}."