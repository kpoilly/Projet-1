//POILLY KILYAN
//000460014
//INFO F-105

#ifndef DEF_STORE
#define DEF_STORE

#include <iostream>
#include <string>
#include <map>
#include <list>
#include "Aisle.hpp"
#include "Item.hpp"

class Store{
	public:
	Store();
	Store(std::string name, int nbRay, int capaRay);
	float getActifs();
	void describe();
	void receiveShipment(std::map<Item, int> shipment);
	void sell(std::map<Item, int> order);
	Aisle* getAisle(int nb);

	private:
	std::string m_name;//Nom donné au store
	int m_cap;//Nombre de rayons dans le store
	int m_capR;//Capacité max des rayons
	std::map<int,Aisle> m_aisles; //Dico contenant tous les rayons

};

#endif
