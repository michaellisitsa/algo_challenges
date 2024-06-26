// rpx_20xx.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>

// https://www.learncpp.com/cpp-tutorial/constructors-and-initialization-of-derived-classes/
class ShopItem
{
public:
    std::string m_name;
    int m_cost;

    ShopItem(std::string name, int cost) : m_name(name), m_cost(cost) {};
};

class Weapon: public ShopItem
{
public:
    int m_damage;

    Weapon(std::string name, int cost, int damage)
        : ShopItem(name, cost), m_damage(damage) {};

    float getValue()
    {
        return m_cost / m_damage;
    }
};

class Armor : public ShopItem
{
public:
    int m_armor;

    Armor(std::string name, int cost, int armor)
        : ShopItem(name, cost), m_armor(armor) {};
    

    float getValue()
    {
        return m_cost / m_armor;
    }
};

class Player
{
private:
    Weapon m_weapon = Weapon("unset", 0, 0);
    Armor m_armor = Armor("unset", 0, 0);

public:
    int m_health;
    
    Player(int initialHealth) : m_health(initialHealth) {};

    void equip(Weapon weapon)
    {
        // TODO: This would make a copy of the weapon class every time
        // Should the player just store a pointer, or just mutate the weapon's properties every time?
        // But if you store a pointer then the weapon will go out of scope and the player's
        // pointer no longer points to something.
        m_weapon = weapon;
    }

    void equip(Armor armor)
    {
        m_armor = armor;
    }

    int armor()
    {
        // TODO: Ring armor to be added
        return m_armor.m_armor;
    }

    // The player can have a method to get total damage and total loss for a specific hit, or how many hits to die for a particular number
    int takeDamage(int damage)
    {
        int damage_taken = damage - armor();
        m_health -= damage_taken;
        return damage_taken;
    }
}; 


int main()
{
    Weapon weapon = Weapon { "Dagger", 8, 4 };
    Armor armor = Armor { "Leather", 13, 1 };
    Player player = Player{ 100 };
    player.equip(weapon);
    player.equip(armor);
    player.takeDamage(6);
    std::cout << player.m_health;

    // TODO:
    // We have to reduce the gradient that you die at and increase the gradient that your partner dies at.
    // Each gradient change has a cost.
    // Can we rank the cost of each gradient change and sort from best to worst?
    // We need to decide the compatible combinations in the list with the best bang for buck.
}