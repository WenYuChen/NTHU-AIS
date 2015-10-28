import requests

def http(method, url, **kwargs):
    resp = requests.request(method, url, headers=head, **kwargs)
    resp.encoding = 'big5'
    return resp

def print_to_file(name, contents, filename):
	print('[' + name + ']\n' + contents, file=open(filename, 'w', encoding='big5'))