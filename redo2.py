# Intro

def intro():

    print("\nYou walked a bit and found yourself in the Baltic Market.\nFew people come out from behind the corner.")

    print("They all wear masks. \nLead by a guy in a mask of Donald Trump.")

    print("One of them wears a mask of a bat, an other wears mask of a snake.")

    print("Next person wears mask of a mouse.\nThey all come runnning after you!\n\n")
    
    input("press ENTER to continue...>\n\n")
    
    print("While the group surrounded you so you can't escape,")

    print('the Bat, the Snake and the Mouse shout at you: "Yo, yo. You\'re gonna get sick, laaa!!!"')

    print("You get scared, but you can't run away, because closed gate and tall fence is behind you!")

    print("However, Donald Trump offers you a vaccine!\n\n")
    
    choice()

# Initial 2 Choices - positive + neutral than negative

def choice():

    print("\nWhat will you do??? \nType 1 to speak to Trump or 2 to deal with the mouse, the snake and the bat.\n\n")

    answer = input("Your choice is?...> ")

    if answer == "1":

        print("\nTrump pulls out a syringe with the vaccine and puts a needle on.")

        print('Are you a doctor?... you ask...\n"No", replies Trump.\nYou: So what\'s in the syringe?')

        print('"It\'s a nice surprise!!! Don\'t worry, we tested it." Replies Trump.')
        
        print('"...and apart from that it is mandatory laa." adding to that and laughs.\n')

        vaccine()

    elif answer == "2":

        fightSMB()

    else:

        choice()

#Choice of getting vaccine or not - sub choice positive + neutral outcome

def vaccine():

    print("\nIf you want to take the vaccine type 1, if you want to refuse, type 2.\n\n")

    vaccine_answer = input("Make choice...> ")

    if vaccine_answer == "1": #positive outcome
        
        print("\n\nYou have rolled up your sleeve up and Trump applied the vaccine.")

        print("You have been injected with a dose of not further specified class A drug.")

        print('"You go out and enjoy your night pal!", says Trump.')
        
        input("You ask: Who the hell are you?\n\n...hit ENTER to get answer...>\n")

        print('"I do this gig for charity lad...and my re-election campaign!" Replies Trump.')
        
        print('"If you like it, give me a buzz" he adds and the Snake passed you a business card')

        print("However the drug has started to kick in and you feel ecstatic!")

        print("You thank Trump and get on your way despite mild but pleasant halucinations.\n\n")

    elif vaccine_answer == "2": #neutral outcome

        print("\n\nBat, Mouse and Snake approach you and all start spitting on you.")

        print("You have problems to deflect their attack!\nYou open your mouth and shout \"Stop it!!!\"")

        print("In that moment spit from the Snake landed in your mounth.")

        print("You have swallowed the spit. \nThis made you terribly sick and you started to projectile vomit.")
        
        print("You have vomited all over the attackers.")

        print("You now deflected the attack but you feel really under the weather.\n\n")

    else:

        vaccine()

# fighting snake, mouse and bat scene  - negative outcome

def fightSMB():

    print("\n\nSnake grabs you around your body and squeezes your belly with force!")

    print("You can\'t move and the mouse started to nibble on your arm!")

    print("Bat takes down the mask. \nIt's a very pretty scouse girl and she smiles at you and winks.")
    
    print('"It was just for a laugh!" she says and passes you a bottle of fine Czech lager.')
          
    print("You all start laughing.\n\n")
    
    input("hit a ENTER to continue...>\n\n")

    print("They all take of their masks and you start chatting. They offer you a spare mask of Boris Johnson.")
    
    print("Bat, the pretty girl, asks you to come with them.")

    print("You decide to stick with them and put the mask of Boris on.")

    print("You laugh at the situation, but suddenly, a drunk scouser spotted you.")

    print("The scouser comes running after you and smashes a bottle of Stella againt your head...")

    print("...shouting \"Stitch it up you tory scum!!!\"...unaware it's just a mask.")
    
    print("You manage to withstand the blast but your face is covered by blood.\n\n")
    
    brawl()
    
def brawl():
    
    print("Do you keep cool or fight with the scouser??? Press 1 to keep your cool or 2 to fight.\n\n")
    
    fight_answer = input("Enter a 1 or 2 to continue...> \n\n")
    
    if fight_answer == "2": #positive otcome - leading back to the streets
        
        print("\n\nScouser looks next to you and punches Trump as a next logical step.\nTrump drops the syringe.")
        
        print("Scouser, still confused who is who, notices the syringe, stops fighting and grabs the syringe.")
        
        print("He rolls up his black hoodie and stubs the syringe in his arm")
        
        print("His face comes up with terrible grim and drops on the floor")
        
        print("Trump gets up looking at the body of the scouser on the floor saying,")
        
        print('"Hope he had covid, because he just wasted all my bleach in one go!!!"')
        
        print("You run away to the streets before the police arrives\n\n")
        
    elif fight_answer == "1": #negative outcome - mission fail
        
        print("\n\nYou stay in the brawl with the scouser, till the police arrives at the scene.")
    
        print("You are all arrested for possession of a class A drug that was in the syringe and an assault.")

        print("They put you all in a cage with the Bat, Mouse, Snake and the scouser")

        print("Your mission has failed!\n")

        print("Later you will catch covid.")
    
        print("Surprisingly, not from the Bat, the Snake or the Mouse from the Baltic Market...")

        print("...but from the scouser.\n")
        
    else:
        brawl()

intro()