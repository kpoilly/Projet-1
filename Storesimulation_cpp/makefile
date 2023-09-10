FLAGS= -std=c++14 -ggdb3 -Wpedantic -Wall -Wextra -Wconversion -Weffc++ -Wstrict-null-sentinel -Wold-style-cast -Wnoexcept -Wctor-dtor-privacy -Woverloaded-virtual -Wsign-promo -Wzero-as-null-pointer-constant -Wsuggest-final-types -Wsuggest-final-methods -Wsuggest-override
CXX= g++
MAIN= Test.cpp
OUT= CalTest.out

all: $(OUT)

$(OUT): Store.o Aisle.o Item.o $(MAIN)
	$(CXX) $(FLAGS) $(MAIN) Store.o Aisle.o Item.o -o $(OUT)

Item.o: Item.cpp Item.hpp
	$(CXX) $(FLAGS) -c Item.cpp

Aisle.o: Aisle.cpp Aisle.hpp
	$(CXX) $(FLAGS) -c Aisle.cpp

Store.o: Store.cpp Store.hpp
	$(CXX) $(FLAGS) -c Store.cpp

.PHONY : clean
clean:
	rm *.o *.out;
