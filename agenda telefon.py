agenda = {
    1: {'nume': 'Nichole Harvey', 'telefon': '(777) 990-2479'},
    2: {'nume': 'Dan Williamson', 'telefon': '(534) 214-4557'},
    3: {'nume': 'Dusty Riley', 'telefon': '(263) 858-2390'},
    4: {'nume': 'Jill Valenzuela', 'telefon': '(509) 903-6512'},
    5: {'nume': 'Elisha Nixon', 'telefon': '(387) 536-9452'},
    6: {'nume': 'Cristina Dickerson', 'telefon': '(765) 470-3473'},
    7: {'nume': 'Catalina Hernandez', 'telefon': '(224) 940-1341'},
    8: {'nume': 'Alexander Neal', 'telefon': '(512) 226-7509'},
    9: {'nume': 'Janis Henry', 'telefon': '(526) 660-7907'},
    10: {'nume': 'Tami Arnold', 'telefon': '(708) 316-2669'},
    11: {'nume': 'Noelle Hoover', 'telefon': '(927) 850-4249'},
    12: {'nume': 'Bryon Richmond', 'telefon': '(915) 443-8471'},
    13: {'nume': 'Carol Blackburn', 'telefon': '(520) 781-9533'},
    14: {'nume': 'Letitia Kirk', 'telefon': '(528) 601-8622'},
    15: {'nume': 'Stewart Harrell', 'telefon': '(296) 715-0018'},
    16: {'nume': 'Tina Ellis', 'telefon': '(851) 905-4546'},
    17: {'nume': 'Humberto Hubbard', 'telefon': '(277) 797-2766'},
    18: {'nume': 'Charity Compton', 'telefon': '(967) 326-3959'},
    19: {'nume': 'Scott Anderson', 'telefon': '(694) 297-6257'},
    20: {'nume': 'Von Knight', 'telefon': '(520) 348-4068'},
    21: {'nume': 'Dwight Fowler', 'telefon': '(337) 646-3170'},
    22: {'nume': 'Luann Briggs', 'telefon': '(725) 702-2235'},
    23: {'nume': 'Ramona Matthews', 'telefon': '(722) 532-3641'},
    24: {'nume': 'Natasha Curtis', 'telefon': '(412) 900-7767'},
    25: {'nume': 'Chi Brewer', 'telefon': '(686) 417-9336'},
    26: {'nume': 'Ada Alvarado', 'telefon': '(639) 811-1216'},
    27: {'nume': 'Christian Osborne', 'telefon': '(534) 506-1447'},
    28: {'nume': 'Brigitte Rivers', 'telefon': '(893) 386-8495'},
    29: {'nume': 'Morton Pham', 'telefon': '(584) 492-1357'},
    30: {'nume': 'Francis Shields', 'telefon': '(466) 485-7599'},
    31: {'nume': 'Abraham Wilkins', 'telefon': '(282) 447-9742'},
    32: {'nume': 'Angelique Willis', 'telefon': '(426) 487-1997'},
    33: {'nume': 'Christoper Kim', 'telefon': '(385) 818-6418'},
    34: {'nume': 'Blanca Wade', 'telefon': '(356) 885-2812'},
    35: {'nume': 'Austin Grimes', 'telefon': '(341) 995-7530'},
    36: {'nume': 'Donald Jacobs', 'telefon': '(482) 961-0948'},
    37: {'nume': 'Fabian Wells', 'telefon': '(921) 835-5378'},
    38: {'nume': 'Russ Humphrey', 'telefon': '(561) 918-0033'},
    39: {'nume': 'Callie Campbell', 'telefon': '(565) 503-4573'},
    40: {'nume': 'Winfred English', 'telefon': '(469) 394-1108'},
    41: {'nume': 'Sallie Perez', 'telefon': '(647) 897-8463'},
    42: {'nume': 'Kristopher Rasmussen', 'telefon': '(700) 366-1619'},
    43: {'nume': 'Robt Nash', 'telefon': '(692) 626-6228'},
    44: {'nume': 'Hugo Byrd', 'telefon': '(682) 236-7284'},
    45: {'nume': 'Otha Gray', 'telefon': '(388) 899-1849'},
    46: {'nume': 'Keenan Hood', 'telefon': '(625) 844-9236'},
    47: {'nume': 'Edwardo Swanson', 'telefon': '(289) 435-1974'},
    48: {'nume': 'Kris Taylor', 'telefon': '(308) 646-4040'},
    49: {'nume': 'Leonardo Trujillo', 'telefon': '(540) 884-3301'},
    50: {'nume': 'Oscar Murray', 'telefon': '(255) 754-7813'}
}

# for i in agenda:
#     print(agenda[i])
#     print(f'Numele persoanei este{agenda[i]["nume"]}, si numarul de telefon este {agenda[i]["telefon"]}')

meniu_principal =['1.agenda', '2.Cautare nume','3.Cautare numar','4.Iesire']

#lungime id +nume =30

id='ID  '
nume='Nume                  '
numar='Numar de telefon'

def linie_agenda(id,nume,telefon):
    if id < 10:
        linie=str(id)+'.    '+nume
    else:
        linie=str(id)+'.    '+nume
    linie +=(30-len(linie))*' '+telefon
    return linie

def strip_num(numar):
    return numar.replace('(','').replace(' )','').replace(' ','').replace('-','')

print('Bine ai venit in AgendaPython')

while True:
    for i in meniu_principal:
        print(i)
    try:
        optiune=int(input('Alege o optiune\n>'))
    except:
        print('Te rog alege un numar valid din lista.')
        continue
    if optiune not in range(1,len(meniu_principal)+1):
        print('Te rog alege un numar valid din lista.')
        continue

    elif optiune ==1:
        print('Agenda:')
        print(id+nume+numar)
        for i in agenda:
            print(linie_agenda(i, agenda[i]['nume'] , agenda[i]['telefon']))
        print('\n***** SFARSIT *****\n')

    elif optiune ==2:
        print('Scrie "Exit" pentru iesire.')
        print('Cautare dupa nume:')
        cauta_alpha=True
        while cauta_alpha:
            cautare = input('>')
            if cautare.isalpha() and not cautare.lower() == 'exti':
                print(f'Peroane gasite cu:"{cautare}"')
                print(id+nume+numar)
                for i in agenda:
                    if cautare.lower() in agenda[i]['nume'].lower():
                        print(linie_agenda(i,agenda[i]['nume'],agenda[i]['telefon']))
            elif cautare.lower() == 'exit':
                cauta_alpha = False
            else:
                print('Te rog cauta dupa nume:')

    elif optiune==3:
        print('Scrie "Exit" pentru iesire.')
        print('Cautare dupa numar:')
        cauta_alpha=True
        while cauta_alpha:
            cautare=input('>')
            if cautare.isnumeric() and not cautare.lower() == 'exit':
                print(f'Persoane gasite cu : "{cautare}"')
                print(id+nume+numar)
                for i in agenda:
                    if cautare in strip_num(agenda[i]['telefon']):
                        print(linie_agenda(i,agenda[i]['nume'], agenda[i]['telefon']))
            elif cautare.lower() == 'exit':
                cauta_alpha= False
            else:
                print('Te rog cauta dupa numar:')
    else:
        print('Programul s-a inchis')
        break



