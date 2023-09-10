//POILLY KILYAN
//000460014
//INFO F-105

#include <iostream>
#include <iomanip>
#include <string>
#include <map>
#include <list>
#include "Store.hpp"
#include "Aisle.hpp"
#include "Item.hpp"

Store::Store(std::string name, int nbRay, int capaRay):m_name(name), m_cap(nbRay), m_capR(capaRay), m_aisles(){
	for (int nb=1; nb<=nbRay; nb++){
		Aisle nouv (nb, capaRay);
		m_aisles[nb] = nouv;}}


float Store::getActifs(){
	//renvoie la valeur totale de tous les articles dans le magasin (sum).
	float sum = 0.0;
	for(std::map<int, Aisle>::iterator it = m_aisles.begin(); it != m_aisles.end(); ++it){ //Parcours des rayons
		Aisle aisle = it->second;
		std::map<Item, int> mapitems = aisle.m_items;
		for(std::map<Item, int>::iterator i = mapitems.begin(); i != mapitems.end(); ++i){ //Parcours des items du rayon
			Item itm = i->first;
			sum += (itm.getPrice())*static_cast< float >(i->second);}}
	return sum;	}

void Store::describe(){
	//renvoie une description des articles présents dans le magasin : prix moyen, prix maximal, prix moyen par allée, etc.
	std::cout<<std::fixed<<std::setprecision(2);
	std::cout<<"\nINVENTAIRE:\n"<<std::endl;
	float maxs = 0.0;
	float counts = 0.0;
	for(std::map<int, Aisle>::iterator it = m_aisles.begin(); it != m_aisles.end(); ++it){ //Parcours des rayons
		Aisle aisle = it->second;
		std::cout<<"Rayon numéro "<<it->first<<" : "<<std::endl;
		aisle.describe();
		std::map<Item, int> mapitems = aisle.m_items;
		if(mapitems.size()>0){
			float sumr = 0.0;
			float maxr = 0.0;
			float countr = 0.0;
			for(std::map<Item, int>::iterator i = mapitems.begin(); i != mapitems.end(); ++i){ //Parcours des items du rayon
				Item itm = i->first;
				countr += static_cast< float >(i->second);
				sumr += (itm.getPrice())*static_cast< float >(i->second);
				if(itm.getPrice()>maxr){maxr = itm.getPrice();}}
			std::cout<<"	Le prix maximal de ce rayon est de "<<maxr<<"€"<<std::endl;
			std::cout<<"	Le prix moyen de ce rayon est de "<<sumr/countr<<"€"<<std::endl;
			if(maxr>maxs){maxs = maxr;}
			counts += countr;
			}}
	std::cout<<"Le prix maximal du magasin est de "<<maxs<<"€"<<std::endl;
	std::cout<<"Le prix moyen du magasin est de "<<Store::getActifs()/counts<<"€"<<std::endl;}

void Store::receiveShipment(std::map<Item, int> shipment){
	//prend une liste contenant des articles et leurs quantités respectifs et les ajoute au magasin si celui-ci a suffisamment d’espace.
	std::cout<<"\nLIVRAISON:\n"<<std::endl;

	for(std::map<Item, int>::iterator iter = shipment.begin(); iter != shipment.end(); ++iter){ //Parcours des items du shipment
		Item itmtoadd = iter->first;
		std::string itmName = itmtoadd.getName();
		std::cout<<"\nItem : "<<itmName;
		int nb = iter->second;
		bool added = false;
		for(std::map<int, Aisle>::iterator it = m_aisles.begin(); it != m_aisles.end(); ++it){ //Parcours des rayons
			Aisle aisle = it->second;
			std::map<Item, int> mapitems = aisle.m_items;
			for(std::map<Item, int>::iterator i = mapitems.begin(); i != mapitems.end(); ++i){ //Parcours des items du rayon
				Item itm = i->first;
				if(itm.getName() == itmName){
					if (aisle.add(itmtoadd, nb)){
						m_aisles[aisle.getNumber()] = aisle;
						std::cout<<nb<<" "<<itmName<<" ont été ajoutés au rayon numéro "<<aisle.getNumber()<<std::endl;
						added = true;}}
 		}}
		if(not added){
		//Si l'item n'a été ajouté à aucun rayon (Qu'un même item n'a été trouvé dans aucun des rayons afin de lui ajouter, on ajoute l'item au premier rayon rencontré qui contient assez de place
			std::cout<<"\nCet item n'est pas déjà présent dans le magasin, il va être ajouté à un rayon qui a de la place !\n"<<std::endl;
			for(std::map<int, Aisle>::iterator j = m_aisles.begin();j != m_aisles.end();j++){
				Aisle aisle = j->second;
				if (not added and aisle.add(itmtoadd, nb)){
					m_aisles[aisle.getNumber()] = aisle;
					std::cout<<nb<<" "<<itmName<<" ont été ajoutés au rayon numéro "<<aisle.getNumber()<<std::endl;
					added = true;}}

			if(not added){std::cout<<"Il n'y a pas assez de place dans le magasin pour y ajouter cet item !"<<std::endl;}
		}}}

void Store::sell(std::map<Item, int> order){
	//prend une liste contenant des articles et leurs quantités respectives et les retire du magasin, si celui-ci en a suffisamment. Sinon, elle met cette quantité à zéro.
	std::cout<<"\nCOMMANDE:\n"<<std::endl;
	for(std::map<Item, int>::iterator iter = order.begin(); iter != order.end(); ++iter){ //Parcours des items du order
		Item itmtoremove = iter->first;
		std::string itmName = itmtoremove.getName();
		int nb = iter->second;
		for(std::map<int, Aisle>::iterator it = m_aisles.begin(); it != m_aisles.end(); ++it){ //Parcours des rayons
			Aisle aisle = it->second;
			std::map<Item, int> mapitems = aisle.m_items;
			for(std::map<Item, int>::iterator i = mapitems.begin(); i != mapitems.end(); ++i){ //Parcours des items du rayon
				Item itm = i->first;
				if(itm.getName() == itmName){aisle.remove(itmtoremove, nb);std::cout<<nb<<" "<<itmName<<" ont été retirés du rayon numéro "<<aisle.getNumber()<<std::endl;m_aisles[aisle.getNumber()] = 							     aisle;}
				}}}}

Aisle* Store::getAisle(int nb){
	//envoie un pointeur vers le rayon avec le numéro de rayon correspondant.
	return &m_aisles[nb];
	}

