import random
import math
import os
#the beginning

#IMPORTANT: SKILL ACTUALLY MEANS DEFENSE!!!!!!

def start():
    Q1 = (input("Press Y or N. Click Enter to submit. "))
    if Q1 == ("Y") or Q1 == ("y"):
        str(data_test())
    elif Q1 == ("N") or Q1 == ("n"):
        print ("terminating...")
    else:
        print ("invalid input")
        str(start())
#test for task two data
def data_test():
    global name1
    global name2
    global ski1
    global str1
    global ski2
    global str2
    name1 = ("player 1")
    name2 = ("player 2")
    ski1 = 10
    str1 = 10
    ski2 = 10
    str2 = 10
    ski_mod = 0
    str_mod = 0
    if os.path.exists('D&D A.txt') == True:
        print ("Their is saved data already in this file. 'Do you want to use this data?")
        Q2 = (input("Press Y or N. Click Enter to submit. "))
        if Q2 == ("Y") or Q2 == ("y"):
            print ("Loading data...")
            str(load_player_data())
        elif Q2 == ("N") or Q2 == ("n"):
            print("OK, proceeding to manually enter player data")
            str(set_player_name())
        else:
            print("Invalid input")
            str(data_test())
    else:
        print ("No saved data detected. Proceeding to manually inputting player data")
        str(set_player_name())
#loads task two data
def load_player_data():
    #fill me in later
    print("this fetcher is currently unavailable")
    str(set_player_name())
#incase task two data is now found
def set_player_name():
    global name1
    global name2
    print ("Let's give names to our characters!")
    print ("OK, now give a name to characters one.")
    name1 = (input("Please input name of characters one "))
    print ("Good, now lets give the second character a name.")
    name2 = (input("input name of characters two "))
    print("")
    print ("Now both characters have names, let's give them attributes")
    print ("How we do this is")
    print ("each attribute is initially set to 10")
    print ("then we roll two dice")
    print ("The score on the 12 sided dice is divided by ")
    print ("the score on the 4 sided dice and rounded down.")
    print ("Then we repeat the process for each characters attributes")
    str(set_player_1_ski())
#dose what the name sais and sets player 1 skill/defense
def set_player_1_ski():
    global ski1
    global name1
    Q3 = input((name1)+(" press r to roll the 12 and 4 sided dice to determine your 'DEFENSE' "))
    if Q3 == ("r") or Q3 == ("R"):
        roll12 = random.randint(1,12)
        roll4 = random.randint (1,4)
        print ("the 12 sided rolled:")
        print (roll12)
        print ("and the 4 sided rolled:")
        print (roll4)
        print ("Good, that makes your 'DEFENSE':")
        ski1 = math.floor(((roll12)/(roll4))+(ski1))
        print (ski1)
        str(set_player_1_str())
    else:
        print ("invalid input")
        str(set_player_1_ski())
#dos this neede a comment if so: sets player 1 strength
def set_player_1_str():
    global name1
    global str1
    global ski1
    Q4 = input ((name1)+(" press 'r' again to roll the dice to determine your 'STRENGTH'"))
    if Q4 == ("r") or Q3 == ("R"):
        roll12 = random.randint(1,12)
        roll4 = random.randint (1,4)
        print ("the 12 sided rolled:")
        print (roll12)
        print ("and the 4 sided rolled:")
        print (roll4)
        str1 = math.floor(((roll12)/(roll4))+(str1))
        print ("Now your 'STRENGTH' is:")
        print (str1)
        print ("good "+ str(name1) + " and your 'DEFENSE' is " +  str(ski1))
        str(set_player_2_ski())
    else:
        print ("invalid input")
        str(set_player_1_str())
#sets player 2 skill
def set_player_2_ski():
    print("")
    global name2
    global ski2
    print ((name2)+(" now its your tern to roll the dice"))
    Q5 = input(" press 'r' to roll the dice to determine your 'DEFENSE!'")
    if Q5 == ("r") or Q2 == ("R"):
        roll12 = random.randint(1,12)
        roll4 = random.randint (1,4)
        print ("the 12 sided rolled:")
        print (roll12)
        print ("and the 4 sided rolled:")
        print (roll4)
        print ("good, that makes your 'DEFENSE':")
        ski2 = math.floor(((roll12)/(roll4))+(ski2))
        print (ski2)
        print ("press r again to roll for your'STRENGTH'")
        str(set_player_2_str())
    else:
        print ("invalid input")
        str(set_player_2_ski())
#sets player 2 strentgh
def set_player_2_str():
    print("")
    global name2
    global str2
    roll12 = random.randint(1,12)
    roll4 = random.randint (1,4)
    Q5 = input("press 'r' agen to roll the dice to determine your 'STRENGTH'")
    if Q5 == ("r") or Q3 == ("R"):
        print ("the 12 sided rolled:")
        print (roll12)
        print ("and the 4 sided rolled:")
        print (roll4)
        str2 = math.floor(((roll12)/(roll4))+(str2))
        print ("now your 'STRENGTH' is:")
        print (str2)
        print ("good "+ str(name2) + " and your 'DEFENSE' is " +  str(ski2))
        print ("now that the attributes have been set do you want to do, move on to the modifiers or reroll them")
        str(player_RR_or_MO())
    else:
        print ("invalid input")
        str(set_player_2_str())
#asks the player if thay whant to reroll ther atrabuts
def player_RR_or_MO():
    Q6 = input("to set the modifiers press 'm' or to reroll the attributes press 'r' ")
    if Q6 == ("m") or Q6 == ("M"):
        print("moving on to modifiers...")
        str(set_mod_ski())
    elif Q6 == ("r") or Q6 == ("R"):
        print("reseting...")
        str(set_player_1_ski())
    else:
        print ("invalid input")
        str(player_RR_or_MO())
#sets the defense/skill modifier
def set_mod_ski():
    global name1
    global name2
    global ski1
    global str1
    global ski2
    global str2
    global ski_mod
    print("calculating modifiers...")
    if ski1 > ski2:
        ski_mod = ski1 - ski2
    elif ski2 > ski1:
        ski_mod = ski2 - ski1
    str(set_mod_srt())
#sets the strength
def set_mod_srt():
    global name1
    global name2
    global ski1
    global str1
    global ski2
    global str2
    global ski_mod
    global str_mod

    if str1 > str2:
        str_mod = str1 - str2
    elif str2 > str1:
        str_mod = str2 - str1
    print("calculation compleat")
    print("the results are:")
    print("strength modifirer:")
    print(ski_mod)
    print("defense modifier:")
    print(str_mod)
    str(battel_start())
#start the battle off
def battel_start():
    print ("to win the battle you need to decrease your opponent's defense to '0'. To do so,")
    print("you need to roll a dice for each player and whichever player has the lowest score")
    print("has their defense decreased by the modifiers and this process continues until there is a winner.")
    str(battel_main())
#tells the player what everything is
def battel_main():
    global name1
    global name2
    global ski1
    global str1
    global ski2
    global str2
    global ski_mod
    global str_mod
    print(str(name1)+" your defense is: ")
    print(str(ski1))
    print("and your strength is: ")
    print(str1)
    print(str(name2)+" your defense is: ")
    print(str(ski2))
    print("and your strength is: ")
    print(str2)
    print("and the modifies are: ")
    print("defense mod: "+str(ski_mod))
    print("strength mod: "+str(str_mod))
    str(battel_test())
#test if the player has whon
def battel_test():
    global ski1
    global str1
    global ski2
    global str2
    if ski1 < 0 and str1 < 0:
        str(battel_p2_win())
    elif ski2 < 0 and str2 < 0:
        str(battel_p1_win())
    else:
        str(battel_attack())
#resets the modifires
def battel_reset_mods():
    global ski1
    global str1
    global ski2
    global str2
    global ski_mod
    global str_mod
    if str1 > str2:
        str_mod = str1 - str2
    elif str2 > str1:
        str_mod = str2 - str1
    if ski1 > ski2:
        ski_mod = ski1 - ski2
    elif ski2 > ski1:
        ski_mod = ski2 - ski1
    str(battel_main())
#makes the players attack
def battel_attack():
    global name1
    global name2
    global ski1
    global str1
    global ski2
    global str2
    global ski_mod
    global str_mod
    print("")
    print(str(name1)+", "+ str(name2)+" press 'R' to roll your attack")
    Q7 = input("please input your answer ")
    if Q7 == ("r")or Q7 ("R"):
        p1_atk_roll = random.randint(1,6)
        p2_atk_roll = random.randint(1,6)
        print(str(name1) + " rolled: " + str(p1_atk_roll))
        print(str(name2) + " rolled: " + str(p2_atk_roll))
    else:
        str(battel_attack())
    if p1_atk_roll < p2_atk_roll:
        print(str(name1)+" was hit")
        str(battel_p1_hit())
    elif p2_atk_roll < p1_atk_roll:
        print(str(name2)+" was hit")
        str(battel_p2_hit())
    else:
        print("the roll was a draw please reroll")
        str(battel_attack())
#when player 1 is hit
def battel_p1_hit():
    global ski1
    global str1
    global ski2
    global str2
    global ski_mod
    global str_mod
    ski1 = ski1 - ski_mod
    str1 = str1 - str_mod
    print("")
    str(battel_reset_mods())
#when player two is hit
def battel_p2_hit():
    global ski1
    global str1
    global ski2
    global str2
    global ski_mod
    global str_mod
    ski2 = ski2 - ski_mod
    str2 = str2 - str_mod
    print("")
    str(battel_reset_mods())
#when plyer 1 wins
def battel_p1_win():
    global name1
    global name2
    print("congratulations " + str(name1) + " you have win")
    str(play_again())
#when player 2 win
def battel_p2_win():
    global name1
    global name2
    print("congratulations " + str(name2) + " you have win")
    str(play_again())
#it playes again
def play_again():
    print ("do you want to play again?")
    str(start())
#the begining at the end
print("Welcome warrior! Are you ready to play Playmobile Warriors?")
str(start())
