# 1. Squash Filesystem

> "소형화된 Device에서 사용되는 고압축 파일 시스템이다."

__소형화/최적화__된 리눅스 시스템을 만들때, 모든 바이트는 device( floppy, flash disk )에 있어서 매우 중요하다. 그렇기 때문에 __압축__이 가능한 모든곳에서 사용된다. 또한, __압축된 파일 시스템__은 주로 보관 목적(개인적 미디어 자료, 공공 보관자료에서 파일 시스템은 필수적)으로 사용된다. __squash 파일 시스템__에서는 이 모든것을 제공하게 된다.

squash 파일 시스템은 __read-only__ 파일 시스템으로 사용자가 __전체 파일시스템__ 혹은 __single 디렉토리__를 압축하고 __디바이스일 경우__에는 직접 마운트 되고, __파일일 경우__에는 __loopback 장치__를 사용하여 마운트하게 된다.

__모듈화/간결화__되어 있으며 tar archive보다 사용자에게 더 많은 유연성과 수행 속도를 제공하게 된다.
이 파일 시스템의 특징은 아래와 같다.

- DATA, inode, 디렉토리가 압축된다.

- Full uid/gids (32bits), 파일 생성 시간을 저장한다.

- 파일 시스템은 2^64 bytes를 지원한다

- inode와 디렉토리 데이터는 높은 수준으로 밀집되어 있으며, Byte로 압축되어 있다. 각각 압축된 inode는 길이가 평균 8byte씩이다. ( 정확한 길이의 변수들은 filetype에 따라, 일반적인 파일, 디렉토리, 심볼릭 링크 그리고 block/char 디바이스 inodes는 다른 크기를 가지고 있다. )

- squashfs는 1MB크기의 블록 사이즈를 지원한다. ( default size : 128Kbytes - 기본적인 4바이트 블록보다 높은 압축률을 보여준다. )

- 중복된 파일을 찾게되면 삭제하게 된다.

- Filesystem은 gzip, xz(lzma2) , lzo , lz4로 압축될 수 있다.

# 2. Filesystem Layout

> "스쿼시 파일 시스템은 최대 9개의 부분으로 나누어져 있다."

```
	 ---------------
	|  superblock   |  -- > squashfs_super_block
	|---------------|
	|  compression  |
	|    options    |
	|---------------|
	|  datablocks   |
	|  & fragments  |
	|---------------|
	|  inode table  |  -- > squashfs_inode_header
	|---------------|
	|   directory   |  -- > squashfs_dir_entry, squashfs_dir_header
	|     table     |
	|---------------|
	|   fragment	|  -- > squashfs_fragment_entry
	|    table      |
	|---------------|
	|    export     |
	|    table      |
	|---------------|
	|    uid/gid	|
	|  lookup table |
	|---------------|
	|     xattr     |  -- > squashfs_xattr_*
    |     table	 |
	 ---------------
```

## 2-1. SuperBlock
