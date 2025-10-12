# include <iostream>
# include <string>
struct move_des{
       std::string m_name;
       int power;   
};
struct Pokemon{
    std::string name;
    int hp;
    int attack;
    int defence;
    int speed;
    move_des moves[4];
    int initialhp;
};
void create_pokemon(Pokemon &p){
   std::cout<<"Name:";
   std::cin>>p.name;
   std::cout<<"HP(1-200):";
   std::cin>>p.hp;
   std::cout<<"Attack(1-100):";
   std::cin>>p.attack;
   std::cout<<"Defence(1-100):";
   std::cin>>p.defence;
   std::cout<<"speed(1-100):";
   std::cin>>p.speed;
   std::cout<<"Enter move names with respective power levels of 4 moves seperated by spaces"<<std::endl;
   std::cout<<"( Eg Format: ThunderShock 40 QuickAttack 30 Agility 0 Thunder 70 )"<<std::endl;
   std::cout<<std::endl;
   std::cout<<"moves:";
   for(int i=0;i<4;i++){
    std::cin>>p.moves[i].m_name>>p.moves[i].power;
   }
   p.initialhp=p.hp;
}
void attack(Pokemon &attacker, Pokemon &defender, int move_index){
    std::cout<<attacker.name<<" used "<<attacker.moves[move_index].m_name<<"!"<<std::endl;
    int damage;
    if (defender.defence!=0){
        damage=(attacker.moves[move_index].power)*attacker.attack/defender.defence;
    }
    else{
        damage=(attacker.moves[move_index].power)*attacker.attack;
    }
    std::cout<<defender.name<<" took "<<damage<<" damage!"<<std::endl;
    if (defender.hp>=damage){
        defender.hp=defender.hp-damage;
    }
    else{
        defender.hp=0;
    }
    std::cout<<std::endl;
}
void display_stats(Pokemon &pokemon){
    std::cout<<pokemon.name<<" - "<<"HP: "<<pokemon.hp<<"/"<<pokemon.initialhp<<", Attack: "<<pokemon.attack<<", Defence: "<<pokemon.defence<<", Speed: "<<pokemon.speed<<std::endl;
    std::cout<<"Moves:";
    for (int j=0;j<4;j++){
       std::cout<<pokemon.moves[j].m_name<<" ("<<pokemon.moves[j].power<<")";
       if (j<3){
          std::cout<<", ";   
       }
    }
    std::cout<<std::endl;
}
int main(){
   //To create first pokemon
   std::cout<<"Create first pokemon"<<std::endl;
   Pokemon pokemon1;
   create_pokemon(pokemon1);
   std::cout<<std::endl;
   //To create second pokemon
   std::cout<<"Create second pokemon"<<std::endl;
   Pokemon pokemon2;
   create_pokemon(pokemon2);
   std::cout<<std::endl;
   std::cout<<std::endl;

    //Display initial stats
    display_stats(pokemon1);
    std::cout<<std::endl;
    display_stats(pokemon2);
    std::cout<<std::endl;
    
    //Determine which pokemon will attack
    Pokemon attacker;
    Pokemon defender;
    if(pokemon1.speed>pokemon2.speed){
        attacker=pokemon1;
        defender=pokemon2;
    }
    else{
        attacker=pokemon2;
        defender=pokemon1;
    }
    int move_index;
    std::cout<<"Enter move index of "<<attacker.name<<"'s move (Move indexes start from 0) :"<<std::endl;
    std::cin>>move_index;
    
    attack(attacker, defender, move_index);
    if(pokemon1.speed>pokemon2.speed){
        pokemon2=defender;
    }
    else{
        pokemon1=defender;
    }

    display_stats(defender);
    std::cout<<std::endl;

    //check if defender fainted
    std::string is_fainted="false";
    if (defender.hp=0){
         is_fainted="true";
    }
    std::cout<<defender.name<<" fainted: "<<is_fainted<<std::endl;
}
