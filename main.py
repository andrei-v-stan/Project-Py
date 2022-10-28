import re


def litere_dictionar(txt):
    txt = txt.upper()
    litere = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0,
              'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

    for chara in txt:
        if chara in litere:
            litere[chara] = litere[chara] + 1

    return litere


def litere_expresie_regulata(txt):
    txt = txt.lower()
    charaL = []
    charaL.extend(range(ord('a'), ord('z') + 1))

    for chara in charaL:
        print('\t', chr(chara - 32), len(re.findall(chr(chara), txt)))

    return 0


def check_text(txt):
    if total_litere(txt) == 0:
        print(" Litere = 0", '\n', "Cuvinte = 0", '\n', "Propoziti = 0", '\n')
        return 0

    else:
        return 1


# Se verifica daca functia total_litere() (functia care returneaza numarul de litere) este 0, daca da inseamna ca nu avem cum sa avem litere, cuvinte sau propozitii si atunci aceste functii de verificare nu se mai apeleaza (in main)


def nr_litera(txt, letter):
    txt = txt.lower()
    ct = 0

    for chara in txt:
        if chara == letter:
            ct = ct + 1

    return ct


# Se ia toate caracterele din fisier si se verifica daca se potrivesc cu litera data, daca caracterul prezent este aceasi cu litera data se creste ct (numarul de aparitii a unei litere)


def total_litere(txt):
    ct = 0
    charaL = []
    charaL.extend(range(ord('A'), ord('Z') + 1))
    charaL.extend(range(ord('a'), ord('z') + 1))

    for chara in txt:
        if ord(chara) in charaL:
            ct = ct + 1

    return ct


# Se ia toate caracterele din fisier si se verifica daca sunt litere, la fiecare litera gasita se creste ct (numarul total de litere)


def p_litere(txt):
    print("Litere: ")

    for i in range(ord('a'), ord('z') + 1):
        nrLetter = nr_litera(txt, chr(i))
        percentage = nr_litera(txt, chr(i)) / (total_litere(txt) / 100)
        # Or : import math   percentage = math.trunc(percentage)
        print('\t', chr(i - 32), '=', nrLetter, ' (%.2f' % percentage, '%)')

    print('\n', "Parcurgere doar odata a literelor folosind un dictionar :", '\n', litere_dictionar(txt))
    print('\n', "Parcurgere folosind expresii regulate :")
    litere_expresie_regulata(txt)

    return 0


# Se iau toate literele, se apeleaza functia nr_litera si apoi in functie de rezultat se face un procentaj de aparitie a literei respective (impartim numarul de aparitii a literei la 1% din numarul total de litere)


def n_cuvinte(txt):
    ct = 0
    charaL = []
    charaL.extend(range(ord('A'), ord('Z') + 1))
    charaL.extend(range(ord('a'), ord('z') + 1))

    chara1 = [' ', ',', ':', chr(10)]
    chara2 = [chr(34), chr(39), '(', '[', '{']
    chara3 = [' ', chr(10)]
    charaX = ['.', ',', '!', '?', ':', ';', ' ', ')', ']', '}', chr(34), chr(39), chr(10)]

    for i in range(0, len(txt) - 1):
        if ord(txt[i]) in charaL and (
                i == 0 or (txt[i - 1] in chara1 or (txt[i - 1] in chara2 and (txt[i - 2] in chara3)))):
            while ord(txt[i + 1]) in charaL:
                i = i + 1
            if txt[i + 1] in charaX:
                ct = ct + 1

    if ord(txt[len(txt) - 1]) in charaL:
        ct = ct + 1

    # Or : ct = len(txt.split())    # However it counts numbers as words as well.
    return ct


# Se iau toate caracterele din text, se verifica daca s-a ajuns la o litera, apoi se verifica daca inaintea literei era un caracter aceptabil (begining of file, chara1 sau chara2), apoi se trece prin text pana ce da de un caracter non-litera.
# Odata ce se da de un caracter non-litera se verifica daca e o incheiere acceptabila de cuvant (charaX), daca da se adauga la contor. La final se cauta de un caz exceptie (fisierul se incheie intr-o litera), daca da se adauga la contor.


def p_cuvinte(txt):
    print("Cuvinte =", n_cuvinte(txt))
    return 0


def n_propozitii(txt):
    ct = 0
    charaL = []
    charaL.extend(range(ord('A'), ord('Z') + 1))
    charaL.extend(range(ord('a'), ord('z') + 1))
    charaL.extend(range(ord('0'), ord('9') + 1))
    charaX = ['.', '!', '?']
    # TODO expresii regulate?

    for i in range(0, len(txt)):
        if ord(txt[i - 1]) in charaL and (txt[i] in charaX or txt[i] == chr(10)):
            ct = ct + 1

    if txt[len(txt) - 1] not in charaX:
        ct = ct + 1

    if txt[len(txt) - 1] == chr(10):
        ct = ct - 1

    # Or : ct = txt.count('.')    # However it just counts the number of periods
    return ct


# Se verifica daca caracterul precedent este fie o litera fie un numar, apoi se verifica daca caracterul curent este unul ce incheie o propozitie (. ? ! \n), daca da se adauga la contor.
# Deasemenea se verifica daca ultimul caracter din text nu este unul ce incheie o propozitie (. ? ! \n), daca nu se adauga la contor. Si se mai verifica daca ultimul caracter este \n, daca da se elimina din contor pentru ca este un caz de exceptie.


def p_propozitii(txt):
    print("Propozitii =", n_propozitii(txt))
    return 0


def n_cnp(txt):
    ct = 0
    i = 0
    cod = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    code = 0
    nCod = []

    charaNr = []
    charaNr.extend(range(ord('0'), ord('9') + 1))

    for i in range(0, len(txt)):
        if ct < 13 and ord(txt[i]) in charaNr:
            cod[ct] = int(txt[i])
            ct = ct + 1

        elif ct == 13 and (txt[i] < '0' or txt[i] > '9'):
            leapY = cod[1] * 10 + cod[2]
            nDays = cod[5] * 10 + cod[6]
            codeJud = cod[7] * 10 + cod[8]
            codeDay = cod[9] * 100 + cod[10] * 10 + cod[11]
            codeDigit = cod[0] * 2 + cod[1] * 7 + cod[2] * 9 + cod[3] * 1 + cod[4] * 4 + cod[5] * 6 + cod[6] * 3 + cod[
                7] * 5 + cod[8] * 8 + cod[9] * 2 + cod[10] * 7 + cod[11] * 9

            codAn = []
            codAn.extend(range(1, 8 + 1))
            codJud = []
            codJud.extend(range(1, 48 + 1))
            codDay = []
            codDay.extend(range(1, 999 + 1))

            cod31Days04 = [1, 3, 5, 7, 9]
            cod31Days14 = [0, 2]
            cod30Days04 = [4, 6, 9]

            nDays29 = []
            nDays29.extend(range(1, 29 + 1))
            nDays28 = []
            nDays28.extend(range(1, 28 + 1))
            nDays30 = []
            nDays30.extend(range(1, 30 + 1))
            nDays31 = []
            nDays31.extend(range(1, 31 + 1))

            if cod[0] in codAn and codeJud in codJud and codeDigit % 11 == cod[12] and codeDay in codDay and ((cod[
                                                                                                                   3] == 0 and
                                                                                                               cod[
                                                                                                                   4] == 2 and (
                                                                                                                       (
                                                                                                                               leapY % 4 == 0 and nDays in nDays29) or (
                                                                                                                               nDays in nDays28))) or nDays in nDays31 and (
                                                                                                                      (
                                                                                                                              cod[
                                                                                                                                  3] == 0 and
                                                                                                                              cod[
                                                                                                                                  4] in cod31Days04) or (
                                                                                                                              cod[
                                                                                                                                  3] == 1 and
                                                                                                                              cod[
                                                                                                                                  4] in cod31Days14)) or nDays in nDays30 and (
                                                                                                                      (
                                                                                                                              cod[
                                                                                                                                  3] == 0 and
                                                                                                                              cod[
                                                                                                                                  4] in cod30Days04) or (
                                                                                                                              cod[
                                                                                                                                  3] == 1 and
                                                                                                                              cod[
                                                                                                                                  4] == 1))):
                for j in range(0, 13):
                    code = code * 10 + cod[j]
                nCod.append(code)
                code = 0

            cod = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ct = 0

        else:
            cod = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ct = 0

    if not nCod:
        return 0

    for i in range(0, len(nCod)):
        i = i + 1

    count = i
    ct = i
    for i in range(0, count):
        for j in range(i + 1, count):
            if nCod[i] == nCod[j] and nCod[i] != 0:
                nCod[j] = 0
                ct = ct - 1

    s = "".join((str(ct), " ["))

    for i in range(0, count):
        if nCod[i] != 0:
            s = "".join((s, str(nCod[i])))
            s = "".join((s, ","))

    s = s[:-1]
    s = "".join((s, "]"))

    return s


# Se trece prin fisier, odata ce se intalneste un caracter numar se verifica daca acel numar este format din 13 caractere numerice, daca da atunci se verifica validitatea codului CNP
# Se verifica validitatea astefel : Primul caracter (0) trebuie sa fie un numar intre 1 si 8; Daca caracterul 1 si 2 formeaza un numar ce da %4 = 0 atunci inseamna ca este Leap Year, asadar se verifica daca caracterul 3 si 4 formeaza numarul 02 si se verifica daca caracterul 5 si 6 formeaza un numar intre 1 si 29
# Apoi daca caracterul 1 si 2 nu formeaza un numar ce da %4 = 0 atunci pe scurt se verifica daca numarul de zile (caracterul 5 si 6) corespunde conform luniilor (caracterul 3 si 4)
# Dupa acestea se verifica daca caracterele 7 si 8 formeaza un numar intre 1 si 48, iar apoi se verifica daca caracterele 9,10,11 formeaza un numar intre 1 si 99. In final se verifica daca caracterul 12 este conform formulei.
# La urma, daca este un CNP valid se adauga in lista si apoi se verifica lista de repetitii inainte de returnare.


def p_cnp(txt):
    print("CNP(uri) =", n_cnp(txt))
    return 0


def n_telefoane(txt):
    ct = 0
    i = 0
    cod = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    code = 0
    nCod = []
    charaNr = []
    charaNr.extend(range(ord('0'), ord('9') + 1))

    for i in range(0, len(txt)):

        if ct < 10 and ord(txt[i]) in charaNr:
            cod[ct] = int(txt[i])
            ct = ct + 1

        elif ct == 10 and (txt[i + 1] < '0' or txt[i + 1] > '9'):
            if cod[0] == 0 and cod[1] == 7:
                for j in range(0, 10):
                    code = code * 10 + cod[j]
                nCod.append(code)
                code = 0

            cod = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ct = 0

        else:
            cod = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ct = 0

    if not nCod:
        return 0

    for i in range(0, len(nCod)):
        i = i + 1

    count = i
    ct = i
    for i in range(0, count):
        for j in range(i + 1, count):
            if nCod[i] == nCod[j] and nCod[i] != 0:
                nCod[j] = 0
                ct = ct - 1

    s = "".join((str(ct), " ["))

    for i in range(0, count):
        if nCod[i] != 0:
            s = "".join((s, str(0)))
            s = "".join((s, str(nCod[i])))
            s = "".join((s, ","))

    s = s[:-1]
    s = "".join((s, "]"))

    return s


# Similar dupa CNP, se merge prin fisier pana ce se gaseste un caracter numar, apoi se verifica daca acel numar este din 10 caractere numerice, daca da se verifica dac caracterul 0 si 1 formeaza un numar 07
# Daca este un numar de telefon valid se adauga in lista si apoi se verifica lista de repetitii inainte de returnare


def telefoane_expresie_regulata(txt):
    lTelefoane = re.findall(r'\b07\w\d{7}', txt)

    return lTelefoane


def p_telefoane(txt):
    print("Telefoane =", n_telefoane(txt))
    print("Telefoane (expresii regulate) :", len(set(telefoane_expresie_regulata(txt))), set(telefoane_expresie_regulata(txt)))

    return 0


if __name__ == '__main__':
    path = input("Enter the file's path: ")
    file = open(path, "r")
    ftxt = file.read()

    if check_text(ftxt) == 0:
        p_cnp(ftxt)
        p_telefoane(ftxt)

    elif check_text(ftxt) == 1:
        p_cuvinte(ftxt)
        p_propozitii(ftxt)
        p_cnp(ftxt)
        p_telefoane(ftxt)
        p_litere(ftxt)

    #  prompt=input('\n\n\nPress Enter to exit...')
