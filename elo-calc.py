#!/usr/bin/env python3
"""Simple program that stores and ranks albums based on the elo calculation"""
import json
import sys


# Load the json file contents into a variable
try:
    with open("./ratings.json", "r", encoding="utf8") as f:
        ratings = json.load(f)
except ValueError:
    ratings = {}

# Start banner
print('========== Welcome to your album database ==========\n')


# Show ordered ratings list
def show(ratings):
	"""Displays current ratings ordered and formatted

	Args:
		ratings (dict): Dictionary of stored ratings
	"""
	srtedcpy = sorted(ratings, key=lambda x: (ratings[x]["rating"]))
	alName = ratings[srtedcpy[i]]['name']
	alRating = ratings[srtedcpy[i]]['rating']
	print(srtedcpy)
	for i in range(len(srtedcpy)):
		print("{} : {} ({})".format(i, alName, alRating))


# Calculate updated ELO
def updElo(rat, opt, exp):
	"""Calculates the elo rating

	Args:
		rat (number): Current ranting
		opt (int): Actual score value
		exp (number): Expected score

	Returns:
		_type_: _description_
	"""
	k_factor = 24
	nElo = rat + (k_factor * (opt - exp))

	return nElo


# Calculate ELO
def getElo(dict1, dict2, opt):
	"""Calculates the relative ELOs of two albums

	Args:
		dict1 (dict): First album
		dict2 (dict): Second album
		opt (int): Preferred album
	"""
	r1 = dict1["rating"]
	r2 = dict2["rating"]
 
    # Get modified actual score
	if opt == 1:
		opt1 = 1
		opt2 = 0
	elif opt == 2:
		opt1 = 0
		opt2 = 1

    # Get transformed rating
	tr1 = 10 ** (r1 / 400)
	tr2 = 10 ** (r2 / 400)
	tot_tr = tr1 + tr2

    # Get expected scores
	e1 = tr1 / tot_tr
	e2 = tr2 / tot_tr

    # Get updated elo
	newR1 = updElo(r1, opt1, e1)
	newR2 = updElo(r2, opt2, e2)

	dict1["rating"] = round(newR1, 2)
	dict2["rating"] = round(newR2, 2)


# Run main prog
def run():
    """Run the main ELO program"""
    dct = {}
    nw = input("Input new album: ")

    dct["name"] = nw
    dct["rating"] = 2500

    if len(ratings) == 0:
        print("Great first entry! Looking forward to more.")

    else:
        print("Which is better? 1 or 2?")
        for dets in ratings.values():
            print("1: " + dct["name"])
            print("2: " + dets["name"])
            try:
                opt = int(input(">>> "))
                getElo(dct, dets, opt)
            except ValueError:
                print("Invalid choice.")
                sys.exit()

    ratings[len(ratings) + 1] = dct
    with open("./ratings.json", "w", encoding="utf8") as f:
        json.dump(ratings, f)

    print("\n********** DONE ***********")
    print("Current standings: ")
    show(ratings)


# Entry point
def entry():
    """Program entry point"""
    print('Select an option: \n')
    print('1. Make new entry')
    print('2. Show current rankings')
    print('3. Quit')

    try:
        option = int(input(""))

        if option == 1:
            run()
        elif option == 2:
            show(ratings)
        elif option == 3:
            sys.exit()
        else:
            print("***************************")
            print("Invalid option. Try again: ")
            entry()
    except ValueError:
        print("***************************")
        print("Kindly use numeric value options 1, 2 or 3")
        entry()


if __name__ == "__main__":
    entry()
