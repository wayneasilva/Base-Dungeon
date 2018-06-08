from player_data import Player
from monsters import Monster
from skills import *
from Menu import *

#This method holds the main game data and initiates dungeon/player/mob data.
def init_dungeon():
    #Press 1 to being game. 1 is type int.
    start = int(input('Press 1 to begin: '))
    #If anything except 1 is pressed game does not start and player is prompted again.
    while start != 1:
        start = int(input('Press 1 to begin: '))
    #When Player enters 1 they are asked for their name.
    #my_player is instantiated with the entered name above. ^
    if start == 1:
        your_name = input('Enter your name: ')
        #Not all properties of my_player are currently being used.
        my_player = Player(name=your_name, player_lvl=0, current_exp=0, lvlup_exp=10, HP=10, MP=10,
                           player_atk=1, weapon='One Punch', skills='One Punch', inventory=['One Punch'])

    #Sets current room number to 1.
    room_num = 1
    #Sets number of enemies required to clear room to 3.
    #enemy_num = 3

    #Tells player current room.
    print('You are in room number: ', room_num)

    #This line checks if poring is dead. If False = fight.
    for i in range(3):
        # Create instance of class Monster.

        enemy = Monster('slime', 1, 'Poring', 1, 1, 3, 3, 4, 'feather')
        #enemy_health = enemy.mob_type
        #enemy_lvl = enemy.lvl
        #enemy_name = enemy.name
        #enemy_atk = enemy.atk_power
        #enemy_matk = enemy.matk_power
        enemy_health = enemy.HP
        #enemy_mana = enemy.MP
        #enemy_exp = enemy.exp_value
        #enemy_swag = enemy.loot

        #Adjust monster instance health for additional use.
        def enemy_property_adjust():
            enemy_health = enemy.HP
        #This will be full heal later.
        player_health = my_player.HP
        player_mana = my_player.HP
        # Start encounter with poring.
        print('You encounter a ', enemy.name)
        #while enemy.is_alive == True:
        for enemy_counter in range (3):
            #Prompts player to take an action.
            action = int(input('Press 1 to attack: '))
            #Action with value 1 leads to an attack on poring.
            if action == 1:
                #Player attack phase.
                print('You attack ', enemy.name, 'for ', my_player.player_atk, 'damage.')
                enemy_health -= my_player.player_atk
                print(enemy.name, ' has', enemy_health, 'left.')
                #Enemy attack phase
                print(enemy.name, 'attacks you for', enemy.atk_power)
                player_health -= enemy.atk_power
                print('You have ', player_health, ' left.')

            #If Poring dies (HP <= 0) do:
            if enemy_health <= 0:
                #Congratulate player on their victory over poring1.
                print('Congratulations! You killed', enemy.name, '!')
                #Alert player of exp received.
                print('You receive ', enemy.exp_value, 'experience!')
                #Calculate exp and update player current_exp.
                my_player.current_exp = my_player.current_exp + enemy.exp_value
                print(my_player.current_exp)
                #Alert player of loot received.
                print('You recieve ', enemy.loot, '! It has been placed in your inventory!')
                #Add loot (str) to inventory (list).
                my_player.inventory.append(enemy.loot)
                print(my_player.inventory)
                #Update number of enemies to beat.
                enemy_counter += 1
                #Reset enemy values for new encounter
                enemy_property_adjust()
                #Check to see if player leveled up, if True: self.levelup().
                if my_player.current_exp >= my_player.lvlup_exp:
                    #Fix this!! Need to full heal on level up and other instances.
                    player_health = my_player.HP
                    player_mana = my_player.MP
                    my_player.level_up()
                    stats = vars(my_player)
                    print(stats)



#def encounter(my_player):
#    poring = Monster('Poring', 1, 1, 3, 3, 4, 'feather', False)
#    poring_dead = False
#    print('You have encountered a', poring.name)
#
#    while poring.HP > 0:
#        input('1 = Attack')
#        action = int(input('Pick an action '))
#        if action == 1:
#            print('You attack the ', poring, 'for ', my_player.player_atk)
#            poring.HP = poring.HP - my_player.player_atk
#            print(poring.HP)
#
#            return my_player







