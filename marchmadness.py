# @Author Ben Thomas
# @Version 2.0

# I strongly recommend if you don't know what march madness is to do quick research
# on how the bracket works before diving into this source code
# however if you don't want to you will probably be fine

# import aid modules
import random
import time

# list of the teams
west = ["Kansas", "UCLA", "Gonzaga", "Uconn", "Saint Mary's", "Texas Christian",
        "North Western", "Arkansas", "Illinois", "Boise St.", "Arizona St.",
        "VCU", "Iona", "Grand Canyon", "UNC Asheville", "Howard"]
east = ["Purdue", "Marquette", "Kansas St", "Tennessee", "Duke", "Kentucky",
        "Michigan State", "Memphis", "Florida Atlantic", "USC", "Providence",
        "Oral Roberts", "Louisiana", "Montana State", "Vermont", "Farleigh Dickinson"]
south = ["Alabama", "Arizona", "Baylor", "Virginia", "San Diego St.", "Creighton",
         "Missouri", "Maryland", "West Virginia", "Utah St.", "NC State", "Charleston",
         "Furnam", "UCSB", "Princeton", "Texas A-M Corpis Christi"]
midwest = ["Houston", "Texas", "Xavier", "Indiana", "Miami", "Iowa St.", "Texas A&M",
           "Iowa", "Auburn", "Penn St.", "Mississippi St.", "Drake", "Kent St.",
           "Kennesaw St.", "Colgate", "North Kentucky"]

# the names of each division
names = ["east", "south", "west", "midwest"]

# the divisions matrix
master = [east, south, west, midwest]


# functions

# This function finds and replaces a team and puts the new team in the same seed
def team_edit(division_edit):
    # print the current teams
    print("Current teams in the division: ")
    for each_team in range(len(division_edit)):
        print(f"{each_team + 1}", division_edit[each_team])

    # remove the desired team
    team_remove = input("Which team do you want to remove: ")
    while team_remove not in division_edit:
        team_remove = input("Which team do you want to remove: ")
    index = division_edit.index(team_remove)
    division_edit.remove(team_remove)
    print(team_remove, "removed")

    # add the desired team
    team_add = input("Which team do you want to add: ")
    division_edit.insert(index, team_add)
    print(team_add, "added")
    print("New Teams: ")

    # print the new divisions
    for each_team in range(len(division_edit)):
        print(f"{each_team + 1}", division_edit[each_team])
    return division_edit


# this function takes seeds and bases the win percentage off of the lower seed
def odds(lower, higher, lst1):
    # get the lower seed
    lower_seed = lst1.index(lower)

    # create a random number
    d = random.randint(1, 17)

    # if lower seed is less then the random number return
    # the lower seed otherwise return the higher seed
    if d > lower_seed:
        return lower
    else:
        return higher


# this loops through a division and prints the teams and seeds
def print_matchups(lst):
    for TEAM in range(0, len(lst), 2):
        print(lst[TEAM], "vs", lst[TEAM + 1])
        print()


# main program

# welcome message
print("Welcome to march madness everything")

# ask the user for there choice make the answer
# not case-sensitive and store their choice
print("If you would like to simulate march madness type 's', if you would like to make you own bracket type b, "
      "If you would like to add new teams type 'n', if you would like to exit the program type 'e'")
choice = input("enter your choice right here: ").lower()

# make the main program run continuously
while True:

    # you chose an invalid choice keep asking continuously for a good choice
    while choice != "b" and choice != "n" and choice != "s" and choice != "e":
        print("If you would like to simulate march madness type 's', if you would like to make you own bracket type b, "
              "If you would like to add new teams type 'n', if you would like to exit the program type 'e'")
        choice = input("enter your choice right here: ").lower()

    # the bracket option
    while choice == "b":

        # print the matchups
        print("your matchups are: ")
        print()

        # loop through the master list and get the match count
        for i in range(len(master)):
            match_count = (len(west) // 2)

            # print the divisions names with the name list
            print("Your Matchups for the", names[i], "are: ")
            print()

            # print the matches with the seeding associated with each team
            for x in range(match_count):
                print(x + 1, master[i][x], "vs.", 16 - x, master[i][-x - 1])
                print()
            time.sleep(5)

        # get the 4 divisions and arrange them, so they can be more easily gone
        # through in accordance to the marchmadness format for the bracket.
        # each of these list are quad set 2 matchups preset, and they ordered so
        # that the "1 section" plays "4" and "2" plays "3"
        r1_wd = [[west[15], west[0], west[8], west[7]],
                 [west[12], west[3], west[11], west[4]],
                 [west[14], west[1], west[9], west[6]],
                 [west[13], west[2], west[10], west[5]],
                 west]
        r1_sd = [[south[15], south[0], south[8], south[7]],
                 [south[12], south[3], south[11], south[4]],
                 [south[14], south[1], south[9], south[6]],
                 [south[13], south[2], south[10], south[5]],
                 south]
        r1_ed = [[east[15], east[0], east[8], east[7]],
                 [east[12], east[3], east[11], east[4]],
                 [east[14], east[1], east[9], east[6]],
                 [east[13], east[2], east[10], east[5]],
                 east]
        r1_mdw = [[midwest[15], midwest[0], midwest[8], midwest[7]],
                  [midwest[12], midwest[3], midwest[11], midwest[4]],
                  [midwest[14], midwest[1], midwest[9], midwest[6]],
                  [midwest[13], midwest[2], midwest[10], midwest[5]],
                  midwest]

        # creat the tournament list to arrange the teams into list
        # corresponding to the rounds that they have advanced to
        # tournament[i] represents a round
        tournament = [[r1_sd, r1_ed, r1_wd, r1_mdw], [], [], [], []]

        # loop through each division in round 1
        for i in range(len(tournament[0])):

            # loop through each quad set in each division exclude the last one
            for j in range(len(tournament[0][i]) - 1):

                # count every two, so you can go by match up
                for x in range(0, len(tournament[0][i][j]), 2):

                    # simplify the code by declaring the team variable
                    # instead of the long string of tokens
                    team1 = tournament[0][i][j][x]
                    team2 = tournament[0][i][j][x + 1]
                    division = tournament[0][i][-1]

                    # let the player choose between the two teams
                    # give the seed to give the player more context
                    team = input(str(division.index(team1) + 1) + " " + team1 + " or " +
                                 str(division.index(team2) + 1) + " " + team2).strip()

                    # assign the appropriate situation based off the user's choice
                    if team == team1:
                        print(division.index(team) + 1, team + " advances")
                    elif team == team2:
                        print(division.index(team) + 1, team + " advances")
                    else:
                        team = team1
                        print(division.index(team) + 1, team + " advances")

                    # add to the team to the next round
                    tournament[1].append(team)

        # loop through each round
        for i in range(1, len(tournament) - 1):

            # print the matchups with the headers
            print("round " + str(i + 1) + " matchups")
            print_matchups(tournament[i])
            print()

            # loop every 2 teams in the list to get the matchups
            for j in range(0, len(tournament[i]), 2):

                # declare team1 and team 2 to make the code more readable
                team1 = tournament[i][j]
                team2 = tournament[i][j + 1]

                # prompt the user and handle the situation appropriately
                team = input(team1 + " or " + team2).strip()
                if team == team1:
                    print(team + " advances")
                elif team == team2:
                    print(team + " advances")
                else:
                    team = team1
                    print(team + " advances")

                # add the team that advances to round 2
                tournament[i + 1].append(team)
                print()

        # final four and championship

        # make the code more readable by declaring these variables
        south_champ = tournament[-1][0]
        east_champ = tournament[-1][1]
        west_champ = tournament[-1][2]
        midwest_champ = tournament[-1][3]

        # final four
        finalist1 = input(south_champ + " or " + east_champ)
        if finalist1 != south_champ and finalist1 != east_champ:
            finalist1 = south_champ
        print(finalist1 + " advances to the finals")
        finalist2 = input(west_champ + " or " + midwest_champ)
        if finalist2 != west_champ and finalist2 != midwest_champ:
            finalist2 = west_champ
        print(finalist2 + " advances to the finals")
        print()

        # championship
        champion = input(finalist2 + " or " + finalist1)
        if champion != finalist1 and champion != finalist2:
            champion = finalist1

        print(champion + " is the champion")

        # clear the list so there is no carry over
        tournament.clear()

        # have them choose there next move if they choose a faulty
        # one they are sent to the infinite choice loop above
        choice = input("to create a bracket press 'b' to simulate marchmadness type 's' "
                       "to exit press 'e' or 'n' to continue: ").lower()
        break
    while choice == "s":

        # print the matchups
        print("your matchups are: ")
        print()

        # loop through the master list and get the match count
        for i in range(len(master)):
            match_count = (len(west) // 2)

            # print the divisions names with the name list
            print("Your Matchups for the", names[i], "are: ")
            print()

            # print the matches with the seeding associated with each team
            for x in range(match_count):
                print(x + 1, master[i][x], "vs.", 16 - x, master[i][-x - 1])
                print()
            time.sleep(5)

        # get the 4 divisions and arrange them, so they can be more easily gone
        # through in accordance to the marchmadness format for the bracket.
        # each of these list are quad set 2 matchups preset, and they ordered so
        # that the "1 section" plays "4" and "2" plays "3"
        r1_wd = [[west[15], west[0], west[8], west[7]],
                 [west[12], west[3], west[11], west[4]],
                 [west[14], west[1], west[9], west[6]],
                 [west[13], west[2], west[10], west[5]],
                 west]
        r1_sd = [[south[15], south[0], south[8], south[7]],
                 [south[12], south[3], south[11], south[4]],
                 [south[14], south[1], south[9], south[6]],
                 [south[13], south[2], south[10], south[5]],
                 south]
        r1_ed = [[east[15], east[0], east[8], east[7]],
                 [east[12], east[3], east[11], east[4]],
                 [east[14], east[1], east[9], east[6]],
                 [east[13], east[2], east[10], east[5]],
                 east]
        r1_mdw = [[midwest[15], midwest[0], midwest[8], midwest[7]],
                  [midwest[12], midwest[3], midwest[11], midwest[4]],
                  [midwest[14], midwest[1], midwest[9], midwest[6]],
                  [midwest[13], midwest[2], midwest[10], midwest[5]],
                  midwest]

        # creat the tournament list to arrange the teams into list
        # corresponding to the rounds that they have advanced to
        # tournament[i] represents a round
        tournament = [[r1_sd, r1_ed, r1_wd, r1_mdw], [], [], [], []]

        # add a space for formatting
        print()

        # loop through each division
        for i in range(len(tournament[0])):

            # loop through each quad set
            for j in range(len(tournament[0][i]) - 1):

                # go by 2 in each quad set
                for x in range(0, len(tournament[0][i][j]), 2):

                    # declare the variables to make the code more readable
                    team1 = tournament[0][i][j][x]
                    team2 = tournament[0][i][j][x + 1]
                    division = tournament[0][i][-1]

                    # choose the team and output it
                    team = odds(team1, team2, tournament[0][i][-1])
                    print(division.index(team) + 1, team + " advances")
                    print()

                    # add the team to the next round
                    tournament[1].append(team)
                    time.sleep(2)

        # loop through each round
        for i in range(1, len(tournament) - 1):

            # print out the round header and matchups
            print("round " + str(i + 1) + " matchups")
            print_matchups(tournament[i])

            # loop through each match-up
            for j in range(0, len(tournament[i]), 2):
                team1 = tournament[i][j]
                team2 = tournament[i][j + 1]

                # round[i + 1] represents teams moved onto the nex round

                # find the division by dividing by the teams place in the
                # list because the list is set up so that placement will work
                teams_per_division = len(tournament[i]) // 4
                if j // teams_per_division == 0:
                    team = odds(team2, team1, south)
                    print(south.index(team) + 1, team + " advances")
                    tournament[i + 1].append(team)
                elif j // teams_per_division == 1:
                    team = odds(team2, team1, east)
                    print(east.index(team) + 1, team + " advances")
                    tournament[i + 1].append(team)
                elif j // teams_per_division == 2:
                    team = odds(team2, team1, west)
                    print(west.index(team) + 1, team + " advances")
                    tournament[i + 1].append(team)
                else:
                    team = odds(team2, team1, midwest)
                    print(midwest.index(team) + 1, team + " advances")
                    tournament[i + 1].append(team)
                time.sleep(3)
                print()

        # the final four variables
        south_champ = tournament[-1][0]
        east_champ = tournament[-1][1]
        west_champ = tournament[-1][2]
        midwest_champ = tournament[-1][3]

        # final four
        print("On to the final four")
        finalist1 = odds(south_champ, east_champ, south)
        print(finalist1 + " advances to the finals")
        print()
        time.sleep(5)
        finalist2 = odds(west_champ, midwest_champ, west)
        print(finalist2 + " advances to the finals")
        print()
        time.sleep(5)

        # national championship
        finals_odds = random.randint(1, 10)
        if finals_odds <= 5:
            champion = finalist1
        else:
            champion = finalist2

        print(champion + " is the champion")

        tournament.clear()

        # put user in choice loop
        choice = input("to create a bracket press 'b' enter 'n' to continue editing the teams "
                       "to exit press 'e' or 's' to continue: ").lower()

    # edit the teams
    while choice == "n" or " n" in choice:

        # give the choice
        division = input(
            "Which division would you like to edit, or if you would like to "
            "stop editing type 'stop': ").lower()

        if division in names:

            # get the index of the division in master which lines up with names
            i = names.index(division)

            # get the division and set it each to the team edit
            master[i] = team_edit(master[i])

        # user choice stop
        elif division == "stop":
            choice = input("to create a bracket press 'b' to simulate marchmadness type 's' "
                           "to exit press 'e' or 'n' to continue editing teams: ").lower()
            break

        # reset the continuous loop if the user enters nonsense
        else:
            continue

    # exit choice
    while choice == "e":
        print("Goodbye")
        time.sleep(3)
        exit()
