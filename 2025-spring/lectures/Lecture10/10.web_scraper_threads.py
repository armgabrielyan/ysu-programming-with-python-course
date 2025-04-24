import time
import threading

import httpx


def download_content(url):
    """Download content from a URL and print the status code."""
    print(f"Starting download from {url}")
    response = httpx.get(url)
    print(f"Finished downloading from {url}: Status Code {response.status_code}")


urls = ["http://example.com", "http://example.org", "http://example.net"] * 10

threads = []

start_time = time.time()

for url in urls:
    thread = threading.Thread(target=download_content, args=(url,)) # Create a thread for each URL
    threads.append(thread)
    thread.start() # Start the thread

# Wait for all threads to complete:
for thread in threads:
    thread.join()

end_time = time.time()

print(f"Multi-threading took {end_time - start_time:.2f} seconds.")
