import os
#Huoneet sanakirjamuodossa
huoneet = {
    'Vankiselli': {
        'Kuvaus': 'Kylmä ja kostea vankiselli, muut vankisellit huoneessa ovat tyhjiä. Huoneen ovi on auki pohjoiseen.',
        'Syvempi kuvaus': 'Huoneessa on noin tusina pieniä sellejä, maassa on pieni heinästä tehty peti ja ämpäri tarpeille',
        'Suunnat': {'pohjoinen': 'Käytävä'},
        'Esineet': []
    },
    'Käytävä': {
        'Kuvaus': 'Pitkä käytävä, lännessä ja idässä on puiset ovet ja käytävän pohjoisessa on valoa. Läntisessä ovessa lukee "Varasto" ja itäisessä ovessa lukee "Parrakit" Lattialla näyttäisi olevan tukeva keppi',
        'Suunnat': {'etelä': 'Vankiselli', 'itä': 'Parrakit', 'länsi': 'Varasto', 'pohjoinen': 'Tyhjä käytävä'},
        'Esineet': ['Keppi']
    },
    'Varasto': {
        'Kuvaus': 'Melkein täysin tyhjätty varasto. Seinällä roikkuu vasara',
        'Suunnat': {'itä': 'Käytävä'},
        'Esineet': ['Vasara']
    },
    'Parrakit': {
        'Kuvaus': 'Parrakit ovat ränsistyneet. Lattian nurkassa lojuu miekka',
        'Syvempi kuvaus': 'Parrakit ovat ränsistyneet ja tavarat ovat sekaisin, paenneet vangit ovat selvästi kapinoineet ja tuhonnut vartijan varusteita. Lattian nurkassa lojuu yksittäinen miekka hieman ruosteisena mutta käyttökelpoisena.',
        'Suunnat': {'länsi': 'Käytävä'},
        'Esineet': ['Miekka']
    },
    'Tyhjä käytävä': {
        'Kuvaus': 'Pitkä tyhjä käytävä, ei näy mitään mielenkiintoista.',
        'Suunnat': {'etelä': 'Käytävä', 'pohjoinen': 'Vastaanottotila'},
        'Esineet': []
    },
    'Vastaanottotila': {
        'Kuvaus': 'Pieni vastaanottotila, jossa on pöytä, tuoli ja kirjahylly.',
        'Syvempi kuvaus': 'Pöydällä on vanha lamppu ja kirjahyllyssä on useita pölyisiä kirjoja. Kirjahyllyn alla on omituinen kaari jossa ei ole likaa tai pölyä, aivan kuin sitä olsi liikutettu äskettäin.',
        'Suunnat': {'etelä': 'Tyhjä käytävä', 'länsi': 'Luola Kirjahyllyn takana', 'itä': 'Vankilan aulahuone'},
        'Esineet': []
    },
    'Luola Kirjahyllyn takana': {
        'Kuvaus': 'Pimeä luola, jossa on outoja kalliomuodostelmia ja heikko valon kajastus kauempana.',
        'Syvempi kuvaus': 'Luola on osittain ihmisen tekemä ja osittain luonnollinen, joku on koittanu paeta täältä kauan.',
        'Suunnat': {'itä': 'Vastaanottotila', 'länsi': 'Syvä luola'},
        'Esineet': []
    },
    'Syvä luola': {
        'Kuvaus': 'luolan katossa on reikä linannan ulkopuolelle, josta valo tulee siään. Jos minulla olisi käyttä ja koukku voisin kiivetä ylös!',
        'Syvempi kuvaus': 'Luolan katossa on reikä, josta näkyy kirkas päivävalo. Ulkona näyttää olevan turvallista, mutta en pääse ylös ilman apuvälineitä.',
        'Suunnat': {'länsi': 'Luola Kirjahyllyn takana'},
        'Esineet': []
    },
    'Vankilan aulahuone': {
        'Kuvaus': 'Vankilan aulahuone, lännessä on vangit, idässä on keittiö, etelässä on ruokasali ja pohjoisessa käytävä eteenpäin.',
        'Syvempi kuvaus': 'Huone on suuri ja jakaa vankilan eri osiin. Kaikki hyödyllinen mitä huoneessa joskus saattoi olla on ryöstetty tai tuhottu.',
        'Suunnat': {'itä': 'Keittiö', 'länsi': 'Vastaanottotila', 'etelä': 'Ruokasali', 'pohjoinen': 'Välihuone'},
        'Esineet': []
    },
    'Keittiö': {
        'Kuvaus': 'Vankilan keittiö josta ruokittiin vangit ja vartijat.',
        'Syvempi kuvaus': 'Keittiö on suuri ja tilava, mutta kaikki keittiövälineet ovat joko rikki tai kadonneet. Lattialla on pala leipää joka on välttynyt kaaokselta.',
        'Suunnat': {'länsi': 'Vankilan aulahuone'},
        'Esineet': ['Leipä']
    },
    'Ruokasali': {
        'Kuvaus': 'Vankilan ruokasali, jossa on pitkät pöydät ja penkit.',
        'Syvempi kuvaus': 'Ruokasalissa on pitkät pöydät ja penkit, huone on aivan sekaisin ja näyttää selviä taistelun merkkejä. Huoneen nurkassa on yksi vartija kuolleena ja hänen vyöllänsä kimaltaa avain parrakkeihin.',
        'Suunnat': {'pohjoinen': 'Vankilan aulahuone'},
        'Esineet': ['Avain parrakeihin']
    },
    'Välihuone': {
        'Kuvaus': 'Välihuone, josta pääsee eteenpäin vankilan sisätiloihin. Ovi eteenpäin on lukittu vanhalla ruosteisella lukolla.',
        'Syvempi kuvaus': 'Ovi eteenpäin on lukittu vanhalla ruosteisella lukolla. Voisin käyttää jotain työkalua avatakseni sen.',
        'Suunnat': {'etelä': 'Vankilan aulahuone', 'pohjoinen': 'Valaistu huone'},
        'Esineet': []
    },
    'Valaistu huone': {
        'Kuvaus': 'Valaistu huone, jonka seinällä on kirkkaasti palavia seinälyhtyjä. Idässä on pieni sairaalahuone, pohjoisessa on kidutushuone ja lännessä on pilkkopimeä käytävä',
        'Syvempi kuvaus': 'Seinällä olevat lyhdyt valaisevat huoneen lämpimästi, voisin sytyttää soihdun näillä lyhdyillä.',
        'Suunnat': {'itä': 'Sairaalahuone', 'pohjoinen': 'Kidutushuone', 'länsi': 'Pimeä käytävä', 'etelä': 'Välihuone'},
        'Esineet': []
    },
    'Sairaalahuone': {
        'Kuvaus': 'Pieni sairaalahuone, jossa on vanha sairaalasänky ja lääkekaappi.',
        'syvempi kuvaus': 'Lääkekaapissa on vanhoja pulloja ja purkkeja, kaapeista löytyy steriili rätti joka tuoksuu alkoholille.',
        'Suunnat': {'länsi': 'Valaistu huone'},
        'Esineet': ['Rätti']
    },
    'Kidutushuone': {
        'Kuvaus': 'Kammottava kidutushuone, jossa on vanhoja kidutusvälineitä ja kahleita.',
        'Syvempi kuvaus': 'Huoneessa on vanhoja kidutusvälineitä, kuten piikkejä ja koukkuja. Yksi koukuista näyttää todella tukevalta.',
        'Suunnat': {'etelä': 'Valaistu huone'},
        'Esineet': ['Koukku']
    },
    'Pimeä käytävä': {
        'Kuvaus': 'Pilkkopimeä käytävä, soihtu valaisee vain vähän edessäni.',
        'Suunnat': {'itä': 'Valaistu huone', 'länsi': 'Pimeä huone'},
        'Esineet': []
    },
    'Pimeä huone': {
        'Kuvaus': 'Pilkkopimeä huone, soihtu antaa hieman valoa.',
        'Syvempi kuvaus': 'Soihdun valossa näen että etelästä pääsee sisäpihalle ja pohjoinen johtaa ulsokäynnille',
        'Suunnat': {'itä': 'Pimeä käytävä', 'pohjoinen': 'Uloskäynti', 'etelä': 'Sisäpiha'},
        'Esineet': []
    },
    'Sisäpiha': {
        'Kuvaus': 'Vankilan sisäpiha, jossa on korkeat muurit joiden takana on juoksuhauta. Keskellä pihaa on kaivo.',
        'Syvempi kuvaus': 'Kaivossa on köysi jota voisin käyttää, olisipa jotain jolla leikata köysi irti',
        'Suunnat': {'pohjoinen': 'Pimeä huone'},
        'Esineet': []
    },
    'Tyhjä Huone': {
        'Kuvaus': 'Tyhjä huone, joss ei näy mitään mielenkiintoista. Idässä on uloskäyntihuone',
        'Suunnat': {'etelä': 'Pimeä huone', 'itä': 'Uloskäynti'},
        'Esineet': []
    },
    'Uloskäynti': {
        'Kuvaus': 'Uloskäynti vankilasta, koitat ovea mutta se ei liikahda millään, täältä on pakko olla toinen reitti ulos!',
        'Suunnat': {'länsi': 'Pimeä huone'},
        'Esineet': []
    },
}

#itsestäänselvä lukitut ovet muuttuja
lukitut_ovet = { 
    ('Käytävä', 'itä'): True,
    ('Välihuone', 'pohjoinen'): True,
}

#Pelin aloitusasetukset ja pari muuta peliin liittyvää muuttujaa 
nykyinen_huone = 'Vankiselli'
tavarat = []
peli_päällä = True
leipa_syoty = False #Tyhmä funktionimi mutta en keksiny parempaa (tai myöskään parempaa paikkaa tälle muuttujalle)
soihtu_sytytetty = False
pisteet = 0

def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')

# Pelinäkymä funktio
def pelinäkymä():
    print("\n" + "-" * 50)
    print(f"SIJAINTI: {nykyinen_huone}")
    print(f"Kuvaus: {huoneet[nykyinen_huone]['Kuvaus']}")

    huoneen_esineet = [esine for esine in huoneet[nykyinen_huone]['Esineet']]
    if huoneen_esineet:
        print(f"\nTäällä olevat esineet: {', '.join(huoneen_esineet)}")

    menosuunnat = list(huoneet[nykyinen_huone]['Suunnat'].keys())
    print(f"Mahdolliset uloskäynnit: {', '.join(menosuunnat)}")
     
    tavaraluettelo = ', '.join(tavarat) if tavarat else 'tyhjä'
    print(f"Inventaario: [{tavaraluettelo}]")
    
# Liikkumisen käsittely funktio lukittu ovi ja kirjahylly käsitellään tässä koska esinettä ei käytetä suoraan
def käsittele_liikkuminen(suunta):
    global nykyinen_huone

    if suunta in huoneet[nykyinen_huone]['Suunnat']:
        
        ovi_avain = (nykyinen_huone, suunta)
        if ovi_avain in lukitut_ovet and lukitut_ovet[ovi_avain]:
           
            if ovi_avain == ('Käytävä', 'itä'):
                if 'Avain parrakeihin' in tavarat:
                    lukitut_ovet[ovi_avain] = False
                    print("Käytät 'Avain parrakeihin' ja avaat oven Parrakkeihin.")
                else:
                    print("Ovi on lukittu. Tarvitset 'Avain parrakeihin' päästäksesi sisään.")
                    return
            else:
                print("Ovi on lukittu. Et pääse siitä läpi.")
                return

        uusi_huone = huoneet[nykyinen_huone]['Suunnat'][suunta]

        if uusi_huone == 'Luola Kirjahyllyn takana' and not leipa_syoty:
            print("Olen liian nälkäinen liikuttaman isoa hyllyä,  jos saisin ensin jotain ruokaa...")
            return

        if 'pimeä' in uusi_huone.lower():
            if not soihtu_sytytetty:
                print("On liian pimeää päästä tähän huoneeseen. Sinun täytyy sytyttää soihtu ensin.")
                return
      
        nykyinen_huone = uusi_huone
    else:
        print(f"Et voi mennä tuohon suuntaan.")

# Esineen ottamisen käsittely funktio
def käsittele_esineen_ottaminen(esineen_nimi):
    global tavarat
    clear_screen()
    oikea_nimi = None
    for esine in huoneet[nykyinen_huone]['Esineet']:
        if esine.lower() == esineen_nimi.lower():
            oikea_nimi = esine
            break
    
    if oikea_nimi:
        tavarat.append(oikea_nimi)
        huoneet[nykyinen_huone]['Esineet'].remove(oikea_nimi)
        global pisteet
        pisteet += 5
    
    else:
        print(f"Esinettä {esineen_nimi} ei ole täällä.")

# Esineen pudottamisen käsittely funktio
def käsittele_esineen_pudottaminen(esineen_nimi):
    global tavarat
    clear_screen()  
    oikea_nimi = None
    for esine in tavarat:
        if esine.lower() == esineen_nimi.lower():
            oikea_nimi = esine
            break

    if not oikea_nimi:
        print(f"Sinulla ei ole {esineen_nimi} mukana.")
    else:
        tavarat.remove(oikea_nimi)
        huoneet[nykyinen_huone]['Esineet'].append(oikea_nimi)
        print(f"Pudotit esineen: {oikea_nimi}")

def käsittele_esineen_käyttö(esineen_nimi):
    oikea_nimi = None
    clear_screen() 
    for esine in tavarat:
        if esine.lower() == esineen_nimi.lower():
            oikea_nimi = esine
            break
    clear_screen()
    if not oikea_nimi:
        print(f"Sinulla ei ole {esineen_nimi} mukana.")
        return
   # Esineen 'Vasara' käyttö lukitun oven avaamiseen käsitellään tässä koska se ei ole suoraan liikkumiseen liittyvä komento
    if oikea_nimi.lower() == 'vasara':
        ovi_avain = (nykyinen_huone, 'pohjoinen')
        if ovi_avain in lukitut_ovet and lukitut_ovet[ovi_avain]:
            lukitut_ovet[ovi_avain] = False
            print("Iskit vasaralla lukkoa ja se hajoaa! Ovi on nyt auki.")
        else:
            print(f"Vasaran käyttö ei vaikuta tähän huoneeseen.")
        return

    if oikea_nimi.lower() == 'leipä':
        global leipa_syoty
        leipa_syoty = True
        tavarat.remove(oikea_nimi)
        print("Söit leipää. Tunnet olosi energisemmäksi!")
        return

    if oikea_nimi.lower() == 'soihtu':
        global soihtu_sytytetty
        if nykyinen_huone == 'Valaistu huone':
            soihtu_sytytetty = True
            print("Sytytit soihtusi seinäliekillä.")
        else:
            print("Et voi sytyttää soihtua täällä")
        return

    # Esineen 'Koukku köydessä' käyttö oikeassa huoneessa johtaa voitton joten tässä voiton koodi
    if oikea_nimi.lower() == 'koukku köydessä':
        if nykyinen_huone == 'Syvä luola':
            print("\n" + "=" * 50)
            print("VOITTO! Olet onnistunut pakenemaan vankilasta!")
            print("Kiipesit köyden avulla ulos luolasta vankilan ulkopuolelle.")
            print("Olet vapaa!")
            print("Pisteesi: ", pisteet)
            print("=" * 50)
            if pisteet >= 50: # Arvioidaan pelaajan suoritus pisteiden perusteella
                print("Onnittelut erinomaisesta suorituksesta! Käytit aktiivisesti katso komentoa ja olit kiinnostunut pelin maailmasta!")
            input("\nPaina Enter sulkeaksesi pelin...")
            global peli_päällä
            peli_päällä = False
        else:
            print("Et voi käyttää tuota tässä.")
        return

    if oikea_nimi.lower() == 'miekka':
        if nykyinen_huone == 'Sisäpiha':
            print("Käytät miekkaa leikataksesi köyden irti kaivosta.")
            tavarat.append('Köysi')
        else:
            print("Et voi käyttää miekkaa tässä.")
        return

    print(f"Et voi käyttää {oikea_nimi} tässä.")

# Esineiden yhdistämisen käsittely funktio
def käsittele_esineiden_yhdistäminen(esine1, esine2):
    global tavarat
    clear_screen() 

    oikea1 = None
    oikea2 = None
    for esine in tavarat:
        if esine.lower() == esine1.lower():
            oikea1 = esine
        if esine.lower() == esine2.lower():
            oikea2 = esine
    
    if not oikea1 or not oikea2:
        print(f"Sinulla ei ole molempia esineitä mukana.")
        return
    
    # Mahdolliset yhdistelyt huom mahdollisuudet molemmin päin
    yhdistelyt = {
        ('Keppi', 'Rätti'): 'Soihtu',
        ('Rätti', 'Keppi'): 'Soihtu',
        ('Koukku', 'Köysi'): 'Koukku köydessä',
        ('Köysi', 'Koukku'): 'Koukku köydessä',
    }
    
    yhdistelyt_avain = (oikea1, oikea2)
    if yhdistelyt_avain in yhdistelyt:
        uusi_esine = yhdistelyt[yhdistelyt_avain]
        tavarat.remove(oikea1)
        tavarat.remove(oikea2)
        tavarat.append(uusi_esine)
        print(f"Yhdistit {oikea1} ja {oikea2}! Sait: {uusi_esine}")
    else:
        print(f"Et voi yhdistää {oikea1} ja {oikea2}.")

# Huoneen katsomisen käsittely funktio
def käsittele_huoneen_katsominen():
    global pisteet
    clear_screen()
    if 'Syvempi kuvaus' in huoneet[nykyinen_huone]:
        print(huoneet[nykyinen_huone]['Syvempi kuvaus'])
    else:
        print("Ei lisätietoja tästä huoneesta.")
    pisteet += 1

# Peli pääfunktio
def pelin_pelaaminen():
    print("Tervetuloa seikkailupeliin!")
    print("Heräät vankisellistäsi, näit kamalaa painajaista vankilan sisällä tapahtuvasta kaaoksesta, kun olet kunnolla herännyt tajuat että sellisi ovi pohjoiseen on auki") 
    global peli_päällä
    peli_päällä = True

    while peli_päällä:
        pelinäkymä()
        komento = input("Mitä haluat tehdä? (mene/ota/katso/pudota/käytä/yhdistä/lopeta) ").strip().lower()
        # Komentojen käsittely
        if komento.startswith('mene'):
            osat = komento.split(' ')
            if len(osat) >= 2:
                suunta = ' '.join(osat[1:])
                käsittele_liikkuminen(suunta)
            else:
                print("Käytä: mene [suunta]")
            clear_screen()
        elif komento.startswith('ota'):
            osat = komento.split(' ')
            if len(osat) >= 2:
                esineen_nimi = ' '.join(osat[1:])
                käsittele_esineen_ottaminen(esineen_nimi)
            else:
                print("Käytä: ota [esine]")
        
        elif komento.startswith('käytä'):
            osat = komento.split(' ')
            if len(osat) >= 2:
                esineen_nimi = ' '.join(osat[1:])
                käsittele_esineen_käyttö(esineen_nimi)
            else:
                print("Käytä: käytä [esine]")
        
        elif komento.startswith('pudota'):
            osat = komento.split(' ')
            if len(osat) >= 2:
                esineen_nimi = ' '.join(osat[1:])
                käsittele_esineen_pudottaminen(esineen_nimi)
            else:
                print("Käytä: pudota [esine]")
        
        elif komento == 'katso':
            käsittele_huoneen_katsominen()
        
        elif komento.startswith('yhdistä'):
            osat = komento.split(' ')
            if len(osat) >= 3:
                esine1 = osat[1]
                esine2 = osat[2]
                käsittele_esineiden_yhdistäminen(esine1, esine2)
            else:
                print("Käytä: yhdistä [esine1] [esine2]")
        
        elif komento == 'lopeta':
            print("Lopetat pelin. Kiitos pelaamisesta!")
            peli_päällä = False
        
        else:
            print("Tuntematon komento. Yritä uudelleen.")


if __name__ == "__main__":
    pelin_pelaaminen()