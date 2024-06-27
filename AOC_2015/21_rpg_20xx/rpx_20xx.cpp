// rpx_20xx.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>

const int INITIAL_PLAYER_HEALTH = 8;
const int INITIAL_ENEMY_HEALTH = 12;

#include <unordered_map>

const std::unordered_map<std::string, std::unordered_map<std::string, int>> WEAPONS = {
    {"Dagger", {{"Cost", 8}, {"Damage", 4}, {"Armor", 0}}},
    {"Shortsword", {{"Cost", 10}, {"Damage", 5}, {"Armor", 0}}},
    {"Warhammer", {{"Cost", 25}, {"Damage", 6}, {"Armor", 0}}},
    {"Longsword", {{"Cost", 40}, {"Damage", 7}, {"Armor", 0}}},
    {"Greataxe", {{"Cost", 74}, {"Damage", 8}, {"Armor", 0}}}};

const std::unordered_map<std::string, std::unordered_map<std::string, int>> ARMOR = {
    {"None", {{"Cost", 0}, {"Damage", 0}, {"Armor", 0}}},
    {"Leather", {{"Cost", 13}, {"Damage", 0}, {"Armor", 1}}},
    {"Chainmail", {{"Cost", 31}, {"Damage", 0}, {"Armor", 2}}},
    {"Splintmail", {{"Cost", 53}, {"Damage", 0}, {"Armor", 3}}},
    {"Bandedmail", {{"Cost", 75}, {"Damage", 0}, {"Armor", 4}}},
    {"Platemail", {{"Cost", 102}, {"Damage", 0}, {"Armor", 5}}}};

const std::unordered_map<std::string, std::unordered_map<std::string, int>> RINGS = {
    {"Damage +1", {{"Cost", 25}, {"Damage", 1}, {"Armor", 0}}},
    {"Damage +2", {{"Cost", 50}, {"Damage", 2}, {"Armor", 0}}},
    {"Damage +3", {{"Cost", 100}, {"Damage", 3}, {"Armor", 0}}},
    {"Defense +1", {{"Cost", 20}, {"Damage", 0}, {"Armor", 1}}},
    {"Defense +2", {{"Cost", 40}, {"Damage", 0}, {"Armor", 2}}},
    {"Defense +3", {{"Cost", 80}, {"Damage", 0}, {"Armor", 3}}}};

// https://www.learncpp.com/cpp-tutorial/constructors-and-initialization-of-derived-classes/
class ShopItem
{
private:
    const std::string m_name;

public:
    int m_cost;

    ShopItem(std::string name, int cost) : m_name(name), m_cost(cost){};
};

class Weapon : public ShopItem
{
public:
    int m_damage;

    Weapon(std::string name, int cost, int damage)
        : ShopItem(name, cost), m_damage(damage){};

    float getValue()
    {
        return m_cost / m_damage;
    }

    void enhance(int cost, int damage)
    {
        m_cost += cost;
        m_damage += damage;
    }
};

class Armor : public ShopItem
{
public:
    int m_armor;

    Armor(std::string name, int cost, int armor)
        : ShopItem(name, cost), m_armor(armor){};

    float getValue()
    {
        return m_cost / m_armor;
    }

    void enhance(int cost, int armor)
    {
        m_cost += cost;
        m_armor += armor;
    }
};

class Player
{
private:
    Weapon m_weapon = Weapon("Combined", 0, 0);
    Armor m_armor = Armor("Combined", 0, 0);

public:
    int m_health;

    Player(int initialHealth) : m_health(initialHealth){};

    void equip(const Weapon &weapon)
    {
        m_weapon.enhance(weapon.m_cost, weapon.m_damage);
    }

    void equip(const Armor &armor)
    {
        m_armor.enhance(armor.m_cost, armor.m_armor);
    }

    bool isAlive()
    {
        return m_health > 0;
    }

    int armor()
    {
        // TODO: Ring armor to be added
        return m_armor.m_armor;
    }

    // The player can have a method to get total damage and total loss for a specific hit, or how many hits to die for a particular number
    bool takeDamage(int damage)
    {
        int netDamage = damage - armor();
        if (netDamage > 0)
        {
            m_health -= netDamage;
        }
        return isAlive();
    }

    int giveDamage()
    {
        return m_weapon.m_damage;
    }

    int getCost()
    {
        return m_weapon.m_cost + m_armor.m_cost;
    }
};

class Battle
{
private:
    // TODO: We're copying the player and enemy classes here. Should we just store pointers?
    // But then the player and enemy classes will go out of scope and the battle class will have pointers to nothing.
    Player m_player;
    Player m_enemy;

public:
    Battle(Player player, Player enemy) : m_player(player), m_enemy(enemy){};

    bool fight()
    {
        while (m_player.isAlive() && m_enemy.isAlive())
        {
            if (!m_enemy.takeDamage(m_player.giveDamage()))
                return true;

            if (!m_player.takeDamage(m_enemy.giveDamage()))
                return false;

            std::cout << "Player: " << m_player.m_health << " Enemy: " << m_enemy.m_health << std::endl;
        }
        // Should never be hit.
        return true;
    };

    int getPlayerSpend()
    {
        return m_player.getCost();
    }
};

int main()
{
    for (const auto &weapon : WEAPONS)
    {
        std::cout << weapon.first << ": " << std::endl;
        for (const auto &attribute : weapon.second)
        {
            std::cout << "  " << attribute.first << ": " << attribute.second << std::endl;
        }
        std::cout << std::endl;
    }

    Weapon weapon = Weapon{"Dagger", 8, 5};
    Armor armor = Armor{"Leather", 13, 5};
    Weapon ring = Weapon{"Damage +1", 25, 1};
    Armor ring_armor = Armor{"Defense +1", 20, 1};
    Player player = Player{INITIAL_PLAYER_HEALTH};
    player.equip(weapon);
    player.equip(armor);

    Player enemy = Player{INITIAL_ENEMY_HEALTH};
    Weapon enemy_weapon = Weapon{"Generic", 0, 7};
    Armor enemy_armor = Armor{"Generic", 0, 2};
    enemy.equip(enemy_weapon);
    enemy.equip(enemy_armor);

    Battle battle = Battle{player, enemy};
    if (battle.fight())
    {
        std::cout << "Player wins!" << std::endl;
        std::cout << "Player spent $" << battle.getPlayerSpend() << std::endl;
    }
    else
    {
        std::cout << "Enemy wins!" << std::endl;
    };

    // TODO:
    // We have to reduce the gradient that you die at and increase the gradient that your partner dies at.
    // Each gradient change has a cost.
    // Can we rank the cost of each gradient change and sort from best to worst?
    // We need to decide the compatible combinations in the list with the best bang for buck.
}