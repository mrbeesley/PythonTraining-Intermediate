from reader.compressed.gzipped import opener as gzip_opener
from reader.compressed.bzipped import opener as bz2_opener

__all__ = ['gzip_opener', 'bz2_opener']