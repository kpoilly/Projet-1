all: SequenceTests

SequenceTests: SequenceTests.o ValidateSequence.o
	g++ -m32 SequenceTests.o ValidateSequence.o -o SequenceTests


ValidateSequence.o: ValidateSequence.asm
	nasm -f elf32 -g ValidateSequence.asm

SequenceTests.o: SequenceTests.cpp
	g++ -c -m32 SequenceTests.cpp




