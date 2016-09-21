#pragma once

#include <stdio.h>

#include "squashfs_structure.h"

class squashfs_superblock
{
	private:
		struct squashfs_super_block st_block;

	public:
		void read(FILE * fp); // squashfs_super_block 데이터 읽기
		void view();
};
