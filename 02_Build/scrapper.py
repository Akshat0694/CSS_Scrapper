from __future__ import print_function
import requests


def file_download(file_url):
    local_filename = file_url.split('/')[-1]
    r = requests.get(file_url, stream=True)
    if r.status_code == 200:
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()
        return local_filename
        pass
    return False


test_takers = ["tandoaks"]

for test_taker in test_takers:
    fileUrl = "http://users.fs.cvut.cz/~" + test_taker + "/test.doc"
    test = file_download(fileUrl)
    if file_download(fileUrl) is False:
        print("Error while downloading files from server.")
