import pokeansi

class CriaPokemon():
    def __init__(self, numero, nome, tipo, ataques, descricao, evolucao_anterior, proxima_evolucao):
        self.numero = numero
        self.nome = nome
        self.tipo = tipo
        self.ataques = ataques
        self.descricao = descricao
        self.evolucao_anterior = evolucao_anterior
        self.proxima_evolucao = proxima_evolucao

    def mostra_pokemon(self):
        print(f"\n\n            {self.numero}")
        print(f"\nNome: {self.nome} / Tipo: {self.tipo}")
        print(f"\nAtaques: {self.ataques}")
        print(f"\nDescrição: {self.descricao}")
        print(f"\nEvolução anterior: {self.evolucao_anterior}")
        print(f"\nPróxima evolução: {self.proxima_evolucao}")

# Primeira Geração

Bulbasaur_pt = CriaPokemon(
    "#001",
    "Bulbasaur",
    ["Grama", "Venenoso"],
    ["Growl", "Tackle"],
    "Bulbasaur pode ser visto cochilando sob luz solar intensa. Há uma semente em suas costas. Ao absorver os raios do sol, sua semente cresce progressivamente.",
    "n/a",
    "Ivysaur (lvl 16) / Venusaur (lvl 32)"
)

Ivysaur_pt = CriaPokemon(
    "#002",
    "Ivysaur",
    ["Grama", "Venenoso"],
    ["Vine Whip", "Tackle", "Growl", "Growth"],
    "Há um broto nas costas desse Pokémon. Para suportar seu peso, as pernas e o tronco de Ivysaur ficam grossos e fortes. Se começar a passar mais tempo deitado sob a luz do sol, é um sinal de que o broto florescerá em uma flor grande em breve.",
    "Bulbasaur",
    "Venusaur (lvl 32)"
)

Venusaur_pt = CriaPokemon(
    "#003",
    "Venusaur",
    ["Grama", "Venenoso"],
    ["Petal Blizzard", "Vine Whip", "Tackle", "Growl", "Growth", "Petal Dance"],
    "Há uma flor grande nas costas de Venusaur. Diz-se que a flor adquire cores vivas se receber muita nutrição e luz solar. O aroma da flor acalma as emoções das pessoas.",
    "Bulbasaur / Ivysaur",
    "n/a"
)

Charmander_pt = CriaPokemon(
    "#004",
    "Charmander",
    ["Fogo"],
    ["Scratch", "Growl"],
    "A chama que queima na ponta da cauda é uma indicação de suas emoções. A chama tremula quando Charmander está se divertindo. Se o Pokémon se enfurecer, a chama queima ferozmente.",
    "n/a",
    "Charmeleon (lvl 16) / Charizard (lvl 36)"
)

Charmeleon_pt = CriaPokemon(
    "#005",
    "Charmeleon",
    ["Fogo"],
    ["Scratch", "Growl", "Ember", "Smokescreen"],
    "Nas montanhas rochosas onde vive Charmeleon, sua cauda de fogo brilha à noite como as estrelas.",
    "Charmander",
    "Charizard (lvl 36)"
)

Charizard_pt = CriaPokemon(
    "#006",
    "Charizard",
    ["Fogo", "Voador"],
    ["Air Slash", "Scratch", "Growl", "Ember", "Smokescreen", "Heat Wave", "Dragon Claw"],
    "Charizard voa pelo céu em busca de oponentes poderosos. Ele respira um calor tão grande que derrete qualquer coisa. No entanto, nunca dá um sopro ardente a qualquer oponente mais fraco que ele.",
    "Charmander / Charmeleon",
    "n/a"
)

Squirtle_pt = CriaPokemon(
    "#007",
    "Squirtle",
    ["Água"],
    ["Tackle", "Tail Whip"],
    "A concha de Squirtle não é apenas usada para proteção. A forma arredondada da concha e as ranhuras na superficie ajudam a minimizar a resistência na água, permitindo que este Pokémon nade em alta velocidade.",
    "n/a",
    "Wartortle (lvl 16) / Blastoise (lvl 36)"
)

Wartortle_pt = CriaPokemon(
    "#008",
    "Wartortle",
    ["Água"],
    ["Tackle", "Tail Whip", "Water Gun", "Withdraw"],
    "Sua cauda é grande e coberta com um pêlo rico e grosso. A cauda torna-se cada vez mais profunda na cor à medida que Wartortle envelhece. Os arranhões em sua concha são um evidência da dureza deste Pokémon como um lutador.",
    "Squirtle",
    "Blastoise (lvl 36)"
)

Blastoise_pt = CriaPokemon(
    "#009",
    "Blastoise",
    ["Água"],
    ["Flash Cannon", "Tackle", "Tail Whip", "Water", "Withdraw"],
    "Blastoise tem canhões de água que se projetam de sua concha. Os bicos de água são muito precisos. Eles podem disparar balas de água com precisão suficiente para atingir latas vazias a uma distância de mais de 60 metros.",
    "Squirtle / Wartortle",
    "n/a"
)

Caterpie_pt = CriaPokemon(
    "#010",
    "Caterpie",
    ["Inseto"],
    ["Tackle", "String Shot", "Bug Bite"],
    "Caterpie tem um apetite voraz. Ele pode devorar folhas maiores que seu corpo diante dos seus olhos. De sua antena, este Pokémon libera um odor terrivelmente forte.",
    "n/a",
    "Metapod (lvl 7) / Butterfree (lvl 10)"
)

Metapod_pt = CriaPokemon(
    "#011",
    "Metapod",
    ["Inseto"],
    ["Harden"],
    "O Pokémon pode curar suas próprias condições de status, trocando de pele.",
    "Caterpie",
    "Butterfree (lvl 10)"
)

Butterfree_pt = CriaPokemon(
    "#012",
    "Butterfree",
    ["Inseto", "Voador"],
    ["Gust", "String Shot", "Bug Bite", "Harden", "Tackle"],
    "Butterfree tem uma capacidade superior para procurar mel delicioso de flores. Pode até procurar, extrair e transportar mel de flores que estão desabrochando a mais de 10 quilômetros do ninho.",
    "Caterpie / Metapod",
    "n/a"
)

Weedle_pt = CriaPokemon(
    "#013",
    "Weedle",
    ["Inseto", "Venenoso"],
    ["Poison Sting", "String Shot"],
    "Weedle tem um olfato extremamente agudo. Ele é capaz de distinguir seus tipos favoritos de folhas daquelas que não gosta, apenas farejando com seu grande nariz vermelho.",
    "n/a",
    "Kakuna (lvl 7) / Beedrill (lvl 10)"
)

Kakuna_pt = CriaPokemon(
    "#014",
    "Kakuna",
    ["Inseto", "Venenoso"],
    ["Harden"],
    "Kakuna permanece praticamente imóvel enquanto se agarra a uma árvore. No entanto, por dentro, é extremamente ocupado, enquanto se prepara para a sua evolução futura. Isso é evidente pelo quão quente a concha fica ao ser tocada.",
    "Weedle",
    "Beedrill (lvl 10)"
)

Beedrill_pt = CriaPokemon(
    "#015",
    "Beedrill",
    ["Inseto", "Venenoso"],
    ["Fury Attack", "String Shot", "Bug Bite", "Poison Sting", "Harden"],
    "Beedrill é extremamente territorial. Ninguém deve se aproximar de seu ninho, isso é para sua própria segurança. Se irritados, eles atacarão em um enxame furioso.",
    "Weedle / Kakuna",
    "n/a"
)

Pidgey_pt = CriaPokemon(
    "#016",
    "Pidgey",
    ["Normal", "Voador"],
    ["Tackle"],
    "Pidgey tem um senso de direção extremamente nítido. Ela é capaz de voltar para o seu ninho de forma infalível, por mais longe que possa ser removida de seu ambiente familiar.",
    "n/a",
    "Pidgeotto (lvl 18) / Pidgeot (lvl 36)"
)

Pidgeotto_pt = CriaPokemon(
    "#017",
    "Pidgeotto",
    ["Normal", "Voador"],
    ["Gust", "Sand Attack", "Tackle"],
    "Pidgeotto reivindica uma grande área como seu pŕoprio território. Este Pokémon voa, patrulhando seu espaço de vida. Se seu território é violado, não mostra piedade de punir completamente o inimigo com suas garras afiadas.",
    "Pidgey",
    "Pidgeot (lvl 36)"
)

Pidgeot_pt = CriaPokemon(
    "#018",
    "Pidgeot",
    ["Normal", "Voador"],
    ["Gust", "Sand Attack", "Tackle", "Quick Attack", "Hurricane"],
    "Este Pokémon tem uma plumagem deslumbrante de penas maravilhosamente brilhantes. Muitos treinadores são cativados pela impressionante beleza das penas em sua cabeça, obrigando-os a escolher Pidgeot como seu Pokémon.",
    "Pidgey / Pidgeotto",
    "n/a"
)

Rattata_pt = CriaPokemon(
    "#019",
    "Rattata",
    ["Normal"],
    ["Tackle", "Tail Whip"],
    "Seus dentes crescem continuamente ao longo de sua vida. Se seus incisivos ficarem muito longos, esse Pokémon se torna incapaz de comer, morrendo de fome.",
    "n/a",
    "Raticate (lvl 20)"
)

Raticate_pt = CriaPokemon(
    "#020",
    "Raticate",
    ["Normal"],
    ["Scary Face", "Swords Dance", "Tackle", "Tail Whip", "Quick Attack", "Focus Energy"],
    "As presas fortes de Raticate crescem constantemente. Para mantê-los triturados, roem pedras e troncos. Pode até mastigar as paredes das casas. Seus bigodes são essenciais para manter o equilíbrio. Não importa o quão amigável você seja, ele ficará com raiva e o morderá se tocar em seus bigodes.",
    "Rattata",
    "n/a"
)

Spearow_pt = CriaPokemon(
    "#021",
    "Spearow",
    ["Normal", "Voador"],
    ["Growl", "Peck"],
    "Seu grito alto pode ser ouvido a mais de 800 metros de distância. Se seu grito alto e agudo for ouvido ecoando por toda parte, é sinal de que eles estão alertando um ao outro sobre o perigo.",
    "n/a",
    "Fearow (lvl 20)"
)

Fearow_pt = CriaPokemon(
    "#022",
    "Fearow",
    ["Normal", "Voador"],
    ["Leer", "Growl", "Peck", "Pluck", "Drill Run"],
    "Não há nenhum problema em voar continuamente por um dia inteiro carregando uma carga pesada. O medo é reconhecido pelo pescoço longo e pelo bico alongado. Eles são convenientemente modelados para capturar presas no solo ou na água. Ele habilmente move seu bico longo e magro para colher presas.",
    "Spearow",
    "n/a"
)

Ekans_pt = CriaPokemon(
    "#023",
    "Ekans",
    ["Venenoso"],
    ["Wrap", "Leer"],
    "Ekans se enrola em espiral enquanto descansa. Assumindo a uma ameaça de qualquer direção com um brilho na cabeça erguida. Quanto mais velho fica, mais cresce. À noite, envolve seu corpo comprido em volta dos galhos das árvores para descansar.",
    "n/a",
    "Arbok (lvl 22)"
)

Arbok_pt = CriaPokemon(
    "#024",
    "Arbok",
    ["Venenoso"],
    ["Crunch", "Wrap", "Poison Sting", "Leer", "Bite", "Thunder Fang", "Ice Fang", "Fire Fang"],
    "Este Pokémon é terrivelmente forte para contrair as coisas com seu corpo. Pode até achatar tambores de óleo de aço. Uma vez que Arbok envolve seu corpo em torno de seu inimigo, é impossível escapar do abraço esmagador.",
    "Arbok",
    "n/a"
)

Pikachu_pt = CriaPokemon(
    "#025",
    "Pikachu",
    ["Elétrico"],
    ["Thunder Shock", "Quick Attack", "Thunder Wave", "Swift", "Spark", "Thunderbolt", "Iron Tail", "Thunder"],
    "É de sua natureza armazenar eletricidade. Ele se sente estressado de vez em quando se não conseguir descarregar completamente sua eletricidade. É o mais popular de toda a franquia Pokémon!",
    "Pichu",
    "Raichu (Pedra do Trovão)"
)

Raichu_pt = CriaPokemon(
    "#026",
    "Raichu",
    ["Elétrico"],
    ["Thunder Shock", "Quick Attack", "Thunder Wave", "Swift", "Spark", "Thunderbolt", "Iron Tail", "Thunder"],
    "À medida que a eletricidade se acumula dentro de seu corpo, ela se torna mais agressiva. Uma teoria é que o acúmulo de eletricidade está realmente causando estresse.",
    "Pichu / Pikachu",
    "n/a"
)

Sandshrew_pt = CriaPokemon(
    "#027",
    "Sandshrew",
    ["Terrestre"],
    ["Scatch", "Defence Curl"],
    "Sandshrew tem uma pele muito seca que é extremamente resistente. Ele pode rolar virando uma bola que repele qualquer ataque do inimigo. À noite,  ele se enterra na areia do deserto para dormir.",
    "n/a",
    "Sandslash (lvl 22)"
)

Sandslash_pt = CriaPokemon(
    "#028",
    "Sandslash",
    ["Terrestre"],
    ["Scratch", "Sand Attack", "Poison Sting", "Defence Curl", "Crush Claw", "Agility"],
    "O corpo do Sandslash é coberto por ponta duras, que são seções endurecidas de sua pele. Uma vez por ano, os picos antigos caem, para serem substituídos por novos picos que crescem por baixo dos antigos. Graças às suas garras grossas, é bom em escalar árvores. Existem muitos Sandslash's que ficam nas árvores e vão dormir.",
    "Sandshrew",
    "n/a"
)

Nidoran_Female_pt = CriaPokemon(
    "#029",
    "Nidoran F",
    ["Venenoso"],
    ["Poison Sting", "Growl"],
    "Embora este Pokémon não prefira lutar, mesmo uma gota do veneno que ele secreta de suas farpas pode ser fatal.",
    "n/a",
    "Nidorina (lvl 16) / Nidoqueen (Pedra da lua)"
)

Nidorina_pt = CriaPokemon(
    "#030",
    "Nidorina",
    ["Venenoso"],
    ["Scratch", "Tail Whip", "Poison Sting", "Growl"],
    "Quando Nidorina está com seus amigos ou familiares eles mantém suas farpas afastadas para evitar se machucar. Este Pokémon parece ficar nervoso se separado dos outros. A fêmea tem um temperamento suave. Emite gritos ultrassônicos que têm o poder de confundir os inimigos.",
    "Nidoran F",
    "Nidoqueen (Pedra da lua)"
)

Nidoqueen_pt = CriaPokemon(
    "#031",
    "Nidoqueen",
    ["Venenoso", "Terrestre"],
    ["Superpower", "Scratch", "Double Kick", "Tail Whip", "Poison Sting", "Toxic", "Helping Hand", "Earth Power", "Sludge Wave", "Growl", "Fury Swipes", "Toxic Spikes", "Bite", "Flatter", "Cruch"],
    "O corpo de Nidoqueen é envolvido em escamas extremamente duras. É hábil em enviar inimigos voando com agressões severas. Este Pokémon é mais forte quando defende seus filhotes. Se ficar excitada, as agulhas se arrepiam para fora.",
    "Nidoran F / Nidorina",
    "n/a"
)

Nidoran_Male_pt = CriaPokemon(
    "#032",
    "Nidoran M",
    ["Venenoso"],
    ["Poison Sting", "Leer"],
    "Ele examina seus arredores levantando as orelhas da grama. O chifre tóxico é para proteção.",
    "n/a",
    "Nidorino (lvl 16) / Nidoking (Pedra da lua)"
)

Nidorino_pt = CriaPokemon(
    "#033",
    "Nidorino",
    ["Venenoso"],
    ["Poison Sting", "Leer", "Peck", "Focus Energy"],
    "Seu chifre é mais duro que um diamante. Se sente uma presença hostil, todas as farpas nas costas se arrepiam de uma só vez e desafia o inimigo com toda a sua força. Ele tem uma disposição violenta e apunhala os inimigos com seu chifre, que exala veneno após o impacto.",
    "Nidoran M",
    "Nidoking (Pedra da lua"
)

Nidoking_pt = CriaPokemon(
    "#034",
    "Nidoking",
    ["Venenoso", "Terrestre"],
    ["Megahorn", "Double Kick", "Horn Attack", "Poison Sting", "Peck", "Toxic", "Focus Energy", "Helping Hand", "Poison Jab", "Earth Power", "Sludge Wave", "Leer", "Fury Attack", "Toxic Spikes", "Flatter"],
    "A cauda grossa de Nidoking possui poder enormemente destrutivo. Com um balanço, pode derrubar uma torre de transmissão de metal. Uma vez que este Pokémon se enfurece, não há como detê-lo.",
    "Nidoran M / Nidorino",
    "n/a"
)

Clefairy_pt = CriaPokemon(
    "#035",
    "Clefairy",
    ["Fada"],
    ["Tacke"],
    "Em todas as noites de lua cheia, eles saem para brincar. Quando o amanhecer chega, os cansados Clefairy's dormem aninhados um no outro em montanhas profundas e tranquilas. Voa usando as asas nas costas para coletar o luar. Este Pokémon é difícil de ser encontrado.",
    "Cleffa",
    "Clefable (Pedra da lua"
)

Clefable_pt = CriaPokemon(
    "#036",
    "Clefable",
    ["Fada"],
    ["Tackle"],
    "Clefable usa suas asas para pular levemente, como se estivesse voando. Seu passo saltitante permite que ele ande sobre a água. Nas noites tranquilas e iluminadas pelo luar, passeia pelos lagos. Sua audição é tão aguda que pode ouvir um alfinete cair a mais de 800 metros de distância. Um tímido Pokémon de fada que raramente é visto, ele corre e se esconde a todo momento em que sente a presença de pessoas.",
    "Cleffa / Clefairy",
    "n/a"
)

Vulpix_pt = CriaPokemon(
    "#037",
    "Vulpix",
    ["Fogo"],
    ["Ember"],
    "Dentro do corpo de Vulpix queima uma chama que nunca se apaga. Durante o dia, quando as temperaturas aumentam, este Pokémon libera chamas da boca para impedir que seu corpo fique muito quente. À medida que se desenvolve, sua única cauda branca ganha cor e se divide em seis. É bastante quente e fofinho.",
    "n/a",
    "Ninetales (Pedra do fogo)"
)

Ninetales_pt = CriaPokemon(
    "#038",
    "Ninetales",
    ["Fogo"],
    ["Ember"],
    "Ninetales lança uma luz sinistra de seus olhos vermelhos brilhantes para obter controle total sobre a mente de seu inimigo. Diz-se que este Pokémon vive por mil anos. Diz a lenda que Ninetales surgiu quando nove bruxos possuindo poderes sagrados se fundiram em um só. Este Pokémon é altamente inteligente - ele pode entender a fala humana.",
    "Vulpix",
    "n/a"
)

Jigglypuff_pt = CriaPokemon(
    "#039",
    "Jigglypuff",
    ["Normal", "Fada"],
    ["Pound", "Sing", "Disable", "Defense Curl", "Disarming", "Sweet Kiss", "Charm", "Copycat"],
    "Quando este Pokémon canta, nunca pára para respirar. Se estiver em uma batalha contra um oponente que não adormeça facilmente, o Jigglypuff não pode respirar, colocando em risco sua vida. Ele cativa os inimigos com seus enormes olhos redondos e os leva a dormir cantando uma melodia suave.",
    "Igglybuff",
    "Wigglytuff"
)

Wigglytuff_pt = CriaPokemon(
    "#040",
    "Wigglytuff",
    ["Normal", "Fada"],
    ["Body Slam", "Double-Edge", "Sing", "Disable", "Mimic", "Defense Curl", "Rest", "Hyper Voice", "Covet", "Gyro Ball", "Round", "Echoed Voice", "Play Rough", "Pound", "Sweet Kiss", "Disarming", "Charm", "Stockpile", "Swallow", "Spit Up", "Copycat"],
    "Wigglytuff tem olhos grandes como pires. A superfície dos olhos está sempre coberta por uma fina camada de lágrimas. Se alguma poeira entrar nos olhos do Pokémon, ela será rapidamente removida. O corpo de Wigglytuff é muito flexível. Ao inalar profundamente, este Pokémon pode se inflar aparentemente sem fim. Uma vez inflado, o WIgglytuff salta levemente como um  balão.",
    "Igglybuff / Jigglypuff",
    "n/a"
)

Zubat_pt = CriaPokemon(
    "#041",
    "Zubat",
    ["Venoso", "Voador"],
    ["Gust"],
    "O Zubat permanece silenciosamente imóvel em um local escuro durante o dia claro. Isso ocorre porque a exposição prolongada ao sol faz com que seu corpo se torne ligeiramente queimado. Não tem globos oculares, por isso não pode ver. Ele verifica seus arredores através das ondas ultrassônicas que emite da boca.",
    "n/a",
    "Golbat (lvl 22) / Crobat (Felicidade)"
)

Golbat_pt = CriaPokemon(
    "#042",
    "Golbat",
    ["Venenoso", "Voador"],
    ["Gust"],
    "Suas presas perfuram facilmente até peles grossas de animais. Adora se deliciar com o sangue das pessoas e dos Pokémons. Ele voa na escuridão e ataca por trás. Uma vez que começa a sugar sangue, ele não para até ficar cheio. Voa à noite em busca de presas.",
    "Zubat",
    "Crobat (Felicidade)"
)

Oddish_pt = CriaPokemon(
    "#043",
    "Oddish",
    ["Grama", "Venenoso"],
    ["Absorve", "Growth"],
    "Oddish procura solo fértil e rico em nutrientes para se plantar. DUrante o dia, enquanto é plantado, acredita-se que os pés deste Pokémon mudam de forma e se tornam semelhantes às raizes das árvores, além de suas folhas ficarem mais brilhantes. Se exposto ao luar, ele começa a se mover. Anda por toda parte à noite para espalhar suas sementes.",
    "n/a",
    "Gloom (lvl 21) / Vileplume (Pedra da folha) or Bellossom (Pedra do sol)"
)

Gloom_pt = CriaPokemon(
    "#044",
    "Gloom",
    ["Grama", "Venenoso"],
    ["Acid", "Absorb", "Sweet Scent", "Growth"],
    "Gloom libera uma fragância suja do pistilo de sua flor. Quando confrontado com o perigo, o fedor piora. Se este Pokémon estiver calmo e seguro, ele não liberará seu aroma fedido habitual. Ele secreta um mel pegajoso em sua boca, parecido com uma baba. Embora doce, cheira muito repulsivo para chegar muito perto.",
    "Gloom",
    "Vileplume (Pedra da folha) or Bellossom (Pedra do sol)"
)

Vileplume_pt = CriaPokemon(
    "#045",
    "Vileplume",
    ["Grama", "Venenoso"],
    ["Petal Blizzard", "Acid", "Absorb", "Mega Drain", "Poison Powder", "Stun Spore", "Sleep Powder", "Petal Dance", "Toxic", "Giga Drain", "Sweet Scent", "Aromatherapy", "Growth", "Moonblast", "Grassy Terrain", "Moonlight"],
    "Suas pétalas são as maiores do mundo. Espalha diabolicamente o pólen causador de alergias de suas pétalas. Nas estações em que produz mais pólen, o ar ao redor de um Vileplume fica amarelo com o pó enquanto caminha. O pólen é altamente tóxico e causa paralisia.",
    "Oddish / Gloom",
    "n/a"
)

Paras_pt = CriaPokemon(
    "#046",
    "Paras",
    ["Inseto", "Grama"],
    ["Absorb"],
    "Paras tem cogumelos parasitas crescendo nas costas, chamados \'tochukaso\'. Eles crescem grandes, atraindo nutriente deste Pokémon. Eles são altamente valorizados como remédio para prolongar a vida humana e dos Pokémons.",
    "n/a",
    "Parasect (lvl 24)"
)

Parasect_pt = CriaPokemon(
    "#047",
    "Parasect",
    ["Inseto", "Grama"],
    ["Absorb"],
    "O Parasect é conhecido por infestar grandes árvores em massa e drenar nutrientes do tronco e raízes inferiores. Quando uma árvore ao mesmo tempo. O cogumelo grande nas costas o controla. Muitas vezes briga por território com o Shiinotic. Seus esporos venenosos também são usados na medicina tradicional.",
    "Paras",
    "n/a"
)

Venonat_pt = CriaPokemon(
    "#048",
    "Venonat",
    ["Inseto", "Grama"],
    ["Tackle", "Disable", "Struggle Bug"],
    "Diz-se que todo seu pelo fino e rígido, que cobre todo o corpo, evoluiu para sua auto proteção. Possui olhos grandes que nunca deixam de detectar presas minúsculas. Vive nas sobras de árvores altas onde come insetos. É atraido pela luz durante a noite.",
    "n/a",
    "Venomoth (lvl 31)"
)

Venomoth_pt = CriaPokemon(
    "#049",
    "Venomoth",
    ["Inseto", "Venenoso"],
    ["Gust", "Whirlwind", "Tackle", "Supersonic", "Bug Buzz", "Quiver Dance"],
    "As asas são cobertas com escamas semelhantes a poeira. Toda vez que bate as asas, perde poeira altamente tóxica. As escamas que cobrem suas asas são codificadas por cores para indicar os tipos de veneno que ela possui. É um Pokémon que só se torna ativo à noite. Suas presas favoritas são pequenos insetos que se reúnem em torno das luzes da rua, atraídos pela luz na escuridão.",
    "Venonat",
    "n/a"
)

Diglett_pt = CriaPokemon(
    "#050",
    "Diglett",
    ["Terrestre"],
    ["Scratch", "Sand Attack"],
    "Digletts são criados na maioria das fazendas. O motivo é simples: onde quer que esse Pokémon se enterre, o solo fica perfeitamente cultivado para qualquer plantação. Este solo é ideal para o cultivo de vegetais deliciosos. Viaja através de túneis que escava no subsolo. Odeia a luz do solo e só sai depois que o sol se põe.",
    "n/a",
    "Dugtrio (lvl 26)"
)

Dugtrio_pt = CriaPokemon(
    "#051",
    "Dugtrio",
    ["Terrestre"],
    ["Sand Tomb", "Scratch", "Sand Attack", "Growl", "Tri Attack", "Astonish", "Night Slash"],
    "Dugtrios são na verdade trigêmeos que emergiram de um corpo. Como resultado, cada trigêmio pensa exatamente como os outros dois trigêmeos. Eles trabalham cooperativamente para escavar sem parar. Extremamente poderosos, eles podem cavar até o solo mais difícil a uma profundidade de mais de 100 quilômetros.",
    "Diglett",
    "n/a"
)

Meowth_pt = CriaPokemon(
    "#052",
    "Meowth",
    ["Normal"],
    ["Growl", "Fake Out"],
    "Meowth retira suas garras afiadas em suas patas para esgueirar-se lentamente sem dar passos incriminadores. Por alguma razão, este Pokémon adora moedas brilhantes que brilham com luz. Ele adora moedas, então, se você der uma, poderá fazer amizade com Meowth facilmente. Mas é incostante, então você não pode contar com essa amizade duradoura.",
    "n/a",
    "Persian (lvl 28)"
)

Persian_pt = CriaPokemon(
    "#053",
    "Persian",
    ["Normal"],
    ["Power Gem", "Scratch", "Growl", "Fake Out", "Feint", "Switcheroo"],
    "Persian tem seis bigodes ousados que lhe conferem uma aparência de resistência. Os bigodes percebem os movimentos do ar para determinar o que há nas proximidades do Pokémon. Torna-se dócil se agarrado pelos bigodes. Tem um temperamento violento. Ele atacará qualquer coisa que olhe nos olhos. Suas garras afiadas causam feridas profundas.",
    "Meowth",
    "n/a"
)

Psyduck_pt = CriaPokemon(
    "#054",
    "Psyduck",
    ["Água"],
    ["Bubble"],
    "Psyduck usa um poder misterioso. Quando faz isso, este Pokémon gera ondas cerebrais que supostamente são vistas apenas em pessoas que dormem. Essa descoberta gerou polêmica entre os estudiosos. Oprimido por habilidades enigmáticas, sofre uma dor de cabeça constante.",
    "n/a",
    "Golduck (lvl 33)"
)

Golduck_pt = CriaPokemon(
    "#055",
    "Golduck",
    ["Água"],
    ["Bubble"],
    "Golduck é o nadador mais rapido entre todos os Pokémons. Nada sem esforço, mesmo em um mar agitado e tempestuoso. Às vezes, resgata pessoas de navios naufragados que se debatem em alto mar. É um excelente Pokémon que salva vidas de pessoas e outros Pokémons que estão em perigo no mar.",
    "Psyduck",
    "n/a"
)

Mankey_pt = CriaPokemon(
    "#056",
    "Mankey",
    ["Lutador"],
    ["Scratch", "Leer", "Low Kick", "Focus Energy", "Covet"],
    "Quando Mankey começa a tremer e sua respiração nasal fica áspera, é um sinal claro de que está ficando com raiva. No entanto, como entra em uma fúria iminente quase instantaneamente, é impossível alguém fugir de sua ira. É extremamente mal-humorado. Grupos deles atacarão qualquer alvo acessível sem motivo.",
    "n/a",
    "Primeape (lvl 28)"
)

Primeape_pt = CriaPokemon(
    "#057",
    "Primeape",
    ["Lutador"],
    ["Scratch", "Leer", "Low Kick", "Focus Energy", "Covet", "Fling", "Final Gambit"],
    "Quando Primeape fica furioso, sua circulação sanguínea é aumentada. Por sua vez, seus músculos são fortalecidos. No entanto, também se torna muito menos inteligente ao mesmo tempo. Os vasos sanguíneos no cérebro são mais resistentes que os de outros Pokémons, portanto, ele pode permanecer saudável, apesar da constante fúria.",
    "Mankey",
    "n/a"
)

Growlithe_pt = CriaPokemon(
    "#058",
    "Growlithe",
    ["Fogo"],
    ["Leer", "Ember"],
    "Growlithe tem um excelente olfato, Uma vez que cheira qualquer coisa, este Pokémon não esquece o perfume, não importa o quê. Ele usa seu sentido olfativo avançado para determinar as emoções de outros seres vivos. Parece bonito, mas quando você se aproxima do Growlithe de outro treinador, ele latirá para você e o morde.",
    "n/a",
    "Arcanine (Pedra do fogo)"
)

Arcanine_pt = CriaPokemon(
    "#059",
    "Arcanine",
    ["Fogo"],
    ["Extreme Speed", "Take Down", "Leer", "Bite", "Roar", "Ember", "Flamethrower", "Flame Wheel", "Extreme Speed", "Helping Hand", "Fire Fang", "Retaliate", "Play Rough", "Burn Up", "Agility", "Crunch", "Reversal", "Flare Blitz", "Howl"],
    "Arcanine é conhecido por sua alta velocidade. Diz-se que é capaz de percorrer mais de 10.000 quilômetros em um único dia e noite. O fogo que arde violentamente dentro do corpo deste Pokémon é sua fonte de energia. Sua casca magnífica transmite uma sensação de majestade. Quem o ouve não pode deixar de rastejar diante dele.",
    "Growlithe",
    "n/a"
)

Poliwag_pt = CriaPokemon(
    "#060",
    "Poliwag",
    ["Água"],
    ["Water", "Hypnosis"],
    "Poliwag tem uma pele muito fina. É possível ver as entranhas em espiral do Pokémon através da pele. Ainda não é muito bom para caminhar. Seus treinadores devem treinar esse Pokémon para andar todos os dias. A direção do redemoinho em seus estômagos difere dependendo de onde eles moram. Os aficionados da Poliwag podem diferenciá-los rapidamente.",
    "n/a",
    "Poliwhirl (lvl 25) / Poliwrath (Pedra da Água) or Politoed (Negociação segurando a Pedra do rei)"
)

Poliwhirl_pt = CriaPokemon(
    "#061",
    "Poliwhirl",
    ["Água"],
    ["Water Gun", "Hypnosis", "Mud Shot", "Pound"],
    "A superfície do corpo de Poliwhirl está sempre molhada e escorregadia com um fluido viscoso. Por causa dessa cobertura escorregadia, ele pode facilmente escorregar e deslizar para fora das garras de qualquer inimigo em batalha. Ele marcha sobre a terra em busca de Pokémons insetos para comer. Em seguida, leva-os para debaixo d'água para que eles possam comer onde é seguro.",
    "Poliwag",
    "Poliwrath (Pedra da água) or Politoed (Negociação segurando a Pedra do rei)"
)

Poliwrath_pt = CriaPokemon(
    "#062",
    "Poliwrath",
    ["Água"],
    ["Submission", "Body Slam", "Double-Edge", "Water Gun", "Bubble Gun", "Hypnosis", "Mind Reader", "Dynamic Punch", "Rain Dance", "Circle Throw", "Pound\n", "Earth Power", "Hydro Pump", "Belly Drum", "Mud Shot"],
    "Os músculos fortes e desenvolvidos do Poliwrath nunca se cansam, por mais que exercite. É tão incansavelmente forte que este Pokémon pode nadar de um lado para o outro sem esforço. Poliwrath na região de Alola são nadadores fortes que usam o peito. Muitas crianças aprendem a nadar imitando Poliwrath.",
    "Poliwag / Poliwhirl",
    "n/a"
)

Abra_pt = CriaPokemon(
    "#063",
    "Abra",
    ["Psíquico"],
    ["Teleport"],
    "Abra precisa dormir dezoito horas por dia. Caso contrário, este Pokémon perde sua capacidade de usar poderes telecinéticos. Se for atacado, Abra escapa usando Teleport enquanto ele ainda está dormindo. Se decide se teletransportar aleatoriamente, evoca a ilusão de que criou cópias de si mesmo.",
    "n/a",
    "Kadabra (lvl 16) / Alakazam (Negociação)"
)

Kadabra_pt = CriaPokemon(
    "#064",
    "Kadabra",
    ["Psíquico"],
    ["Confusion", "Teleport"],
    "Kadabra tem uma colher de prata na mão. A colher é usada para amplificar as ondas alfa em seu cérebro. Sem a colher; diz-se que o Pokémon está limitado à metade da quantidade usual de seus poderes telecinéticos. Existe uma teoria de que este Pokémon era um garoto que não conseguia controlar seus poderes psíquicos e acabou se transforamente nesse Pokémon.",
    "Abra",
    "Alakazam (Negociação)"
)

Alakazam_pt = CriaPokemon(
    "#065",
    "Alakazam",
    ["Psíquico"],
    ["Teleport"],
    "O cérebro de Alakazam cresce continuamente multiplicando infinitamente as células cerebrais. Este cérebro incrível dá a este Pokémon um QI surpreendentemente alto de 5.000. Ele tem uma memória completa de tudo o que ocorreu no mundo. Diz-se que as colheres apertadas em suas mãos foram criadas por seus poderes psíquicos.",
    "Abra / Kadabra",
    "n/a"
)

Machop_pt = CriaPokemon(
    "#066",
    "Machop",
    ["Lutador"],
    ["Tackle"],
    "Os músculos de Machop são especiais, eles nunca ficam doloridos, por mais que sejam usados em exercícios. Este Pokémon tem poder suficiente para arremeçar uma centena de humanos adultos. É um Pokémon fitness e adora malhar. À medida que olha paa os músculos, que continuam a inchar dia após dia, torna-se cada vez mais dedicado ao seu treinamento.",
    "n/a",
    "Machoke (lvl 28) / Machamp (Negociação)"
)

Machoke_pt = CriaPokemon(
    "#067",
    "Machoke",
    ["Lutador"],
    ["Tacke"],
    "O Machoke realiza musculação todos os dias, ao mesmo tempo em que ajuda pessoas com trabalho duro, é exigente fisicamente. Nos dias de folga, esse Pokémon vai para os campos e montanhas para se exercitar e treinar. Os músculos completamente tonificados de Machoke possuem a mesma dureza que a do aço.",
    "Machop",
    "Machamp (Negociação)"
)

Machamp_pt = CriaPokemon(
    "#068",
    "Machamp",
    ["Lutador"],
    ["Tackle"],
    "Machamp tem o poder de lançar qualquer coisa de lado. No entanto, tentar fazer qualquer trabalho que exija cuidado e destreza faz com que seus braços se enrosquem. Este Pokémon tende a entrar em ação antes de pensar. Se ele agarra o inimigo com seus quatro braços, a batalha termina. O infeliz inimigo é jogado para longe no horizonte.",
    "Machop / Machoke",
    "n/a"
)

Bellsprout_pt = CriaPokemon(
    "#069",
    "Bellsprout",
    ["Grama", "Venenoso"],
    ["Vine Whip"],
    "O corpo fino e flexível do Bellsprout permite que ele se curve e balance para evitar qualquer ataque, por mais forte que seja. Da sua boca, este Pokémon cospe um fluido corrosivo que derrete até ferro. Prefere ambientes quentes e úmidos. É rápido em capturar presas com suas videiras.",
    "n/a",
    "Weepinbell (lvl 21) / Victreebel (Pedra da folha)"
)

Weepinbell_pt = CriaPokemon(
    "#070",
    "Weepinbell",
    ["Grama", "Venenoso"],
    ["Vine Whip", "Wrap", "Growth"],
    "Weepinbell tem um gancho grande na extremidade traseira. À noite, o Pokémon se conecta a um galho de árvore e vai dormir. Se ele se move durante o sono, pode acordar e se encontrar no chão. Quando está com fome, engole qualquer coisa que se mexa. Sua presa infeliz é dissolvida por ácidos fortes.",
    "Bellsprout",
    "Victreebel (Pedra da folha)"
)

Victreebel_pt = CriaPokemon(
    "#071",
    "Victreebel",
    ["Grama", "Venenoso"],
    ["Leaf Tornado", "Vine Whip", "Wrap", "Acid", "Razor Leaf", "Poison Powder", "Stun Spore", "Sleep Powder", "Sweet Scent", "Stockpile", "Spit Up", "Swallow", "Knock Off", "Gastro Acid", "Poison Jab", "Growth", "Slam", "Leaf Storm", "Leaf Blade"],
    "Victreebel tem uma longa videira que se estende de sua cabeça. Esta videira é ondulada e sacudida como se fosse um animal para atrair presas. Quando uma presa desavisada se aproxima, esse Pokémon o engole inteiro. Atrai as presas com o doce aroma do mel. Engolida inteira, a presa é dissolvida em um dia, ossos e tudo.",
    "Bellsprout / Weepinbell",
    "n/a"
)

Tentacool_pt = CriaPokemon(
    "#072",
    "Tentacool",
    ["Água", "Venenoso"],
    ["Poison Sting"],
    "O corpo do Tentacool é basicamente composto de água. Se for removido do mar, seca como pergaminho. Se este Pokémon ficar desidratado, coloque-o novamente no mar. Absorve a luz do sol e a refrata usando água dentro de seu corpo para convertê-lo em energia do feixe. Este Pokémon lança raios do pequeno órgão redondo acima dos olhos.",
    "n/a",
    "Tentacruel (lvl 30)"
)

Tentacruel_pt = CriaPokemon(
    "#073",
    "Tentacruel",
    ["Água", "Venenoso"],
    ["Poison Sting"],
    "Tentacruel tem grandes esferas vermelhas em sua cabeça. Os orbes brilham antes de atacar a vizinhança com uma forte explosão ultrassônica. A explosão deste Pokémon cria ondas violentas ao seu redor. Possui tentáculos que podem ser livremente alongados e encurtados à sua vontade. Ele prende a presa com seus tentáculos e a enfraquece, dosando-a com uma toxina dura. Pode pegar até 80 presas ao mesmo tempo.",
    "Tentacool",
    "n/a"
)

Geodude_pt = CriaPokemon(
    "#074",
    "Geodude",
    ["Pedra", "Terrestre"],
    ["Rollout"],
    "Quanto mais um Geodude vive, mais suas bordas ficam lascadas e desgastadas, tornando-a mais arredondada em sua aparência. No entanto, o coração deste Pokémon permanecerá duro e áspero para sempre. Geralmente é encontrado perto de trilhas nas montanhas e afins. Se você pisar em um por acidente, ele ficará com bastante raiva.",
    "n/a",
    "Graveler (lvl 25) / Golem (Negociação)"
)

Graveler_pt = CriaPokemon(
    "#075",
    "Graveler",
    ["Pedra", "Terrestre"],
    ["Rollout"],
    "Rochas são a comida favorita de Graveler. Este Pokémon escalará uma montanha da base até o cume, banquetando-se com pedras o tempo todo. Ao atingir o pico, ele volta ao fundo. Rola descidas para se mover. Ele rola sobre qualquer obstáculo sem diminuir a velocidade ou mudar de direção.",
    "Geodude",
    "Golem (Negociação)"
)

Golem_pt = CriaPokemon(
    "#076",
    "Golem",
    ["Pedra", "Terrestre"],
    ["Rollout"],
    "Golem vive nas montanhas. Se houver um grande terremoto, esses Pokémons virão rolando das montanhas em massa até o sopé abaixo. Mesmo a dinamite não pode prejudicar seu corpo duro e parecido com uma rocha. Ele se esconde apenas uma vez por ano. Quando Golem envelhece, ele para de derramar suas conchas. Aqueles que viveram muito, muito tempo, têm conchas verdes de musgo.",
    "Geodude / Graveler",
    "n/a"
)

Ponyta_pt = CriaPokemon(
    "#077",
    "Ponyta",
    ["Fogo"],
    ["Tackle"],
    "Ponyta é muito fraco ao nascer, mal conseguindo se levantar. Este Pokémon se torna mais forte tropeçando e caindo para acompanhar seu pai. É capaz de dar saltos incrivelmente altos. Seus cascos e pernas resistentes absorvem o impacto de um pouso forçado.",
    "n/a",
    "Rapidash (lvl 40)"
)

Rapidash_pt = CriaPokemon(
    "#078",
    "Rapidash",
    ["Fogo"],
    ["Tackle"],
    "Rapidash geralmente pode ser visto casualmente galopando nos campos e planíces. No entanto, quando esse Pokémon fica sério, suas crinas ardentes brilham e brilham à medida que galopam até 240 km/h. Adora correr. Se vir algo mais rápido que ele, perseguirá em alta velocidade.",
    "Ponyta",
    "n/a"
)

Slowpoke_pt = CriaPokemon(
    "#079",
    "Slowpoke",
    ["Água", "Psíquico"],
    ["Tackle", "Curse"],
    "Slowpoke usa sua cauda para capturar presas mergulhando-a na água ao lado de um rio. No entanto, esse Pokémon geralmente esquece o que está fazendo e muitas vezes passa dias inteiros apenas vagando à beira da água. Sua cauda longa frequentemente se rompe. No entanto, ele realmente não sente dor e a cauda volta a crescer; então Slowpoke não é particularmente incomodado.",
    "n/a",
    "Slowbro (lvl 37) or Slowking (Negociação segurando a Pedra do rei)"
)

Slowbro_pt = CriaPokemon(
    "#080",
    "Slowbro",
    ["Água", "Psíquico"],
    ["Tackle", "Growl", "Water Gun", "Withdraw", "Curse"],
    "A cauda de Slowbro tem um Shellder firmemente preso com uma mordida. Como resultado, a cauda não pode mais ser usada para pescar. Isso faz com que Slowbro nade de má vontade e pegue presas. Ele se abre enquanto olha para o mar. Com o veneno de Shellder fluindo através de seu corpo, ele se torna ainda mais especial.",
    "Slowpoke",
    "n/a"
)

Magnemite_pt = CriaPokemon(
    "#081",
    "Magnemite",
    ["Elétrico", "Metal"],
    ["Thunder Shock"],
    "Magnemite se liga às linhas de energia para se alimentar de eletricidade. Se sua casa tiver uma queda de energia, verifique seus disjuntores. Você pode encontrar um grande número desse Pokémon agarrado à caixa de disjuntores. Flutua no ar emitindo ondas eletromagnéticas das unidades em seus lados. Essas ondas bloqueiam a gravidade. Este Pokémon se torna incapaz de fluturar se seu suprimento elétrico interno estiver esgotado.",
    "n/a",
    "Magneton (lvl 30) / Magnezone (Evoluir em lugar elétrico)"
)

Magneton_pt = CriaPokemon(
    "#082",
    "Magneton",
    ["Elétrico", "Metal"],
    ["Thunder Shock"],
    "Magneton emite uma força magnética poderosa que é fatal para dispositivos mecânicos. Como resultado, grandes cidades soamsirenes para alertar os cidadãos sobre surtos em larga escala deste Pokémon. Na verdade, essa evolução são três Magnemites ligados um ao outro por magnetismo. Um grupo pode desencadear uma tempestade magnética.",
    "Magneton",
    "Magnezone (Evoluir em lugar elétrico)"
)

Farfetchd_pt = CriaPokemon(
    "#083",
    "Farfetch'd",
    ["Normal", "Voador"],
    ["Sand Attack", "Peck"],
    "Eles vivem onde as plantas crescem. Farfetch'd raramente é visto, então acredita-se que seus números estejam entrando em extinção. Não pode viver sem o nabo de alho-poró que segura. É por isso que defende o caule dos atacantes com sua vida.",
    "n/a",
    "n/a"
)

Doduo_pt = CriaPokemon(
    "#084",
    "Doduo",
    ["Normal", "Voador"],
    ["Growl", "Peck"],
    "As duas cabeças de Doduo nunca dormem ao mesmo tempo. Suas duas cabeças se revezam no sono, para que uma sempre possa vigiar os inimigos enquanto a outra dorme. Suas asas curtas dificultam o voo. Em vez disso, este Pokémon corre em alta velocidade com suas pernas desenvolvidas.",
    "n/a",
    "Dodrio (lvl 31)"
)

Dodrio_pt = CriaPokemon(
    "#085",
    "Dodrio",
    ["Normal", "Voador"],
    ["Tri Attack", "Growl", "Peck", "Quick Attack"],
    "Cuidado se as três cabeças de Dodrio estiverem olhando em três direções separadas. É um sinal claro de que está em guarda. Não chegue perto deste Pokémon se ele estiver cauteloso, ele pode decidir dar um selinho em você. Aparentemente, as cabeças não são as únicas partes do corpo que Dodrio possui três. Também possui três conjuntos de corações e pulmões, sendo capaz de percorrer longas distâncias sem descanso.",
    "Doduo",
    "n/a"
)

Seel_pt = CriaPokemon(
    "#086",
    "Seel",
    ["Água"],
    ["Headbutt"],
    "Seel caça presas no mar gelado sob as camadas de gelo. Quando precisa respirar, faz um buraco no gelo com a seção acentuadamente saliente da cabeça. Graças à sua gordura espessa, os mares frios não o incomodam de forma alguma, mas se cansam facilmente em águas mornas. Adora condições de frio congelante. Aprecia nadar em um clima frio de cerca de -14 graus ºF.",
    "n/a",
    "Dewgong (lvl 34)"
)

Dewgong_pt = CriaPokemon(
    "#087",
    "Dewgong",
    ["Água", "Gelo"],
    ["Sheer Cold", "Headbutt", "Growl", "Water Gun", "Bubble Beam", "Icy Wind"],
    "Dewgong adora adormecer no gelo amargamente frio. A visão deste Pokémon dormindo em uma geleira foi erroneamente considerada uma sereia por um marinheiro há muito tempo. Adora tomar banhos de sol na praia após as refeições. O aumento da temperatura corporal ajuda na digestão. Todo o seu corpo é branco como a neve. É um Pokémon imaculado pelo frio intenso, por isso é apaixonado por águas geladas.",
    "Seel",
    "n/a"
)

Grimer_pt = CriaPokemon(
    "#088",
    "Grimer",
    ["Venenoso"],
    ["Pound", "Poison Gas"],
    "O corpo lamacento e emborrachado de Grimer pode ser forçado através de qualquer abertura, por menor que seja. Este Pokémon entra em canos de esgoto para beber água suja. Feito de lodo congelado. Cheira muito podre ao toca-lo. Mesmo as ervas daninhas não crescerão em seu caminho pelo odor forte.",
    "n/a",
    "Muk (lvl 38)"
)

Muk_pt = CriaPokemon(
    "#089",
    "Muk",
    ["Venenoso"],
    ["Venom Drench", "Pound", "Harden", "Poison Gas", "Mud-Slap"],
    "Do corpo de Muk escoa um fluido imundo que emite um fedor horrível e dobrador de nariz. Apenas uma gota do fluido corporal deste Pokémon pode tornar uma pscina estagnada e rançosa com seu insuportável fedor. A comida favorita deste Pokémon é algo repugnantemente e imundo. Nas cidades sujas onde as pessoas pensam que não jogam lixo nas ruas, Muk certamente se reunirá.",
    "Grimer",
    "n/a"
)

Shellder_pt = CriaPokemon(
    "#090",
    "Shellder",
    ["Água"],
    ["Tackle", "Water Gun"],
    "A noite, esse Pokémon usa sua língua larga para cavar um buraco na areia do fundo do mar e depois dormir nela. Enquanto dorme, Shellder fecha sua concha, mas deixa a língua para fora. A dureza de sua concha supera a dureza de um diamante! Nos tempos passados, as pessoas usavam as conchas para fazer escudos.",
    "n/a",
    "Cloyster (Pedra da água)"
)

Cloyster_pt = CriaPokemon(
    "#091",
    "Cloyster",
    ["Água", "Gelo"],
    ["Icicle Spear", "Supersonic", "Water Gun", "Hydro Pump", "Ice Beam", "Aurora Beam", "Withdraw", "Protect", "Spikes", "Whirlpool", "Iron Defense", "Toxic Spikes", "Sheel Smash", "Tackle", "Leer", "Icicle Crash", "Razor Shell", "Ice Shard"],
    "Cloyster é capaz de nadar no mar. Isso é feito engolindo água e depois jateando em direção à parte traseira. Este Pokémon dispara espinhos de sua concha usando o mesmo sistema. Sua casca dura não pode ser quebrada, nem mesmo por uma bomba. O conteúdo do shell permanece desconhecido.",
    "Shellder",
    "n/a"
)

Gastly_pt = CriaPokemon(
    "#092",
    "Gastly",
    ["Fantasma", "Venenoso"],
    ["Astonish"],
    "Gastly é amplamente composto de matéria gasosa. Quando exposto a um vento forte, o corpo gasoso diminui rapidamente. Grupos deste Pokémon agrupam-se sob os beirais das casas para escapar da devastação do vento.",
    "n/a",
    "Hunter (lvl 25) / Gengar (Negociação)"
)

Haunter_pt = CriaPokemon(
    "#093",
    "Haunter",
    ["Fantasma", "Venenoso"],
    ["Astonish"],
    "Haunter é um Pokémon perigoso. Se um acena para você enquanto flutua na escuridão, você nunca deve se aproximar dele. Este Pokémon tentará lamber vocẽ com a língua e roubar sua vida. É perigoso sair sozinho nas noites em que você está se sentindo triste. Haunter irá te pegar e você não poderá voltar para casa. Tem medo de luz e deleita-se com a escuridão. Pode estar à beira da extinção em cidades que ficam fortemente iluminadas à noite.",
    "Gastly",
    "Gengar (Negociação)"
)

Gengar_pt = CriaPokemon(
    "#094",
    "Gengar",
    ["Fantasma", "Venenoso"],
    ["Astonish"],
    "Às vezes, em uma noite escura, sua sombra lançada por uma luz da rua repentina e surpreendentemente o ultrapassa. Na verdade, é um Gengar passando por você, fingindo ser sua sombra. Se você se sentir atacado por um calafrio repentino, é evidência de um Gengar se aproximando onde não há escapatória. Aparentemente, deseja um companheiro de viagem. Como já foi humano, tenta criar um vínculo tirando a vida de outros humanos.",
    "Gastly / Haunter",
    "n/a"
)

Onix_pt = CriaPokemon(
    "#095",
    "Onix",
    ["Pedra", "Terrestre"],
    ["Rollout"],
    "Onix tem um ímã em seu cérebro. Ele atua como uma bússola para que este Pokémon não perca a direção enquanto estiver em tunelamento. À medida que envelhece, seu corpo se torna cada vez mais redondo e suave. Ao cavar o solo, absorve muitos objetos duros. É isso que torna seu corpo tão sólido. Ele perfura rapidamente o solo a 80 km/h, contorcendo e girando todo seu corpo robusto e maciço.",
    "n/a",
    "Steelix (Negociação segurando Metal coat)"
)

Drowzee_pt = CriaPokemon(
    "#096",
    "Drowzee",
    ["Psíquico"],
    ["Pound", "Hypnosis"],
    "Se seu nariz coçar enquanto você dorme, é um sinal claro de que um desses Pokémons está em cima de seu travesseiro e tentará comer seu sonho pelas narinas. Um Pokémon que se nutre comendo sonhos alheios, acredita-se que ele compartilha ancestralidade comum com os Pokémons Munna e Musharna.",
    "n/a",
    "Hypno (lvl 26)"
)

Hypno_pt = CriaPokemon(
    "#097",
    "Hypno",
    ["Psíquico"],
    ["Pound", "Disable", "Confusion", "Hypnosis", "Future Sight", "Switcheroo", "Nasty Plot"],
    "Hypno segura um pêndulo na mão. O movimento de arco e o brilho do pêndulo embalam o inimigo em um profundo estado de hipnose. Enquanto este Pokémon procura presas, ele pole o pêndulo. Embora seja um Pokémon extremamente perigoso, as pessoas que precisam de um bom sono profundo o chamam de seu salvador. Existem alguns Hypnos que ajudam médicos com pacientes que não conseguem dormir à noite em hospitais.",
    "Dowzee",
    "n/a"
)

Krabby_pt = CriaPokemon(
    "#098",
    "Krabby",
    ["Água"],
    ["Leer", "Water Gun"],
    "Krabby vive nas praias, escavados dentro de buracos cavados na areia. Em praias arenosas com pouco alimento, esses Pokémons podem ser vistos brigando entre si por território. Suas pinças são excelentes armas. Às vezes eles se separam durante a batalha, mas crescem rapidamente. Se sentir o perigo se aproximando, ele se esconde com bolhas da boca para parecerem maiores e assustarem inimigos.",
    "n/a",
    "Kingler (lvl 28)"
)

Kingler_pt = CriaPokemon(
    "#099",
    "Kingler",
    ["Água"],
    ["Leer", "Water Gun", "Harden", "Metal Claw", "Wide Guard", "Hammer Arm"],
    "Kingler tem uma garra forte e enorme. Ele agita essa enorme garra no ar para se comunicar com os outros. No entanto, como a garra é muito pesada, o Pokémon se cansa rapidamente. Uma garra cresceu maciçamente e é tão dura quanto o aço. Tem força de 10.000 cavalos de potência. No entanto, é muito pesado.",
    "Krabby",
    "n/a"
)

Voltorb_pt = CriaPokemon(
    "#100",
    "Voltorb",
    ["Elétrico"],
    ["Tackle", "Charge"],
    "Voltorb foi avistado pela primeira vez em uma empresa que fabrica Pokebolas. A ligação entre esse avistamento e o fato desse Pokémon ser muito semelhante a uma Pokebola permanece um mistério. Voltorb é extremamente sensível, explode ao menor choque. Há rumores de que ele foi criado quando uma Pokebola foi exposta a um poderoso pulso de energia.",
    "n/a",
    "Electrode (lvl 30)"
)

Electrode_pt = CriaPokemon(
    "#101",
    "Electrode",
    ["Elétrico"],
    ["Tackle", "Charge", "Eerie Impulse", "Magnetic Flux"],
    "O Electrode consome eletricidade na atmosfera. Nos dias em que um raio atinge, você pode ver este Pokémon explodindo em todo o lugar por comer muita eletricidade. Uma das características do Electrode é sua atração pela eletricidade. É um Pokémon problemático que se reúne principalmente em usinas de energia elétrica para se alimentar de eletricidade que acaba de ser gerada.",
    "Voltorb",
    "n/a"
)

Exeggcute_pt = CriaPokemon(
    "#102",
    "Exeggcute",
    ["Grama", "Psíquico"],
    ["Hypnosis", "Absorb"],
    "Seus seis ovos usam telepatia para se comunicar entre si. Acredita-se que carrega genes de plantas e os genes de outras espécies. Embora sejam do mesmo tamanho que outros Exeggcutes, os produzidos em Alola são bastante pesados. Suas conchas estão cheias.",
    "n/a",
    "Exeggutor (Pedra da folha)"
)

Exeggutor_pt = CriaPokemon(
    "#103",
    "Exeggutor",
    ["Grama", "Psíquico"],
    ["Stomp", "Mega Drain", "Solar Beam", "Confusion", "Hypnosis", "Reflect", "Giga Drain", "Synthesis", "Bullet Seed", "Worry Seed", "Seed Bomb", "Leaf Storm", "Wood Hammer", "Psyshock", "Extrasensory, Uproar", "Absorb", "Leech Seed"],
    "O exeggutor veio originalmente dos trópicos. Suas cabeças ficam cada vez maiores com a exposição à forte luz do sol. Diz-se que quando as cabeças caem, elas se agrupam no chão para formar um Execcute. Seus gritos são muito barulhentos. Isso ocorre porque cada uma de suas cabeças tem sua própria vontade e pensam diferente. Eles usam a telepatia para discutir seus planos antes de chegar a uma decisão conjunta.",
    "Exeggcute",
    "n/a"
)

Cubone_pt = CriaPokemon(
    "#104",
    "Cubone",
    ["Terrestre"],
    ["Growl", "Mud-Slap"],
    "O crânio que usa na cabeça é o de sua mãe morta. Segundo alguns, ele evoluirá quando chegar a um acordo com a dor de sua morte. Ele sempre anseia pela mãe que nunca mais o verá. Vendo uma semelhança de sua mãe na lua cheia, ele chora. As manchas no crânio que usa são de suas lágrimas.",
    "n/a",
    "Marowak (lvl 28)"
)

Marowak_pt = CriaPokemon(
    "#105",
    "Marowak",
    ["Terrestre"],
    ["Tail Whip", "Growl", "Mud-Slap", "False Swipe"],
    "Marowak é a forma evoluída de um Cubone que superou sua tristeza pela perda de sua mãe e se tornou um Pokémon durão. O espírito temperado e endurecido deste Pokémon não é facilmente quebrado. Originalmente, era fraco e tímido. Após a evolução, seu temperamento torna-se violento e ele passa a usar os ossos como armas.",
    "Cubone",
    "n/a"
)

Hitmonlee_pt = CriaPokemon(
    "#106",
    "Hitmonlee",
    ["Lutador"],
    ["Brick Break", "Focus Energy", "Helping Hand", "Feint", "Low Sweep", "Tackle", "Fake Out"],
    "As pernas de Hitmonlee se contraem e se esticam livremente. Usando essas pernas de mola, ele se curva sobre os inimigos com chutes devastadores. Após a batalha, esfrega as pernas e relaxa os músculos para superar a fadiga. Este Pokémon tem um incrível senso de equilíbrio. Pode chutar em sucessão a partir de qualquer posição.",
    "Tyrogue",
    "n/a"
)

Hitmonchan_pt = CriaPokemon(
    "#107",
    "Hitmonchan",
    ["Lutador"],
    ["Drain Punch", "Helping Hand", "Feint", "Drain Punch", "Vaccum Wave", "Bullet Punch", "Focus Energy", "Tackle", "Fake Out"],
    "Diz-se que Hitmonchan possui o espírito de um boxeador que estava trabalhando em direção a um campeonato mundial. Este Pokémon tem um espírito indomável e nunca desistirá diante das adversidades. Seus socos cortam o ar. Eles são lançados a uma velocidade tão alta que até um leve arranhão pode causar queimaduras.",
    "Tyrogue",
    "n/a"
)

Lickitung_pt = CriaPokemon(
    "#108",
    "Lickitung",
    ["Normal"],
    ["Tackle"],
    "Sempre que o Lickitung se deparar com algo novo, ele irá infalivelmente dar uma lambida. Esse Pokémon memoriza as coisas pela textura e pelo sabor. É um pouco desconcertado por coisas azedas. Ser lambido por sua lingua comprida e coberta de saliva deixa uma sensação de formigamento. Ao estender sua língua sua cauda é retraida.",
    "n/a",
    "Lickilicky (Evoluir sabendo Rollout)"
)

Koffing_pt = CriaPokemon(
    "#109",
    "Koffing",
    ["Venenoso"],
    ["Tackle", "Poison Gas"],
    "Se Koffing ficar agitado, ele aumenta a toxicidade de seus gases internos e os jorra de todo o corpo. Este Pokémon também pode inflar demais seu corpo redondo e explodir. Koffing contém substâncias tóxicas. Ele mistura as toxinas com o lixo bruto para desencadear uma reação química que resulta em um gás venenoso terrívelmente poderoso. Quanto mais alta a temperatura, mais gás é fabriado por este Pokémon.",
    "n/a",
    "Weezing (lvl 35)"
)

Weezing_pt = CriaPokemon(
    "#110",
    "Weezing",
    ["Venenoso"],
    ["Double Hit", "Tackle", "Smokescreen", "Smog", "Poison Gas", "Double Hit", "Heat Wave"],
    "Weezing adora os gases emitidos pelo lixo podre da cozinha. Este Pokémon encontrará uma casa suja e mal cuidada e fará dela seu lar. À noite, quando as pessoas da casa estão dormindo, ele vai para o lixo. Weezing encolhe e infla alternadamente seus corpos gêmeos para misturar gases tóxicos em seu interior. Quanto mais os gases são misturados, mais poderosas as toxínas se tornam. O Pokémon também se torna mais apodrecido.",
    "Koffing",
    "n/a"
)

Rhyhorn_pt = CriaPokemon(
    "#111",
    "Rhyhorn",
    ["Terrestre", "Pedra"],
    ["Tackle"],
    "Rhyhorn corre em linha reta, esmagando tudo em seu caminho. Ele não se incomoda nem mesmo se bater de cabeça em um bloco de aço. Este Pokémon pode sentir um pouco de dor com a colisão no dia seguinte, no entanto, o cérebro de Rhyhorn é muito pequeno. É tão denso que, ao correr, ele esquece o motivo pelo qual começou a funcionar. Parece que as vezes se lembra quando destrói alguma coisa.",
    "n/a",
    "Rhydon (lvl 42) / Rhyperior (Negociação segurando Protector)"
)

Rhydon_pt = CriaPokemon(
    "#112",
    "Rhydon",
    ["Terrestre", "Pedra"],
    ["Tackle"],
    "O chifre de Rhydon pode esmagar até diamantes não lapidados. Um golpe violento de sua cauda pode derrubar um edifício. A pele deste Pokémon é extremamente resistente. Mesmo os golpes de canhão diretos não deixam um arranhão. Rhydon tem um chifre que serve de broca. É usado para destruir rochas e pedregulhos. Este Pokémon ocasionalmente bate em fluxos de magma, mas a pele semelhante a uma armadura o impede de sentir o calor.",
    "Rhydon",
    "Rhyperior (Negociação segurando Protector)"
)

Chansey_pt = CriaPokemon(
    "#113",
    "Chansey",
    ["Normal"],
    ["Tackle"],
    "Chansey põe ovos nutricionalmente excelentes todos os dias. Os ovos são tão deliciosos que são devorados fácil e avidamente, mesmo por aquelas pessoas que jpa perderam o apetite. Esse Pokémon não são apenas corredores rápidos, mas também são poucos em número, portanto, qualquer pessoa que encontrar um, teve muita sorte no mundo Pokémon.",
    "Happiny",
    "Blissey (Felicidade)"
)

Tangela_pt = CriaPokemon(
    "#114",
    "Tangela",
    ["Grama"],
    ["Absorb"],
    "As vinhas de Tangela se quebram fácilmente se forem agarradas. Isso acontece sem dor, permitindo uma fuga raṕida. As vinhas perdidas são substituídas por vinhas recém-cultivadas no dia seguinte. Sua identidade é obscurecida por massas grossas vinhas azuis por cima de todo o seu corpo. Diz-se que as vinhas nunca param de crescer.",
    "n/a",
    "Tangrowth (Evoluir sabendo Poder Ancestral)"
)

Kangaskhan_pt = CriaPokemon(
    "#115",
    "Kangaskhan",
    ["Normal"],
    ["Tail Whip", "Pound"],
    "Se você encontrar um jovem Kangaskhan brincando sozinho, nunca deve perturbá-lo ou tentar pegá-lo. A mãe do bebê Pokémon com certeza está na área, e ela ficará violentamente furiosa com você. Cria seus filhotes na bolsa da barriga. Não fugirá de nenhuma luta para manter seus filhotes sempre protegidos.",
    "n/a",
    "n/a"
)

Horsea_pt = CriaPokemon(
    "#116",
    "Horsea",
    ["Água"],
    ["Leer", "Water Gun"],
    "Horsea come pequenos insetos e musgo das rochas. Se a corrente do oceano se torna mais rápida, este Pokémon se ancora enrolando sua cauda em rochas ou corais para evitar que seja levado pela água. Se Horsea perceber o perigo, ele irá borrifar reflexivamente uma densa tinta preta de sua boca e tentar escapar. Este Pokémon nada batendo habilmente a barbatana de sua costas.",
    "n/a",
    "Seadra (lvl 32) / Kingdra (Negociação segurando Dragon Scale)"
)

Seadra_pt = CriaPokemon(
    "#117",
    "Seadra",
    ["Água"],
    ["Leer", "Water Gun", "Smokescreen", "Twister"],
    "Seadra dorme depois de se contorcer entre os galhos de coral. Aqueles que tentam coletar corais são ocasionalmente picados pelas farpas venososas deste Pokémon, caso não percebam. Seadra gera redemoinhos girando todo seu are corpo. Os redemoinhos são fortes o suficiente para engolir até barcos de pesca. Este Pokémon enfraquece a presa com essas correntes, a então a engole inteira.",
    "Horsea",
    "Kingdra (Negociação segurando Dragon Scale)"
)

Goldeen_pt = CriaPokemon(
    "#118",
    "Goldeen",
    ["Água"],
    ["Tail Whip", "Peck"],
    "Goldeen é um Pokémon muito bonito com barbatanas que ondulam elegantemente na água. No entanto, não baixe a guarda em torno deste Pokémon, ele pode atingir você com força usando seu chifre. Goldeen adora nadar livremente em rios e lagoas. Se um desses Pokémons for colocado em um aquário, ele irá quebrar até o vidro mais grosso com um aríete de seu chifre e escapar.",
    "n/a",
    "Seaking (lvl 33)"
)

Seaking_pt = CriaPokemon(
    "#119",
    "Seaking",
    ["Água"],
    ["Tail Whip", "Supersonic", "Peck", "Water Pulse"],
    "No outono, os machos Seaking podem ser vistos realizando danças de corte no leito do rio para cortejar a fêmeas. Durante esta temporada, a coloração do corpo deste Pokémon fica mais bonita. Seaking é muito protetor de seus ovos. O macho e a fêmea se revezam para patrulhar o o ninho e os ovos. A guarda de ovos por esses Pokémon dura mais de um mês.",
    "Goldeen",
    "n/a"
)

Staryu_pt = CriaPokemon(
    "#120",
    "Staryu",
    ["Água"],
    ["Tackle", "Harden"],
    "A seção central de Staryu tem um órgão denominado de núcelo que brilha em vermelho vivo. Se você for a uma praia no final do verão, os núcleos brilhantes desses Pokémons parecem estrelas no céu. Staryu aparentemente se comunica com as estrelas do céu noturno piscando o núcleo vermelho no centro de seu corpo. Se partes de seu corpo forem rasgadas, este Pokémon simplesmente regenera as peças e membros que o faltam.",
    "n/a",
    "Starmie (Pedra da água)"
)

Starmie_pt = CriaPokemon(
    "#121",
    "Starmie",
    ["Água", "Psíquico"],
    ["Tackle", "Water Gun", "Hydro Pump", "Surf", "Psychic", "Recover", "Harden", "Confuse Ray", "Light Screen", "Swift", "Rapid Spin", "Brine", "Minimize", "Psybeam", "Power Gem", "Cosmic Power"],
    "A seção central de Starmie (o núcleo) brilha intensamente em sete cores. Devido à sua natureza luminosa, este Pokémon recebeu o apelido de \"a joia do mar\". Starmie nada na água girando seu corpo em forma de estrela como se fosse a hélice de um navio.",
    "Staryu",
    "n/a"
)

Mr_Mime_pt = CriaPokemon(
    "#122",
    "Mr.Mime",
    ["Psíquico", "Fada"],
    ["Confusion"],
    "O Mr. Mime é um mestre da pantomima (representação de uma história exclusivamente através de gestos, expressões faciais e movimentos de uma dança ou drama). Seus gestos e movimentos convencem os observadores de que algo invisível realmente existe. Uma vez que os observadores estão convencidos, a coisa invisível começa a existir como se fosse real. A largura de suas mãos pode não ser coincidência e muitos acreditam que suas palmas aumentaram especificamente para pantomima.",
    "Mime Jr.",
    "n/a"
)

Scyther_pt = CriaPokemon(
    "#123",
    "Scyther",
    ["Inseto", "Voador"],
    ["Quick Attack"],
    "Scyther é incrivelmente rápido. Sua velocidade incrível aumenta a eficácia das foices gêmeas em seus antebraços. As foices deste Pokémon são tão eficazes que podem cortar troncos grossos com um único golpe. Ele confunde sua presa com seus movimentos rápidos de ninja. Então, em um instante, ele os fende com suas foices.",
    "v",
    "Scizor (Negociação segurando Metal coat) / Kleavor (Black Augurite)."
)

Jynx_pt = CriaPokemon(
    "#124",
    "Jynx",
    ["Gelo", "Psíquico"],
    ["Pound", "Lick", "Powder Snow", "Sweet Kiss", "Copycat"],
    "Jynx caminha ritmicamente, balançando e balançando os quadris como se estivesse dançando. Seus movimentos são  tão atraentes que as pessoas que o veem são compelidas a balançar os quadris sem se preocupar com o que estão fazendo. Seus gritos estranhos soam como linguagem humana. Existem alguns núcleos que compõem canções para Jynx cantar.",
    "Smoochum",
    "n/a"
)

Electabuzz_pt = CriaPokemon(
    "#125",
    "Electabuzz",
    ["Elétrico"],
    ["Thunder Shock"],
    "Quando uma tempestade chega, gangues deste Pokémon competem entre si para escalar alturas que provavelmente serão atingidas por raios. Algumas cidades do mundo Pokémon usam Electabuzz no lugar dos pára-raios. Metade de todos os apagões repentinos são causados por Electabuzz se reunindo em usinas de energia elétrica e engolindo eletricidade.",
    "Elekid",
    "Electivire (Negociação segurando Electrizer)"
)

Magmar_pt = CriaPokemon(
    "#126",
    "Magmar",
    ["Fogo"],
    ["Ember"],
    "Na batalha, Magmar sopra chamas intensamente quentes por todo o corpo para intimidar seu oponente. As explosões de fogo deste Pokémon criam ondas de calor que incendiam a grama e as árvores ao redor. Quando irritado, ele jorra fogo brilhante por todo o corpo. Ele não se acalma até que seu oponente seja reduzido a cinzas.",
    "Magby",
    "Magmortar (Negociação segurando Magmarizer)"
)

Pinsir_pt = CriaPokemon(
    "#127",
    "Pinsir",
    ["Inseto"],
    ["Vice Grip", "Harden"],
    "Pinsir é incrivelmente forte. Ele pode agarrar um inimigo com o dobro de seu peso em seus chifres e levantá-lo facilmente. Os movimentos deste Pokémon tornam-se lentos em locais frios. Ele agarra sua presa com as pinças e as divide. Um golpe sólido de seus chifres é suficiente para partir uma grande árvore. Seu maior rival em Alola é o Pokémon Vikavolt.",
    "n/a",
    "n/a"
)

Tauros_pt = CriaPokemon(
    "#128",
    "Tauros",
    ["Normal"],
    ["Tackle", "Tail Whip"],
    "Este Pokémon não fica satisfeito a menos que esteja furioso o tempo todo. Se não houver oponente para Tauros lutar, ele irá atacar árvores grossas e derrubá-las para se acalmar. Historicamente, pessoas em áreas de todo o mundo montaram em Tauros, mas dizem que a prática começou em Alola. Quando está prestes a atacar, chicoteia seu próprio corpo repetidamente com suas três longas caudas. Uma vez que mira em seu inimigo, ele faz uma investida violenta.",
    "n/a",
    "n/a"
)

Magikarp_pt = CriaPokemon(
    "#129",
    "Magikarp",
    ["Água"],
    ["Splash"],
    "Magikarp é uma desculpa patética para um Pokémon que só é capaz de bater e espirrar. No entanto, é na verdade um Pokémon muito resistente que pode sobreviver em qualquer corpo d'água, não importa o quão poluído esteja. ESse comportamento levou os cientistas a fazerem pesquisas sobre ele. Embora fraco e indefeso, este Pokémon é incrivelmente fértil. Eles existem em tantas multidões que você logo se cansará de vê-los.",
    "n/a",
    "Gyrados (lvl 20)"
)

Gyarados_pt = CriaPokemon(
    "#130",
    "Gyarados",
    ["Água", "Voador"],
    ["Water Pulse", "Splash"],
    "Quando Magikarp evolui para Gyarados, suas célular cerebrais sofrem uma transformação estrutural. Diz-se que essa transformação é a culpada pela natureza violenta desse Pokémon. Depois que Gyarados começa a se alastrar, seu sangue ferozmente violento não se acalma até que tenha queimado tudo. Existem registros dos ataques deste Pokémon que duraram por um mês inteiro. Conta-se a história de uma cidade que irritou Gyarados. Antes do sol nascer no dia seguinte, as chamas consumiram totalmente a cidade, sem deixar vestígios.",
    "Magikarp",
    "n/a"
)

Lapras_pt = CriaPokemon(
    "#131",
    "Lapras",
    ["Água", "Gelo"],
    ["Growl", "Water Gun"],
    "As pessoas levaram Lapras quase à extinção. À noite diz-se que este Pokémon canta melancolicamente enquanto busca o que poucos outros de sua espécie ainda permanecem. Sua alta inteligência permite compreender a fala humana. Quando está de bom humor, canta com sua bela voz. Gosta de nadar com humanos nas costas. Na região de Alola, é um importante meio de transporte fluvial.",
    "n/a",
    "n/a"
)

Ditto_pt = CriaPokemon(
    "#132",
    "Ditto",
    ["Normal"],
    ["Transform"],
    "Ditto reorganiza sua estrutura celular para se transformar em outras formas. No entanto, se tentar se transformar em algo contando com sua memória, esse Pokémon consegue errar os detalhes. Com sua surpreendente capacidade de metamorfose, pode conviver com qualquer coisa. Ele não se dá bem com seu colega Ditto. Ditto aparentemente tem seus próprios pontos fortes e fracos quando se trata de transformações.",
    "n/a",
    "n/a"
)

Eevee_pt = CriaPokemon(
    "#133",
    "Eevee",
    ["Normal"],
    ["Tackle"],
    "Eevee tem uma composição genética instável que sofre uma mutação repentina devido ao ambiente em que vive. A radiação de várias pedras evolutivas do mundo Pokémon faz com que este Pokémon evolua em várias formas e tipos.",
    "n/a",
    "Vaporeon (Pedra da água) / Jolteon (Pedra do trovão) / Flareon (Pedra do fogo) / Espeon (Felicidade durante o dia) / Umbreon (Felicidade durante a noite) Leafeon (Evoluir perto de Moss Rock) / Glaceon (Evoluir segurando Ice Rock) / Sylveon (Afeto conhecendo a técnica do tipo fada.)" 
)

Vaporeon_pt = CriaPokemon(
    "#134",
    "Vaporeon",
    ["Água"],
    ["Bubble", "Tackle"],
    "Vaporeon sofreu uma mutação espontânea e cultivou barbatanas e brânquias que lhe permitem viver debaixo d'água. Este Pokémon tem a capacidade de controlar livremente a água. Sua composição celular é semelhante às moléculas de água. Como resultado, não pode ser visto quando derrete na água. Prefere praias bonitas.",
    "Eevee",
    "n/a"
)

Jolteon_pt = CriaPokemon(
    "#135",
    "Jolteon",
    ["Elétrico"],
    ["Thunder Shock", "Tackle"],
    "As células de Jolteon geram um baixo nível de eletricidade. Esse poder é amplificado pela eletricidade estática de sua pelagem, permitindo que o Pokémon solte raios. O pelo eriçado é feito de agulhas carregadas com eletricidade. Um Pokémon sensível que facilmente fica triste ou com raiva. Toda vez que seu humor muda, ele cobra energia.",
    "Eevee",
    "n/a"
)

Flareon_pt = CriaPokemon(
    "#136",
    "Flareon",
    ["Fogo"],
    ["Ember", "Tackle"],
    "O pelo macio de Flareon tem um objetivo funcional, liberar calor no ar para que seu corpo não fique excessivamente quente. A temperatura corporal deste Pokémon pode subir para um máximo de 1.650 graus Fahrenheit. Quando pega presas ou encontra berrys, sopra fogo nelas até que estejam bem cozidas e depois as engole.",
    "Eevee",
    "n/a"
)

Porygon_pt = CriaPokemon(
    "#137",
    "Porygon",
    ["Normal"],
    ["Tackle"],
    "Porygon é capaz de se reverter inteiramente de volta aos dados do programa e entrar no ciberespaço (espaço das comunicações por redes de computadores). Este Pokémon é protegido contra cópia, portanto não pode ser duplicado por cópia. Foi construido há 20 anos por ciencitstas que sonhavam em explorar o espaço. Seus sonhos ainda não se realizaram.",
    "n/a",
    "Porygon 2 (Negociação segurando Up-Grade) / Porygon-Z (Negociação segurando Dubious Disc)"
)

Omanyte_pt = CriaPokemon(
    "#138",
    "Omanyte",
    ["Pedra", "Água"],
    ["Bind", "Withdraw"],
    "Omanyte é um dos Pokémons antigos e já extintos que foram regenerados a partir de fósseis por pessoas. Se atacado por um inimigo, ele se retira dentro de sua casca dura. Este Pokémon usa o ar armazenado em sua concha para afundar e subir na água e nada torcendo seus 10 tentáculos de maneira inteligente.",
    "n/a",
    "Omastar (lvl 40)"
)

Omastar_pt = CriaPokemon(
    "#139",
    "Omastar",
    ["Pedra", "Água"],
    ["Crunch", "Bind", "Withdraw", "Rollout", "Sand Attack"],
    "Omastar usa seus tentáculos para capturar suas presas. Acredita-se que tenha se extínguido porque sua concha ficou muito grande e pesada, fazendo com que seus movimentos se tornassem muito lentos e pesados. Seus tentáculos são altamente desenvolvidos como se fosse mãos e pés. Assim que prende a presa, ele morde.",
    "Omanyte",
    "n/a"
)

Kabuto_pt = CriaPokemon(
    "#140",
    "Kabuto",
    ["Pedra", "Água"],
    ["Absorb", "Harden"],
    "Kabuto é um Pokémon que foi regenerado a partir de um fóssil. No entanto, em casos extremamente raros, exemplos vivos foram descobertos. O Pokémon não mudou em nada por 300 milhões de anos. Este Pokémon foi extinto em praticamente todos os lugares, exceto em algumas áreas específicas. Ele se protege com sua casca dura.",
    "n/a",
    "Kabutops (lvl 40)"
)

Kabutops_pt = CriaPokemon(
    "#141",
    "Kabutops",
    ["Pedra", "Água"],
    ["Slash", "Scratch", "Sand Attack", "Absorb", "Harden", "Feint", "Night Slash"],
    "Os Kabutops nadavam debaixo d'água para caçar suas presas nos tempos antigos. Aparentemente, o Pokémon estava evoluindo de morador de água para morar em terra, como é evidente desde o início da mudança em suas brânquias e pernas. Na água, ele enfia os membros para se tornar mais compacto, depois balança a concha para nadar mais rápido.",
    "Kabuto",
    "n/a"
)

Aerodactyl_pt = CriaPokemon(
    "#142",
    "Aerodactyl",
    ["Pedra", "Voador"],
    ["Bite", "Ancient Power"],
    "Aerodactyl é um Pokémon da era dos dinossauros. Foi regenerado a partir de material genético extraído de âmbar. Imagina-se que tenha sido o rei dos céus nos tempos antigos. Usou suas presas de serra para rasgar suas presas antes de comê-las. Voa com gritos agudos.",
    "n/a",
    "n/a"
)

Snorlax_pt = CriaPokemon(
    "#143",
    "Snorlax",
    ["Normal"],
    ["Rollout"],
    "O dia típico de Snorlax consiste em nada mais do que comer e dormir. É um Pokémon tão dócil que há crianças que usam sua barriga expansiva como um lugar para brincar. Come quase 900 quilos de comida todos os dias. Começa a cochilar enquanto come e continua a comer mesmo enquanto dorme. Até o veneno de Muk não passa de uma pitada de tempero na língua de Snorlax.",
    "Munchlax",
    "n/a"
)

Articuno_pt = CriaPokemon(
    "#144",
    "Articuno",
    ["Gelo", "Voador"],
    ["Gust", "Mist"],
    "Articuno é um Pokémon pássaro lendário que pode controlar o gelo. O bater de suas asas esfria totalmente o ar. Como resultado, diz-se que quando este Pokémon voa, a never cai. Com sua cauda longa de trás, sua forma voadora é magnífica. Congela a água que está contida no ar do inverno e faz nevar.",
    "n/a",
    "n/a"
)

Zapdos_pt = CriaPokemon(
    "#145",
    "Zapdos",
    ["Elétrico", "Voador"],
    ["Peck", "Thunder Wave"],
    "Zapdos é um Pokémon lendário de pássaros que tem a capacidade de controlar a eletricidade. Geralmente vive em nuvens de trovoada. O Pokémon ganha poder se for atingido por raios. Diz-se que este Pokémon lendário pássaro aparece quando o céu fica escuro e os raios caem.",
    "n/a",
    "n/a"
)

Moltres_pt = CriaPokemon(
    "#146",
    "Moltres",
    ["Fogo", "Voador"],
    ["Leer", "Gust"],
    "Moltres é um Pokémon pássaro lendário que tem a capacidade de controlar o fogo. Se este Pokémon for ferido, é dito que ele mergulha seu corpo no magma derretido de um vulcão para queimar e curar a sí próprio. Diz-se que este lendário Pokémon traz o início da primavera para as terras invernais que o visita. Moltres espalha brasas a cada batida de suas asas. É uma visão emocionante de se ver.",
    "n/a",
    "n/a"
)

Dratini_pt = CriaPokemon(
    "#147",
    "Dratini",
    ["Dragão"],
    ["-"],
    "Dratini muda constantemente e descama sua pele velha. Faz isso porque a energia da vida dentro de seu corpo aumenta constantemente para atingir níveis incontroláveis. Após uma luta de 10 horas, um pescador foi capaz de puxá-lo e confirmar suas existência no mundo Pokémon.",
    "n/a",
    "Dragonair (lvl 30) / Dragonite (lvl 55)"
)

Dragonair_pt = CriaPokemon(
    "#148",
    "Dragonair",
    ["Dragão"],
    ["Wrap", "Leer", "Thunder Wave", "Twister"],
    "Dragonair armazena uma enorme quantidade de energia dentro de seu corpo. Diz-se que altera as condições climáticas nas proximidades, descarregando energia dos cristais no pescoço e na cauda. Diz-se que vive em mares e lagos. Mesmo que não tenha asas, foi visto voando ocasionalmente.",
    "Dratini",
    "Dragonite (lvl 55)"
)

Dragonite_pt = CriaPokemon(
    "#149",
    "Dragonite",
    ["Dragão", "Voador"],
    ["Hurricane", "Fire Punch", "Thunder Punch", "Wing Attack", "Wrap", "Leer", "Thunder Wave", "Twister", "Roost", "Extreme Speed"],
    "Dragonite é capaz de circular o globo em apenas 16 horas. É um Pokémon de bom coração que leva navios perdidos e afundando em uma tempestade à segurança da terra. Diz-se que sua inteligência corresponde à dos humanos.",
    "Dratini / Dragonair",
    "n/a"
)

Mewtwo_pt = CriaPokemon(
    "#150",
    "Mewtwo",
    ["Psíquico"],
    ["Disable", "Confusion", "Swift", "Lases Focus", "Life Dew"],
    "Mewtwo é um Pokémon que foi criado por manipulação genética. No entanto, embora o poder científico dos humanos tenha criado o corpo desse Pokémon, eles não conseguiram dotar Mewtwo de um coração compassivo. Como suas habilidades de batalha foram elevadas ao nível máximo, ele pensa apenas em derrotar seus inimigos, independente de quem seja.",
    "n/a",
    "n/a"
)

Mew_pt = CriaPokemon(
    "#151",
    "Mew",
    ["Psíquico"],
    ["Pound", "Reflect Type"],
    "Diz-se que Mew possui a composição genética de todos os Pokémons. Ele é capaz de tornar-se invisível à vontade, por isso evita a percepção, mesmo que se aproxime das pessoas. Quando é visto detalhadamente através de um microscópio, os cabelos curtos, finos e delicados deste Pokémon mítico podem ser vistos.",
    "n/a",
    "n/a"
)