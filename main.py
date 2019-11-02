culprit = []

with open("dna.txt", "r") as dna_file:
    dna = dna_file.read()

gender = {"female": "TGAAGGACCTTC", "male": "TGCAGGAACTTC"}
race = {"white": "AAAACCTCA", "black": "CGACTACAG", "asian": "CGCGGGCCG"}
hair_color = {"black": "CCAGCAATCGC", "brown": "GCCAGTGCCG", "blonde": "TTAGCTATCGC"}
eye_color = {"blue": "TTGTGGTGGC", "green": "GGGAGGTGGC", "brown": "AAGTAGTGAC"}
facial_shape = {"square": "GCCACGG", "round": "ACCACAA", "oval": "AGGCCTCA"}

suspects = {"Eva": ["female", "white", "blonde", "blue", "oval"],
            "Larisa": ["female", "white", "brown", "brown", "oval"],
            "Matej": ["male", "white", "black", "blue", "oval"],
            "Miha": ["male", "white", "brown", "green", "square"]
            }

for ch in gender:
    if gender[ch] in dna:
        culprit.append(ch)

for ch in race:
    if race[ch] in dna:
        culprit.append(ch)

for ch in hair_color:
    if hair_color[ch] in dna:
        culprit.append(ch)

for ch in eye_color:
    if eye_color[ch] in dna:
        culprit.append(ch)

for ch in facial_shape:
    if facial_shape[ch] in dna:
        culprit.append(ch)

for s in suspects:
    if suspects[s] == culprit:
        print("The culprit is " + str(s))

        break
