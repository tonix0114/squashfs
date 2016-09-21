#include <stdio.h>

#include "squashfs_superblock.h"


int main(int argc, char ** argv)
{
	
	if(argc < 2)
	{
		printf("[-] %s image.img", argv[0]);
		return -1;
	}
	
	FILE * fp = fopen(argv[1], "rb");
	if( !fp )
	{
		printf("[-] File Read Error");
		return -1;
	}

	squashfs_superblock s_block;
	printf("[+] Squashfs Superblock read\n");
	s_block.read(fp);
	s_block.view();	
}
