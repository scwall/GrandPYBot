# import urllib3
# http = urllib3.PoolManager()
# r = http.request('GET', 'http://localhost:5000')
# print(r.status)
# print(r.data)
#
#
#
import requests
import os.path
def getssh(): # pseudo application code
    return os.path.join(os.path.expanduser("~admin"), '.ssh')

def test_mytest(monkeypatch):
    def mockreturn(path):
        return '/abc'
    monkeypatch.setattr(os.path, 'expanduser', mockreturn)
    x = getssh()
    assert x == '/abc/.ssh'