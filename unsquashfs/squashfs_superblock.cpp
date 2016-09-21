#include "squashfs_superblock.h"

void squashfs_superblock::read(FILE * fp)
{
	if( fp )
	{
		fread(&(squashfs_superblock::st_block), 1, sizeof(struct squashfs_super_block), fp); 	
	}
}

void squashfs_superblock::view(void)
{
	printf("\t[+] s_magic\t\t\t: 0x%x\n", squashfs_superblock::st_block.s_magic);
	printf("\t[+] inodes\t\t\t: 0x%x\n", squashfs_superblock::st_block.inodes);
	printf("\t[+] mkfs_time\t\t\t: 0x%x\n", squashfs_superblock::st_block.mkfs_time);
	printf("\t[+] block_size\t\t\t: 0x%x\n", squashfs_superblock::st_block.block_size);
	printf("\t[+] fragments\t\t\t: 0x%x\n", squashfs_superblock::st_block.fragments);
	printf("\t[+] compression\t\t\t: 0x%x\n", squashfs_superblock::st_block.compression);
	printf("\t[+] block_log\t\t\t: 0x%x\n", squashfs_superblock::st_block.block_log);
	printf("\t[+] flags\t\t\t: 0x%x\n", squashfs_superblock::st_block.flags);
	printf("\t[+] no_ids\t\t\t: 0x%x\n", squashfs_superblock::st_block.no_ids);
	printf("\t[+] s_major\t\t\t: 0x%x\n", squashfs_superblock::st_block.s_major);
	printf("\t[+] s_minor\t\t\t: 0x%x\n", squashfs_superblock::st_block.s_minor);
	printf("\t[+] root_inode\t\t\t: 0x%llx\n", squashfs_superblock::st_block.root_inode);
	printf("\t[+] bytes_used\t\t\t: 0x%llx\n", squashfs_superblock::st_block.bytes_used);
	printf("\t[+] id_table_start\t\t: 0x%llx\n", squashfs_superblock::st_block.id_table_start);
	printf("\t[+] xattr_id_table_start\t: 0x%llx\n", squashfs_superblock::st_block.xattr_id_table_start);
	printf("\t[+] inode_table_start\t\t: 0x%llx\n", squashfs_superblock::st_block.inode_table_start);
	printf("\t[+] directory_table_start\t: 0x%llx\n", squashfs_superblock::st_block.directory_table_start);
	printf("\t[+] fragment_table_start\t: 0x%llx\n", squashfs_superblock::st_block.fragment_table_start);
	printf("\t[+] lookup_table_start\t\t: 0x%llx\n", squashfs_superblock::st_block.lookup_table_start); 
}
