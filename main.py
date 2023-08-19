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
        "usedVP":0
    },
    "silver-crown": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0
    },
    "bronze-crown": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0
    },
    "witch-hat": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0
    },
    "stars": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0
    },
    "santa-hat": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0
    },
    "blue-santa-hat": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0
    },
    "flames": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0
    },
    "blue-flames": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0
    },
    "halo": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0
    },
    "gold-wreath": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0
    },
    "spring-wreath": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0
    },
    "autumn-wreath": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0
    },
    "winter-wreath": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0
    },
    "summer-wreath": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0
    },
    "summer-olympics-wreath": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0
    },
    "summer-olympics-wreath-2": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0
    },
    "winter-olympics-wreath": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0
    },
    "sunglasses": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0
    },
    "flower-headband": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0
    },
    "autumn-leaves": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0
    },
    "fedora": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0
    },
    "coconut-holes": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0
    },
    "plastic-shine": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0
    },
    "pellets": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0
    },
    "pirate-hat": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0
    },
    "rose-wreath": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0
    },
}
bodycounts = {
    "sticky-coat": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0
    },
    "toxic-coat": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0
    },
    "orbit-ring": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0
    },
    "clouds": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0
    },
    "storm-clouds": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0
    },
    "tuxedo": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0
    },
    "angel-wings": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0
    },
    "one-winged-angel": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0
    },
    "stick": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0
    },
    "royal-robes": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0
    },
    "mummy-wrap": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0
    },
    "doughnut": {
        "unlockedCount":0,
        "usedCount":0,
        "unlockedVP":0,
        "usedVP":0
    }
}
achievementcounts = {
    "scientist": 0,
    "tree_tapper": 0,
    "snowball_mayhem": 0,
    "savior": 0,
    "money_moves": 0,
    "pellet_obfuscator": 0,
    "champion": 0,
    "core_revival": 0,
    "peculiar_pathing": 0,
    "ground_control": 0,
    "lush_sands": 0,
    "baneful_bunker": 0,
    "wacky_ride": 0,
    "radioactive_dasher": 0,
    "serene_garden": 0,
    "stomper": 0,
    "enormous_tribute": 0,
    "glacial_grouping": 0,
    "magnetic_highway": 0,
    "gardener": 0,
    "survivalist": 0,
    "mysterious_mangrove": 0,
    "ominous_occult": 0,
    "relentless_ridge": 0,
    "intense_inferno": 0,
    "district_demolition": 0,
    "two_winged_angel": 0,
    "humongous_visit": 0,
    "quintessential_quarry": 0,
    "endless_expansion": 0,
    "visit_grandma": 0,
    "traveller": 0,
    "victor": 0,
    "one_winged_angel": 0,
    "frosty_fjord": 0,
    "dipole_diversion": 0
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
            hatcounts[h]["unlockedCount"]+=1
            hatcounts[h]["unlockedVP"]+=userdict["stats"]["highest_area_achieved_counter"]
        if h == userdict["accessories"]["hat_selection"]:
            hatcounts[h]["usedCount"]+=1
            hatcounts[h]["usedVP"]+=userdict["stats"]["highest_area_achieved_counter"]
    for b in body:
        if userdict["accessories"]["collection"][b]:
            if b in alertcosmetics:
                print(f"{username} has {b}")
            userinfo.cosmetics+=1
            userinfo.bodies+=1
            bodycounts[b]["unlockedCount"]+=1
            bodycounts[b]["unlockedVP"]+=userdict["stats"]["highest_area_achieved_counter"]
        if b == userdict["accessories"]["body_selection"]:
            bodycounts[b]["usedCount"]+=1
            bodycounts[b]["usedVP"]+=userdict["stats"]["highest_area_achieved_counter"]
    for a in achievement:
        if a in userdict["stats"]["achievements"]:
            achievementcounts[a]+=1
    userlist.append(userinfo)

print(f"Checked {len(profiles)} profiles in {time.perf_counter()-start:.2f} seconds.")
print(f"Average time per profile: {(time.perf_counter()-start)/len(profiles):.2f} seconds.")

start = time.perf_counter()

print(f"\nHat statistics from {len(profiles)} users:")
processStats(hatcounts, "hat")

print(f"\nBody cosmetic statistics from {len(profiles)} users:")
processStats(bodycounts, "body cosmetic")

print(f"\nAchievement statistics from {len(profiles)} users:")
achievementcounts = dict(sorted(achievementcounts.items(), key=lambda item: item[1]))

percents = []
for a in achievementcounts:
    percents.append(f"{achievementcounts[a]/len(profiles)*100:.2f}%")
twoarray = [percents, list(achievementcounts.values()), list(achievementcounts.keys())]
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

print()
print("Done")
print(f"{time.perf_counter()-start:.2f} seconds, or {(time.perf_counter()-start)/len(usernames):.2f}s per username")
