//POILLY KILYAN
//000460014
//INFO F-105

#ifndef DEF_ITEM
#define DEF_ITEM

#include <string>

class Item{

	public:
	Item();
	Item(std::string name, float price);
	std::string getName();
	float getPrice();
	bool operator<(const Item& t) const{ //Définition de l'opérateur < pour la classe Item afin d'utiliser des Item comme clés d'un map et éviter l'erreur.
		return this->m_itName < t.m_itName;}

	private:
	std::string m_itName;//Nom de l'item
	float m_itPrice; //Prix de l'item
};

#endif
