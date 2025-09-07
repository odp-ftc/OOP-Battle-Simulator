import random
import BananaBoss
from goblin import Goblin
from hero import Hero

def main():
    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    # Create a hero
    hero = Hero("Jeremy")

    

    # Create goblins ༼ ºل͟º ༽ ༼ ºل͟º ༽ ༼ ºل͟º ༽
    goblins = [Goblin(f"Goblin {i+1}", "green") for i in range(3)]

    # Keep track of stats
    defeated_goblins = 0
    total_damage = 0
    rounds_survived = 0
    boss_beat = False
    # Battle Loop 
    while hero.is_alive() and any(goblin.is_alive() for goblin in goblins):
        print("\nNew Round!")
        rounds_survived += 1
        # Hero's turn to attack
        target_goblin = random.choice([goblin for goblin in goblins if goblin.is_alive()])
        damage = hero.strike()
        print(f"Hero attacks {target_goblin.name} for {damage} damage!")
        target_goblin.take_damage(damage)
        total_damage += damage

        # Check if the target goblin was defeated
        if not target_goblin.is_alive():
            defeated_goblins += 1
            print(f"{target_goblin.name} has been defeated!")

        # Goblins' turn to attack
        for goblin in goblins:
            if goblin.is_alive():
                damage = goblin.attack()
                print(f"{goblin.name} attacks hero for {damage} damage!")
                hero.receive_damage(damage)
        
    # Determine outcome
    if hero.is_alive():
        print(f"\nThe hero has defeated all the goblins! ༼ ᕤ◕◡◕ ༽ᕤ")
    else:
        print(f"\nThe hero has been defeated. Game Over. (｡•́︿•̀｡)")

    if hero.is_alive():
        print("BOSS TIME")
        boss = BananaBoss.BananaMan("BananaMan")
        while hero.is_alive() and boss.is_alive():
            damage = hero.strike()
            boss.take_damage(damage)
            damage = boss.attack()
            hero.receive_damage(damage)
    
    if hero.is_alive():
        print(f"\nThe hero has defeated the BOSS! ༼ ᕤ◕◡◕ ༽ᕤ")
        boss_beat = True

    else:
        print(f"\nThe hero has been defeated. Game Over. (｡•́︿•̀｡)")


    # Final tally of goblins defeated
    print(f"\nTotal goblins defeated: {defeated_goblins} / {len(goblins)}")
    print("")
    print("")
    print("---------------BATTLE STATS---------------")
    print(f"\nTotal Damage Dealt by Hero: {total_damage}")
    print(f"\nTotal Rounds: {rounds_survived}")
    if boss_beat:
        print("Boss Defeated")

if __name__ == "__main__":
    main()
