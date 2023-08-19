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
        "usedUsers": []
    },
    "silver-crown": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": []
    },
    "bronze-crown": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": []
    },
    "witch-hat": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": []
    },
    "stars": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": []
    },
    "santa-hat": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": []
    },
    "blue-santa-hat": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": []
    },
    "flames": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": []
    },
    "blue-flames": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": []
    },
    "halo": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": []
    },
    "gold-wreath": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": []
    },
    "spring-wreath": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": []
    },
    "autumn-wreath": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": []
    },
    "winter-wreath": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": []
    },
    "summer-wreath": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": []
    },
    "summer-olympics-wreath": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": []
    },
    "summer-olympics-wreath-2": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": []
    },
    "winter-olympics-wreath": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": []
    },
    "sunglasses": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": []
    },
    "flower-headband": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": []
    },
    "autumn-leaves": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": []
    },
    "fedora": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": []
    },
    "coconut-holes": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": []
    },
    "plastic-shine": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": []
    },
    "pellets": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": []
    },
    "pirate-hat": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": []
    },
    "rose-wreath": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": []
    },
}
bodycounts = {
    "sticky-coat": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": []
    },
    "toxic-coat": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": []
    },
    "orbit-ring": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": []
    },
    "clouds": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": []
    },
    "storm-clouds": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": []
    },
    "tuxedo": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": []
    },
    "angel-wings": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": []
    },
    "one-winged-angel": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": []
    },
    "stick": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": []
    },
    "royal-robes": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": []
    },
    "mummy-wrap": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": []
    },
    "doughnut": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0,
        "unlockedUsers": [],
        "usedUsers": []
    }
}
achievementcounts = {
    "scientist": {
        "count":0,
        "users":[]
    },
    "tree_tapper": {
        "count":0,
        "users":[]
    },
    "snowball_mayhem": {
        "count":0,
        "users":[]
    },
    "savior": {
        "count":0,
        "users":[]
    },
    "money_moves": {
        "count":0,
        "users":[]
    },
    "pellet_obfuscator": {
        "count":0,
        "users":[]
    },
    "champion": {
        "count":0,
        "users":[]
    },
    "core_revival": {
        "count":0,
        "users":[]
    },
    "peculiar_pathing": {
        "count":0,
        "users":[]
    },
    "ground_control": {
        "count":0,
        "users":[]
    },
    "lush_sands": {
        "count":0,
        "users":[]
    },
    "baneful_bunker": {
        "count":0,
        "users":[]
    },
    "wacky_ride": {
        "count":0,
        "users":[]
    },
    "radioactive_dasher": {
        "count":0,
        "users":[]
    },
    "serene_garden": {
        "count":0,
        "users":[]
    },
    "stomper": {
        "count":0,
        "users":[]
    },
    "enormous_tribute": {
        "count":0,
        "users":[]
    },
    "glacial_grouping": {
        "count":0,
        "users":[]
    },
    "magnetic_highway": {
        "count":0,
        "users":[]
    },
    "gardener": {
        "count":0,
        "users":[]
    },
    "survivalist": {
        "count":0,
        "users":[]
    },
    "mysterious_mangrove": {
        "count":0,
        "users":[]
    },
    "ominous_occult": {
        "count":0,
        "users":[]
    },
    "relentless_ridge": {
        "count":0,
        "users":[]
    },
    "intense_inferno": {
        "count":0,
        "users":[]
    },
    "district_demolition": {
        "count":0,
        "users":[]
    },
    "two_winged_angel": {
        "count":0,
        "users":[]
    },
    "humongous_visit": {
        "count":0,
        "users":[]
    },
    "quintessential_quarry": {
        "count":0,
        "users":[]
    },
    "endless_expansion": {
        "count":0,
        "users":[]
    },
    "visit_grandma": {
        "count":0,
        "users":[]
    },
    "traveller": {
        "count":0,
        "users":[]
    },
    "victor": {
        "count":0,
        "users":[]
    },
    "one_winged_angel": {
        "count":0,
        "users":[]
    },
    "frosty_fjord": {
        "count":0,
        "users":[]
    },
    "dipole_diversion": {
        "count":0,
        "users":[]
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
achievementcounts = dict(sorted(achievementcounts.items(), key=lambda item: item[1]['count']))
percents = []
countsachievements = []
for a in achievementcounts:
    percents.append(f"{achievementcounts[a]['count']/len(profiles)*100:.2f}%")
    countsachievements.append(achievementcounts[a]['count'])
print(countsachievements)
twoarray = [percents, countsachievements, list(achievementcounts.keys())]
tablizer(list(zip(*twoarray[::-1])), header=["Achievement", "Count", "Percent"], alignment=["left", "right"])

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
    print("Enter a cosmetic or achievement to view its speciric users or those who have it unlocked, or 'exit' to exit:")
    print("NOTE: Values are not ordered in any specific order.")
    search = input("")
    if search == "exit":
        break
    elif search in hat or search in body:
        usedorunlocked = input("Enter 'used' or 'unlocked' to view the users who have used or unlocked the cosmetic:\n")
        if usedorunlocked == "used":
            if search in hat:
                for i, u in enumerate(hatcounts[search]["usedUsers"]):
                    print(f"{i+1}. {u}")
            elif search in body:
                for i, u in enumerate(bodycounts[search]["usedUsers"]):
                    print(f"{i+1}. {u}")
        elif usedorunlocked == "unlocked":
            if search in hat:
                for i, u in enumerate(hatcounts[search]["unlockedUsers"]):
                    print(f"{i+1}. {u}")
            elif search in body:
                for i, u in enumerate(bodycounts[search]["unlockedUsers"]):
                    print(f"{i+1}. {u}")
    elif search in achievement:
        for i, u in enumerate(achievementcounts[search]["users"]):
            print(f"{i+1}. {u}")
    else:
        print("Invalid input")


print()
print("Done")
print(f"{time.perf_counter()-start:.2f} seconds, or {(time.perf_counter()-start)/len(usernames):.2f}s per username")
