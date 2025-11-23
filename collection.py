collection = [ {
    "name": "Pawns",
    "level": "0/3"},
        {
    "name": "Archers",
    "level": "0/3"},
        {
    "name": "Scouts",
    "level": "0/3"},
        {
    "name": "Skeletons",
    "level": "0/3"},
        {
    "name": "Freeze",
    "level": "0/3"},
        {
    "name": "Musketeer",
    "level": "0/3"},
        {
    "name": "Barbarians",
    "level": "0/3"},
        {
    "name": "Barbed wires",
    "level": "0/3"},
        {
    "name": "Rapid dogs",
    "level": "0/3"},
        {
    "name": "Medic",
    "level": "0/3"},
        {
    "name": "Blazer",
    "level": "0/3"},
        {
    "name": "Goblin barrel",
    "level": "0/3"},
        {
    "name": "Knight",
    "level": "0/3"},
        {
    "name": "Goblin gankers",
    "level": "0/3"},
        {
    "name": "The barrel",
    "level": "0/3"},
        {
    "name": "Money cage",
    "level": "0/3"},
        {
    "name": "Pirate gang",
    "level": "0/3"},
        {
    "name": "Burn",
    "level": "0/3"},
        {
    "name": "Zombie party",
    "level": "0/3"},
        {
    "name": "Ogre",
    "level": "0/3"},
        {
    "name": "Copper golemn",
    "level": "0/3"},
        {
    "name": "Spiders",
    "level": "0/3"},
        {
    "name": "Arrows",
    "level": "0/3"},
        {
    "name": "Snowball",
    "level": "0/3"},
        {
    "name": "Landmine",
    "level": "0/3"},
        {
    "name": "Suspicious bush",
    "level": "0/3"},
        {
    "name": "Bee swarm",
    "level": "0/3"},
        {
    "name": "The balloon",
    "level": "0/3"},
        {
    "name": "Fireball",
    "level": "0/3"},
        {
    "name": "Bomber",
    "level": "0/3"},        
        {
    "name": "Shielder",
    "level": "0/3"},
        {
    "name": "Explosive formula",
    "level": "0/3"},
            {
    "name": "Miner",
    "level": "0/3"},
        {
    "name": "Cannon",
    "level": "0/3"},
            {
    "name": "Lightning",
    "level": "0/3"},
        {
    "name": "Go cart",
    "level": "0/3"},
            {
    "name": "Wizard",
    "level": "0/3"},
        {
    "name": "Goblin spawner",
    "level": "0/3"},
            {
    "name": "Exterminator",
    "level": "0/3"},
        {
    "name": "Tombstone",
    "level": "0/3"},
            {
    "name": "Mech",
    "level": "0/3"},
        {
    "name": "Poisonous gas",
    "level": "0/3"},
            {
    "name": "Spirits",
    "level": "0/3"},
        {
    "name": "Missionary",
    "level": "0/3"},
            {
    "name": "Drill",
    "level": "0/3"},
        {
    "name": "Baby dino",
    "level": "0/3"},
            {
    "name": "Elixir blob",
    "level": "0/3"},
        {
    "name": "Electric wizard",
    "level": "0/3"},
            {
    "name": "Aboralists",
    "level": "0/3"},
        {
    "name": "Monk",
    "level": "0/3"},
            {
    "name": "Wormhole",
    "level": "0/3"},
        {
    "name": "Night lich",
    "level": "0/3"},
            {
    "name": "Earthquake",
    "level": "0/3"},
        {
    "name": "The log",
    "level": "0/3"},
            {
    "name": "Tesla coil",
    "level": "0/3"},
        {
    "name": "Skeleton king",
    "level": "0/3"},
            {
    "name": "Thundermine",
    "level": "0/3"},
        {
    "name": "Honor knights",
    "level": "0/3"},
            {
    "name": "Phoenix",
    "level": "0/3"},
        {
    "name": "Mega knight",
    "level": "0/3"},

]
num = 0
x = input(">")
y = (len(collection))
for i in range(y):
    if x != collection[num]["name"]:
        num += 1
print(collection[num]["level"])
