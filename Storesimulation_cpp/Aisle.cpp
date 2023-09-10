//POILLY KILYAN
//000460014
//INFO F-105

#include <iostream>
#include <map>
#include "Aisle.hpp"
#include "Item.hpp"

Aisle::Aisle():m_items(), m_nbRayon(0), m_capRayon(0), m_etat(0){}
Aisle::Aisle(int nb, int cap):m_items(), m_nbRayon(nb), m_capRayon(cap), m_etat(0){}

void Aisle::describe(){
	//imprime les éléments présents au rayon, ainsi que leurs prix et leurs quantités.
	if(not m_items.size()){std::cout<<"	Ce rayon est vide."<<std::endl;}
	else{
		std::cout<<"Dans ce rayon il y a :"<<std::endl;
		for (std::map<Item,int>::iterator it = m_items.begin(); it != m_items.end(); ++it){
			Item item = it->first;
			std::cout<<"	- "<<it->second<<" "<<item.getName()<<" au prix de "<<item.getPrice()<<"€"<<std::endl;}}
	}

bool Aisle::add(Item item, int nbItems){
	//ajoute le nombre spécifié d’articles au rayon.
	std::cout<<"Ajout de l'item au rayon #"<<m_nbRayon<<"... "<<std::endl;
	if (not(m_items.count(item))){ //On vérifie si l'item existe dans le rayon, sinon on le crée.
		m_items[item] = 0;}

	if (m_etat + nbItems <= m_capRayon){
		m_etat += nbItems;
		m_items[item] += nbItems;
		return true;}
	else{
		std::cout<<"Capacité du rayon insuffisante pour ajouter autant d'items."<<std::endl;
		return false;}}

void Aisle::remove(Item item, int nbItems){
	//supprime le nombre spécifié d’articles au rayon.
	m_items[item] -= nbItems;
	m_etat -= nbItems;
	if (m_items[item] <= 0){
		m_items.erase(item);}}

int Aisle::getNumber(){
	return m_nbRayon;}
