import time
import json
import operator
from tables import tablizer # custom module


def processStats(dictionary, cosmetictype):
    dictionary = dict(sorted(dictionary.items(), key=lambda item: item[1]["unlockedCount"]))
    values = []
    unlockedCount = []
    usedCount = []
    percentUsed = []
    percentUnlocked = []
    percentUsedOfUnlocked = []
    aULVP = []
    aUVP = []
    for value in dictionary:
        values.append(value)
        unlockedCount.append(str(dictionary[value]["unlockedCount"]))
        usedCount.append(str(dictionary[value]["usedCount"]))
        percentUsed.append(f"{dictionary[value]['usedCount']/len(profiles)*100:.2f}%")
        percentUnlocked.append(f"{dictionary[value]['unlockedCount']/len(profiles)*100:.2f}%")
        if dictionary[value]['unlockedCount'] == 0:
            percentUsedOfUnlocked.append("0.00%")
        else:
            percentUsedOfUnlocked.append(f"{dictionary[value]['usedCount']/dictionary[value]['unlockedCount']*100:.2f}%")
        if dictionary[value]['unlockedCount'] == 0:
            aULVP.append("0")
        else:
            aULVP.append(str(round(dictionary[value]['unlockedVP']/dictionary[value]['unlockedCount'])))
        if dictionary[value]['usedCount'] == 0:
            aUVP.append("0")
        else:
            aUVP.append(str(round(dictionary[value]['usedVP']/dictionary[value]['usedCount'])))

    twod = []
    for i in range(len(values)):
        thislist = []
        thislist.append(values[i])
        thislist.append(unlockedCount[i])
        thislist.append(usedCount[i])
        thislist.append(percentUnlocked[i])
        thislist.append(percentUsed[i])
        thislist.append(percentUsedOfUnlocked[i])
        thislist.append(aULVP[i])
        thislist.append(aUVP[i])
        twod.append(thislist)
    tablizer(twod, header=[cosmetictype.title()+" Name", "# of Users\nUnlocked", "# of Users\nUsing", "% of All Users\nUnlocked", "% of Users\nUsing", "% of Unlocked\nUsers Using", "Unlocked User\nAverage VP", "Using User\nAverage VP"], alignment=["left", "right"])


# open file and read the content in a list
with open("username.txt",errors='ignore') as f:
    usernames = f.readlines()
    usernames = [*set(usernames)]


with open("profiles.json", "r",errors='ignore') as f:
    profiles = json.load(f)

hatcounts = {
    "gold-crown": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": [],
        "unlocked": "being in the top 3 in the hall of fame at the end of the week"
    },
    "silver-crown": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": [],
        "unlocked": "being in the top 10 in the hall of fame at the end of the week"
    },
    "bronze-crown": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": [],
        "unlocked": "being in the top 30 in the hall of fame at the end of the week"
    },
    "witch-hat": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": [],
        "unlocked": "beating the hedge route of Mysterious Mansion"
    },
    "stars": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": [],
        "unlocked": "beating area 80 in Elite Expanse Hard"
    },
    "santa-hat": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": [],
        "unlocked": "beating Frozen Fjord"
    },
    "blue-santa-hat": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": [],
        "unlocked": "beating Frozen Fjord Hard"
    },
    "flames": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": [],
        "unlocked": "beating Burning Bunker"
    },
    "blue-flames": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": [],
        "unlocked": "beating Burning Bunker Hard"
    },
    "halo": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": [],
        "unlocked": "beating Monumental Migration 480"
    },
    "gold-wreath": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": [],
        "unlocked": "winning a tournament"
    },
    "spring-wreath": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": [],
        "unlocked": "winning the spring seasonal tournament"
    },
    "autumn-wreath": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": [],
        "unlocked": "winning the fall seasonal tournament"
    },
    "winter-wreath": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": [],
        "unlocked": "winning the winter seasonal tournament"
    },
    "summer-wreath": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": [],
        "unlocked": "winning the summer seasonal tournament"
    },
    "summer-olympics-wreath": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": [],
        "unlocked": "winning the summer olympics"
    },
    "summer-olympics-wreath-2": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": [],
        "unlocked": "previously winning the summer olympics (no longer obtainable)"
    },
    "winter-olympics-wreath": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": [],
        "unlocked": "winning the winter olympics"
    },
    "sunglasses": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": [],
        "unlocked": "obtaining 10 quest points"
    },
    "flower-headband": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": [],
        "unlocked": "obtaining 30 quest points"
    },
    "autumn-leaves": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": [],
        "unlocked": "beating Haunted Halls as Cybot while having a tree copied"
    },
    "fedora": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": [],
        "unlocked": "beating any region as Cent"
    },
    "coconut-holes": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": [],
        "unlocked": "beating Shifting Sands as Echelon in under 9 minutes"
    },
    "plastic-shine": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": [],
        "unlocked": "gaining access to Research Lab"
    },
    "pellets": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": [],
        "unlocked": "beating any region without collecting any pellets"
    },
    "pirate-hat": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": [],
        "unlocked": "obtaining 100 quest points"
    },
    "rose-wreath": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": [],
        "unlocked": "being a top 3 solo speedrunner or top 2 duo speedrunner"
    },
}
bodycounts = {
    "sticky-coat": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": [],
        "unlocked": "beating Toxic Territoy 20"
    },
    "toxic-coat": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": [],
        "unlocked": "beating Toxic Territoy Hard 20"
    },
    "orbit-ring": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": [],
        "unlocked": "beating Elite Expanse 80"
    },
    "clouds": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": [],
        "unlocked": "beating Endless Echo 400"
    },
    "storm-clouds": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": [],
        "unlocked": "beating Endless Echo Hard 400"
    },
    "tuxedo": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": [],
        "unlocked": "obtaining 60 quest points"
    },
    "angel-wings": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": [],
        "unlocked": "beating Monumental Migration 480 as a duo"
    },
    "one-winged-angel": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": [],
        "unlocked": "beating Monumental Migration 480 solo"
    },
    "stick": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": [],
        "unlocked": "beating Vicious Valley with 20 or more upgrade points available"
    },
    "royal-robes": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": [],
        "unlocked": "downing 25 players with snowballs in Stellar Square"
    },
    "mummy-wrap": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": [],
        "unlocked": "beating Peculiar Pyramid Hard Perimeter and Inner"
    },
    "doughnut": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": [],
        "unlocked": "obtain 150 quest points"
    }
}
achievementcounts = {
    "scientist": {
        "count":0,
        "users":[],
        "unlocked": "finding Research Lab"
    },
    "tree_tapper": {
        "count":0,
        "users":[],
        "unlocked": "beating Haunted Halls as Cybot while having a tree copied"
    },
    "snowball_mayhem": {
        "count":0,
        "users":[],
        "unlocked": "downing 25 players with snowballs in Stellar Square"
    },
    "savior": {
        "count":0,
        "users":[],
        "unlocked": "unlocking all of the heroes"
    },
    "money_moves": {
        "count":0,
        "users":[],
        "unlocked": "beating any region as Cent"
    },
    "pellet_obfuscator": {
        "count":0,
        "users":[],
        "unlocked": "beating any region without collecting any pellets"

    },
    "champion": {
        "count":0,
        "users":[],
        "unlocked": "winning a tournament"
    },
    "core_revival": {
        "count":0,
        "users":[],
        "unlocked": "beating Central Core as Necro while solo"
    },
    "peculiar_pathing": {
        "count":0,
        "users":[],
        "unlocked": "beating Peculiar Pyramid Hard Perimeter and Inner"
    },
    "ground_control": {
        "count":0,
        "users":[],
        "unlocked": "beating Vicious Valley with 20 or more upgrade points available"
    },
    "lush_sands": {
        "count":0,
        "users":[],
        "unlocked": "beating Shifting Sands as Echelon in under 9 minutes"
    },
    "baneful_bunker": {
        "count":0,
        "users":[],
        "unlocked": "beating Burning Bunker as Magmax"
    },
    "wacky_ride": {
        "count":0,
        "users":[],
        "unlocked": "beating Wacky Wonderland 80 as Ghoul"
    },
    "radioactive_dasher": {
        "count":0,
        "users":[],
        "unlocked": "beating Toxic Territory in under 5 minutes"
    },
    "serene_garden": {
        "count":0,
        "users":[],
        "unlocked": "beating Grand Garden in under 6 minutes"
    },
    "stomper": {
        "count":0,
        "users":[],
        "unlocked": "stomping 1000 enemies as Brute"
    },
    "enormous_tribute": {
        "count":0,
        "users":[],
        "unlocked": "entering the large hidden area in the bottom right corner of Burning Bunker 26"
    },
    "glacial_grouping": {
        "count":0,
        "users":[],
        "unlocked": "beating Glacial Gorge as Magno"
    },
    "magnetic_highway": {
        "count":0,
        "users":[],
        "unlocked": "beating Magnetic Monopolo with 10 or less speed"
    },
    "gardener": {
        "count":0,
        "users":[],
        "unlocked": "activating all grass enemies Grand Garden 28"
    },
    "survivalist": {
        "count":0,
        "users":[],
        "unlocked": "reaching level 100 in Stellar Square"
    },
    "mysterious_mangrove": {
        "count":0,
        "users":[],
        "unlocked": "reaching 10 victory zones in Mysterious Mansion (does not have to be 10 different zones)"
    },
    "ominous_occult": {
        "count":0,
        "users":[],
        "unlocked": "beating Ominous Occult as Glob with 2 other people"
    },
    "relentless_ridge": {
        "count":0,
        "users":[],
        "unlocked": "beating Restless Ridge as Cybot while having a slippery enemy copied"
    },
    "intense_inferno": {
        "count":0,
        "users":[],
        "unlocked": "beating Infinite Inferno as Demona in a duo"
    },
    "district_demolition": {
        "count":0,
        "users":[],
        "unlocked": "beating Dangerous District Hard 80 as Stella"
    },
    "two_winged_angel": {
        "count":0,
        "users":[],
        "unlocked": "beating Monumental Migration 480 in a duo"
    },
    "humongous_visit": {
        "count":0,
        "users":[],
        "unlocked": "beating Humongous Hollow as Boldrock"
    },
    "quintessential_quarry": {
        "count":0,
        "users":[],
        "unlocked": "beating Quiet Quarry Hard as Mirage in under 8 minutes"
    },
    "endless_expansion": {
        "count":0,
        "users":[],
        "unlocked": "beating 1000 areas of Endless Echo (does not have to be in a single run)"
    },
    "visit_grandma": {
        "count":0,
        "users":[],
        "unlocked": "finding Grandma's House in Restless Ridge Hard 40"
    },
    "traveller": {
        "count":0,
        "users":[],
        "unlocked": "beating 10000 total areas"
    },
    "victor": {
        "count":0,
        "users":[],
        "unlocked": "reaching 250 victory zones"
    },
    "one_winged_angel": {
        "count":0,
        "users":[],
        "unlocked": "beating Monumental Migration 480 solo"
    },
    "frosty_fjord": {
        "count":0,
        "users":[],
        "unlocked": "beating Frozen Fjord Hard solo"
    },
    "dipole_diversion": {
        "count":0,
        "users":[],
        "unlocked": "beating Magnetic Monopolo Dipole and Magnetic Monopole Hard Dipole"
    }
}

hat = list(hatcounts.keys())
body = list(bodycounts.keys())
achievement = list(achievementcounts.keys())

alertcosmetics = ["one-winged-angel", "summer-olympics-wreath-2", "rose-wreath", "doughnut"]

# loop through usernames
start = time.perf_counter()

userlist = []

class user:
    def __init__(self, name='', achievements=0, cosmetics=0, hats=0, bodies=0):
        self.name = ''
        self.achievements = 0
        self.cosmetics = 0
        self.hats = 0
        self.bodies = 0

for i, userprofile in enumerate(profiles):
    #print(f"[{i+1}/{len(profiles)}] {list(username.keys())[0]}")
    userinfo = user()
    username = list(userprofile.keys())[0]
    userinfo.name = username
    userdict = userprofile[username]
    userinfo.achievements = len(userdict["stats"]["achievements"])
    for h in hat:
        if userdict["accessories"]["collection"][h]:
            if h in alertcosmetics:
                print(f"{username} has {h}")
            userinfo.cosmetics+=1
            userinfo.hats+=1
            hatcounts[h]["unlockedUsers"].append(username)
            hatcounts[h]["unlockedCount"]+=1
            hatcounts[h]["unlockedVP"]+=userdict["stats"]["highest_area_achieved_counter"]
        if h == userdict["accessories"]["hat_selection"]:
            hatcounts[h]["usedUsers"].append(username)
            hatcounts[h]["usedCount"]+=1
            hatcounts[h]["usedVP"]+=userdict["stats"]["highest_area_achieved_counter"]
    for b in body:
        if userdict["accessories"]["collection"][b]:
            if b in alertcosmetics:
                print(f"{username} has {b}")
            userinfo.cosmetics+=1
            userinfo.bodies+=1
            bodycounts[b]["unlockedUsers"].append(username)
            bodycounts[b]["unlockedCount"]+=1
            bodycounts[b]["unlockedVP"]+=userdict["stats"]["highest_area_achieved_counter"]
        if b == userdict["accessories"]["body_selection"]:
            bodycounts[b]["usedUsers"].append(username)
            bodycounts[b]["usedCount"]+=1
            bodycounts[b]["usedVP"]+=userdict["stats"]["highest_area_achieved_counter"]
    for a in achievement:
        if a in userdict["stats"]["achievements"]:
            achievementcounts[a]["users"].append(username)
            achievementcounts[a]['count']+=1
    userlist.append(userinfo)

print(f"Checked {len(profiles)} profiles in {time.perf_counter()-start:.2f} seconds.")
print(f"Average time per profile: {(time.perf_counter()-start)/len(profiles):.2f} seconds.")

start = time.perf_counter()

print(f"\nHat statistics from {len(profiles)} users:")
processStats(hatcounts, "hat")

print(f"\nBody cosmetic statistics from {len(profiles)} users:")
processStats(bodycounts, "body cosmetic")

print(f"\nAchievement statistics from {len(profiles)} users:")
achievementcounts = dict(sorted(achievementcounts.items(), key=lambda item: item[1]['count'])) # sort by count
percents = []
countsachievements = []
for a in achievementcounts:
    percents.append(f"{achievementcounts[a]['count']/len(profiles)*100:.2f}%") # make percents column
    countsachievements.append(achievementcounts[a]['count']) # make counts column
twoarray = [percents, countsachievements, list(achievementcounts.keys())] # make 2d array
tablizer(list(zip(*twoarray[::-1])), header=["Achievement", "Count", "Percent"], alignment=["left", "right"]) # print table (zip is used to rotate the array)

hatcounts["usersChecked"] = len(profiles)
bodycounts["usersChecked"] = len(profiles)
achievementcounts["usersChecked"] = len(profiles)

with open('hatdata.json', 'w', encoding='utf-8') as f:
    json.dump(hatcounts, f, ensure_ascii=False, indent=4)
with open('bodydata.json', 'w', encoding='utf-8') as f:
    json.dump(bodycounts, f, ensure_ascii=False, indent=4)
with open('achievementdata.json', 'w', encoding='utf-8') as f:
    json.dump(achievementcounts, f, ensure_ascii=False, indent=4)

userlist.sort(key=operator.attrgetter('achievements'), reverse=True)
with open('achievementslb.txt', 'w', encoding='utf-8') as f:
    f.write("Name: Achievement Count\n")
    f.write("Total Achievements: 36\n")
    for u in userlist:
        f.write(f"{u.name}: {u.achievements}\n")

userlist.sort(key=operator.attrgetter('cosmetics'), reverse=True)
with open('cosmeticslb.txt', 'w', encoding='utf-8') as f:
    f.write("Name: Cosmetic Count\n")
    f.write(f"Total Cosmetics: {len(hat)+len(body)}\n")
    for u in userlist:
        f.write(f"{u.name}: {u.cosmetics}\n")

userlist.sort(key=operator.attrgetter('hats'), reverse=True)
with open('hatslb.txt', 'w', encoding='utf-8') as f:
    f.write("Name: Hat Count\n")
    f.write(f"Total Hats: {len(hat)}\n")
    for u in userlist:
        f.write(f"{u.name}: {u.hats}\n")

userlist.sort(key=operator.attrgetter('bodies'), reverse=True)
with open('bodieslb.txt', 'w', encoding='utf-8') as f:
    f.write("Name: Body Cosmetic Count\n")
    f.write(f"Total Body Cosmetics: {len(body)}\n")
    for u in userlist:
        f.write(f"{u.name}: {u.bodies}\n")

print("Saved to files.")

while True:
    # try:
    print()
    print("Enter 'cosmetic' 'achievement' or 'username' to view more detailed information, or 'exit' to exit:")
    print("NOTE: Values are not ordered in any specific order.")
    search = input("")
    if search == "exit":
        break
    elif search == "cosmetic":
        search = input("Enter a cosmetic name to view more detailed information:\n")
        if search in hat or search in body:
            usedorunlocked = input("Enter 'used' or 'unlocked' to view the users who have used or unlocked the cosmetic:\n")
            if usedorunlocked == "used":
                if search in hat:
                    print(f"Unlocked by {hatcounts[search]['unlocked']}.")
                    print(f"Unlocked: {hatcounts[search]['unlockedCount']} users ({hatcounts[search]['unlockedCount']/len(profiles):.4%})")
                    print(f"Using: {hatcounts[search]['usedCount']} users ({hatcounts[search]['usedCount']/len(profiles):.4%})")
                    print(f"Out of all users with the cosmetic unlocked, {hatcounts[search]['usedCount']/hatcounts[search]['unlockedCount']:.4%} are using it.")
                    for i, u in enumerate(hatcounts[search]["usedUsers"]):
                        print(f"{i+1}. {u}")
                elif search in body:
                    print(f"Unlocked by {bodycounts[search]['unlocked']}.")
                    print(f"Unlocked: {bodycounts[search]['unlockedCount']} users ({bodycounts[search]['unlockedCount']/len(profiles):.4%})")
                    print(f"Using: {bodycounts[search]['usedCount']} users ({bodycounts[search]['usedCount']/len(profiles):.4%})")
                    print(f"Out of all users with the cosmetic unlocked, {bodycounts[search]['usedCount']/bodycounts[search]['unlockedCount']:.4%} are using it.")
                    for i, u in enumerate(bodycounts[search]["usedUsers"]):
                        print(f"{i+1}. {u}")
            elif usedorunlocked == "unlocked":
                if search in hat:
                    print(f"Unlocked by {hatcounts[search]['unlocked']}.")
                    print(f"Unlocked: {hatcounts[search]['unlockedCount']} users ({hatcounts[search]['unlockedCount']/len(profiles):.4%})")
                    print(f"Using: {hatcounts[search]['usedCount']} users ({hatcounts[search]['usedCount']/len(profiles):.4%})")
                    print(f"Out of all users with the cosmetic unlocked, {hatcounts[search]['usedCount']/hatcounts[search]['unlockedCount']:.4%} are using it.")
                    for i, u in enumerate(hatcounts[search]["unlockedUsers"]):
                        print(f"{i+1}. {u}")
                elif search in body:
                    print(f"Unlocked by {bodycounts[search]['unlocked']}.")
                    print(f"Unlocked: {bodycounts[search]['unlockedCount']} users ({bodycounts[search]['unlockedCount']/len(profiles):.4%})")
                    print(f"Using: {bodycounts[search]['usedCount']} users ({bodycounts[search]['usedCount']/len(profiles):.4%})")
                    print(f"Out of all users with the cosmetic unlocked, {bodycounts[search]['usedCount']/bodycounts[search]['unlockedCount']:.4%} are using it.")
                    for i, u in enumerate(bodycounts[search]["unlockedUsers"]):
                        print(f"{i+1}. {u}")
            else:
                print("Invalid input")
        else:
            print("Invalid input")
    elif search == "achievement":
        search = input("Enter an achievement name to view more detailed information:\n")
        if search in achievement:
            print(f"Unlocked by {achievementcounts[search]['unlocked']}.")
            print(f"{achievementcounts[search]['count']} users ({achievementcounts[search]['count']/len(profiles):.4%}) have unlocked {search}:")
            for i, u in enumerate(achievementcounts[search]["users"]):
                print(f"{i+1}. {u}")
    elif search == "username":
        search = input("Enter a username to view more detailed information:\n")
        print(f"Username: {search}")
        hatused = "None"
        hatsunlocked = []
        for h in hat:
            if search in hatcounts[h]["usedUsers"]:
                hatused = h
            if search in hatcounts[h]["unlockedUsers"]:
                hatsunlocked.append(h)
        bodyused = "None"
        bodyunlocked = []
        for b in body:
            if search in bodycounts[b]["usedUsers"]:
                bodyused = b
            if search in bodycounts[b]["unlockedUsers"]:
                bodyunlocked.append(b)
        achievementunlocked = []
        achievementlocked = []
        for a in achievement:
            if search in achievementcounts[a]["users"]:
                achievementunlocked.append(a)
            else:
                achievementlocked.append(a)
        print(f"Hat used: {hatused}")
        print(f"{len(hatsunlocked)} hats unlocked: {','.join(hatsunlocked)}")
        print(f"Body cosmetic used: {bodyused}")
        print(f"{len(bodyunlocked)} body cosmetics unlocked: {','.join(bodyunlocked)}")
        print(f"{len(achievementunlocked)} achievements unlocked: {','.join(achievementunlocked)}")
        print(f"{len(achievementlocked)} achievements missing: {','.join(achievementlocked)}")
    else:
        print("Invalid input")


print()
print("Done")
print(f"{time.perf_counter()-start:.2f} seconds, or {(time.perf_counter()-start)/len(usernames):.2f}s per username")
