import random
z1 = random.randint(1,9)
x1 = random.randint(1,12)
y1 = random.randint(1,5)
w1 = random.randint(1,36)


################ Race

if z1 == 1: z2=("Dwarrf")
if z1 == 2: z2=("Elf")
if z1 == 3: z2=("Halfling")
if z1 == 4: z2=("Human")
if z1 == 5: z2=("Dragonborn")
if z1 == 6: z2=("Gnome")
if z1 == 7: z2=("Half-Elf")
if z1 == 8: z2=("Half-Orc")
if z1 == 9: z2=("Tiefling")

################# Class

if x1 == 1: x2=("Barbarian,")
if x1 == 2: x2=("Bard,")
if x1 == 3: x2=("Cleric,") 
if x1 == 4: x2=("Druid,")
if x1 == 5: x2=("Fighter,")
if x1 == 6: x2=("Monk,")
if x1 == 7: x2=("Paladin,")
if x1 == 8: x2=("Ranger,")
if x1 == 9: x2=("Rogue,")
if x1 == 10: x2=("Sorcerer,")
if x1 == 11: x2=("Warlock,")
if x1 == 12: x2=("Wizzard,")

################# Path
##### Barbarian

if x1 == 1 and y1 == 1: y2=("Path of the Ancestral Guardian.")
if x1 == 1 and y1 == 2: y2=("Path of the Berseker.")
if x1 == 1 and y1 == 3: y2=("Path of the Storm Herald.")
if x1 == 1 and y1 == 4: y2=("Path of the Totem Warrior.")
if x1 == 1 and y1 == 5: y2=("Path of the Zealot.")

##### Bard

if x1 == 2 and y1 == 1: y2=("College of Glamour.")
if x1 == 2 and y1 == 2: y2=("College of Lore.")
if x1 == 2 and y1 == 3: y2=("College of Swords.")
if x1 == 2 and y1 == 4: y2=("College of Valor.")
if x1 == 2 and y1 == 5: y2=("College of Whispers.")

##### Cleric

if x1 == 3 and y1 == 1: y2=("Death Domain.")
if x1 == 3 and y1 == 2: y2=("Life Domain.")
if x1 == 3 and y1 == 3: y2=("Nature Domain.")
if x1 == 3 and y1 == 4: y2=("Order Domain.")
if x1 == 3 and y1 == 5: y2=("Tempest Domain.")

##### Druid

if x1 == 4 and y1 == 1: y2=("Circle of Dreams.")
if x1 == 4 and y1 == 2: y2=("Circle of Land.")
if x1 == 4 and y1 == 3: y2=("Circle of Moon.")
if x1 == 4 and y1 == 4: y2=("Circle of Shepherd.")
if x1 == 4 and y1 == 5: y2=("Circle of Spores.")

##### Fighter

if x1 == 5 and y1 == 1: y2=("Battle Master.")
if x1 == 5 and y1 == 2: y2=("Cavalier.")
if x1 == 5 and y1 == 3: y2=("Champion.")
if x1 == 5 and y1 == 4: y2=("Eldrich Knight.")
if x1 == 5 and y1 == 5: y2=("Samurai.")

##### Monk

if x1 == 6 and y1 == 1: y2=("Way of the Drunken Master.")
if x1 == 6 and y1 == 2: y2=("Way of the Kensei.")
if x1 == 6 and y1 == 3: y2=("Way of the Long Death.")
if x1 == 6 and y1 == 4: y2=("Way of the Open Hand.")
if x1 == 6 and y1 == 5: y2=("Way of the Shadow.")

##### Paladin

if x1 == 7 and y1 == 1: y2=("Oath of the Ancients.")
if x1 == 7 and y1 == 2: y2=("Oath of Conquest.")
if x1 == 7 and y1 == 3: y2=("Oath of Crown.")
if x1 == 7 and y1 == 4: y2=("Oath of Redemption.")
if x1 == 7 and y1 == 5: y2=("Oath of Vengeance.")

##### Ranger

if x1 == 8 and y1 == 1: y2=("Beast Master Conclave.")
if x1 == 8 and y1 == 2: y2=("Gloom Stalker Conclave.")
if x1 == 8 and y1 == 3: y2=("Horizon Walker Conclave.")
if x1 == 8 and y1 == 4: y2=("Hunter Conclave.")
if x1 == 8 and y1 == 5: y2=("Monster Slayer Conclave.")

##### Rogue

if x1 == 9 and y1 == 1: y2=("Arcane Trickster.")
if x1 == 9 and y1 == 2: y2=("Assassin.")
if x1 == 9 and y1 == 3: y2=("Scout.")
if x1 == 9 and y1 == 4: y2=("Swashbuckler.")
if x1 == 9 and y1 == 5: y2=("Thief.")

##### Sorcerer

if x1 == 10 and y1 == 1: y2=("Draconic Bloodline.")
if x1 == 10 and y1 == 2: y2=("Divine Soul.")
if x1 == 10 and y1 == 3: y2=("Shadow Magic.")
if x1 == 10 and y1 == 4: y2=("Storm Sorcery.")
if x1 == 10 and y1 == 5: y2=("Wild Magic.")

##### Warlock

if x1 == 11 and y1 == 1: y2=("Archfey.")
if x1 == 11 and y1 == 2: y2=("Celestial.")
if x1 == 11 and y1 == 3: y2=("Fiend.")
if x1 == 11 and y1 == 4: y2=("Hexblade.")
if x1 == 11 and y1 == 5: y2=("Undying.")

##### Wizard

if x1 == 12 and y1 == 1: y2=("School of Abjuration.")
if x1 == 12 and y1 == 2: y2=("School of Divination.")
if x1 == 12 and y1 == 3: y2=("School of Evocation.")
if x1 == 12 and y1 == 4: y2=("School of Necromancy.")
if x1 == 12 and y1 == 5: y2=("School of War Magic.")



################################ Backgrounds

if w1 == 1: w2 =("Acolyte.")
if w1 == 2: w2 =("Anthropologist.")
if w1 == 3: w2 =("Archaeologist.")
if w1 == 4: w2 =("Charlatan.")
if w1 == 5: w2 =("City Watch.")
if w1 == 6: w2 =("Clan Crafter.")
if w1 == 7: w2 =("Cloistered Scholar.")
if w1 == 8: w2 =("Courtier.")
if w1 == 9: w2 =("Criminal.")

if w1 == 10: w2 =("Entertainer.")
if w1 == 11: w2 =("Faceless.")
if w1 == 12: w2 =("Faction Agent.")
if w1 == 13: w2 =("Far Traveler.")
if w1 == 14: w2 =("Folk Hero.")
if w1 == 15: w2 =("Gladiator.")
if w1 == 16: w2 =("Guild Artisan.")
if w1 == 17: w2 =("Guild Merchant.")
if w1 == 18: w2 =("Hounted One.")
if w1 == 19: w2 =("House Agent.")

if w1 == 20: w2 =("Heremit.")
if w1 == 21: w2 =("Inheritor.")
if w1 == 22: w2 =("Investigator.")
if w1 == 23: w2 =("Knight.")
if w1 == 24: w2 =("Knight of the Order.")
if w1 == 25: w2 =("Mercenary Veteran.")
if w1 == 26: w2 =("Noble.")
if w1 == 27: w2 =("Outlander.")
if w1 == 28: w2 =("Pirate.")
if w1 == 29: w2 =("Sage.")

if w1 == 30: w2 =("Sailor.")
if w1 == 31: w2 =("Soldier.")
if w1 == 32: w2 =("Spy.")
if w1 == 33: w2 =("Urban Bounty Hunter.")
if w1 == 34: w2 =("Urchin.")
if w1 == 35: w2 =("Uthgardt Tribe Member.")
if w1 == 36: w2 =("Waterdhavian Noble.")

########################### Resultado

print("You are a member of the",z2,"Race, and your Class is:",x2,y2,"Additionally, your background is:",w2)





















