"""
LXML
get_etree(self, url, encoding=None, headers=None)
zip_dir(path)
clear_file(path)
"""
class web_crawler():
    def __init__(self, encoding="UTF-8", headers=None):
        self.encoding = encoding
        if(headers != None):
            self.headers = headers
        else:
            self.headers = {'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
            
    def get_etree(self, url, encoding=None, headers=None):
        import requests
        from lxml import etree
        if(headers == None):
            headers = self.headers
        if(encoding == None):
            encoding = self.encoding
        res = requests.get(url, headers=headers)
        content = res.content.decode(encoding=encoding, errors='strict')
        html = etree.HTML(content.encode(encoding))
        return html

    def zip_dir(path):
        import os
        import zipfile
        zf = zipfile.ZipFile('{}.zip'.format(path), 'w', zipfile.ZIP_DEFLATED)
        for root, dirs, files in os.walk(path):
            for file_name in files:
                zf.write(os.path.join(root, file_name))

    def clear_file(path):
        import shutil
        shutil.rmtree(path)
