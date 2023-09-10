//POILLY KILYAN
//000460014
//INFO F-105

#include <string>
#include "Item.hpp"

Item::Item(std::string name, float price):m_itName(name), m_itPrice(price){}

std::string Item::getName(){
	//Renvoie le nom de l'item
	return m_itName;}

float Item::getPrice(){
	//Renvoie le prix de l'item
	return m_itPrice;}




