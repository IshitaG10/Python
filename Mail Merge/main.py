PLACEHOLDER = "[name]"

with open("Mail Merge\Input\\Names\invited_names.txt") as names:
    name_list = names.readlines()

with open("Mail Merge\Input\Letters\starting_letter.txt") as letter:
    content = letter.read()
   
for name in name_list:
    stripped_name = name.strip()
    new_letter = content.replace(PLACEHOLDER,stripped_name)
    with open(f"Mail Merge\Output\ReadyToSend\letter_to_{stripped_name}",mode="w") as complete:
        complete.write(new_letter)