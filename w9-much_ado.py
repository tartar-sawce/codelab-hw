with open('much_ado.txt', 'r') as infile:
    play = infile.read()

# create variables to which we will add line and character counts.
Beatrice_lines = 0
Beatrice_length = 0
Benedick_lines = 0
Benedick_length = 0

# split the text into separate strings wherever there is a double empty line (\n\n) i.e. into individual dialogues.
for line in play.split("\n\n"):
    if line.startswith("BEATRICE"):
        Beatrice_lines += 1
        # ".strip" removes white space at the beginning and end of a string.
        # "-9" removes "BEATRICE./ BENEDICK." from the character count, so the character name isn't counted.
        Beatrice_length += len(line.strip())-9

    elif line.startswith("BENEDICK"):
        Benedick_lines += 1
        Benedick_length += len(line.strip())-9

print("Beatrice has " + str(Beatrice_lines) + " lines comprising " + str(Beatrice_length) + " characters, while Benedick has " + str(Benedick_lines) + " lines comprising " + str(Benedick_length) + " characters.")
        