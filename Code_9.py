def upload_file(filename):
    url = 'https://example.com/upload'
    with open(filename, 'rb') as file:
        files = {'file': file}
        response = requests.post(url, files=files)
        return response
