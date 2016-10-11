SQUASHFS_COMPRESSED_BIT = (1 << 15)
SQUASHFS_CHECK = 2
SQUASHFS_METADATA_SIZE  = 8192

def SQUASHFS_ID_BYTES(A): 
	return A * 4
def SQUASHFS_ID_BLOCKS(A): 
	return ((SQUASHFS_ID_BYTES(A) + SQUASHFS_METADATA_SIZE - 1) / SQUASHFS_METADATA_SIZE)
def SQUASHFS_ID_BLOCK_BYTES(A):
	return	(SQUASHFS_ID_BLOCKS(A) * 8)
def SQUASHFS_BIT(flag, bit):
	return (((flag >> bit) & 1)!=0)
def SQUASHFS_CHECK_DATA(flag):
	return SQUASHFS_BIT(flag, SQUASHFS_CHECK)
def SQUASHFS_COMPRESSED(B):
	return ((B & SQUASHFS_COMPRESSED_BIT) == 0)
def SQUASHFS_COMPRESSED_SIZE(B):
	if ((B) & ~SQUASHFS_COMPRESSED_BIT):
		return (B) & ~SQUASHFS_COMPRESSED_BIT
	else:
		return SQUASHFS_COMPRESSED_BIT