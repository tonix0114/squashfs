import sys

from common import common

class super_block(common):
	def __init__(self):
		self.s_magic = ""
		self.inodes = ""
		self.mkfs_time = ""
		self.block_size = ""
		self.fragments = ""
		self.compression = ""
		self.block_log = ""
		self.flags = ""
		self.no_ids = ""
		self.s_major = ""
		self.s_minor = ""
		self.root_inode = ""
		self.bytes_used = ""
		self.id_table_start = ""
		self.xattr_id_table_start = ""
		self.inode_table_start = ""
		self.directory_table_start = ""
		self.fragment_table_start = ""
		self.lookup_table_start = ""
	
	def get_hexuct(self, image):
		self.s_magic = self.read_int(image)
		self.inodes = self.read_int(image)
		self.mkfs_time = self.read_int(image)
		self.block_size = self.read_int(image)
		self.fragments = self.read_int(image)
		self.compression = self.read_short(image)
		self.block_log = self.read_short(image)
		self.flags = self.read_short(image)
		self.no_ids = self.read_short(image)
		self.s_major = self.read_short(image)
		self.s_minor = self.read_short(image)
		self.root_inode = self.read_long(image)
		self.bytes_used = self.read_long(image)
		self.id_table_start = self.read_long(image)
		self.xattr_id_table_start = self.read_long(image)
		self.inode_table_start = self.read_long(image)
		self.directory_table_start = self.read_long(image)
		self.fragment_table_start = self.read_long(image)
		self.lookup_table_start = self.read_long(image)

	def view(self):
		print "[+] s_magic : " + hex(self.s_magic)
		print "[+] inodes : " + hex(self.inodes)
		print "[+] mkfs_time : " + hex(self.mkfs_time)
		print "[+] block_size : " + hex(self.block_size)
		print "[+] fragments : " + hex(self.fragments)
		print "[+] compression : " + hex(self.compression)
		print "[+] block_log : " + hex(self.block_log)
		print "[+] flags : " + hex(self.flags)
		print "[+] no_ids : " + hex(self.no_ids)
		print "[+] s_major : " + hex(self.s_major)
		print "[+] s_minor : " + hex(self.s_minor)
		print "[+] root_inode : " + hex(self.root_inode)
		print "[+] bytes_used : " + hex(self.bytes_used)
		print "[+] id_table_start : " + hex(self.id_table_start)
		print "[+] xattr_id_table_start : " + hex(self.xattr_id_table_start)
		print "[+] inode_table_start : " + hex(self.inode_table_start)
		print "[+] directory_table_start : " + hex(self.directory_table_start)
		print "[+] fragment_table_start : " + hex(self.fragment_table_start)
		print "[+] lookup_table_start : " + hex(self.lookup_table_start)


f = open(sys.argv[1])

s = super_block()
s.get_hexuct(f)
s.view()
