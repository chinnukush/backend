import requests

def fetch_movie_details(movie_id):
    try:
        response = requests.get(f"https://imdb-api.pandapelisv.workers.dev/title/{movie_id}")
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return None

movie_id = "tt22898462"
details = fetch_movie_details(movie_id)
if details:
    print(details)
else:
    print("Failed to fetch movie details.")
