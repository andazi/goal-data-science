import time

def delay_print(text):
    for cha in text:
        print(cha, end='', flush=True)
        time.sleep(0.05)
    print()
    time.sleep(0.1)



def story():
    delay_print('You find youself standing at the edge of the Dense and Mysterious Enchanted Forest')
    delay_print('The towering trees loom overhead, and the air is filled with the sweet scent of wildflowers')
    delay_print('you can hear the gentle rustling of leaves and the distant hum of an unknown creature')

def over():
    delay_print('Your spirit floats as hands stretched out from darkness drag your soul')
    delay_print('You are DEAD')

def wrong_choice():
    delay_print('Unknown choice, you are dead')
    over()

def fork_path():
    delay_print('As you venture deeper into the forrest, the path forks')
    delay_print('To you Left, you see a narrow, well-trodden trail leading to a glowing clearing.')
    delay_print('To your Right, a more rugged and overgrown path descends into the Darkness')

def glowing_clearing():
    delay_print('You follow the path to the left, and it leads you to a beautiful, moonlit clearing')
    delay_print('At the center, you find the Enchanted amulet hanging from a tree branch, radiating with an ethernal light')
    delay_print('As you reach out to take it')
    delay_print('You feel  an overhelming sense of peace and enlightenment')

def return_from_clearing():
    delay_print('With the enchanted Amulet at hand, you journey back to the realm of Eldoria.')
    delay_print('with the enchanted Amulet and the peaceful way to which you acquire it, you choose to settle down and live a peaceful life')

def darkness_within():
    delay_print('You decided to brave the rugged path to the right')
    delay_print('The further you go, the darker it becomes and eerie sounds fill the air')
    delay_print('Suddenly, you encounter a shadowy creature with piercing red eyes.')
    delay_print('It growls menacingly, and you can feel the evil presence')
    delay_print('You wonder, do you confront the shadowy creature or not')

def confrontation():
    delay_print('You choose to confront the shadowy creature.')
    delay_print('With courage, you engage in a fierce battle,')
    delay_print('As you raise your weapon, the creature vanishes into a wisp of smoke')
    delay_print('With eyes open wide and focus as steady as the mountain')
    delay_print('The creature appeared behind you, striking the fragile expose part of body')
    delay_print('flying in the air, your eyes caught your detached body drenched with red wine brought forth from thy veins')
    over()

def escape():
    delay_print('You chose to apply the great tactics of Andazi, and choose to escape with no second thought')
    delay_print('The shadowy creature shocked at your action chose to pursue')
    delay_print('escape upon escape, destruction upon destrustion, you found out there is no way for escape')
    delay_print('At death call, you notice the shadowy creature dodging the liquid on the cave floor')

def hopeless():
    delay_print('you decide to keep escaping till ended up with nowhere')
    delay_print('The shadowy creature decides to strike you fast to avoid another chase again')
    over()

def strikeback():
    delay_print('you decided to take your chances and fetch the nearest liquid with your shield')
    delay_print('you splashed the liquid on the shadowy creature and it started burning it')
    delay_print ('you picked your sword dipped in the liquid and strike the shadowy creature till its destruction')
    delay_print('you found a redish glowing power crystal from conquest')

def return_from_darkness():
    delay_print('Having experience the true nature of Death')
    delay_print('You decided to pick the power crystal and trace your way back, leaving the fight for those with death wish')


def gameStart():
    story()
    fork_path()

    choice = input('Do you go left or Right? ')
    choice = choice.lower()
    if 'left' in choice:
        glowing_clearing()
        return_from_clearing()
    elif 'right' in choice:
        darkness_within()
        choice = input('Do you confronts creature? YES or No ')
        choice = choice.lower()
        if 'yes' in choice:
            confrontation()
        elif 'no' in choice:
            escape()
            choice = input('Do you try your luck with the liquid or keep escaping?').lower()
            if 'yes' in choice:
                strikeback()
                return_from_darkness
            elif 'no' in choice:
                hopeless()
            else:
                wrong_choice()
        else:
            wrong_choice()
            
    else:
        wrong_choice()

    delay_print('Thanks for playing!!!')
    


gameStart()
