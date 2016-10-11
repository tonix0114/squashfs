import struct

class common:
	def read_short(self, file):
		return struct.unpack("<H", file.read(2))[0]

	def read_int(self, file):
		return struct.unpack("<I", file.read(4))[0]

	def read_long(self, file):
		return struct.unpack("<Q", file.read(8))[0]

