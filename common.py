import struct

class common:
	def read_short(self, file):
		return struct.unpack("<H", file.read(2))[0]

	def read_int(self, file):
		return struct.unpack("<I", file.read(4))[0]

	def read_long(self, file):
		return struct.unpack("<Q", file.read(8))[0]

	def make_buf_int(self,buf,start,lenght):
		ret = 0
		pwr = 1
		for i in range(start,start+lenght):
			ret += ((ord(buf[i])&0xFF)*pwr)
			pwr *= 0x100
		return ret
		
	def auto_make_buf_int(self,buf,start,length):
		return (self.make_buf_int(buf,start,length), start+length)
