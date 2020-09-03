import os

from scrapy.http import TextResponse, Request
def fake_response_from_file(file_name, url=None):
    if not url:
        url = 'http://www.example.com'

    request = Request(url=url)
    if not file_name[0] == '/':
        responses_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(responses_dir, file_name)
    else:
        file_path = file_name
    filePointer=open(file_path, 'rb')
    file_content =filePointer.read()
    filePointer.close()
    response = TextResponse(url=url,
        request=request,
        body=file_content)

    return response
