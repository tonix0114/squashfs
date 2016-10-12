#-*- coding:utf-8 -*-
import sys
from common import common
from compressor import *
from squash_common import *

compressor_list = ( ZlibCompressor(), )


class Inode(common):
	def __init__(self, image):
		self.squash_imgae = image
		self.blocks = 0
		self.block_ptr = 0
		self.data = 0
		self.fragment = 0
		self.frag_bytes = 0
		self.gid = 0
		self.inode_number = 0
		self.mode = 0
		self.offset = 0
		self.start = 0
		self.symlink = 0
		self.time = 0
		self.type = 0
		self.uid = 0
		self.sparse = 0
		self.xattr = 0


class SuperBlock(common):

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

	def setStructure(self, image):
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

class FragmentEntry(common):
	def __init__(self):
		self.start_block = 0
		self.size = 0
		self.unused = 0

	def setStructure(self, image):
		self.start_block = self.read_long(image)
		self.size = self.read_int(image)
		self.unused = self.read_int(image)

	def setBufToStructure(self, block, offset):
		self.start_block, offset = self.auto_make_buf_int(block, offset, 8)
		self.size, offset = self.auto_make_buf_int(block, offset, 4)
		self.unused, offset = self.auto_make_buf_int(block, offset, 4)
		return offset

class XattrTable(common):
	def __init__(self):
		self.xattr_table_start = ""
		self.xattr_ids = ""
		self.unused = ""

	def setStructure(self, image):
		self.xattr_table_start = self.read_long(image)
		self.xattr_ids = self.read_int(image)
		self.unused = self.read_int(image)

class SquashFsFile():
	def __init__(self, name, parent):
		self.name = name
		self.parent = parent
		self.child  = []
		self.inode = ""

class SquashFsImage(SuperBlock):
	def __init__(self, image):
		# 스쿼시 파일 시스템 이미지		
		self.image = open(image, 'rb')

		# 슈퍼 블록    
		self.setStructure(self.image)

		# 압축 방식
		self.compressor = self.setCompressor()

		# uid / gid 테이블
		self.id_table = [None] * self.no_ids
		self.setUidGuid()

		# fragment 테이블
		self.fragment_table = []
		self.setFragmentTable()

		# inode 테이블
		self.inode_table = ""
		self.inode_index_table = {}
		self.setInodeTable()

		# directory 테이블
		self.directory_table = ""
		self.directory_index_table = {}
		self.setDirectoryTable()

		# Xattr 
		self.xattr_table = ""
		self.setXattrTable()

		# root path
		self.root = SquashFsFile("", None)
		self.pre_scan("root", SQUASHFS_INODE_BLK(self.root_inode), SQUASHFS_INODE_OFFSET(self.root_inode), self.root)



	def setCompressor(self):
		for compressor in compressor_list:
			if compressor.supported == self.compression:
				return compressor

	def read_inode(self, start, offset):
		start = self.inode_table_start + start
		bytes = self.inode_index_table[start]
		block_ptr = bytes + offset
		inode = Inode(self)


	def read_block(self, file, n):
		offset = 2
		file.seek(n , 0)
		c_byte = self.read_short(file)

		if SQUASHFS_CHECK_DATA(self.flags):
			offset = 3

		# 압축 되었으면
		if SQUASHFS_COMPRESSED(c_byte): 
			file.seek(n + offset)
			c_byte = SQUASHFS_COMPRESSED_SIZE(c_byte)
			buffer = file.read(c_byte)
			block = self.compressor.uncompress(buffer)
			return (block, n + offset + c_byte, c_byte)
		else:
			file.seek(n + offset)
			c_byte = SQUASHFS_COMPRESSED_SIZE(c_byte)
			block = file.read(c_byte)
			return (block, n + offset + c_byte, c_byte)
	def squashfs_opendir(self,start, offset, parent):
		self.read_inode(start, offset)

	def setUidGuid(self):
		index = SQUASHFS_ID_BLOCKS(self.no_ids)
		self.image.seek(self.id_table_start, 0)
		index_table = [ self.read_long(self.image) for i in range(0,index) ]

		for i in range(0, index):
			self.image.seek(index_table[i])
			block, next, bytes = self.read_block(self.image, index_table[i])
			
			offset = 0
			idx = i * (SQUASHFS_METADATA_SIZE / 4)
			while offset < len(block):
				self.id_table[idx], offset = self.auto_make_buf_int(block, offset, 4)
				idx+=1
	def setFragmentTable(self):
		index = SQUASHFS_FRAGMENT_INDEXES(self.fragments)
		self.image.seek(self.fragment_table_start, 0)
		index_table = [ self.read_long(self.image) for i in range(0, index) ]

		table = ""
		for i in range(0, index):
			block = self.read_block(self.image, index_table[i])[0]
			table += block

		offset = 0
		while offset < len(table):
			fragment_entry = FragmentEntry()
			offset = fragment_entry.setBufToStructure(table, offset)
			self.fragment_table.append(fragment_entry)
	def setInodeTable(self):
		start = self.inode_table_start
		end = self.directory_table_start
		while start < end:
			self.inode_index_table[start] = len(self.inode_table)
			block, start, bytes = self.read_block(self.image, start)
			self.inode_table += block
	def setDirectoryTable(self):
		start = self.directory_table_start
		end   = self.fragment_table_start
		while start < end:
			self.directory_index_table[start] = len(self.directory_table)
			block, start, bytes = self.read_block(self.image, start)
			self.directory_table += block
	def setXattrTable(self):
		if self.xattr_id_table_start == SQUASHFS_INVALID_BLK:
			return SQUASHFS_INVALID_BLK
		self.image.seek(self.xattr_id_table_start)
		xattr = XattrTable()
		xattr.setStructure(self.image)
		# 이 부분은 아직 구현 안해도될것 같음. ( 로보킹 스쿼시에서 사용 X ? )

	def pre_scan(self, parent_name, start, offset, parent):
		self.squashfs_opendir(start, offset, parent)

f = SquashFsImage(sys.argv[1])
print f.view()
