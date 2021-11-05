while True: 
    import os

    print(" ")
    print(" ")
    print("KABUL: Afganistan.")
    print(" ")
    print("Trucks die normaal werden gebruikt om vuilnis op halen, rijden nu propvol politieagenten, ambtenaren en andere mannen in uniform de stad uit. Toen je bijna bij werk was word je gebeldt door je Baas vanuit een restaurant op het internationale kamp 'Ga terug naar huis, Kabul is gevallen'.")
    print(" ")
    print("Nog geen tien minuten later is de stad gevuld met TalibanMannen met lange haren en baarden: ze zijn overal. In hun ene hand een geweer, in de andere een zweep.Iedereen word geslagen. Mannen, vrouwen en kinderen. In shock kwam je aan bij jou flat.Daar word net een bewoner naar buiten gesleurd. “Het komt goed”, roept de man naar zijn kinderen, die huilen en schreeuwen.Maar de Taliban schoten de man dood. Midden op straat, voor de ogen van zijn familie en ons allemaal.")
    print(" ")
    print(" ")
    print("Die avond hoor je van De Nederlandse Ambasade dat ze bij het vliegveld mensen evaccueren.")
    print(" ")
# 1
    print("Wat ga je doen?")
    Vraag1=input("a Thuis Blijven. B Vluchten\n")
    print(" ")
    if (Vraag1 =="a"):
# 7_______________________________bc____________bc_______________b_______________b_______________b______________ > ||~|| <

        print("Je besluit je te verstoppen. voor je zijn de inklapladder naar het dak en de keuken.")
        print("waar ga je je verstoppen?")
        Vraag7=input("A de keuken B op het dak\n")
        print(" ")
# 7A
        if (Vraag7 =="a"):
            print("je gaat in een van de keukenkastjes zitten en wacht to de chaos voorbij gaat. Je hoort  3 talibanen de deur intrappen en binnen komen, ze doorzoeken je huis en gooien alles overhoop. Ze vinden je en excuteren je onmiddellijk.")
            f1=input(" ")
            if (f1 ==""):
                os.system('cls')
                input("[ FAIL ]")
# 7b
        elif (Vraag7 =="b"):
            print("je klimt de ladder op en gaat stil op het dak liggen. Je hoort 3 mannen binnen stormen en je huis overhoop gooien. Na 4 minuten Hoor je niets meer dus besluit je naar beneden te gaan.")
# 8
            print("je besluit dat je hier weg moet maar je auto is kapotgemaakt. Waar ga je heen?")
            Vraag8=input("A steegje B weg\n")
            print(" ")
# 8A
# Toekomst 4
            if (Vraag8 =="a"):
                print("je rent door de steegjes heen om te ontkomen van de taliban,  maar dan loopt het steegje  dood. Je hoort geschreeuw en opeens staan er 4 soldaten voor je. Je word meegenomen naar de gevangenis.")
                print(" ")
                print("Nu zit je vast in de gevangenis voor de rest van je leven.")
                print(" ")
                f1=input(" ")
                if (f1 ==""):
                    os.system('cls')
                    input("( BAD ENDING )")
# 8b
            elif (Vraag8 =="b"):
                print("Je gaat naar de weg vol met taliban soldaten en word neergeschoten.")
                f1=input(" ")
                if (f1 ==""):
                    os.system('cls')
                    input("[ FAIL ]")
#__________________________________A__________________A__________________A________________A_________________A_______________A___________\\\
## 1B
    elif (Vraag1 =="b"):
# 2
        print("hoe wil je vluchten?")
        Vraag2=input("A auto B op voet\n")
        print(" ")
# 2A
        if (Vraag2 =="a"):
            print("je pakt je auto en gaat richting het vliegveld, Onderweg zie je de chaos die daar wwas uitgebroken. Na 12 uur proberen was je geen stap dichterbij en dus ga je terug naar huis. je wilde je opties overwegen, maar er is geen tijd. Je huisbaas belde; de Taliban waren langs geweest met een lijst en mijn naam stond erop. “Ga nu weg, want ze komen je halen”, waarschuwde hij.")
            print("Maar waar kon ik heen?  denk je, Mijn familie heeft me al lang geleden in de steek gelaten. Vrienden en kennissen durven niet te helpen of zijn zelf ook op de vlucht. Uiteindelijk boden wat onbekenden je een nacht onderdak aan")
            print(" ")


# 3
            print("waar ga je heen?")
            Vraag3=input("A Het huis, B door reizen\n")
            print(" ")
# 3A
            if (Vraag3 =="a"):
                print("je loopt naar het huis en klopt aan, na een tijdje gaat de deur open en je vraagt of je hier mag blijven. Ze twijfelden maar het antwoord was ja")
                print(" ")
                print("de volgende ochtend is de groep mensen al vertrokken je kijkt in de horizon en ziet een groep mensen en een boot aankomen. Je vind ook een auto die een lege tank heeft")
                print(" ")
# 4
                print("wat ga je doen?")
                Vraag4=input("A Naar het vliegveld lopen B de auto fixen\n")
                print(" ")
# 4b
                if (Vraag4 =="b"):
                    print("net als je klaar bent word het huis ingevallen door de Taliban en word je ontvoerd")
                    f1=input(" ")
                    if (f1 ==""):
                        os.system('cls')
                        input("[ FAIL ]")
# 4A
                elif (Vraag4 =="a"):
                    print("je verlaat het huis loopt naar het vliegveld als je bijna over een heuvel bent zie je dat het huis Word overgenomen door de Taliban.  je ziet een haven, en een groep mensen het riool in gaan.")
# 5
                    print("waar ga je heen?")
                    Vraag5=input("A Groep met boot B Vliegveld\n")
                    print(" ")
# 5a
                    if (Vraag5 =="a"):
                        print("je rend naar de boot en schreeuwt: wacht op mij!!. je haalt het nog net")
                        print(" ")
# Toekomst 1
                        print("toen de boot aankwam in nederland werd je doorgestuurd naar een asielzoeker kamp. na 3 jaar wachten hoor je van de gemeente dat je in nederland mag blijven.")
                        os.system('cls')
                        input("( ENDING boot )")
# 5b
                    elif (Vraag5 =="b"):
                        print("je besluit om opnieuw naar het vliegveld te gaan. Naar instructie van de Nederlandse ambassade doe je een oranje sjaal om en loopt tot je knieën het open riool in. Daar moest je, tussen honderden anderen, de aandacht zien te trekken van een Nederlandse soldaat. We waren wanhopig, angstig en gedroegen ons als wilden. Urenlang schreeuw je jouw longen kapot. Totdat een Nederlandse soldaat, met een oranje baard, je ziet.")
                        print(" ")
# Toekomst 2
                        print("toen je gevonden werd, werd je meteen in een vliegtuig naar Nederland gevlogen. toen je lande, werd je opgevangen in een vluchtelingenkamp waar je zal blijven voor een paar jaar")
                        os.system('cls')
                        input("ENDING vliegtuig")
# 3b_____
            elif (Vraag3 =="b"):
                print("je besluit door te lopen naar het vliegveld. Het is nu nacht en je kan niet ver zien, na 4 uur lopen val je in slaap op het koude zand. De volgende ochted schrik je wakker en kijkt om je heen. In de verte zie je een groep mensen en een stad, of wat er van over is.")
                print(" ")
# 6
                print("waar ga je heen?")
                Vraag6=input("A groep mensen, B stad\n")
# 6a
                if (Vraag6 =="a"):
                    print("je besluit om opnieuw naar het vliegveld te gaan. Naar instructie van de Nederlandse ambassade doe je een oranje sjaal om en loopt tot je knieën het open riool in. Daar moest je, tussen honderden anderen, de aandacht zien te trekken van een Nederlandse soldaat. We waren wanhopig, angstig en gedroegen ons als wilden. Urenlang schreeuw je jouw longen kapot. Totdat een Nederlandse soldaat, met een oranje baard, je ziet.")
                    print(" ")
# Toekomst 2
                    print("Toen je gevonden werd, werd je meteen in een vliegtuig naar Nederland gevlogen. toen je lande, werd je opgevangen in een vluchtelingenkamp waar je zal blijven voor een paar jaar")
                    f1=input(" ")
                    if (f1 ==""):
                        os.system('cls')
                        input("( ENDING VLIEGTUIG )")
# 6b
                elif (Vraag6 =="b"):
                    print("je gaat naar de verwoeste stad. Na wat rondlopen vind je een haven met een kleine speedboot.")
                    print(" ")
# Toekomst 3
                    print("Toen je aankwam in de nederlandse haven ging je naar de politie, die je naar een asiel centrum stuurt na 2 Maanden wachten hoor je van de gemeente dat je in Nederland mag blijven.")
                    f1=input(" ")
                    if (f1 ==""):
                        os.system('cls')
                        input("( SURVIVOR ENDING )")
####################______________________________________________________________#__________________________________________________________ > ~ < 
# 2b
        elif (Vraag2 =="b"):
            print("je rent zo hard als je kan door de steegjes totdat je het dorp uitbent.  het is nu donker buiten dus moet je een plek vinden om te overnachten. Je ziet een huis met het licht aan.")

# 3
            print("waar ga je heen?")
            Vraag3=input("A Het huis, B door reizen\n")
            print(" ")
# 3A
            if (Vraag3 =="a"):
                print("je loopt naar het huis en klopt aan, na een tijdje gaat de deur open en je vraagt of je hier mag blijven. Ze twijfelden maar het antwoord was ja")
                print(" ")
                print("de volgende ochtend is de groep mensen al vertrokken je kijkt in de horizon en ziet een groep mensen en een boot aankomen. Je vind ook een auto die een lege tank heeft")
                print(" ")
# 4
                print("wat ga je doen?")
                Vraag4=input("A Naar het vliegveld lopen B de auto fixen\n")
                print(" ")
# 4b
                if (Vraag4 =="b"):
                    print("net als je klaar bent word het huis ingevallen door de Taliban en word je ontvoerd")
                    f1=input(" ")
                    if (f1 ==""):
                        os.system('cls')
                        input("[ FAIL ]")
# 4A
                elif (Vraag4 =="a"):
                    print("je verlaat het huis loopt naar het vliegveld als je bijna over een heuvel bent zie je dat het huis Word overgenomen door de Taliban.  je ziet een haven, en een groep mensen het riool in gaan.")
# 5
                    print("waar ga je heen?")
                    Vraag5=input("A Groep met boot B Vliegveld\n")
                    print(" ")
# 5a
                    if (Vraag5 =="a"):
                        print("je rend naar de boot en schreeuwt: wacht op mij!!. je haalt het nog net")
                        print(" ")
# Toekomst 1
                        print("Toen de boot aankwam in nederland werd je doorgestuurd naar een asielzoeker kamp. na 3 jaar wachten hoor je van de gemeente dat je in nederland mag blijven.")
                        os.system('cls')
                        input("( ENDING boot )")
# 5b
                    elif (Vraag5 =="b"):
                        print("je besluit om opnieuw naar het vliegveld te gaan. Naar instructie van de Nederlandse ambassade doe je een oranje sjaal om en loopt tot je knieën het open riool in. Daar moest je, tussen honderden anderen, de aandacht zien te trekken van een Nederlandse soldaat. We waren wanhopig, angstig en gedroegen ons als wilden. Urenlang schreeuw je jouw longen kapot. Totdat een Nederlandse soldaat, met een oranje baard, je ziet.")
                        print(" ")
# Toekomst 2
                        print("toen je gevonden werd, werd je meteen in een vliegtuig naar Nederland gevlogen. toen je lande, werd je opgevangen in een vluchtelingenkamp waar je zal blijven voor een paar jaar")
                        os.system('cls')
                        input("ENDING vliegtuig")
# 3b_____
            elif (Vraag3 =="b"):
                print("je besluit door te lopen naar het vliegveld. Het is nu nacht en je kan niet ver zien, na 4 uur lopen val je in slaap op het koude zand. De volgende ochted schrik je wakker en kijkt om je heen. In de verte zie je een groep mensen en een stad, of wat er van over is.")
                print(" ")
# 6
                print("waar ga je heen?")
                Vraag6=input("A groep mensen, B stad\n")
# 6a
                if (Vraag6 =="a"):
                    print("je besluit om opnieuw naar het vliegveld te gaan. Naar instructie van de Nederlandse ambassade doe je een oranje sjaal om en loopt tot je knieën het open riool in. Daar moest je, tussen honderden anderen, de aandacht zien te trekken van een Nederlandse soldaat. We waren wanhopig, angstig en gedroegen ons als wilden. Urenlang schreeuw je jouw longen kapot. Totdat een Nederlandse soldaat, met een oranje baard, je ziet.")
                    print(" ")
# Toekomst 2
                    print("Toen je gevonden werd, werd je meteen in een vliegtuig naar Nederland gevlogen. toen je lande, werd je opgevangen in een vluchtelingenkamp waar je zal blijven voor een paar jaar")
                    f1=input(" ")
                    if (f1 ==""):
                        os.system('cls')
                        input("( ENDING VLIEGTUIG )")
# 6b
                elif (Vraag6 =="b"):
                    print("je gaat naar de verwoeste stad. Na wat rondlopen vind je een haven met een kleine speedboot.")
                    print(" ")
# Toekomst 3
                    print("Toen je aankwam in de nederlandse haven ging je naar de politie, die je naar een asiel centrum stuurt na 2 Maanden wachten hoor je van de gemeente dat je in Nederland mag blijven.")
                    f1=input(" ")
                    if (f1 ==""):
                        os.system('cls')
                        input("( SURVIVOR ENDING )")