import pokeansi

class CreatePokemon():
    def __init__(self, number, name, type, attacks, description, previous_evolution, next_evolution):
        self.number = number
        self.name = name
        self.type = type
        self.attacks = attacks
        self.description = description
        self.previous_evolution = previous_evolution
        self.next_evolution = next_evolution

    def show_pokemon(self):
        print(f"\n\n            {self.number}")
        print(f"\nName: {self.name} / Type: {self.type}")
        print(f"\nMoves: {self.attacks}")
        print(f"\nDesc: {self.description}")
        print(f"\nPrevious Evolution: {self.previous_evolution}")
        print(f"\nNext Evolution: {self.next_evolution}")

# First Generation

Bulbasaur_en = CreatePokemon(
    "#001",
    "Bulbasaur",
    ("Grass", "Poison"),
    ["Growl", "Tackle"],
    "For some time after its birth, it grows by taking nourishment from the seed on its back.",
    "It doesn't have",
    "Ivysaur (lvl 16) / Venusaur (lvl 32)"
)

Ivysaur_en = CreatePokemon(
    "#002",
    "Ivysaur",
    ["Grass", "Poison"],
    ["Vine Whip", "Tackle", "Growl", "Growth"],
    "When the bud on its back starts swelling, a sweet aroma wafts to indicate the flower's coming bloom.",
    "Bulbasaur",
    "Venusaur (lvl 32)"
)

Venusaur_en = CreatePokemon(
    "#003",
    "Venusaur",
    ["Grass", "Poison"],
    ["Petal Blizzard", "Vine Whip", "Tackle", "Growl", "Growth", "Petal Dance"],
    "After a rainy day, the flower on its back smells stronger. The scent attracts other Pokémon.",
    "Bulbasaur / Ivysaur",
    "It doesn't have"
)

Charmander_en = CreatePokemon(
    "#004",
    "Charmander",
    ["Fire"],
    ["Scratch", "Growl"],
    "The fire on the tip of its tail is a measure of its life. If the Pokémon is healthy, its tail burns intensely.",
    "It doesn't have",
    "Charmeleon (lvl 16) / Charizard (lvl 36)"
)

Charmeleon_en = CreatePokemon(
    "#005",
    "Charmeleon",
    ["Fire"],
    ["Scratch", "Growl", "Ember", "Smokescreen"],
    "In the rocky mountains where Charmeleon lives, their fiery tails shine at night like stars.",
    "Charmander",
    "Charizard (lvl 36)"
)

Charizard_en = CreatePokemon(
    "#006",
    "Charizard",
    ["Fire", "Flying"],
    ["Air Slash", "Scratch", "Growl", "Ember", "Smokescreen", "Heat Wave", "Dragon Claw"],
    "It is said that Charizard's fire burns hotter if it has experienced harsh battles.",
    "Charmander / Charmeleon",
    "It doesn't have"
)

Squirtle_en = CreatePokemon(
    "#007",
    "Squirtle",
    ["Water"],
    ["Tackle", "Tail Whip"],
    "It hides in its shell to protect itself, then strikes back with spouts of water at every opportunity.",
    "It doesn't have",
    "Wartortle (lvl 16) / Blastoise (lvl 36)"
)

Wartortle_en = CreatePokemon(
    "#008",
    "Wartortle",
    ["Water"],
    ["Tackle", "Tail Whip", "Water Gun", "Withdraw"],
    "It is said to live 10.000 years. Its furry tail is popular as a symbol of longevity",
    "Squirtle",
    "Blastoise (lvl 36)"
)

Blastoise_en = CreatePokemon(
    "#009",
    "Blastoise",
    ["Water"],
    ["Flash Cannon", "Tackle", "Tail Whip", "Water", "Withdraw"],
    "The jets of water it spouts from the rocket cannons on its shell can punch through thick steel.",
    "Squirtle / Wartortle",
    "It doesn't have"
)

Caterpie_en = CreatePokemon(
    "#010",
    "Caterpie",
    ["Bug"],
    ["Tackle", "String Shot", "Bug Bite"],
    "It relases a stench from its red antennae to repel enemies. It grows by molting reapeatedly",
    "It doesn't have",
    "Metapod (lvl 7) / Butterfree (lvl 10)"
)

Metapod_en = CreatePokemon(
    "#011",
    "Metapod",
    ["Bug"],
    ["Harden"],
    "A steel-hard shell protects its tender body. The Pokémon quietly endures hardships while awaiting evolution.",
    "Caterpie",
    "Butterfree (lvl 10)"
)

Butterfree_en = CreatePokemon(
    "#012",
    "Butterfree",
    ["Bug", "Flying"],
    ["Gust", "String Shot", "Bug Bite", "Harden", "Tackle"],
    "It loves the nectar of flowers and can locate flower patches that have even tiny amounts of pollen.",
    "Caterpie / Metapod",
    "It doesn't have"
)

Weedle_en = CreatePokemon(
    "#013",
    "Weedle",
    ["Bug", "Poison"],
    ["Poison Sting", "String Shot"],
    "It eats its weight in leaves every day. It fends off attackers with the needle on its head.",
    "It doesn't have",
    "Kakuna (lvl 7) / Beedrill (lvl 10)"
)

Kakuna_en = CreatePokemon(
    "#014",
    "Kakuna",
    ["Bug", "Poison"],
    ["Harden"],
    "While awaiting evolution, it hides from predators under leaves and in nooks of branches.",
    "Weedle",
    "Beedrill (lvl 10)"
)

Beedrill_en = CreatePokemon(
    "#015",
    "Beedrill",
    ["Bug", "Poison"],
    ["Fury Attack", "String Shot", "Bug Bite", "Poison Sting", "Harden"],
    "Its best attack involves flying around at high speed, striking with poison needles, then flying off.",
    "Weedle / Kakuna",
    "It doesn't have"
)

Pidgey_en = CreatePokemon(
    "#016",
    "Pidgey",
    ["Normal", "Flying"],
    ["Tackle"],
    "It is docile and prefers to avoid conflict. If disturbed, however, it can feorciously strike back.",
    "It doesn't have",
    "Pidgeotto (lvl 18) / Pidgeot (lvl 36)"
)

Pidgeotto_en = CreatePokemon(
    "#017",
    "Pidgeotto",
    ["Normal", "Flying"],
    ["Gust", "Sand Attack", "Tackle"],
    "It flies over its wide territory in search of prey, downing it with its highly developed claws.",
    "Pidgey",
    "Pidgeot (lvl 36)"
)

Pidgeot_en = CreatePokemon(
    "#018",
    "Pidgeot",
    ["Normal", "Flying"],
    ["Gust", "Sand Attack", "Tackle", "Quick Attack", "Hurricane"],
    "By flapping its wings with all its might, Pidgeot can make a gust of wind capable of bending tall trees.",
    "Pidgey / Pidgeotto",
    "It doesn't have"
)

Rattata_en = CreatePokemon(
    "#019",
    "Rattata",
    ["Normal"],
    ["Tackle", "Tail Whip"],
    "It's cautious in the extreme, and its hardy vitality lets it live in any kind of environment.",
    "It doesn't have",
    "Raticate (lvl 20)"
)

Raticate_en = CreatePokemon(
    "#020",
    "Raticate",
    ["Normal"],
    ["Scary Face", "Swords Dance", "Tackle", "Tail Whip", "Quick Attack", "Focus Energy"],
    "It whittles down its constantly growing fangs by gnawing on hard things. It can chew apart cinder block walls.",
    "Rattata",
    "It doesn't have"
)

Spearow_en = CreatePokemon(
    "#021",
    "Spearow",
    ["Normal", "Flying"],
    ["Growl", "Peck"],
    "It flaps its small wings busily to fly. Using its beak, it searchs in grass for prey.",
    "It doesn't have",
    "Fearow (lvl 20)"
)

Fearow_en = CreatePokemon(
    "#022",
    "Fearow",
    ["Normal", "Flying"],
    ["Leer", "Growl", "Peck", "Pluck", "Drill Run"],
    "It has the stamina to fly all day on its broad wings. It fights by using its sharp beak.",
    "Spearow",
    "It doesn't have"
)

Ekans_en = CreatePokemon(
    "#023",
    "Ekans",
    ["Poison"],
    ["Wrap", "Leer"],
    "It sneaks through grass without making a sound and strikes unsuspecting prey from behind.",
    "It doesn't have",
    "Arbok (lvl 22)"
)

Arbok_en = CreatePokemon(
    "#024",
    "Arbok",
    ["Poison"],
    ["Crunch", "Wrap", "Poison Sting", "Leer", "Bite", "Thunder Fang", "Ice Fang", "Fire Fang"],
    "The pattern on its belly is for intimidation. It constricts foes while they are frozen in fear.",
    "Arbok",
    "It doesn't have"
)

Pikachu_en = CreatePokemon(
    "#025",
    "Pikachu",
    ["Eletric"],
    ["Thunder Shock", "Quick Attack", "Thunder Wave", "Swift", "Spark", "Thunderbolt", "Iron Tail", "Thunder"],
    "Possesses cheek sacs in which it stores electricity. This clever forest-dweller roasts tough berries with an electric shock before consuming them.",
    "Pichu",
    "Raichu (Thunder Stone)"
)

Raichu_en = CreatePokemon(
    "#026",
    "Raichu",
    ["Eletric"],
    ["Thunder Shock", "Quick Attack", "Thunder Wave", "Swift", "Spark", "Thunderbolt", "Iron Tail", "Thunder"],
    "It can discharge bursts of electricity exceeding 100,000 volts-- a single strike with that amount of power would incapacitate one of the Copperajah of my homeland.",
    "Pichu / Pikachu",
    "It doesn't have"
)

Sandshrew_en = CreatePokemon(
    "#027",
    "Sandshrew",
    ["Ground"],
    ["Scatch", "Defence Curl"],
    "To protect itself from attackers, it curls up into a ball. It lives in arid regions with minimal rainfall.",
    "It doesn't have",
    "Sandslash (lvl 22)"
)

Sandslash_en = CreatePokemon(
    "#028",
    "Sandslash",
    ["Ground"],
    ["Scratch", "Sand Attack", "Poison Sting", "Defence Curl", "Crush Claw", "Agility"],
    "It curls up, then rolls into foes with its back. Its sharp spines inflict severe damage.",
    "Sandshrew",
    "It doesn't have"
)

Nidoran_Female_en = CreatePokemon(
    "#029",
    "Nidoran F",
    ["Poison"],
    ["Poison Sting", "Growl"],
    "While this Pokémon does not prefer to fight, even one drop of the venom it secretes from its barbs can be fatal.",
    "It doesn't have",
    "Nidorina (lvl 16) / Nidoqueen (Moon Stone)"
)

Nidorina_en = CreatePokemon(
    "#030",
    "Nidorina",
    ["Poison"],
    ["Scratch", "Tail Whip", "Poison Sting", "Growl"],
    "When it senses danger, it raises all the barbs on its body. These barbs grow more slowly than Nidorino's.",
    "Nidoran F",
    "Nidoqueen (Moon Stone)"
)

Nidoqueen_en = CreatePokemon(
    "#031",
    "Nidoqueen",
    ["Poison", "Ground"],
    ["Superpower", "Scratch", "Double Kick", "Tail Whip", "Poison Sting", "Toxic", "Helping Hand", "Earth Power", "Sludge Wave", "Growl", "Fury Swipes", "Toxic Spikes", "Bite", "Flatter", "Cruch"],
    "Its entire body is armored with hard scales. It will protect the young in its burrow with its life.",
    "Nidoran F / Nidorina",
    "It doesn't have"
)

Nidoran_Male_en = CreatePokemon(
    "#032",
    "Nidoran M",
    ["Poison"],
    ["Poison Sting", "Leer"],
    "It scans its surroundings by raising its ears out of the grass. It toxic horn is for protection.",
    "It doesn't have",
    "Nidorino (lvl 16) / Nidoking (Moon Stone)"
)

Nidorino_en = CreatePokemon(
    "#033",
    "Nidorino",
    ["Poison"],
    ["Poison Sting", "Leer", "Peck", "Focus Energy"],
    "It has a violent disposition and stabs foes with its horn, which oozes venom upon impact.",
    "Nidoran M",
    "Nidoking (Moon Stone)"
)

Nidoking_en = CreatePokemon(
    "#034",
    "Nidoking",
    ["Poison", "Ground"],
    ["Megahorn", "Double Kick", "Horn Attack", "Poison Sting", "Peck", "Toxic", "Focus Energy", "Helping Hand", "Poison Jab", "Earth Power", "Sludge Wave", "Leer", "Fury Attack", "Toxic Spikes", "Flatter"],
    "One swing of its mighty tail can snap a telephone pole as if it were a matchstick.",
    "Nidoran M / Nidorino",
    "It doesn't have"
)

Clefairy_en = CreatePokemon(
    "#035",
    "Clefairy",
    ["Fairy"],
    ["Tacke"],
    "It can be found in quiet mountain areas on a full moon's night. Its dancing and its tiny, faintly glowing wings confer upon it a lovely fairylike quality.",
    "Cleffa",
    "Clefable (Moon Stone)"
)

Clefable_en = CreatePokemon(
    "#036",
    "Clefable",
    ["Fairy"],
    ["Tackle"],
    "Legend says that on clear, quiet nights, it listens for the voices of its kin living on the moon. I, too, often think of my homeland, so far away.",
    "Cleffa / Clefairy",
    "It doesn't have"
)

Vulpix_en = CreatePokemon(
    "#037",
    "Vulpix",
    ["Fire"],
    ["Ember"],
    "In its belly burns a firem which Vulpix spits out in the form of fireballs. When young, this Pokémon has but one white tail. As the Pokémon matures, this single tail splits into six.",
    "It doesn't have",
    "Ninetales (Fire Stone)"
)

Ninetales_en = CreatePokemon(
    "#038",
    "Ninetales",
    ["Fire"],
    ["Ember"],
    "The coat of gleamng golden fur is quite magnificent. This species is said to store sacred power in its nine long tails and to live for a millennium.",
    "Vulpix",
    "It doesn't have"
)

Jigglypuff_en = CreatePokemon(
    "#039",
    "Jigglypuff",
    ["Normal", "Fairy"],
    ["Pound", "Sing", "Disable", "Defense Curl", "Disarming", "Sweet Kiss", "Charm", "Copycat"],
    "When it wavers its big, round eyes, it begins singing a lullaby that makes everyone drowsy.",
    "Igglybuff",
    "Wigglytuff"
)

Wigglytuff_en = CreatePokemon(
    "#040",
    "Wigglytuff",
    ["Normal", "Fairy"],
    ["Body Slam", "Double-Edge", "Sing", "Disable", "Mimic", "Defense Curl", "Rest", "Hyper Voice", "Covet", "Gyro Ball", "Round", "Echoed Voice", "Play Rough", "Pound", "Sweet Kiss", "Disarming", "Charm", "Stockpile", "Swallow", "Spit Up", "Copycat"],
    "Its fine fur feels sublime to the touch. It can expand its body by inhaling air.",
    "Igglybuff / Jigglypuff",
    "It doesn't have"
)

Zubat_en = CreatePokemon(
    "#041",
    "Zubat",
    ["Poison", "Flying"],
    ["Gust"],
    "Make its home in gloomy caves, Atrophied eyes have left this Pokémon blind, so it scans its surroundings via sound waves that it emits from its mouth as it flies.",
    "It doesn't have",
    "Golbat (lvl 22) / Crobat (Happiness)"
)

Golbat_en = CreatePokemon(
    "#042",
    "Golbat",
    ["Poison", "Flying"],
    ["Gust"],
    "It sinks its sharp fangs into other creatures and slurps up their blood. A closer look at the fangs reveals that they are hollow and akin to straws.",
    "Zubat",
    "Crobat (Happiness)"
)

Oddish_en = CreatePokemon(
    "#043",
    "Oddish",
    ["Grass", "Poison"],
    ["Absorve", "Growth"],
    "It often plants its root feet in the ground during the day and sows seeds as it walks about at night.",
    "It doesn't have",
    "Gloom (lvl 21) / Vileplume (Leaf Stone) or Bellossom (Sun Stone)"
)

Gloom_en = CreatePokemon(
    "#044",
    "Gloom",
    ["Grass", "Poison"],
    ["Acid", "Absorb", "Sweet Scent", "Growth"],
    "The nectar it drools from its mouth smells so atrocious that it can make noses curl from more than a mile away.",
    "Gloom",
    "Vileplume (Leaf Stone) or Bellossom (Sun Stone)"
)

Vileplume_en = CreatePokemon(
    "#045",
    "Vileplume",
    ["Grass", "Poison"],
    ["Petal Blizzard", "Acid", "Absorb", "Mega Drain", "Poison Powder", "Stun Spore", "Sleep Powder", "Petal Dance", "Toxic", "Giga Drain", "Sweet Scent", "Aromatherapy", "Growth", "Moonblast", "Grassy Terrain", "Moonlight"],
    "Its petals are the largest in the world. As it walks, it scatters extremely allergenic pollen.",
    "Oddish / Gloom",
    "It doesn't have"
)

Paras_en = CreatePokemon(
    "#046",
    "Paras",
    ["Bug", "Grass"],
    ["Absorb"],
    "Sometimes seen at the foot of trees in humid forests. The mushrooms on its back --called tochukaso-- are not present on infant specimens and instead emerge as Paras matures.",
    "It doesn't have",
    "Parasect (lvl 24)"
)

Parasect_en = CreatePokemon(
    "#047",
    "Parasect",
    ["Bug", "Grass"],
    ["Absorb"],
    "Mushroom-lacking specimens of this Pokémon lie unmoving in the forest, lending credence to the hypothesis that the large mushroom is in control of Parasect's actions.",
    "Paras",
    "It doesn't have"
)

Venonat_en = CreatePokemon(
    "#048",
    "Venonat",
    ["Bug", "Poison"],
    ["Tackle", "Disable", "Struggle Bug"],
    "Its big eyes are actually clusters of tiny eyes. At night, its kind is drawn by light.",
    "It doesn't have",
    "Venomoth (lvl 31)"
)

Venomoth_en = CreatePokemon(
    "#049",
    "Venomoth",
    ["Bug", "Poison"],
    ["Gust", "Whirlwind", "Tackle", "Supersonic", "Bug Buzz", "Quiver Dance"],
    "It flutters its wings to scatter dustlike scales. The scales leach toxins if they contact skin.",
    "Venonat",
    "It doesn't have"
)

Diglett_en = CreatePokemon(
    "#050",
    "Diglett",
    ["Ground"],
    ["Scratch", "Sand Attack"],
    "This Pokémon lives underground. Because of its dark habitat, it is repelled by bright sunlight.",
    "It doesn't have",
    "Dugtrio (lvl 26)"
)

Dugtrio_en = CreatePokemon(
    "#051",
    "Dugtrio",
    ["Ground"],
    ["Sand Tomb", "Scratch", "Sand Attack", "Growl", "Tri Attack", "Astonish", "Night Slash"],
    "Its three heads move alternately, driving it through tough soil to depths of over 60 miles.",
    "Diglett",
    "It doesn't have"
)

Meowth_en = CreatePokemon(
    "#052",
    "Meowth",
    ["Normal"],
    ["Growl", "Fake Out"],
    "It is nocturnal by nature. If it spots something shiny, its eyes glitter as brightly as the shiny object.",
    "It doesn't have",
    "Persian (lvl 28)"
)

Persian_en = CreatePokemon(
    "#053",
    "Persian",
    ["Normal"],
    ["Power Gem", "Scratch", "Growl", "Fake Out", "Feint", "Switcheroo"],
    "It is a very haughty Pokémon. Among fans of Persian, the size of the jewel in its forehead is a topic of much talk.",
    "Meowth",
    "It doesn't have"
)

Psyduck_en = CreatePokemon(
    "#054",
    "Psyduck",
    ["Water"],
    ["Bubble"],
    "Suffers perpetual headaches. If the agony grows too great, Psyduck's latent power erupts, contrary to Psyduck's intent. Ergo, I am exploring ways to ease the pain.",
    "It doesn't have",
    "Golduck (lvl 33)"
)

Golduck_en = CreatePokemon(
    "#055",
    "Golduck",
    ["Water"],
    ["Bubble"],
    "Its body is strong, and it has webbing on its hands and feet. Golduck can swim easily through rough seas, clawing its way through the high waves.",
    "Psyduck",
    "It doesn't have"
)

Mankey_en = CreatePokemon(
    "#056",
    "Mankey",
    ["Fighting"],
    ["Scratch", "Leer", "Low Kick", "Focus Energy", "Covet"],
    "It lives in treetop colonies. If one member of the group becomes enraged, the whole colony rampages for no reason.",
    "It doesn't have",
    "Primeape (lvl 28)"
)

Primeape_en = CreatePokemon(
    "#057",
    "Primeape",
    ["Fighting"],
    ["Scratch", "Leer", "Low Kick", "Focus Energy", "Covet", "Fling", "Final Gambit"],
    "It becomes angry if it sees an opponent's eyes and gets angrier if the opponent runs. Even after it beats the opponent, it is still angry.",
    "Mankey",
    "It doesn't have"
)

Growlithe_en = CreatePokemon(
    "#058",
    "Growlithe",
    ["Fire"],
    ["Leer", "Ember"],
    "It is a Pokémon with a loyal nature. It will remain motionless until it is given an order by its Trainer.",
    "It doesn't have",
    "Arcanine (Fire Stone)"
)

Arcanine_en = CreatePokemon(
    "#059",
    "Arcanine",
    ["Fire"],
    ["Extreme Speed", "Take Down", "Leer", "Bite", "Roar", "Ember", "Flamethrower", "Flame Wheel", "Extreme Speed", "Helping Hand", "Fire Fang", "Retaliate", "Play Rough", "Burn Up", "Agility", "Crunch", "Reversal", "Flare Blitz", "Howl"],
    "Its proud and regal appearance has captured the hearts of people since long ago.",
    "Growlithe",
    "It doesn't have"
)

Poliwag_en = CreatePokemon(
    "#060",
    "Poliwag",
    ["Water"],
    ["Water", "Hypnosis"],
    "Its skin is so thin, its internal organs are visible it has trouble walking on its newly grown feet.",
    "It doesn't have",
    "Poliwhirl (lvl 25) / Poliwrath (Water Stone) or Politoed (Trade with King's rock)"
)

Poliwhirl_en = CreatePokemon(
    "#061",
    "Poliwhirl",
    ["Water"],
    ["Water Gun", "Hypnosis", "Mud Shot", "Pound"],
    "The spiral pattern on its belly subtly undulates. Staring at it gradually causes drowsiness.",
    "Poliwag",
    "Poliwrath (Water Stone) or Politoed (Trade with King's rock)"
)

Poliwrath_en = CreatePokemon(
    "#062",
    "Poliwrath",
    ["Water"],
    ["Submission", "Body Slam", "Double-Edge", "Water Gun", "Bubble Gun", "Hypnosis", "Mind Reader", "Dynamic Punch", "Rain Dance", "Circle Throw", "Pound", "Earth Power", "Hydro Pump", "Belly Drum", "Mud Shot"],
    "With its extremely tough muscles, it could keep swimming in the Pacific Ocean without resting.",
    "Poliwag / Poliwhirl",
    "It doesn't have"
)

Abra_en = CreatePokemon(
    "#063",
    "Abra",
    ["Psychic"],
    ["Teleport"],
    "Spends 18 hours of the day sleeping. Even while asleep, Abra can control its psychic powers--should danger approach, the Pokémon will simply teleport away.",
    "It doesn't have",
    "Kadabra (lvl 16) / Alakazam (Trade)"
)

Kadabra_en = CreatePokemon(
    "#064",
    "Kadabra",
    ["Psychic"],
    ["Confusion", "Teleport"],
    "There are rumors that a child with mystical powers became a Kadabra;however, this remains unverified. I suspect that the spoon Kadabra holds enhances its brain waves.",
    "Abra",
    "Alakazam (Trade)"
)

Alakazam_en = CreatePokemon(
    "#065",
    "Alakazam",
    ["Psychic"],
    ["Teleport"],
    "The longer Alakazam lives, the larger and heavier is head becomes. Our tests have shown that the strength of its psychic powers correlates positively to the weight of its head.",
    "Abra / Kadabra",
    "It doesn't have"
)

Machop_en = CreatePokemon(
    "#066",
    "Machop",
    ["Fighting"],
    ["Tackle"],
    "Though as small as a child, it has strength enough to easily throw a well-built adult. Striving to become ever stronger, Machop trains by carrying a Graveler on its shoulders.",
    "It doesn't have",
    "Machoke (lvl 28) / Machamp (Trade)"
)

Machoke_en = CreatePokemon(
    "#067",
    "Machoke",
    ["Fighting"],
    ["Tacke"],
    "A sturdy creature boasting a robust physique and boundless stamina. Loves training above all else and voluntarily assists with tasks such as construction and clearing land.",
    "Machop",
    "Machamp (Trade)"
)

Machamp_en = CreatePokemon(
    "#068",
    "Machamp",
    ["Fighting"],
    ["Tackle"],
    "In close combat, its four arms afford it offensive and defensive supremacy. In but a blink, this valiant Pokémon can overwhelm its foes with more than 1,000 blows from its fists.",
    "Machop / Machoke",
    "It doesn't have"
)

Bellsprout_en = CreatePokemon(
    "#069",
    "Bellsprout",
    ["Grass", "Poison"],
    ["Vine Whip"],
    "It prefers hot and humid environments. It is quick at capturing prey with its vines.",
    "It doesn't have",
    "Weepinbell (lvl 21) / Victreebel (Leaf Stone)"
)

Weepinbell_en = CreatePokemon(
    "#070",
    "Weepinbell",
    ["Grass", "Poison"],
    ["Vine Whip", "Wrap", "Growth"],
    "This Pokémon has the appearance of a plant. It captures unwary prey by dousing them with a toxic powder.",
    "Bellsprout",
    "Victreebel (Leaf Stone)"
)

Victreebel_en = CreatePokemon(
    "#071",
    "Victreebel",
    ["Grass", "Poison"],
    ["Leaf Tornado", "Vine Whip", "Wrap", "Acid", "Razor Leaf", "Poison Powder", "Stun Spore", "Sleep Powder", "Sweet Scent", "Stockpile", "Spit Up", "Swallow", "Knock Off", "Gastro Acid", "Poison Jab", "Growth", "Slam", "Leaf Storm", "Leaf Blade"],
    "In its mouth, it pools a fragrant nectar-like fluid. The fluid is really an acid that dissolves anything.",
    "Bellsprout / Weepinbell",
    "It doesn't have"
)

Tentacool_en = CreatePokemon(
    "#072",
    "Tentacool",
    ["Water", "Poison"],
    ["Poison Sting"],
    "They fire beams from the glassy, magenta orbs that resemble eyes atop their heads, and they drift in shallow seas. During low tide, they can sometimes be found on beaches, desiccated.",
    "It doesn't have",
    "Tentacruel (lvl 30)"
)

Tentacruel_en = CreatePokemon(
    "#073",
    "Tentacruel",
    ["Water", "Poison"],
    ["Poison Sting"],
    "It has 80 tentacles, each with a venomous tip. These tentacles are also extendible, lengthening when Tentacruel attempts to catch prey. Use caution.",
    "Tentacool",
    "It doesn't have"
)

Geodude_en = CreatePokemon(
    "#074",
    "Geodude",
    ["Rock", "Ground"],
    ["Rollout"],
    "Makes its home in mountainous regions, using its arms to climb along harsh mountain roads. Can be troublesome--carelessly kicking one will cause it to fly into a rage and chase after you.",
    "It doesn't have",
    "Graveler (lvl 25) / Golem (Trade)"
)

Graveler_en = CreatePokemon(
    "#075",
    "Graveler",
    ["Rock", "Ground"],
    ["Rollout"],
    "Dwells in holes dug into sheer walls of stone. It enjoys rolling down slopes as though it were a boulder during a rockfall, so keep an eye upward while traversing mountain roads.",
    "Geodude",
    "Golem (Trade)"
)

Golem_en = CreatePokemon(
    "#076",
    "Golem",
    ["Rock", "Ground"],
    ["Rollout"],
    "The rocklike shell is shead each year. THe cast-off shell then crumbles, reverting to a mass of soil, which can be spread across fields to promote crop growth.",
    "Geodude / Graveler",
    "It doesn't have"
)

Ponyta_en = CreatePokemon(
    "#077",
    "Ponyta",
    ["Fire"],
    ["Tackle"],
    "These Pokémon live in heards out in the grassland. Newborn foals lack their fiery manes, wich will develop about an hour after birth.",
    "It doesn't have",
    "Rapidash (lvl 40)"
)

Rapidash_en = CreatePokemon(
    "#078",
    "Rapidash",
    ["Fire"],
    ["Tackle"],
    "Fiery mane aglow, Rapidash darts like an arrow across the land. This prodigiously swift creature can traverse the vast region of Hisui in a day and a half.",
    "Ponyta",
    "It doesn't have"
)

Slowpoke_en = CreatePokemon(
    "#079",
    "Slowpoke",
    ["Water", "Psychic"],
    ["Tackle", "Curse"],
    "Although slow, it is skilled at fishing with its tail. It does not feel pain if its tail is bitten.",
    "It doesn't have",
    "Slowbro (lvl 37) or Slowking (With King's Rock)"
)

Slowbro_en = CreatePokemon(
    "#080",
    "Slowbro",
    ["Water", "Psychic"],
    ["Tackle", "Growl", "Water Gun", "Withdraw", "Curse"],
    "Though usually dim-witted, it seems to become inspired if the Shellder on its tail bites down.",
    "Slowpoke",
    "It doesn't have"
)

Magnemite_en = CreatePokemon(
    "#081",
    "Magnemite",
    ["Electric", "Steel"],
    ["Thunder Shock"],
    "A bizarre Pokémon with but a single eye embedded in an iron sphere. I suspect this creature levitates due to the magnetism it emits from its arms, which resemble horseshoe-shaped magnets.",
    "It doesn't have",
    "Magneton (lvl 30) / Magnezone (Level up at a Magnectic Place)"
)

Magneton_en = CreatePokemon(
    "#082",
    "Magneton",
    ["Electric", "Steel"],
    ["Thunder Shock"],
    "Three Magnemite gathered to evolve into this Pokémon. The source of much vexation on my part, as its powerful magnetism destroys my research equipment.",
    "Magneton",
    "Magnezone (Level up at a Magnectic Place)"
)

Farfetchd_en = CreatePokemon(
    "#083",
    "Farfetch'd",
    ["Normal", "Flying"],
    ["Sand Attack", "Peck"],
    "It can't live without the stalk it holds. That's why it defends the stalk from attackers with its life.",
    "It doesn't have",
    "It doesn't have"
)

Doduo_en = CreatePokemon(
    "#084",
    "Doduo",
    ["Normal", "Flying"],
    ["Growl", "Peck"],
    "The brains in its two heads appear to communicate emotions to each other with a telepathic power.",
    "It doesn't have",
    "Dodrio (lvl 31)"
)

Dodrio_en = CreatePokemon(
    "#085",
    "Dodrio",
    ["Normal", "Flying"],
    ["Tri Attack", "Growl", "Peck", "Quick Attack"],
    "When Doduo evolves into this off breed, one of its heads splits into two. This Pokémon runs at nearly 40 mph.",
    "Doduo",
    "It doesn't have"
)

Seel_en = CreatePokemon(
    "#086",
    "Seel",
    ["Water"],
    ["Headbutt"],
    "This Pokémon lives on icebergs. It uses the sharp point on its head to break up ice as it swims in the sea.",
    "It doesn't have",
    "Dewgong (lvl 34)"
)

Dewgong_en = CreatePokemon(
    "#087",
    "Dewgong",
    ["Water", "Ice"],
    ["Sheer Cold", "Headbutt", "Growl", "Water Gun", "Bubble Beam", "Icy Wind"],
    "In snow, the pure white coat covering its body obscures it from predators.",
    "Seel",
    "It doesn't have"
)

Grimer_en = CreatePokemon(
    "#088",
    "Grimer",
    ["Poison"],
    ["Pound", "Poison Gas"],
    "It was born when sludge in a dirty stream was exposed to the mooon's X-rays. It appears among filth.",
    "It doesn't have",
    "Muk (lvl 38)"
)

Muk_en = CreatePokemon(
    "#089",
    "Muk",
    ["Poison"],
    ["Venom Drench", "Pound", "Harden", "Poison Gas", "Mud-Slap"],
    "A toxic fluid seeps from its body. The fluid kills plants and trees immediately upon contact.",
    "Grimer",
    "It doesn't have"
)

Shellder_en = CreatePokemon(
    "#090",
    "Shellder",
    ["Water"],
    ["Tackle", "Water Gun"],
    "It swims backward by opening and closing its two shells. Its large tongue is always kept hanging out.",
    "It doesn't have",
    "Cloyster (Water Stone)"
)

Cloyster_en = CreatePokemon(
    "#091",
    "Cloyster",
    ["Water", "Ice"],
    ["Icicle Spear", "Supersonic", "Water Gun", "Hydro Pump", "Ice Beam", "Aurora Beam", "Withdraw", "Protect", "Spikes", "Whirlpool", "Iron Defense", "Toxic Spikes", "Sheel Smash", "Tackle", "Leer", "Icicle Crash", "Razor Shell", "Ice Shard"],
    "It fights by keeping its shell tightly shut for protection and by shooting spikes to repel foes.",
    "Shellder",
    "It doesn't have"
)

Gastly_en = CreatePokemon(
    "#092",
    "Gastly",
    ["Ghost", "Poison"],
    ["Astonish"],
    "Gaseous and completely impalpable. Also highly dangerous-- inhaling part of its poisonous body will cause one to faint instantly.",
    "It doesn't have",
    "Hunter (lvl 25) / Gengar (Trade)"
)

Haunter_en = CreatePokemon(
    "#093",
    "Haunter",
    ["Ghost", "Poison"],
    ["Astonish"],
    "This frightful, malevolent spirit can glide through walls, appearing wherever it likes. According to rumor, victims of a Haunter's lick will wither to death day by day.",
    "Gastly",
    "Gengar (Trade)"
)

Gengar_en = CreatePokemon(
    "#094",
    "Gengar",
    ["Ghost", "Poison"],
    ["Astonish"],
    "Possesses potential victims' shadows in an effort to steal away the victims' lives. If your shandow begins to laugh, you must take hold of a protective charm posthaste!",
    "Gastly / Haunter",
    "It doesn't have"
)

Onix_en = CreatePokemon(
    "#095",
    "Onix",
    ["Rock", "Ground"],
    ["Rollout"],
    "This chain of immense stones resembles a giant serpent. Tremors shake the earth above as it burrows deep beneath the ground, feeding on boulders as it goes.",
    "It doesn't have",
    "Steelix (With Metal Coat)"
)

Drowzee_en = CreatePokemon(
    "#096",
    "Drowzee",
    ["Psychic"],
    ["Pound", "Hypnosis"],
    "It can tell what people are dreaming by sniffing with its big nose. It loves fun dreams.",
    "It doesn't have",
    "Hypno (lvl 26)"
)

Hypno_en = CreatePokemon(
    "#097",
    "Hypno",
    ["Psychic"],
    ["Pound", "Disable", "Confusion", "Hypnosis", "Future Sight", "Switcheroo", "Nasty Plot"],
    "Seeing its swinging pendulum can induce sleep in three seconds, even in someone who just woke up.",
    "Dowzee",
    "It doesn't have"
)

Krabby_en = CreatePokemon(
    "#098",
    "Krabby",
    ["Water"],
    ["Leer", "Water Gun"],
    "It lives in burrows dug on sandy beaches. Its pincers fully grow back if they are lost in battle.",
    "It doesn't have",
    "Kingler (lvl 28)"
)

Kingler_en = CreatePokemon(
    "#099",
    "Kingler",
    ["Water"],
    ["Leer", "Water Gun", "Harden", "Metal Claw", "Wide Guard", "Hammer Arm"],
    "The larger pincer has 10,000-horsepower strength. However, it is so heavy, it is difficult to aim.",
    "Krabby",
    "It doesn't have"
)

Voltorb_en = CreatePokemon(
    "#100",
    "Voltorb",
    ["Electric"],
    ["Tackle", "Charge"],
    "It looks just like a Poké Ball. It is dangerous because it may electrocute or explode on touch.",
    "It doesn't have",
    "Electrode (lvl 30)"
)

Electrode_en = CreatePokemon(
    "#101",
    "Electrode",
    ["Electric"],
    ["Tackle", "Charge", "Eerie Impulse", "Magnetic Flux"],
    "It is known to drift on winds if it is bloated to bursting with stored electricity.",
    "Voltorb",
    "It doesn't have"
)

Exeggcute_en = CreatePokemon(
    "#102",
    "Exeggcute",
    ["Grass", "Psychic"],
    ["Hypnosis", "Absorb"],
    "Its six eggs converse using telepathy. They can quickly gather if they become separated.",
    "It doesn't have",
    "Exeggutor (Leaf Stone)"
)

Exeggutor_en = CreatePokemon(
    "#103",
    "Exeggutor",
    ["Grass", "Psychic"],
    ["Stomp", "Mega Drain", "Solar Beam", "Confusion", "Hypnosis", "Reflect", "Giga Drain", "Synthesis", "Bullet Seed", "Worry Seed", "Seed Bomb", "Leaf Storm", "Wood Hammer", "Psyshock", "Extrasensory, Uproar", "Absorb", "Leech Seed"],
    "It is called the Walking Jungle. If a head grows too big, it falls off and becomes an Exeggcute.",
    "Exeggcute",
    "It doesn't have"
)

Cubone_en = CreatePokemon(
    "#104",
    "Cubone",
    ["Ground"],
    ["Growl", "Mud-Slap"],
    "When it thinks of its dead mother, it cries. Its crying makes the skull it wears rattle hollowly.",
    "It doesn't have",
    "Marowak (lvl 28)"
)

Marowak_en = CreatePokemon(
    "#105",
    "Marowak",
    ["Ground"],
    ["Tail Whip", "Growl", "Mud-Slap", "False Swipe"],
    "The bones it uses have been in its possession since it was born. It has a ferocious nature.",
    "Cubone",
    "It doesn't have"
)

Hitmonlee_en = CreatePokemon(
    "#106",
    "Hitmonlee",
    ["Fighting"],
    ["Brick Break", "Focus Energy", "Helping Hand", "Feint", "Low Sweep", "Tackle", "Fake Out"],
    "Its legs can stretch to double their length. First-time foes are startled by Hitmonlee's extensible reach.",
    "Tyrogue",
    "It doesn't have"
)

Hitmonchan_en = CreatePokemon(
    "#107",
    "Hitmonchan",
    ["Fighting"],
    ["Drain Punch", "Helping Hand", "Feint", "Drain Punch", "Vaccum Wave", "Bullet Punch", "Focus Energy", "Tackle", "Fake Out"],
    "When Hitmonchan twists its arm while throwing a punch, the blow will pulverize even concrete. The Pokémon rests after three minutes of fighting.",
    "Tyrogue",
    "It doesn't have"
)

Lickitung_en = CreatePokemon(
    "#108",
    "Lickitung",
    ["Normal"],
    ["Tackle"],
    "Wields its long tongue deftly, as though it were an arm. The Pokémon's viscous saliva, once it has been collected and boiled down, yields a strong and highly useful adhesive.",
    "It doesn't have",
    "Lickilicky (Level up with Rollout)"
)

Koffing_en = CreatePokemon(
    "#109",
    "Koffing",
    ["Poison"],
    ["Tackle", "Poison Gas"],
    "Lighter-than-air gases in its body keep it aloft. The gases not only smell; they are also explosive.",
    "It doesn't have",
    "Weezing (lvl 35)"
)

Weezing_en = CreatePokemon(
    "#110",
    "Weezing",
    ["Poison"],
    ["Double Hit", "Tackle", "Smokescreen", "Smog", "Poison Gas", "Double Hit", "Heat Wave"],
    "It grows by feeding on gases released by garbage. Though very rare, triplets have been found.",
    "Koffing",
    "It doesn't have"
)

Rhyhorn_en = CreatePokemon(
    "#111",
    "Rhyhorn",
    ["Ground", "Rock"],
    ["Tackle"],
    "Ludicrously strong--when it butts heads with a mountain, it is the mountain that shatters. But its short legs struggle with turns, and it is incapable of stopping unless it collides with something.",
    "It doesn't have",
    "Rhydon (lvl 42) / Rhyperior (trade with Protector)"
)

Rhydon_en = CreatePokemon(
    "#112",
    "Rhydon",
    ["Ground", "Rock"],
    ["Tackle"],
    "Rapidly rotates its horn to bore through bedrock. It swaggers around volcanic regions, protected from the lava's heat by it tough, armorlike hide.",
    "Rhydon",
    "Rhyperior (trade with Protector)"
)

Chansey_en = CreatePokemon(
    "#113",
    "Chansey",
    ["Normal"],
    ["Tackle"],
    "This purehearted Pokémon shares its eggs with the injured. These eggs are so nutritious that they've been nicknamed \"doctors\" doubles.",
    "Happiny",
    "Blissey (Hapiness)"
)

Tangela_en = CreatePokemon(
    "#114",
    "Tangela",
    ["Grass"],
    ["Absorb"],
    "It is cloaked entirely in blue vines, preventing any glimpse of its true identity. The vines impart a refreshing sensation when chewed-- they're useful as a spice.",
    "It doesn't have",
    "Tangrowth (level up with Ancient Power)"
)

Kangaskhan_en = CreatePokemon(
    "#115",
    "Kangaskhan",
    ["Normal"],
    ["Tail Whip", "Pound"],
    "It raises its offspring in its belly pouch. It lets its baby out to play only when it feels safe to do so.",
    "It doesn't have",
    "It doesn't have"
)

Horsea_en = CreatePokemon(
    "#116",
    "Horsea",
    ["Water"],
    ["Leer", "Water Gun"],
    "It makes its nest in the shade of corals. If it senses danger, it spits black ink and flees.",
    "It doesn't have",
    "Seadra (lvl 32) / Kingdra (Trade with Dragon Scale)"
)

Seadra_en = CreatePokemon(
    "#117",
    "Seadra",
    ["Water"],
    ["Leer", "Water Gun", "Smokescreen", "Twister"],
    "Its spines provide protection. Its fins and bones are prized as traditional medicine ingredients.",
    "Horsea",
    "Kingdra (Trade with Dragon Scale)"
)

Goldeen_en = CreatePokemon(
    "#118",
    "Goldeen",
    ["Water"],
    ["Tail Whip", "Peck"],
    "It swims elegantly by flittering its tail fin as if it were a dress. It has the look of a queen.",
    "It doesn't have",
    "Seaking (lvl 33)"
)

Seaking_en = CreatePokemon(
    "#119",
    "Seaking",
    ["Water"],
    ["Tail Whip", "Supersonic", "Peck", "Water Pulse"],
    "It makes its nest by hollowing out boulders in streams with its horn. The Pokémon defends its eggs with its life.",
    "Goldeen",
    "It doesn't have"
)

Staryu_en = CreatePokemon(
    "#120",
    "Staryu",
    ["Water"],
    ["Tackle", "Harden"],
    "If Staryu's body is damaged, it will regenerate as long as the red core remains. The core flashes at midnight.",
    "It doesn't have",
    "Starmie (Water Stone)"
)

Starmie_en = CreatePokemon(
    "#121",
    "Starmie",
    ["Water", "Psychic"],
    ["Tackle", "Water Gun", "Hydro Pump", "Surf", "Psychic", "Recover", "Harden", "Confuse Ray", "Light Screen", "Swift", "Rapid Spin", "Brine", "Minimize", "Psybeam", "Power Gem", "Cosmic Power"],
    "At the center of its body is a red core that sends mysterious radio signals into the night sky.",
    "Staryu",
    "It doesn't have"
)

Mr_Mime_en = CreatePokemon(
    "#122",
    "Mr.Mime",
    ["Psychic", "Fairy"],
    ["Confusion"],
    "The behavior of this clown-like Pokémon reminds one of pantmine. It creates invisible walls using a force emitted from its fingertips.",
    "Mime Jr.",
    "It doesn't have"
)

Scyther_en = CreatePokemon(
    "#123",
    "Scyther",
    ["Bug", "Flying"],
    ["Quick Attack"],
    "The large, wickedly sharp scythes on its forearms are truly fearsome weapons. Prey's attempts to flee are unfailingly thwarted by this Pokémon's nimble motions.",
    "It doesn't have",
    "Scizor (trade with Metal Coat) / Kleavor (Black Augurite)."
)

Jynx_en = CreatePokemon(
    "#124",
    "Jynx",
    ["Ice", "Psychic"],
    ["Pound", "Lick", "Powder Snow", "Sweet Kiss", "Copycat"],
    "Its cries sound like human speech. However, it is impossible to tell what it is trying to say.",
    "Smoochum",
    "It doesn't have"
)

Electabuzz_en = CreatePokemon(
    "#125",
    "Electabuzz",
    ["Electric"],
    ["Thunder Shock"],
    "Feeds on electrical energy. During sudden showers beneath looming thunderclouds, one can observe Electabuzz scaling tall trees, where the Pokémon will then wait for lightning to strike.",
    "Elekid",
    "Electivire (Trade with Electrizer)"
)

Magmar_en = CreatePokemon(
    "#126",
    "Magmar",
    ["Fire"],
    ["Ember"],
    "Legend has it that this Pokémon was born from the crater of a volcano. When wounded, it bathes in lava to heal its body, much as one would soak in a hot spring.",
    "Magby",
    "Magmortar (Trade with Magmarizer)"
)

Pinsir_en = CreatePokemon(
    "#127",
    "Pinsir",
    ["Bug"],
    ["Vice Grip", "Harden"],
    "It grips prey with its pincers until the prey is torn apart. What it can't tear, It tosses far away.",
    "It doesn't have",
    "It doesn't have"
)

Tauros_en = CreatePokemon(
    "#128",
    "Tauros",
    ["Normal"],
    ["Tackle", "Tail Whip"],
    "Once it takes aim at its prey, it makes a headlong charge. It is famous for its violent nature.",
    "It doesn't have",
    "It doesn't have"
)

Magikarp_en = CreatePokemon(
    "#129",
    "Magikarp",
    ["Water"],
    ["Splash"],
    "A feeble, pitiful imbecile of a Pokémon that is nonetheless very hardy. Unperturbed by turbid water, it can be found living in all sorts of places.",
    "It doesn't have",
    "Gyrados (lvl 20)"
)

Gyarados_en = CreatePokemon(
    "#130",
    "Gyarados",
    ["Water", "Flying"],
    ["Water Pulse", "Splash"],
    "I suspect this Pokémon to be the true identity of a dragon written of in ancient texts, which claimed that it razed an entire village with white-hot beams from its maw.",
    "Magikarp",
    "It doesn't have"
)

Lapras_en = CreatePokemon(
    "#131",
    "Lapras",
    ["Water", "Ice"],
    ["Growl", "Water Gun"],
    "It loves crossing the sea with people and Pokémon on its back. It understands human speech.",
    "It doesn't have",
    "It doesn't have"
)

Ditto_en = CreatePokemon(
    "#132",
    "Ditto",
    ["Normal"],
    ["Transform"],
    "It has the ability to reconstitute its entire cellular structure to transform into whatever it sees.",
    "It doesn't have",
    "It doesn't have"
)

Eevee_en = CreatePokemon(
    "#133",
    "Eevee",
    ["Normal"],
    ["Tackle"],
    "Harbors the potential to evolve into manifold forms. Within Eevee lies the key to the mysteries of Pokémon evolution--I'm certain of it.",
    "It doesn't have",
    "Vaporeon (Water Stone) / Jolteon (Thunder Stone) / Flareon (Fire Stone) / Espeon (Happiness during in the day) / Umbreon (Happiness during at night) / Leafeon (Level up near the Moss Rock) / Glaceon (level up with Ice Rock) / Sylveon (Affection knowing fairy-type technique.)" 
)

Vaporeon_en = CreatePokemon(
    "#134",
    "Vaporeon",
    ["Water"],
    ["Bubble", "Tackle"],
    "Tests show that its cells closely resemble water molecules, which perhaps explains its ability to conceal its form while submerged. I believe the origins of mermaid folklore lie with this Pokémon.",
    "Eevee",
    "It doesn't have"
)

Jolteon_en = CreatePokemon(
    "#135",
    "Jolteon",
    ["Electric"],
    ["Thunder Shock", "Tackle"],
    "Bristles its fur into sharp, needlelike points when enraged. One can hear electricity crackle in its breath when it exhales.",
    "Eevee",
    "It doesn't have"
)

Flareon_en = CreatePokemon(
    "#136",
    "Flareon",
    ["Fire"],
    ["Ember", "Tackle"],
    "Flames burn within a saclike organ inside this Pokémon. When Flareon inhales, these flames frow in intensity, reaching a mighty 3,000 degrees Fahrenheit.",
    "Eevee",
    "It doesn't have"
)

Porygon_en = CreatePokemon(
    "#137",
    "Porygon",
    ["Normal"],
    ["Tackle"],
    "It has no discernible heartbeat and does not seem to draw breath, and yet it appears to function without issue. I cannot even begin to explain this utterly bizarre anomaly.",
    "It doesn't have",
    "Porygon 2 (Trade with Up-Grade) / Porygon-Z (Trade with Dubious Disc)"
)

Omanyte_en = CreatePokemon(
    "#138",
    "Omanyte",
    ["Rock", "Water"],
    ["Bind", "Withdraw"],
    "It's a Pokémon that was resurrected from a fossil using modern science. It swam in ancient seas.",
    "It doesn't have",
    "Omastar (lvl 40)"
)

Omastar_en = CreatePokemon(
    "#139",
    "Omastar",
    ["Rock", "Water"],
    ["Crunch", "Bind", "Withdraw", "Rollout", "Sand Attack"],
    "It is thought that this Pokémon became extinct because its spiral shell grew too large.",
    "Omanyte",
    "It doesn't have"
)

Kabuto_en = CreatePokemon(
    "#140",
    "Kabuto",
    ["Rock", "Water"],
    ["Absorb", "Harden"],
    "It is thought to have inhabited beaches 300 million years ago. It is protected by a sturdy shell.",
    "It doesn't have",
    "Kabutops (lvl 40)"
)

Kabutops_en = CreatePokemon(
    "#141",
    "Kabutops",
    ["Rock", "Water"],
    ["Slash", "Scratch", "Sand Attack", "Absorb", "Harden", "Feint", "Night Slash"],
    "It is thought that this Pokémon came onto land because its prey adapted to life on land.",
    "Kabuto",
    "It doesn't have"
)

Aerodactyl_en = CreatePokemon(
    "#142",
    "Aerodactyl",
    ["Rock", "Flying"],
    ["Bite", "Ancient Power"],
    "It's a Pokémon that roamed the skies in the dinosaur era. Its teeth are like saw blades.",
    "It doesn't have",
    "It doesn't have"
)

Snorlax_en = CreatePokemon(
    "#143",
    "Snorlax",
    ["Normal"],
    ["Rollout"],
    "This glutton appears in billages without warning and devours the entirety of their rice granaries--such occurrences have long been counted among the gravest of disasters.",
    "Munchlax",
    "It doesn't have"
)

Articuno_en = CreatePokemon(
    "#144",
    "Articuno",
    ["Ice", "Flying"],
    ["Gust", "Mist"],
    "This legendary bird Pokémon can create blizzards by freezing moinsture in the air.",
    "It doesn't have",
    "It doesn't have"
)

Zapdos_en = CreatePokemon(
    "#145",
    "Zapdos",
    ["Electric", "Flying"],
    ["Peck", "Thunder Wave"],
    "This legendary Pokémon is said to live in thunderclouds. It freely controls lightning bolts.",
    "It doesn't have",
    "It doesn't have"
)

Moltres_en = CreatePokemon(
    "#146",
    "Moltres",
    ["Fire", "Flying"],
    ["Leer", "Gust"],
    "It is one of the legendary bird Pokémon. Its appearance is said to indicate the coming of spring.",
    "It doesn't have",
    "It doesn't have"
)

Dratini_en = CreatePokemon(
    "#147",
    "Dratini",
    ["Dragon"],
    ["-"],
    "It is called the Mirage Pokémon because so few have seen it, but its shed skin has been found.",
    "It doesn't have",
    "Dragonair (lvl 30) / Dragonite (lvl 55)"
)

Dragonair_en = CreatePokemon(
    "#148",
    "Dragonair",
    ["Dragon"],
    ["Wrap", "Leer", "Thunder Wave", "Twister"],
    "If its body takes on an aura, the weather changes instantly. It is said to live in seas and lakes.",
    "Dratini",
    "Dragonite (lvl 55)"
)

Dragonite_en = CreatePokemon(
    "#149",
    "Dragonite",
    ["Dragon", "Flying"],
    ["Hurricane", "Fire Punch", "Thunder Punch", "Wing Attack", "Wrap", "Leer", "Thunder Wave", "Twister", "Roost", "Extreme Speed"],
    "It is said to make its home somewhere in the sea. It guides wrecked ships to shore.",
    "Dratini / Dragonair",
    "It doesn't have"
)

Mewtwo_en = CreatePokemon(
    "#150",
    "Mewtwo",
    ["Psychic"],
    ["Disable", "Confusion", "Swift", "Lases Focus", "Life Dew"],
    "Mewtwo was created by recombining Mew's genes. It's said to have the most savage heart among Pokémon.",
    "It doesn't have",
    "It doesn't have"
)

Mew_en = CreatePokemon(
    "#151",
    "Mew",
    ["Psychic"],
    ["Pound", "Reflect Type"],
    "Because it can use all kinds of moves, many scientists believe Mew to be the ancestor of Pokémon.",
    "It doesn't have",
    "It doesn't have"
)