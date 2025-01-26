import concurrent.futures
import requests

#Using python executors we will download files from different urls in internet
URLS = ['https://www.gutenberg.org/cache/epub/1342/pg1342.txt',
        'https://gutenberg.org/cache/epub/730/pg730.txt',
        'https://gutenberg.org/cache/epub/1513/pg1513.txt']

#You will need to create a folder called download at the local directory where you run program
#Or change the url where you want to download the file
FILES = ['download/Pride_and_Prejudice_by_Jane_Austen.txt',
        'download/Oliver_Twist_By_Charles_Dickens.txt',
        'download/Romeo_and_Juliet_by_William_Shakespeare.txt']

# download files
def download(url, filename, timeout):
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes
    if (response.status_code == 200):
        with open(filename, "wb") as file:
            file.write(response.content)

# with statement can be used to shutdown and cleanup futures
#alternately you can use for loop with shutdown at the end
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    download_future = []
    for i in range(len(URLS)):
        future = executor.submit(download, URLS[i], FILES[i], 120)
        download_future.append(future)

    for future in concurrent.futures.as_completed(download_future):
        try:
            future.result() # block until file download is complete
        except Exception as exc:
            print(exc)
        else:
            print("Download success!")