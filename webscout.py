
import requests



# def fetch():
#     with open("recon.txt", "r") as urls:  # Use 'with' to ensure file is properly closed after its suite finishes
#         for url in urls:
#             url = url.strip()  # Correctly call strip() on the string object
#             print("Footprint report for "+url+" Web server :")
#             response = requests.get(url)  # Use a different variable name to avoid shadowing the 'requests' module
#             result = dict(response.headers)
#             for item, value in result.items():
#                 print(item + " : " + value + "\n")

def fetch_urls(file_path):
    urls_headers = []
    with open(file_path, "r") as file:
        for url in file:
            url = url.strip()
            try:
                response = requests.get(url)
                urls_headers.append((url, dict(response.headers)))
            except requests.RequestException as e:
                print(f"Failed to fetch data for {url}: {e}")
    return urls_headers