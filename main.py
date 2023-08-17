import time
import json

def processStats(dictionary, cosmetictype):
    print(f"\n\n{cosmetictype.upper()}S STATS BY USERS")

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
            aULVP.append("N/A")
        try: 
            aUVP.append(str(round(dictionary[value]['usedVP']/dictionary[value]['usedCount'])))
        except ZeroDivisionError:
            aUVP.append("N/A")

    values.append(cosmetictype.title() + " Name")
    unlockedCount.append("Unlocked")
    usedCount.append("Using")
    percentUnlocked.append("% of All Users")
    percentUsed.append("Users Using")
    percentUsedOfUnlocked.append("% of Unlocked")
    aULVP.append("Average VP per")
    aUVP.append("Average VP per")

    maxlength = lambda x: len(max(x, key=len))+1

    valspace = maxlength(values)
    unlockedcountspace = maxlength(unlockedCount)
    usedcountspace = maxlength(usedCount)
    percentusedspace = maxlength(percentUsed)
    percentunlockedspace = maxlength(percentUnlocked)
    percentusedofunlockedspace = maxlength(percentUsedOfUnlocked)
    aulvpspace = maxlength(aULVP)
    auvpspace = maxlength(aUVP)

    header = f"{values[-1]:<{valspace}} {('Users'):>{unlockedcountspace}} {('Users'):>{usedcountspace}} {(percentUnlocked[-1]):>{percentunlockedspace}} {(percentUsed[-1]):>{percentusedspace}} {('% of All'):>{percentusedofunlockedspace}} {(aULVP[-1]):>{aulvpspace}} {(aUVP[-1]):>{auvpspace}}"
    print(header)
    print(f"{'':<{valspace}} {(unlockedCount[-1]):>{unlockedcountspace}} {(usedCount[-1]):>{usedcountspace}} {('Unlocked'):>{percentunlockedspace}} {('Users Using'):>{percentusedspace}} {(percentUsedOfUnlocked[-1]):>{percentusedofunlockedspace}} {('Unlocked User'):>{aulvpspace}} {('Using User'):>{auvpspace}}")
    print("-"*len(header))
    for i in range(len(values)-1):
        print(f"{(values[i]):<{valspace}} {(unlockedCount[i]):>{unlockedcountspace}} {(usedCount[i]):>{usedcountspace}} {(percentUnlocked[i]):>{percentunlockedspace}} {(percentUsed[i]):>{percentusedspace}} {(percentUsedOfUnlocked[i]):>{percentusedofunlockedspace}} {(aULVP[i]):>{aulvpspace}} {(aUVP[i]):>{auvpspace}}")

    # if section == "unlocked":
    #     print(f"{(values[-1]):<{valspace}} {('# of'):>{countspace}} {(percents[-1]):>{percentspace}} {(avp[-1]):>{avpspace}}")
    #     print(" "*(1+len(f"{(values[-1]):<{valspace}}")) + f"{('Users'):>{countspace}} {('Users'):>{percentspace}} {('VP'):>{avpspace}}")
    #     print("-"*len(f"{(values[-1]):<{valspace}} {(counts[-1]):>{countspace}} {(percents[-1]):>{percentspace}} {(avp[-1]):>{avpspace}}"))
    #     for i in range(len(values)-1):
    #         print(f"{(values[i]):<{valspace}} {(counts[i]):>{countspace}} {(percents[i]):>{percentspace}} {(avp[i]):>{avpspace}}")
    # else:
    #     print(f"{(values[-1]):<{valspace}} {('# of'):>{countspace}} {(percents[-1]):>{percentspace}} {(percentsUnlocked[-1]):>{percentsUnlockedSpace}} {(avp[-1]):>{avpspace}}")
    #     print(" "*(1+len(f"{(values[-1]):<{valspace}}")) + f"{('Users'):>{countspace}} {('Users'):>{percentspace}} {('Users'):>{percentsUnlockedSpace}} {('VP'):>{avpspace}}")
    #     print("-"*len(f"{(values[-1]):<{valspace}} {(counts[-1]):<{countspace}} {(percents[-1]):<{percentspace}} {(percentsUnlocked[-1]):<{percentsUnlockedSpace}} {(avp[-1]):<{avpspace}}"))
    #     for i in range(len(values)-1):
    #         print(f"{(values[i]):<{valspace}} {(counts[i]):>{countspace}} {(percents[i]):>{percentspace}} {(percentsUnlocked[i]):>{percentsUnlockedSpace}} {(avp[i]):>{avpspace}}")

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

cosmetics = []
hat = ["gold-crown","silver-crown","bronze-crown","witch-hat","stars","santa-hat","blue-santa-hat","flames","blue-flames","halo","gold-wreath","spring-wreath","autumn-wreath","winter-wreath","summer-wreath","summer-olympics-wreath","summer-olympics-wreath-2","winter-olympics-wreath","sunglasses","flower-headband","autumn-leaves","fedora","coconut-holes","plastic-shine","pellets","pirate-hat","rose-wreath"]
body = ["sticky-coat","toxic-coat","orbit-ring","clouds","storm-clouds","tuxedo","angel-wings","one-winged-angel","stick","royal-robes","mummy-wrap","doughnut"]

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


# loop through usernames
start = time.perf_counter()

for i, username in enumerate(profiles):
    print(f"[{i+1}/{len(profiles)}] {list(username.keys())[0]}")
    username = username[list(username.keys())[0]]
    for h in hat:
        if username["accessories"]["collection"][h]:
            hatcounts[h]["unlockedCount"]+=1
            hatcounts[h]["unlockedVP"]+=username["stats"]["highest_area_achieved_counter"]
        if h == username["accessories"]["hat_selection"]:
            hatcounts[h]["usedCount"]+=1
            hatcounts[h]["usedVP"]+=username["stats"]["highest_area_achieved_counter"]
    for b in body:
        if username["accessories"]["collection"][b]:
            bodycounts[b]["unlockedCount"]+=1
            bodycounts[b]["unlockedVP"]+=username["stats"]["highest_area_achieved_counter"]
        if b == username["accessories"]["body_selection"]:
            bodycounts[b]["usedCount"]+=1
            bodycounts[b]["usedVP"]+=username["stats"]["highest_area_achieved_counter"]


print(f"Checked {len(profiles)} profiles in {time.perf_counter()-start:.2f} seconds.")
print(f"Average time per profile: {(time.perf_counter()-start)/len(profiles):.2f} seconds.")

start = time.perf_counter()

# unlocked

processStats(hatcounts, "hat")
processStats(bodycounts, "body cosmetic")

print()
print("Done")
print(f"{time.perf_counter()-start:.2f} seconds, or {(time.perf_counter()-start)/len(usernames):.2f}s per username")

# with open("counts.txt", "w") as f:
#     for u in userlist:
#         f.write(f"{u.name}: {u.achievements}\n")
# print("Saved to file.")