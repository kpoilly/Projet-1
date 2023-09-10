//POILLY KILYAN
//000460014
//INFO F-105

#include <iostream>
#include <string>
#include "Store.hpp"
#include "Aisle.hpp"
#include "Item.hpp"

int main(){
	//INIT :
	Store store ("Test Store", 5, 30);
	std::map<Item, int> shipment; //Liste des items reçu en magasin pour le receiveShipment.
	Item baguette ("Baguettes", static_cast< float >(0.8));
	Item lait ("Briques de lait", static_cast< float >(0.6));
	Item biscuit ("Paquets de biscuits", static_cast< float >(2.7));
	Item pomme ("Pommes", static_cast< float >(0.4));
	Item eau ("Bouteilles d'eau", static_cast< float >(0.3));
	Item banane ("Bananes", static_cast< float >(0.2));
	Item TV ("Téléviseurs", static_cast< float >(2000));
	shipment[baguette] = 17;
	shipment[lait] = 11;
	shipment[biscuit] = 23;
	shipment[pomme] = 12;
	shipment[eau] = 15;
	shipment[TV] = 6;
	shipment[banane] = 18;
	std::map<Item, int> order; //Liste des items retirés du magasin pour le sell.
	order[baguette] = 7;
	order[biscuit] = 12;
	order[eau] = 3;

	//Test des méthodes de la classe STORE :
	store.receiveShipment(shipment); //Ici, les méthodes Aisle::add, Aisle::getNumber et Item::getName sont utilisées.
	store.describe(); //Ici, les méthodes Aisle::describe et Item::getPrice sont utilisées.
	store.sell(order); //Ici, les méthodes Aisle::remove et Item::getName sont utilisées.
	store.describe(); //Ici, les méthodes Aisle::describe et Item::getPrice sont utilisées.
	std::cout<<"\nTest getActifs (valeur total des items) : "<<store.getActifs()<<"€\n"<<std::endl;
	for(int i=1;i<=5;i++){
	std::cout<<"Test getAisle (pointeur vers rayon #"<<i<<"): "<<store.getAisle(i)<<std::endl;}
	return 0;
	}
