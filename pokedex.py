import author # Para conteúdo do sobre/about
import pokemons_en # Para os objetos e funções em inglês
import pokemons_ptbr # Para os objetos e funções em Português
import pokeansi # Para as arts dos pokemons

print("                                  ,'\                              ")
print("    _.----.        ____         ,'  _\   ___    ___     ____       ")
print("_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`. ")
print("\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |")
print(" \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |")
print("   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |")
print("    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |")
print("     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |")
print("      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |")
print("       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |")
print("        \_.-'       |__|    `-._ |              '-.|     '-.| |   |")
print("                                `'                            '-._|")
                                            
                                            
def menu():
    
    print("\n\n                                     Created by Maycon Douglas")

    print("\nSeja Bem vindo a sua Pokedex!")
    print("\nWelcome to your Pokedex!")

    print("\n\nDigite [Sobre] para saber mais sobre o programa.")
    print("\nType [About] to learn more about the program.")

    print("\n\nDigite [Sair] para fechar a Pokedex.")
    print("\nType [Quit] to close the Pokedex.")

    print("\n\nQual idioma você deseja?")
    print("\nWhich language do you prefer?")

    print("\n\nDigite [pt] Para Português")
    print("\nType [en] for English")


run = True
while run == True:

    menu()
    
    user_answer = input(":").strip().lower()

    # SAIR/QUIT =====v

    if user_answer == "sair":
        print("\n\nAté logo !!")
        run = False

    elif user_answer == "exit":
        print("\n\nSee you !!")
        run = False

    elif user_answer == "quit":
        print("\n\nSee you !!")
        run = False


    # INFORMAÇÕES ADICIONAIS =====v
    
    elif user_answer == "sobre":
        author.author()
        continue

    elif user_answer == "about":
        author.author()
        continue

    # PARA CÓDIGO EM PORTUGUÊS =====v

    elif user_answer == "pt":
        run_pt = "y"
        while run_pt == "y":
            print("\n\n\n(Apenas pokémons da primeira geração disponíveis no momento.)\n\nDigite números de 1 à 151; ou digite o nome do Pokémon")
            print("\nDigite \"menu\" para voltar a seleção de linguagem.")

            pokemon_desejado = input("\n\nQual pokemon você deseja procurar?\n\n").lower().strip()
            
            if pokemon_desejado == "menu":
                run_pt = "n"

            elif pokemon_desejado == "sair":
                print("\n\nAté logo !!")
                exit()

            elif pokemon_desejado == "quit":
                print("\n\nSee you !!")
                exit()

            elif pokemon_desejado == "exit":
                print("\n\nSee you !!")
                exit()

            elif pokemon_desejado == "1":
                pokeansi.bulbasaur_image()
                pokemons_ptbr.Bulbasaur_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                
            elif pokemon_desejado == "bulbasaur":
                pokeansi.bulbasaur_image()
                pokemons_ptbr.Bulbasaur_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                
            elif pokemon_desejado == "2":
                pokeansi.ivysaur_image()
                pokemons_ptbr.Ivysaur_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                
            elif pokemon_desejado == "ivysaur":
                pokeansi.ivysaur_image()
                pokemons_ptbr.Ivysaur_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                
            elif pokemon_desejado == "3":
                pokeansi.venusaur_image()
                pokemons_ptbr.Venusaur_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                
            elif pokemon_desejado == "venusaur":
                pokeansi.venusaur_image()
                pokemons_ptbr.Venusaur_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                
            elif pokemon_desejado == "4":
                pokeansi.charmander_image()
                pokemons_ptbr.Charmander_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                
            elif pokemon_desejado == "charmander":
                pokeansi.charmander_image()
                pokemons_ptbr.Charmander_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                
            elif pokemon_desejado == "5":
                pokeansi.charmeleon_image()
                pokemons_ptbr.Charmeleon_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                
            elif pokemon_desejado == "charmeleon":
                pokeansi.charmeleon_image()
                pokemons_ptbr.Charmeleon_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                
            elif pokemon_desejado == "6":
                pokeansi.charizard_image()
                pokemons_ptbr.Charizard_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                
            elif pokemon_desejado == "charizard":
                pokeansi.charizard_image()
                pokemons_ptbr.Charizard_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                
            elif pokemon_desejado == "7":
                pokeansi.squirtle_image()
                pokemons_ptbr.Squirtle_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                
            elif pokemon_desejado == "squirtle":
                pokeansi.squirtle_image()
                pokemons_ptbr.Squirtle_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                
            elif pokemon_desejado == "8":
                pokeansi.wartortle_image()
                pokemons_ptbr.Wartortle_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                
            elif pokemon_desejado == "wartortle":
                pokeansi.wartortle_image()
                pokemons_ptbr.Wartortle_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                
            elif pokemon_desejado == "9":
                pokeansi.blastoise_image()
                pokemons_ptbr.Blastoise_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                
            elif pokemon_desejado == "blastoise":
                pokeansi.blastoise_image()
                pokemons_ptbr.Blastoise_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                
            elif pokemon_desejado == "10":
                pokeansi.caterpie_image()
                pokemons_ptbr.Caterpie_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                
            elif pokemon_desejado == "caterpie":
                pokeansi.caterpie_image()
                pokemons_ptbr.Caterpie_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                
            elif pokemon_desejado == "11":
                pokeansi.metapod_image()
                pokemons_ptbr.Metapod_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                
            elif pokemon_desejado == "metapod":
                pokeansi.metapod_image()
                pokemons_ptbr.Metapod_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                
            elif pokemon_desejado == "12":
                pokeansi.butterfree_image()
                pokemons_ptbr.Butterfree_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                
            elif pokemon_desejado == "butterfree":
                pokeansi.butterfree_image()
                pokemons_ptbr.Butterfree_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                
            elif pokemon_desejado == "13":
                pokeansi.weedle_image()
                pokemons_ptbr.Weedle_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                
            elif pokemon_desejado == "weedle":
                pokeansi.weedle_image()
                pokemons_ptbr.Weedle_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                
            elif pokemon_desejado == "14":
                pokeansi.kakuna_image()
                pokemons_ptbr.Kakuna_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                
            elif pokemon_desejado == "kakuna":
                pokeansi.kakuna_image()
                pokemons_ptbr.Kakuna_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                
            elif pokemon_desejado == "15":
                pokeansi.beedrill_image()
                pokemons_ptbr.Beedrill_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                
            elif pokemon_desejado == "beedrill":
                pokeansi.beedrill_image()
                pokemons_ptbr.Beedrill_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                
            elif pokemon_desejado == "16":
                pokeansi.pidgey_image()
                pokemons_ptbr.Pidgey_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                
            elif pokemon_desejado == "pidgey":
                pokeansi.pidgey_image()
                pokemons_ptbr.Pidgey_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                
            elif pokemon_desejado == "17":
                pokeansi.pidgeotto_image()
                pokemons_ptbr.Pidgeotto_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                
            elif pokemon_desejado == "pidgeotto":
                pokeansi.pidgeotto_image()
                pokemons_ptbr.Pidgeotto_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                
            elif pokemon_desejado == "18":
                pokeansi.pidgeot_image()
                pokemons_ptbr.Pidgeot_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                
            elif pokemon_desejado == "pidgeot":
                pokeansi.pidgeot_image()
                pokemons_ptbr.Pidgeot_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "19":
                pokeansi.rattata_image()
                pokemons_ptbr.Rattata_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "rattata":
                pokeansi.rattata_image()
                pokemons_ptbr.Rattata_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "20":
                pokeansi.raticate_image()
                pokemons_ptbr.Raticate_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "raticate":
                pokeansi.raticate_image()
                pokemons_ptbr.Raticate_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "21":
                pokeansi.spearow_image()
                pokemons_ptbr.Spearow_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "spearow":
                pokeansi.spearow_image()
                pokemons_ptbr.Spearow_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "22":
                pokeansi.fearow_image()
                pokemons_ptbr.Fearow_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "fearow":
                pokeansi.fearow_image()
                pokemons_ptbr.Fearow_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "23":
                pokeansi.ekans_image()
                pokemons_ptbr.Ekans_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "ekans":
                pokeansi.ekans_image()
                pokemons_ptbr.Ekans_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "24":
                pokeansi.arbok_image()
                pokemons_ptbr.Arbok_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "arbok":
                pokeansi.arbok_image()
                pokemons_ptbr.Arbok_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "25":
                pokeansi.pikachu_image()
                pokemons_ptbr.Pikachu_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "pikachu":
                pokeansi.pikachu_image()
                pokemons_ptbr.Pikachu_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "26":
                pokeansi.raichu_image()
                pokemons_ptbr.Raichu_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "raichu":
                pokeansi.raichu_image()
                pokemons_ptbr.Raichu_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "27":
                pokeansi.sandshrew_image()
                pokemons_ptbr.Sandshrew_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "sandshrew":
                pokeansi.sandshrew_image()
                pokemons_ptbr.Sandshrew_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "28":
                pokeansi.sandslash_image()
                pokemons_ptbr.Sandslash_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "sandslash":
                pokeansi.sandslash_image()
                pokemons_ptbr.Sandslash_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "29":
                pokeansi.nidoran_female_image()
                pokemons_ptbr.Nidoran_Female_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "nidoran f":
                pokeansi.nidoran_female_image()
                pokemons_ptbr.Nidoran_Female_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "30":
                pokeansi.nidorina_image()
                pokemons_ptbr.Nidorina_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "nidorina":
                pokeansi.nidorina_image()
                pokemons_ptbr.Nidorina_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "31":
                pokeansi.nidoqueen_image()
                pokemons_ptbr.Nidoqueen_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "nidoqueen":
                pokeansi.nidoqueen_image()
                pokemons_ptbr.Nidoqueen_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "32":
                pokeansi.nidoran_male_image()
                pokemons_ptbr.Nidoran_Male_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "nidoran m":
                pokeansi.nidoran_male_image()
                pokemons_ptbr.Nidoran_Male_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "33":
                pokeansi.nidorino_image()
                pokemons_ptbr.Nidorino_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "nidorino":
                pokeansi.nidorino_image()
                pokemons_ptbr.Nidorino_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "34":
                pokeansi.nidoking_image()
                pokemons_ptbr.Nidoking_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "nidoking":
                pokeansi.nidoking_image()
                pokemons_ptbr.Nidoking_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "35":
                pokeansi.clefairy_image()
                pokemons_ptbr.Clefairy_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "clefairy":
                pokeansi.clefairy_image()
                pokemons_ptbr.Clefairy_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "36":
                pokeansi.clefable_image()
                pokemons_ptbr.Clefable_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "clefable":
                pokeansi.clefable_image()
                pokemons_ptbr.Clefable_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "37":
                pokeansi.vulpix_image()
                pokemons_ptbr.Vulpix_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "vulpix":
                pokeansi.vulpix_image()
                pokemons_ptbr.Vulpix_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "38":
                pokeansi.ninetales_image()
                pokemons_ptbr.Ninetales_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "ninetales":
                pokeansi.ninetales_image()
                pokemons_ptbr.Ninetales_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "39":
                pokeansi.jigglypuff_image()
                pokemons_ptbr.Jigglypuff_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "jigglypuff":
                pokeansi.jigglypuff_image()
                pokemons_ptbr.Jigglypuff_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "40":
                pokeansi.wigglytuff_image()
                pokemons_ptbr.Wigglytuff_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "wigglytuff":
                pokeansi.wigglytuff_image()
                pokemons_ptbr.Wigglytuff_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "41":
                pokeansi.zubat_image()
                pokemons_ptbr.Zubat_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "zubat":
                pokeansi.zubat_image()
                pokemons_ptbr.Zubat_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "42":
                pokeansi.golbat_image()
                pokemons_ptbr.Golbat_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "golbat":
                pokeansi.golbat_image()
                pokemons_ptbr.Golbat_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "43":
                pokeansi.oddish_image()
                pokemons_ptbr.Oddish_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "oddish":
                pokeansi.oddish_image()
                pokemons_ptbr.Oddish_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "44":
                pokeansi.gloom_image()
                pokemons_ptbr.Gloom_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "gloom":
                pokeansi.gloom_image()
                pokemons_ptbr.Gloom_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "45":
                pokeansi.vileplume_image()
                pokemons_ptbr.Vileplume_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "vileplume":
                pokeansi.vileplume_image()
                pokemons_ptbr.Vileplume_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "46":
                pokeansi.paras_image()
                pokemons_ptbr.Paras_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "paras":
                pokeansi.paras_image()
                pokemons_ptbr.Paras_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "47":
                pokeansi.parasect_image()
                pokemons_ptbr.Parasect_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                    
            elif pokemon_desejado == "parasect":
                pokeansi.parasect_image()
                pokemons_ptbr.Parasect_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "48":
                pokeansi.venonat_image()
                pokemons_ptbr.Venonat_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "venonat":
                pokeansi.venonat_image()
                pokemons_ptbr.Venonat_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "49":
                pokeansi.venomoth_image()
                pokemons_ptbr.Venomoth_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "venomoth":
                pokeansi.venomoth_image()
                pokemons_ptbr.Venomoth_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "50":
                pokeansi.diglett_image()
                pokemons_ptbr.Diglett_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "diglett":
                pokeansi.diglett_image()
                pokemons_ptbr.Diglett_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "51":
                pokeansi.dugtrio_image()
                pokemons_ptbr.Dugtrio_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "dugtrio":
                pokeansi.dugtrio_image()
                pokemons_ptbr.Dugtrio_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "52":
                pokeansi.meowth_image()
                pokemons_ptbr.Meowth_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "meowth":
                pokeansi.meowth_image()
                pokemons_ptbr.Meowth_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "53":
                pokeansi.persian_image()
                pokemons_ptbr.Persian_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "persian":
                pokeansi.persian_image()
                pokemons_ptbr.Persian_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "54":
                pokeansi.psyduck_image()
                pokemons_ptbr.Psyduck_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "psyduck":
                pokeansi.psyduck_image()
                pokemons_ptbr.Psyduck_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "55":
                pokeansi.golduck_image()
                pokemons_ptbr.Golduck_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "golduck":
                pokeansi.golduck_image()
                pokemons_ptbr.Golduck_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "56":
                pokeansi.mankey_image()
                pokemons_ptbr.Mankey_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "mankey":
                pokeansi.mankey_image()
                pokemons_ptbr.Mankey_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "57":
                pokeansi.primeape_image()
                pokemons_ptbr.Primeape_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "primeape":
                pokeansi.primeape_image()
                pokemons_ptbr.Primeape_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "58":
                pokeansi.growlithe_image()
                pokemons_ptbr.Growlithe_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "growlithe":
                pokeansi.growlithe_image()
                pokemons_ptbr.Growlithe_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "59":
                pokeansi.arcanine_image()
                pokemons_ptbr.Arcanine_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "arcanine":
                pokeansi.arcanine_image()
                pokemons_ptbr.Arcanine_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "60":
                pokeansi.poliwag_image()
                pokemons_ptbr.Poliwag_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "poliwag":
                pokeansi.poliwag_image()
                pokemons_ptbr.Poliwag_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "61":
                pokeansi.poliwhirl_image()
                pokemons_ptbr.Poliwhirl_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "poliwhirl":
                pokeansi.poliwhirl_image()
                pokemons_ptbr.Poliwhirl_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "62":
                pokeansi.poliwrath_image()
                pokemons_ptbr.Poliwrath_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "poliwrath":
                pokeansi.poliwrath_image()
                pokemons_ptbr.Poliwrath_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "63":
                pokeansi.abra_image()
                pokemons_ptbr.Abra_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "abra":
                pokeansi.abra_image()
                pokemons_ptbr.Abra_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "64":
                pokeansi.kadabra_image()
                pokemons_ptbr.Kadabra_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "kadabra":
                pokeansi.kadabra_image()
                pokemons_ptbr.Kadabra_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "65":
                pokeansi.alakazam_image()
                pokemons_ptbr.Alakazam_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "alakazam":
                pokeansi.alakazam_image()
                pokemons_ptbr.Alakazam_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "66":
                pokeansi.machop_image()
                pokemons_ptbr.Machop_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "machop":
                pokeansi.machop_image()
                pokemons_ptbr.Machop_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "67":
                pokeansi.machoke_image()
                pokemons_ptbr.Machoke_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "machoke":
                pokeansi.machoke_image()
                pokemons_ptbr.Machoke_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "68":
                pokeansi.machamp_image()
                pokemons_ptbr.Machamp_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "machamp":
                pokeansi.machamp_image()
                pokemons_ptbr.Machamp_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "69":
                pokeansi.bellsprout_image()
                pokemons_ptbr.Bellsprout_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "bellsprout":
                pokeansi.bellsprout_image()
                pokemons_ptbr.Bellsprout_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "70":
                pokeansi.weepinbell_image()
                pokemons_ptbr.Weepinbell_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "weepinbell":
                pokeansi.weepinbell_image()
                pokemons_ptbr.Weepinbell_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "71":
                pokeansi.victreebel_image()
                pokemons_ptbr.Victreebel_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "victreebel":
                pokeansi.victreebel_image()
                pokemons_ptbr.Victreebel_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "72":
                pokeansi.tentacool_image()
                pokemons_ptbr.Tentacool_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "tentacool":
                pokeansi.tentacool_image()
                pokemons_ptbr.Tentacool_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "73":
                pokeansi.tentacruel_image()
                pokemons_ptbr.Tentacruel_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "tentacruel":
                pokeansi.tentacruel_image()
                pokemons_ptbr.Tentacruel_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "74":
                pokeansi.geodude_image()
                pokemons_ptbr.Geodude_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "geodude":
                pokeansi.geodude_image()
                pokemons_ptbr.Geodude_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "75":
                pokeansi.graveler_image()
                pokemons_ptbr.Graveler_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "graveler":
                pokeansi.graveler_image()
                pokemons_ptbr.Graveler_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "76":
                pokeansi.golem_image()
                pokemons_ptbr.Golem_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "golem":
                pokeansi.golem_image()
                pokemons_ptbr.Golem_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "77":
                pokeansi.ponyta_image()
                pokemons_ptbr.Ponyta_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "ponyta":
                pokeansi.ponyta_image()
                pokemons_ptbr.Ponyta_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "78":
                pokeansi.rapidash_image()
                pokemons_ptbr.Rapidash_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "rapidash":
                pokeansi.rapidash_image()
                pokemons_ptbr.Rapidash_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "79":
                pokeansi.slowpoke_image()
                pokemons_ptbr.Slowpoke_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "slowpoke":
                pokeansi.slowpoke_image()
                pokemons_ptbr.Slowpoke_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "80":
                pokeansi.slowbro_image()
                pokemons_ptbr.Slowbro_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "slowbro":
                pokeansi.slowbro_image()
                pokemons_ptbr.Slowbro_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "81":
                pokeansi.magnemite_image()
                pokemons_ptbr.Magnemite_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "magnemite":
                pokeansi.magnemite_image()
                pokemons_ptbr.Magnemite_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "82":
                pokeansi.magneton_image()
                pokemons_ptbr.Magneton_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "magneton":
                pokeansi.magneton_image()
                pokemons_ptbr.Magneton_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "83":
                pokeansi.farfetchd_image()
                pokemons_ptbr.Farfetchd_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "farfetchd":
                pokeansi.farfetchd_image()
                pokemons_ptbr.Farfetchd_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "84":
                pokeansi.doduo_image()
                pokemons_ptbr.Doduo_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "doduo":
                pokeansi.doduo_image()
                pokemons_ptbr.Doduo_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "85":
                pokeansi.dodrio_image()
                pokemons_ptbr.Dodrio_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "dodrio":
                pokeansi.dodrio_image()
                pokemons_ptbr.Dodrio_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "86":
                pokeansi.seel_image()
                pokemons_ptbr.Seel_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "seel":
                pokeansi.seel_image()
                pokemons_ptbr.Seel_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "87":
                pokeansi.dewgong_image()
                pokemons_ptbr.Dewgong_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "dewgong":
                pokeansi.dewgong_image()
                pokemons_ptbr.Dewgong_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "88":
                pokeansi.grimer_image()
                pokemons_ptbr.Grimer_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "grimer":
                pokeansi.grimer_image()
                pokemons_ptbr.Grimer_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "89":
                pokeansi.muk_image()
                pokemons_ptbr.Muk_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "muk":
                pokeansi.muk_image()
                pokemons_ptbr.Muk_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "90":
                pokeansi.muk_image()
                pokemons_ptbr.Muk_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "shellder":
                pokeansi.shellder_image()
                pokemons_ptbr.Shellder_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "91":
                pokeansi.cloyster_image()
                pokemons_ptbr.Cloyster_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "cloyster":
                pokeansi.cloyster_image()
                pokemons_ptbr.Cloyster_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "92":
                pokeansi.gastly_image()
                pokemons_ptbr.Gastly_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "gastly":
                pokeansi.gastly_image()
                pokemons_ptbr.Gastly_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "93":
                pokeansi.haunter_image()
                pokemons_ptbr.Haunter_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "haunter":
                pokeansi.haunter_image()
                pokemons_ptbr.Haunter_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "94":
                pokeansi.gengar_image()
                pokemons_ptbr.Gengar_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "gengar":
                pokeansi.gengar_image()
                pokemons_ptbr.Gengar_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "95":
                pokeansi.onix_image()
                pokemons_ptbr.Onix_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "onix":
                pokeansi.onix_image()
                pokemons_ptbr.Onix_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "96":
                pokeansi.drowzee_image()
                pokemons_ptbr.Drowzee_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "drowzee":
                pokeansi.drowzee_image()
                pokemons_ptbr.Drowzee_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "97":
                pokeansi.hypno_image()
                pokemons_ptbr.Hypno_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "hypno":
                pokeansi.hypno_image()
                pokemons_ptbr.Hypno_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "98":
                pokeansi.krabby_image()
                pokemons_ptbr.Krabby_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "krabby":
                pokeansi.krabby_image()
                pokemons_ptbr.Krabby_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "99":
                pokeansi.kingler_image()
                pokemons_ptbr.Kingler_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "kingler":
                pokeansi.kingler_image()
                pokemons_ptbr.Kingler_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "100":
                pokeansi.voltorb_image()
                pokemons_ptbr.Voltorb_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "voltorb":
                pokeansi.voltorb_image()
                pokemons_ptbr.Voltorb_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "101":
                pokeansi.electrode_image()
                pokemons_ptbr.Electrode_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "electrode":
                pokeansi.electrode_image()
                pokemons_ptbr.Electrode_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "102":
                pokeansi.exeggcute_image()
                pokemons_ptbr.Exeggcute_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "exeggcute":
                pokeansi.exeggcute_image()
                pokemons_ptbr.Exeggcute_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "103":
                pokeansi.exeggutor_image()
                pokemons_ptbr.Exeggutor_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "exeggutor":
                pokeansi.exeggutor_image()
                pokemons_ptbr.Exeggutor_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "104":
                pokeansi.cubone_image()
                pokemons_ptbr.Cubone_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "cubone":
                pokeansi.cubone_image()
                pokemons_ptbr.Cubone_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "105":
                pokeansi.marowak_image()
                pokemons_ptbr.Marowak_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "marowak":
                pokeansi.marowak_image()
                pokemons_ptbr.Marowak_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "106":
                pokeansi.hitmonlee_image()
                pokemons_ptbr.Hitmonlee_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "hitmonlee":
                pokeansi.hitmonlee_image()
                pokemons_ptbr.Hitmonlee_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "107":
                pokeansi.hitmonchan_image()
                pokemons_ptbr.Hitmonchan_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "hitmonchan":
                pokeansi.hitmonchan_image()
                pokemons_ptbr.Hitmonchan_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "108":
                pokeansi.lickitung_image()
                pokemons_ptbr.Lickitung_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "lickitung":
                pokeansi.lickitung_image()
                pokemons_ptbr.Lickitung_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "109":
                pokeansi.koffing_image()
                pokemons_ptbr.Koffing_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "koffing":
                pokeansi.koffing_image()
                pokemons_ptbr.Koffing_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "110":
                pokeansi.weezing_image()
                pokemons_ptbr.Weezing_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "weezing":
                pokeansi.weezing_image()
                pokemons_ptbr.Weezing_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "111":
                pokeansi.rhyhorn_image()
                pokemons_ptbr.Rhyhorn_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "rhyhorn":
                pokeansi.rhyhorn_image()
                pokemons_ptbr.Rhyhorn_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "112":
                pokeansi.rhydon_image()
                pokemons_ptbr.Rhydon_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "rhydon":
                pokeansi.rhydon_image()
                pokemons_ptbr.Rhydon_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "113":
                pokeansi.chansey_image()
                pokemons_ptbr.Chansey_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "chansey":
                pokeansi.chansey_image()
                pokemons_ptbr.Chansey_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "114":
                pokeansi.tangela_image()
                pokemons_ptbr.Tangela_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "tangela":
                pokeansi.tangela_image()
                pokemons_ptbr.Tangela_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "115":
                pokeansi.kangaskhan_image()
                pokemons_ptbr.Kangaskhan_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "kangaskhan":
                pokeansi.kangaskhan_image()
                pokemons_ptbr.Kangaskhan_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "116":
                pokeansi.horsea_image()
                pokemons_ptbr.Horsea_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "horsea":
                pokeansi.horsea_image()
                pokemons_ptbr.Horsea_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "117":
                pokeansi.seadra_image()
                pokemons_ptbr.Seadra_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "seadra":
                pokeansi.seadra_image()
                pokemons_ptbr.Seadra_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "118":
                pokeansi.goldeen_image()
                pokemons_ptbr.Goldeen_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "goldeen":
                pokeansi.goldeen_image()
                pokemons_ptbr.Goldeen_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "119":
                pokeansi.seaking_image()
                pokemons_ptbr.Seaking_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "seaking":
                pokeansi.seaking_image()
                pokemons_ptbr.Seaking_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "120":
                pokeansi.staryu_image()
                pokemons_ptbr.Staryu_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "staryu":
                pokeansi.staryu_image()
                pokemons_ptbr.Staryu_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "121":
                pokeansi.starmie_image()
                pokemons_ptbr.Starmie_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "starmie":
                pokeansi.starmie_image()
                pokemons_ptbr.Starmie_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "122":
                pokeansi.mr_mime_image()
                pokemons_ptbr.Mr_Mime_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "mr mime":
                pokeansi.mr_mime_image()
                pokemons_ptbr.Mr_Mime_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "123":
                pokeansi.scyther_image()
                pokemons_ptbr.Scyther_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "scyther":
                pokeansi.scyther_image()
                pokemons_ptbr.Scyther_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "124":
                pokeansi.jynx_image()
                pokemons_ptbr.Jynx_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "jynx":
                pokeansi.jynx_image()
                pokemons_ptbr.Jynx_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "125":
                pokeansi.electabuzz_image()
                pokemons_ptbr.Electabuzz_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "electabuzz":
                pokeansi.electabuzz_image()
                pokemons_ptbr.Electabuzz_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "126":
                pokeansi.magmar_image()
                pokemons_ptbr.Magmar_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "magmar":
                pokeansi.magmar_image()
                pokemons_ptbr.Magmar_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "127":
                pokeansi.pinsir_image()
                pokemons_ptbr.Pinsir_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "pinsir":
                pokeansi.pinsir_image()
                pokemons_ptbr.Pinsir_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "128":
                pokeansi.tauros_image()
                pokemons_ptbr.Tauros_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "tauros":
                pokeansi.tauros_image()
                pokemons_ptbr.Tauros_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "129":
                pokeansi.magikarp_image()
                pokemons_ptbr.Magikarp_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "magikarp":
                pokeansi.magikarp_image()
                pokemons_ptbr.Magikarp_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "130":
                pokeansi.gyarados_image()
                pokemons_ptbr.Gyarados_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "gyarados":
                pokeansi.gyarados_image()
                pokemons_ptbr.Gyarados_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "131":
                pokeansi.lapras_image()
                pokemons_ptbr.Lapras_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "lapras":
                pokeansi.lapras_image()
                pokemons_ptbr.Lapras_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "132":
                pokeansi.ditto_image()
                pokemons_ptbr.Ditto_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "ditto":
                pokeansi.ditto_image()
                pokemons_ptbr.Ditto_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "133":
                pokeansi.eevee_image()
                pokemons_ptbr.Eevee_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "eevee":
                pokeansi.eevee_image()
                pokemons_ptbr.Eevee_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "134":
                pokeansi.vaporeon_image()
                pokemons_ptbr.Vaporeon_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "vaporeon":
                pokeansi.vaporeon_image()
                pokemons_ptbr.Vaporeon_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "135":
                pokeansi.jolteon_image()
                pokemons_ptbr.Jolteon_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                    
            elif pokemon_desejado == "jolteon":
                pokeansi.jolteon_image()
                pokemons_ptbr.Jolteon_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                                 
            elif pokemon_desejado == "136":
                pokeansi.flareon_image()
                pokemons_ptbr.Flareon_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                                 
            elif pokemon_desejado == "flareon":
                pokeansi.flareon_image()
                pokemons_ptbr.Flareon_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                                 
            elif pokemon_desejado == "137":
                pokeansi.porygon_image()
                pokemons_ptbr.Porygon_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                                 
            elif pokemon_desejado == "porygon":
                pokeansi.porygon_image()
                pokemons_ptbr.Porygon_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                                 
            elif pokemon_desejado == "138":
                pokeansi.omanyte_image()
                pokemons_ptbr.Omanyte_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                                 
            elif pokemon_desejado == "omanyte":
                pokeansi.omanyte_image()
                pokemons_ptbr.Omanyte_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                                 
            elif pokemon_desejado == "139":
                pokeansi.omastar_image()
                pokemons_ptbr.Omastar_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                                 
            elif pokemon_desejado == "omastar":
                pokeansi.omastar_image()
                pokemons_ptbr.Omastar_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                                 
            elif pokemon_desejado == "140":
                pokeansi.kabuto_image()
                pokemons_ptbr.Kabuto_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                                 
            elif pokemon_desejado == "kabuto":
                pokeansi.kabuto_image()
                pokemons_ptbr.Kabuto_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                                 
            elif pokemon_desejado == "141":
                pokeansi.kabutops_image()
                pokemons_ptbr.Kabutops_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                                 
            elif pokemon_desejado == "kabutops":
                pokeansi.kabutops_image()
                pokemons_ptbr.Kabutops_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                                 
            elif pokemon_desejado == "142":
                pokeansi.aerodactyl_image()
                pokemons_ptbr.Aerodactyl_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                                 
            elif pokemon_desejado == "aerodactyl":
                pokeansi.aerodactyl_image()
                pokemons_ptbr.Aerodactyl_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                                 
            elif pokemon_desejado == "143":
                pokeansi.snorlax_image()
                pokemons_ptbr.Snorlax_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                                 
            elif pokemon_desejado == "snorlax":
                pokeansi.snorlax_image()
                pokemons_ptbr.Snorlax_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                                 
            elif pokemon_desejado == "144":
                pokeansi.articuno_image()
                pokemons_ptbr.Articuno_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                                 
            elif pokemon_desejado == "articuno":
                pokeansi.articuno_image()
                pokemons_ptbr.Articuno_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                                 
            elif pokemon_desejado == "145":
                pokeansi.zapdos_image()
                pokemons_ptbr.Zapdos_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                                 
            elif pokemon_desejado == "zapdos":
                pokeansi.zapdos_image()
                pokemons_ptbr.Zapdos_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                                 
            elif pokemon_desejado == "146":
                pokeansi.moltres_image()
                pokemons_ptbr.Moltres_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                                 
            elif pokemon_desejado == "moltres":
                pokeansi.moltres_image()
                pokemons_ptbr.Moltres_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                                 
            elif pokemon_desejado == "147":
                pokeansi.dratini_image()
                pokemons_ptbr.Dratini_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                                 
            elif pokemon_desejado == "dratini":
                pokeansi.dratini_image()
                pokemons_ptbr.Dratini_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                                 
            elif pokemon_desejado == "148":
                pokeansi.dragonair_image()
                pokemons_ptbr.Dragonair_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                                 
            elif pokemon_desejado == "dragonair":
                pokeansi.dragonair_image()
                pokemons_ptbr.Dragonair_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                                 
            elif pokemon_desejado == "149":
                pokeansi.dragonite_image()
                pokemons_ptbr.Dragonite_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                                 
            elif pokemon_desejado == "dragonite":
                pokeansi.dragonite_image()
                pokemons_ptbr.Dragonite_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                                 
            elif pokemon_desejado == "150":
                pokeansi.mewtwo_image()
                pokemons_ptbr.Mewtwo_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                                 
            elif pokemon_desejado == "mewtwo":
                pokeansi.mewtwo_image()
                pokemons_ptbr.Mewtwo_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                                 
            elif pokemon_desejado == "151":
                pokeansi.mew_image()
                pokemons_ptbr.Mew_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                                 
            elif pokemon_desejado == "mew":
                pokeansi.mew_image()
                pokemons_ptbr.Mew_pt.mostra_pokemon()
                input("\n\nAperte \"enter\" para continuar.")
                                                                 
            else:
                print("\n\n**** Pokémon não encontrado ou comando inválido ****")
                input("\n\nAperte \"enter\" para continuar.")




    # PARA CÓDIGO EM INGLÊS =====v

    elif user_answer == "en":
        run_en = "y"
        while run_en == "y":
            print("\n\n\n(* Only first generation pokemon available at the moment.)\n\nEnter numbers from 1 to 151; or type the Pokemon's name *")
            print("\nType \"menu\" to go back to language menu.")

            pokemon_desejado = input("\n\nWhich pokemon do you want to look for?\n\n").lower().strip() ##############
            
            if pokemon_desejado == "menu":
                run_en = "n"

            elif pokemon_desejado == "quit":
                print("\n\nSee you !!")
                exit()

            elif pokemon_desejado == "sair":
                print("\n\nAté logo !!")
                exit()

            elif pokemon_desejado == "exit":
                print("\n\nSee you !!")
                exit()

            elif pokemon_desejado == "1":
                pokeansi.bulbasaur_image()
                pokemons_en.Bulbasaur_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "bulbasaur":
                pokeansi.bulbasaur_image()
                pokemons_en.Bulbasaur_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "2":
                pokeansi.ivysaur_image()
                pokemons_en.Ivysaur_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "ivysaur":
                pokeansi.ivysaur_image()
                pokemons_en.Ivysaur_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "3":
                pokeansi.venusaur_image()
                pokemons_en.Venusaur_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "venusaur":
                pokeansi.venusaur_image()
                pokemons_en.Venusaur_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "4":
                pokeansi.charmander_image()
                pokemons_en.Charmander_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "charmander":
                pokeansi.charmander_image()
                pokemons_en.Charmander_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "5":
                pokeansi.charmeleon_image()
                pokemons_en.Charmeleon_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "charmeleon":
                pokeansi.charmeleon_image()
                pokemons_en.Charmeleon_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "6":
                pokeansi.charizard_image()
                pokemons_en.Charizard_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "charizard":
                pokeansi.charizard_image()
                pokemons_en.Charizard_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "7":
                pokeansi.squirtle_image()
                pokemons_en.Squirtle_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "squirtle":
                pokeansi.squirtle_image()
                pokemons_en.Squirtle_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "8":
                pokeansi.wartortle_image()
                pokemons_en.Wartortle_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "wartortle":
                pokeansi.wartortle_image()
                pokemons_en.Wartortle_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "9":
                pokeansi.blastoise_image()
                pokemons_en.Blastoise_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "blastoise":
                pokeansi.blastoise_image()
                pokemons_en.Blastoise_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "10":
                pokeansi.caterpie_image()
                pokemons_en.Caterpie_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "caterpie":
                pokeansi.caterpie_image()
                pokemons_en.Caterpie_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "11":
                pokeansi.metapod_image()
                pokemons_en.Metapod_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "metapod":
                pokeansi.metapod_image()
                pokemons_en.Metapod_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "12":
                pokeansi.butterfree_image()
                pokemons_en.Butterfree_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "butterfree":
                pokeansi.butterfree_image()
                pokemons_en.Butterfree_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "13":
                pokeansi.weedle_image()
                pokemons_en.Weedle_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "weedle":
                pokeansi.weedle_image()
                pokemons_en.Weedle_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "14":
                pokeansi.kakuna_image()
                pokemons_en.Kakuna_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "kakuna":
                pokeansi.kakuna_image()
                pokemons_en.Kakuna_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "15":
                pokeansi.beedrill_image()
                pokemons_en.Beedrill_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "beedrill":
                pokeansi.beedrill_image()
                pokemons_en.Beedrill_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "16":
                pokeansi.pidgey_image()
                pokemons_en.Pidgey_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "pidgey":
                pokeansi.pidgey_image()
                pokemons_en.Pidgey_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "17":
                pokeansi.pidgeotto_image()
                pokemons_en.Pidgeotto_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "pidgeotto":
                pokeansi.pidgeotto_image()
                pokemons_en.Pidgeotto_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "18":
                pokeansi.pidgeot_image()
                pokemons_en.Pidgeot_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "pidgeot":
                pokeansi.pidgeot_image()
                pokemons_en.Pidgeot_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "19":
                pokeansi.rattata_image()
                pokemons_en.Rattata_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "rattata":
                pokeansi.rattata_image()
                pokemons_en.Rattata_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "20":
                pokeansi.raticate_image()
                pokemons_en.Raticate_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "raticate":
                pokeansi.raticate_image()
                pokemons_en.Raticate_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "21":
                pokeansi.spearow_image()
                pokemons_en.Spearow_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "spearow":
                pokeansi.spearow_image()
                pokemons_en.Spearow_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "22":
                pokeansi.fearow_image()
                pokemons_en.Fearow_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "fearow":
                pokeansi.fearow_image()
                pokemons_en.Fearow_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "23":
                pokeansi.ekans_image()
                pokemons_en.Ekans_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "ekans":
                pokeansi.ekans_image()
                pokemons_en.Ekans_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "24":
                pokeansi.arbok_image()
                pokemons_en.Arbok_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "arbok":
                pokeansi.arbok_image()
                pokemons_en.Arbok_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "25":
                pokeansi.pikachu_image()
                pokemons_en.Pikachu_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "pikachu":
                pokeansi.pikachu_image()
                pokemons_en.Pikachu_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "26":
                pokeansi.raichu_image()
                pokemons_en.Raichu_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "raichu":
                pokeansi.raichu_image()
                pokemons_en.Raichu_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "27":
                pokeansi.sandshrew_image()
                pokemons_en.Sandshrew_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "sandshrew":
                pokeansi.sandshrew_image()
                pokemons_en.Sandshrew_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "28":
                pokeansi.sandslash_image()
                pokemons_en.Sandslash_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "sandslash":
                pokeansi.sandslash_image()
                pokemons_en.Sandslash_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "29":
                pokeansi.nidoran_female_image()
                pokemons_en.Nidoran_Female_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "nidoran f":
                pokeansi.nidoran_female_image()
                pokemons_en.Nidoran_Female_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "30":
                pokeansi.nidorina_image()
                pokemons_en.Nidorina_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "nidorina":
                pokeansi.nidorina_image()
                pokemons_en.Nidorina_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "31":
                pokeansi.nidoqueen_image()
                pokemons_en.Nidoqueen_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "nidoqueen":
                pokeansi.nidoqueen_image()
                pokemons_en.Nidoqueen_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "32":
                pokeansi.nidoran_male_image()
                pokemons_en.Nidoran_Male_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "nidoran m":
                pokeansi.nidoran_male_image()
                pokemons_en.Nidoran_Male_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "33":
                pokeansi.nidorino_image()
                pokemons_en.Nidorino_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "nidorino":
                pokeansi.nidorino_image()
                pokemons_en.Nidorino_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "34":
                pokeansi.nidoking_image()
                pokemons_en.Nidoking_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "nidoking":
                pokeansi.nidoking_image()
                pokemons_en.Nidoking_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "35":
                pokeansi.clefairy_image()
                pokemons_en.Clefairy_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "clefairy":
                pokeansi.clefairy_image()
                pokemons_en.Clefairy_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "36":
                pokeansi.clefable_image()
                pokemons_en.Clefable_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "clefable":
                pokeansi.clefable_image()
                pokemons_en.Clefable_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "37":
                pokeansi.vulpix_image()
                pokemons_en.Vulpix_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "vulpix":
                pokeansi.vulpix_image()
                pokemons_en.Vulpix_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "38":
                pokeansi.ninetales_image()
                pokemons_en.Ninetales_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "ninetales":
                pokeansi.ninetales_image()
                pokemons_en.Ninetales_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "39":
                pokeansi.jigglypuff_image()
                pokemons_en.Jigglypuff_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "jigglypuff":
                pokeansi.jigglypuff_image()
                pokemons_en.Jigglypuff_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "40":
                pokeansi.wigglytuff_image()
                pokemons_en.Wigglytuff_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "wigglytuff":
                pokeansi.wigglytuff_image()
                pokemons_en.Wigglytuff_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "41":
                pokeansi.zubat_image()
                pokemons_en.Zubat_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "zubat":
                pokeansi.zubat_image()
                pokemons_en.Zubat_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "42":
                pokeansi.golbat_image()
                pokemons_en.Golbat_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "golbat":
                pokeansi.golbat_image()
                pokemons_en.Golbat_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "43":
                pokeansi.oddish_image()
                pokemons_en.Oddish_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "oddish":
                pokeansi.oddish_image()
                pokemons_en.Oddish_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "44":
                pokeansi.gloom_image()
                pokemons_en.Gloom_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "gloom":
                pokeansi.gloom_image()
                pokemons_en.Gloom_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "45":
                pokeansi.vileplume_image()
                pokemons_en.Vileplume_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "vileplume":
                pokeansi.vileplume_image()
                pokemons_en.Vileplume_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "46":
                pokeansi.paras_image()
                pokemons_en.Paras_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "paras":
                pokeansi.paras_image()
                pokemons_en.Paras_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "47":
                pokeansi.parasect_image()
                pokemons_en.Parasect_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "parasect":
                pokeansi.parasect_image()
                pokemons_en.Parasect_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "48":
                pokeansi.venonat_image()
                pokemons_en.Venonat_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "venonat":
                pokeansi.venonat_image()
                pokemons_en.Venonat_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "49":
                pokeansi.venomoth_image()
                pokemons_en.Venomoth_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "venomoth":
                pokeansi.venomoth_image()
                pokemons_en.Venomoth_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "50":
                pokeansi.diglett_image()
                pokemons_en.Diglett_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "diglett":
                pokeansi.diglett_image()
                pokemons_en.Diglett_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "51":
                pokeansi.dugtrio_image()
                pokemons_en.Dugtrio_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "dugtrio":
                pokeansi.dugtrio_image()
                pokemons_en.Dugtrio_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "52":
                pokeansi.meowth_image()
                pokemons_en.Meowth_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "meowth":
                pokeansi.meowth_image()
                pokemons_en.Meowth_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "53":
                pokeansi.persian_image()
                pokemons_en.Persian_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "persian":
                pokeansi.persian_image()
                pokemons_en.Persian_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "54":
                pokeansi.psyduck_image()
                pokemons_en.Psyduck_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "psyduck":
                pokeansi.psyduck_image()
                pokemons_en.Psyduck_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "55":
                pokeansi.golduck_image()
                pokemons_en.Golduck_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "golduck":
                pokeansi.golduck_image()
                pokemons_en.Golduck_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "56":
                pokeansi.mankey_image()
                pokemons_en.Mankey_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "mankey":
                pokeansi.mankey_image()
                pokemons_en.Mankey_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "57":
                pokeansi.primeape_image()
                pokemons_en.Primeape_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "primeape":
                pokeansi.primeape_image()
                pokemons_en.Primeape_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "58":
                pokeansi.growlithe_image()
                pokemons_en.Growlithe_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "growlithe":
                pokeansi.growlithe_image()
                pokemons_en.Growlithe_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "59":
                pokeansi.arcanine_image()
                pokemons_en.Arcanine_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "arcanine":
                pokeansi.arcanine_image()
                pokemons_en.Arcanine_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "60":
                pokeansi.poliwag_image()
                pokemons_en.Poliwag_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "poliwag":
                pokeansi.poliwag_image()
                pokemons_en.Poliwag_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "61":
                pokeansi.poliwhirl_image()
                pokemons_en.Poliwhirl_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "poliwhirl":
                pokeansi.poliwhirl_image()
                pokemons_en.Poliwhirl_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "62":
                pokeansi.poliwrath_image()
                pokemons_en.Poliwrath_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "poliwrath":
                pokeansi.poliwrath_image()
                pokemons_en.Poliwrath_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "63":
                pokeansi.abra_image()
                pokemons_en.Abra_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "abra":
                pokeansi.abra_image()
                pokemons_en.Abra_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "64":
                pokeansi.kadabra_image()
                pokemons_en.Kadabra_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "kadabra":
                pokeansi.kadabra_image()
                pokemons_en.Kadabra_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "65":
                pokeansi.alakazam_image()
                pokemons_en.Alakazam_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "alakazam":
                pokeansi.alakazam_image()
                pokemons_en.Alakazam_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "66":
                pokeansi.machop_image()
                pokemons_en.Machop_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "machop":
                pokeansi.machop_image()
                pokemons_en.Machop_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "67":
                pokeansi.machoke_image()
                pokemons_en.Machoke_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "machoke":
                pokeansi.machoke_image()
                pokemons_en.Machoke_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "68":
                pokeansi.machamp_image()
                pokemons_en.Machamp_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "machamp":
                pokeansi.machamp_image()
                pokemons_en.Machamp_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "69":
                pokeansi.bellsprout_image()
                pokemons_en.Bellsprout_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "bellsprout":
                pokeansi.bellsprout_image()
                pokemons_en.Bellsprout_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "70":
                pokeansi.weepinbell_image()
                pokemons_en.Weepinbell_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "weepinbell":
                pokeansi.weepinbell_image()
                pokemons_en.Weepinbell_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "71":
                pokeansi.victreebel_image()
                pokemons_en.Victreebel_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "victreebel":
                pokeansi.victreebel_image()
                pokemons_en.Victreebel_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "72":
                pokeansi.tentacool_image()
                pokemons_en.Tentacool_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "tentacool":
                pokeansi.tentacool_image()
                pokemons_en.Tentacool_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "73":
                pokeansi.tentacruel_image()
                pokemons_en.Tentacruel_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "tentacruel":
                pokeansi.tentacruel_image()
                pokemons_en.Tentacruel_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")

            elif pokemon_desejado == "74":
                pokeansi.geodude_image()
                pokemons_en.Geodude_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "geodude":
                pokeansi.geodude_image()
                pokemons_en.Geodude_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "75":
                pokeansi.graveler_image()
                pokemons_en.Graveler_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "graveler":
                pokeansi.graveler_image()
                pokemons_en.Graveler_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "76":
                pokeansi.golem_image()
                pokemons_en.Golem_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "golem":
                pokeansi.golem_image()
                pokemons_en.Golem_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "77":
                pokeansi.ponyta_image()
                pokemons_en.Ponyta_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "ponyta":
                pokeansi.ponyta_image()
                pokemons_en.Ponyta_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "78":
                pokeansi.rapidash_image()
                pokemons_en.Rapidash_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "rapidash":
                pokeansi.rapidash_image()
                pokemons_en.Rapidash_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "79":
                pokeansi.slowpoke_image()
                pokemons_en.Slowpoke_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "slowpoke":
                pokeansi.slowpoke_image()
                pokemons_en.Slowpoke_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "80":
                pokeansi.slowbro_image()
                pokemons_en.Slowbro_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "slowbro":
                pokeansi.slowbro_image()
                pokemons_en.Slowbro_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "81":
                pokeansi.magnemite_image()
                pokemons_en.Magnemite_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "magnemite":
                pokeansi.magnemite_image()
                pokemons_en.Magnemite_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "82":
                pokeansi.magneton_image()
                pokemons_en.Magneton_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "magneton":
                pokeansi.magneton_image()
                pokemons_en.Magneton_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "83":
                pokeansi.farfetchd_image()
                pokemons_en.Farfetchd_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "farfetchd":
                pokeansi.farfetchd_image()
                pokemons_en.Farfetchd_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "84":
                pokeansi.doduo_image()
                pokemons_en.Doduo_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "doduo":
                pokeansi.doduo_image()
                pokemons_en.Doduo_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "85":
                pokeansi.dodrio_image()
                pokemons_en.Dodrio_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "dodrio":
                pokeansi.dodrio_image()
                pokemons_en.Dodrio_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "86":
                pokeansi.seel_image()
                pokemons_en.Seel_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "seel":
                pokeansi.seel_image()
                pokemons_en.Seel_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "87":
                pokeansi.dewgong_image()
                pokemons_en.Dewgong_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "dewgong":
                pokeansi.dewgong_image()
                pokemons_en.Dewgong_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "88":
                pokeansi.grimer_image()
                pokemons_en.Grimer_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "grimer":
                pokeansi.grimer_image()
                pokemons_en.Grimer_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "89":
                pokeansi.muk_image()
                pokemons_en.Muk_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "muk":
                pokeansi.muk_image()
                pokemons_en.Muk_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "90":
                pokeansi.muk_image()
                pokemons_en.Muk_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "shellder":
                pokeansi.shellder_image()
                pokemons_en.Shellder_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "91":
                pokeansi.cloyster_image()
                pokemons_en.Cloyster_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "cloyster":
                pokeansi.cloyster_image()
                pokemons_en.Cloyster_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "92":
                pokeansi.gastly_image()
                pokemons_en.Gastly_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "gastly":
                pokeansi.gastly_image()
                pokemons_en.Gastly_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "93":
                pokeansi.haunter_image()
                pokemons_en.Haunter_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "haunter":
                pokeansi.haunter_image()
                pokemons_en.Haunter_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "94":
                pokeansi.gengar_image()
                pokemons_en.Gengar_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "gengar":
                pokeansi.gengar_image()
                pokemons_en.Gengar_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "95":
                pokeansi.onix_image()
                pokemons_en.Onix_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "onix":
                pokeansi.onix_image()
                pokemons_en.Onix_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "96":
                pokeansi.drowzee_image()
                pokemons_en.Drowzee_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "drowzee":
                pokeansi.drowzee_image()
                pokemons_en.Drowzee_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "97":
                pokeansi.hypno_image()
                pokemons_en.Hypno_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "hypno":
                pokeansi.hypno_image()
                pokemons_en.Hypno_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "98":
                pokeansi.krabby_image()
                pokemons_en.Krabby_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "krabby":
                pokeansi.krabby_image()
                pokemons_en.Krabby_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "99":
                pokeansi.kingler_image()
                pokemons_en.Kingler_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "kingler":
                pokeansi.kingler_image()
                pokemons_en.Kingler_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "100":
                pokeansi.voltorb_image()
                pokemons_en.Voltorb_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "voltorb":
                pokeansi.voltorb_image()
                pokemons_en.Voltorb_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "101":
                pokeansi.electrode_image()
                pokemons_en.Electrode_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "electrode":
                pokeansi.electrode_image()
                pokemons_en.Electrode_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "102":
                pokeansi.exeggcute_image()
                pokemons_en.Exeggcute_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "exeggcute":
                pokeansi.exeggcute_image()
                pokemons_en.Exeggcute_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "103":
                pokeansi.exeggutor_image()
                pokemons_en.Exeggutor_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "exeggutor":
                pokeansi.exeggutor_image()
                pokemons_en.Exeggutor_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "104":
                pokeansi.cubone_image()
                pokemons_en.Cubone_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "cubone":
                pokeansi.cubone_image()
                pokemons_en.Cubone_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "105":
                pokeansi.marowak_image()
                pokemons_en.Marowak_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "marowak":
                pokeansi.marowak_image()
                pokemons_en.Marowak_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "106":
                pokeansi.hitmonlee_image()
                pokemons_en.Hitmonlee_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "hitmonlee":
                pokeansi.hitmonlee_image()
                pokemons_en.Hitmonlee_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "107":
                pokeansi.hitmonchan_image()
                pokemons_en.Hitmonchan_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "hitmonchan":
                pokeansi.hitmonchan_image()
                pokemons_en.Hitmonchan_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "108":
                pokeansi.lickitung_image()
                pokemons_en.Lickitung_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "lickitung":
                pokeansi.lickitung_image()
                pokemons_en.Lickitung_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "109":
                pokeansi.koffing_image()
                pokemons_en.Koffing_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "koffing":
                pokeansi.koffing_image()
                pokemons_en.Koffing_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "110":
                pokeansi.weezing_image()
                pokemons_en.Weezing_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "weezing":
                pokeansi.weezing_image()
                pokemons_en.Weezing_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "111":
                pokeansi.rhyhorn_image()
                pokemons_en.Rhyhorn_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "rhyhorn":
                pokeansi.rhyhorn_image()
                pokemons_en.Rhyhorn_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "112":
                pokeansi.rhydon_image()
                pokemons_en.Rhydon_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "rhydon":
                pokeansi.rhydon_image()
                pokemons_en.Rhydon_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "113":
                pokeansi.chansey_image()
                pokemons_en.Chansey_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "chansey":
                pokeansi.chansey_image()
                pokemons_en.Chansey_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "114":
                pokeansi.tangela_image()
                pokemons_en.Tangela_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "tangela":
                pokeansi.tangela_image()
                pokemons_en.Tangela_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "115":
                pokeansi.kangaskhan_image()
                pokemons_en.Kangaskhan_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "kangaskhan":
                pokeansi.kangaskhan_image()
                pokemons_en.Kangaskhan_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "116":
                pokeansi.horsea_image()
                pokemons_en.Horsea_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "horsea":
                pokeansi.horsea_image()
                pokemons_en.Horsea_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "117":
                pokeansi.seadra_image()
                pokemons_en.Seadra_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "seadra":
                pokeansi.seadra_image()
                pokemons_en.Seadra_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "118":
                pokeansi.goldeen_image()
                pokemons_en.Goldeen_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "goldeen":
                pokeansi.goldeen_image()
                pokemons_en.Goldeen_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "119":
                pokeansi.seaking_image()
                pokemons_en.Seaking_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "seaking":
                pokeansi.seaking_image()
                pokemons_en.Seaking_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "120":
                pokeansi.staryu_image()
                pokemons_en.Staryu_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "staryu":
                pokeansi.staryu_image()
                pokemons_en.Staryu_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "121":
                pokeansi.starmie_image()
                pokemons_en.Starmie_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "starmie":
                pokeansi.starmie_image()
                pokemons_en.Starmie_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "122":
                pokeansi.mr_mime_image()
                pokemons_en.Mr_Mime_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "mr mime":
                pokeansi.mr_mime_image()
                pokemons_en.Mr_Mime_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "123":
                pokeansi.scyther_image()
                pokemons_en.Scyther_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "scyther":
                pokeansi.scyther_image()
                pokemons_en.Scyther_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "124":
                pokeansi.jynx_image()
                pokemons_en.Jynx_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "jynx":
                pokeansi.jynx_image()
                pokemons_en.Jynx_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "125":
                pokeansi.electabuzz_image()
                pokemons_en.Electabuzz_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "electabuzz":
                pokeansi.electabuzz_image()
                pokemons_en.Electabuzz_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "126":
                pokeansi.magmar_image()
                pokemons_en.Magmar_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "magmar":
                pokeansi.magmar_image()
                pokemons_en.Magmar_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "127":
                pokeansi.pinsir_image()
                pokemons_en.Pinsir_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "pinsir":
                pokeansi.pinsir_image()
                pokemons_en.Pinsir_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "128":
                pokeansi.tauros_image()
                pokemons_en.Tauros_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "tauros":
                pokeansi.tauros_image()
                pokemons_en.Tauros_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "129":
                pokeansi.magikarp_image()
                pokemons_en.Magikarp_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "magikarp":
                pokeansi.magikarp_image()
                pokemons_en.Magikarp_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "130":
                pokeansi.gyarados_image()
                pokemons_en.Gyarados_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "gyarados":
                pokeansi.gyarados_image()
                pokemons_en.Gyarados_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "131":
                pokeansi.lapras_image()
                pokemons_en.Lapras_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "lapras":
                pokeansi.lapras_image()
                pokemons_en.Lapras_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "132":
                pokeansi.ditto_image()
                pokemons_en.Ditto_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "ditto":
                pokeansi.ditto_image()
                pokemons_en.Ditto_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "133":
                pokeansi.eevee_image()
                pokemons_en.Eevee_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "eevee":
                pokeansi.eevee_image()
                pokemons_en.Eevee_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "134":
                pokeansi.vaporeon_image()
                pokemons_en.Vaporeon_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "vaporeon":
                pokeansi.vaporeon_image()
                pokemons_en.Vaporeon_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "135":
                pokeansi.jolteon_image()
                pokemons_en.Jolteon_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "jolteon":
                pokeansi.jolteon_image()
                pokemons_en.Jolteon_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "136":
                pokeansi.flareon_image()
                pokemons_en.Flareon_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "flareon":
                pokeansi.flareon_image()
                pokemons_en.Flareon_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "137":
                pokeansi.porygon_image()
                pokemons_en.Porygon_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "porygon":
                pokeansi.porygon_image()
                pokemons_en.Porygon_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "138":
                pokeansi.omanyte_image()
                pokemons_en.Omanyte_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "omanyte":
                pokeansi.omanyte_image()
                pokemons_en.Omanyte_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "139":
                pokeansi.omastar_image()
                pokemons_en.Omastar_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "omastar":
                pokeansi.omastar_image()
                pokemons_en.Omastar_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "140":
                pokeansi.kabuto_image()
                pokemons_en.Kabuto_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "kabuto":
                pokeansi.kabuto_image()
                pokemons_en.Kabuto_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "141":
                pokeansi.kabutops_image()
                pokemons_en.Kabutops_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "kabutops":
                pokeansi.kabutops_image()
                pokemons_en.Kabutops_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "142":
                pokeansi.aerodactyl_image()
                pokemons_en.Aerodactyl_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "aerodactyl":
                pokeansi.aerodactyl_image()
                pokemons_en.Aerodactyl_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "143":
                pokeansi.snorlax_image()
                pokemons_en.Snorlax_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "snorlax":
                pokeansi.snorlax_image()
                pokemons_en.Snorlax_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "144":
                pokeansi.articuno_image()
                pokemons_en.Articuno_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "articuno":
                pokeansi.articuno_image()
                pokemons_en.Articuno_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "145":
                pokeansi.zapdos_image()
                pokemons_en.Zapdos_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "zapdos":
                pokeansi.zapdos_image()
                pokemons_en.Zapdos_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "146":
                pokeansi.moltres_image()
                pokemons_en.Moltres_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "moltres":
                pokeansi.moltres_image()
                pokemons_en.Moltres_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "147":
                pokeansi.dratini_image()
                pokemons_en.Dratini_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "dratini":
                pokeansi.dratini_image()
                pokemons_en.Dratini_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "148":
                pokeansi.dragonair_image()
                pokemons_en.Dragonair_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "dragonair":
                pokeansi.dragonair_image()
                pokemons_en.Dragonair_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "149":
                pokeansi.dragonite_image()
                pokemons_en.Dragonite_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "dragonite":
                pokeansi.dragonite_image()
                pokemons_en.Dragonite_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "150":
                pokeansi.mewtwo_image()
                pokemons_en.Mewtwo_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "mewtwo":
                pokeansi.mewtwo_image()
                pokemons_en.Mewtwo_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "151":
                pokeansi.mew_image()
                pokemons_en.Mew_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            elif pokemon_desejado == "mew":
                pokeansi.mew_image()
                pokemons_en.Mew_en.show_pokemon()
                input("\n\nPress \"enter\" to continue.")
 
            else:
                print("\n\n**** Pokemon not found or invalid command ****")
                input("\n\nPress \"enter\" to continue.")





    else:
        print("\n\n**** Resposta inválida / Invalid answer ****")
        continue