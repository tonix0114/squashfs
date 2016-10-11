import zlib

ZLIB_COMPRESSION = 1

class ZlibCompressor:
	def __init__(self):
		self.supported = ZLIB_COMPRESSION
		self.name="zlib"
		
	def uncompress(self, src):
		return zlib.decompress(src)



