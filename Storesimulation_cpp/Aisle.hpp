//POILLY KILYAN
//000460014
//INFO F-105

#ifndef DEF_AISLE
#define DEF_AISLE

#include <iostream>
#include <map>
#include "Item.hpp"

class Aisle{

	public:
	Aisle();
	Aisle(int nb, int cap);
	void describe();
	bool add(Item item, int nbItems);
	void remove(Item item, int nbItems);
	int getNumber();
	std::map<Item,int> m_items; //Map contenant tous les items du rayon

	private:

	int m_nbRayon; //Numéro du rayon
	int m_capRayon; //Capacité du rayon
	int m_etat; //Etat du rayon (nombre d'Items à l'intérieur)
};

#endif
