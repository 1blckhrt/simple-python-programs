import sys
from progress_bar import start_bar

try:
    import requests
except ImportError:
    print("This program requires the requests module, please install it!")
    sys.exit()
    
CHUNK_SIZE = 10 * 1024 * 1024
    
def download_file(url: str, destination: str, bar_length: int = 15):
    response = requests.get(url, stream=True)
    
    total_bytes = int(response.headers.get("content-length", 0))
    
    last_progress = -1
    
    with open(destination, 'wb') as file:
        current_size = 0
        
        for data in response.iter_content(CHUNK_SIZE):
            if data:
                file.write(data)
                current_size += len(data)
                
                last_progress = start_bar(current_size, total_bytes, bar_length, "#", "-", last_progress)
                
    print(f"File downloaded to {destination}")
    
def main():
    url = input("Please enter a URL to a file: \n>")
    destination = input("Please enter the file name you wish to save the downloaded file as: \n>")
    
    print("Starting download!")
    download_file(url, destination)

if __name__ == "__main__":
    main()
