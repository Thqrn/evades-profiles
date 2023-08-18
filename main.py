import time
import json
import operator

def maxlength(tab):

    newtab = []

    for col in tab:
        newcol = []
        for r in col:
            if type(r) != str and type(r) != list:
                r = str(r)
            if type(r) == list:
                r = max(r, key = len)
            newcol.append(r)
        newtab.append(newcol)

    spacers = []

    for i in range(len(newtab[0])):
        spacers.append(max([len(col[i]) for col in newtab]))

    return spacers
        

def tablizer(table, header, alignment=["left"]):
    # set alignments

    if len(alignment) == 1:
        alignment = alignment*len(header)

    if len(alignment) == 2 and len(alignment) != len(header):
        alignment.extend([alignment[1]]*(len(header)-2))

    # find longest lines of any multi-line headers
    # and make all headers strings (maybe)
    newheader = []
    longesthead = 1
    for i, head in enumerate(header):
        if type(head) != str:
            head = str(head)
        head = head.split("\n")
        if len(head) == 1:
            head = head[0]
        if type(head) == list:
            if len(head) > longesthead:
                longesthead = len(head)
        newheader.append(head)

    # spacing for everything
    spacing = maxlength(table + [newheader])

    # print header with alignment
    for h in range(longesthead):
        for i, head in enumerate(newheader):
            if type(head) == list:
                if len(head) > longesthead-(h+1):
                    if len(head) == longesthead:
                        ran = h
                    else:
                        ran = h+(len(head)-longesthead)
                    if alignment[i] == "left":
                        print(f"{head[ran]:<{spacing[i]}}", end="")
                    elif alignment[i] == "right":
                        print(f"{head[ran]:>{spacing[i]}}", end="")
                    else:
                        print(f"{head[ran]:^{spacing[i]}}", end="")
                    if i != len(newheader)-1:
                        print(" | ", end="")
                    else:
                        print()
                else:
                    print(f"{'':<{spacing[i]}}", end="")
                    if i != len(newheader)-1:
                        print(" | ", end="")
                    else:
                        print()
            else:
                if h == longesthead-1:
                    if alignment[i] == "left":
                        print(f"{head:<{spacing[i]}}", end="")
                    elif alignment[i] == "right":
                        print(f"{head:>{spacing[i]}}", end="")
                    else:
                        print(f"{head:^{spacing[i]}}", end="")
                    if i != len(newheader)-1:
                        print(" | ", end="")
                    else:
                        print()
                else:
                    print(f"{'':<{spacing[i]}}", end="")
                    if i != len(newheader)-1:
                        print(" | ", end="")
                    else:
                        print()

    # print separator
    for i, space in enumerate(spacing):
        print(f"{'-'*space}", end="")
        if i != len(spacing)-1:
            print("-+-", end="")
        else:
            print()

    # print each row of data with alignment
    for row in table:
        for i, col in enumerate(row):
            if alignment[i] == "left":
                print(f"{col:<{spacing[i]}}", end="")
            elif alignment[i] == "right":
                print(f"{col:>{spacing[i]}}", end="")
            else:
                print(f"{col:^{spacing[i]}}", end="")
            if i != len(row)-1:
                print(" | ", end="")
        print()


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
        try:
            percentUsed.append(f"{dictionary[value]['usedCount']/len(profiles)*100:.2f}%")
        except ZeroDivisionError:
            percentUsed.append("0")
        try:
            percentUnlocked.append(f"{dictionary[value]['unlockedCount']/len(profiles)*100:.2f}%")
        except ZeroDivisionError:
            percentUnlocked.append("0")
        try:
            percentUsedOfUnlocked.append(f"{dictionary[value]['usedCount']/dictionary[value]['unlockedCount']*100:.2f}%")
        except ZeroDivisionError:
            percentUsedOfUnlocked.append("0")
        try: 
            aULVP.append(str(round(dictionary[value]['unlockedVP']/dictionary[value]['unlockedCount'])))
        except ZeroDivisionError:
            aULVP.append("0")
        try: 
            aUVP.append(str(round(dictionary[value]['usedVP']/dictionary[value]['usedCount'])))
        except ZeroDivisionError:
            aUVP.append("0")

    twod = []
    for i in range(len(values)-1):
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

# class user:
#     def __init__(self, name='', achievements=0):
#         self.name = name
#         self.achievements = achievements


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
# loop through usernames
start = time.perf_counter()

userlist = []

class user:
  def __init__(self, name='', achievements=0):
      self.name = ''
      self.achievements = 0

for i, userprofile in enumerate(profiles):
    #print(f"[{i+1}/{len(profiles)}] {list(username.keys())[0]}")
    userinfo = user()
    username = list(userprofile.keys())[0]
    userinfo.name = username
    userdict = userprofile[username]
    userinfo.achievements = len(userdict["stats"]["achievements"])
    userlist.append(userinfo)
    for h in hat:
        if userdict["accessories"]["collection"][h]:
            hatcounts[h]["unlockedCount"]+=1
            hatcounts[h]["unlockedVP"]+=userdict["stats"]["highest_area_achieved_counter"]
        if h == userdict["accessories"]["hat_selection"]:
            hatcounts[h]["usedCount"]+=1
            hatcounts[h]["usedVP"]+=userdict["stats"]["highest_area_achieved_counter"]
    for b in body:
        if userdict["accessories"]["collection"][b]:
            # if b == "one-winged-angel":
            #     print(f"{username} has one-winged-angel")
            bodycounts[b]["unlockedCount"]+=1
            bodycounts[b]["unlockedVP"]+=userdict["stats"]["highest_area_achieved_counter"]
        if b == userdict["accessories"]["body_selection"]:
            bodycounts[b]["usedCount"]+=1
            bodycounts[b]["usedVP"]+=userdict["stats"]["highest_area_achieved_counter"]
    for a in achievement:
        if a in userdict["stats"]["achievements"]:
            # if a == "one_winged_angel":
            #     print(f"{username} has one_winged_angel")
            achievementcounts[a]+=1

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

with open('hatdata.json', 'w', encoding='utf-8') as f:
    json.dump(hatcounts, f, ensure_ascii=False, indent=4)
with open('bodydata.json', 'w', encoding='utf-8') as f:
    json.dump(bodycounts, f, ensure_ascii=False, indent=4)

userlist.sort(key=operator.attrgetter('achievements'), reverse=True)

with open('achievements.txt', 'w', encoding='utf-8') as f:
    for u in userlist:
        f.write(f"{u.name}: {u.achievements}\n")
print("Saved to file.")

print()
print("Done")
print(f"{time.perf_counter()-start:.2f} seconds, or {(time.perf_counter()-start)/len(usernames):.2f}s per username")
