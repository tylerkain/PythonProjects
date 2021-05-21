PlaceHolder = "[name]"

with open("./Mail Merge Project Start/Input/Names/names.txt") as names_file:
    names = names_file.readlines()

with open("./Mail Merge Project Start/Input/Letters/startingletter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PlaceHolder, stripped_name)
        with open(f"./Mail Merge Project Start/Output/ReadyToSend/letter_for{stripped_name}.txt", mode='w') as completed_leter:
            completed_leter.write(new_letter)





