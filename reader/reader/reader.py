import os
from reader.compressed import bzipped, gzipped

extension_map = {
    '.bz2': bzipped.opener,
    '.gz': gzipped.opener
}

class Reader:
    def __init__(self, filename):
        extenstion = os.path.splitext(filename)[1]
        opener = extension_map.get(extenstion, open)
        self.f = opener(filename, 'rt')

    def close(self):
        self.f.close()

    def read(self):
        return self.f.read()