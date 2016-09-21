squashfs_reader : main.o superblock.o
	g++ -o squashfs_reader main.o superblock.o

main.o : main.cpp
	g++ -c -o main.o main.cpp

superblock.o : squashfs_superblock.cpp squashfs_superblock.h
	g++ -c -o superblock.o squashfs_superblock.cpp

clean : 
	rm -rf *.o squashfs_reader
