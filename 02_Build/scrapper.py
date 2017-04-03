from __future__ import print_function
import requests


def file_download(file_url):
    local_filename = file_url.split('/')[-1]
    print(local_filename)
    r = requests.get(file_url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
    return local_filename

fileUrl = "http://users.fs.cvut.cz/~tandoaks/test.docx"

test = file_download(fileUrl)



