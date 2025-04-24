import time

import httpx


def download_content(url):
    """Download content from a URL and print the status code."""
    print(f"Starting download from {url}")
    response = httpx.get(url)
    print(f"Finished downloading from {url}: Status Code {response.status_code}")


urls = ["http://example.com", "http://example.org", "http://example.net"] * 10

start_time = time.time()

for url in urls:
    download_content(url)

end_time = time.time()

print(f"Sequential took {end_time - start_time:.2f} seconds.")
