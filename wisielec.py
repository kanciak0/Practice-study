import random



word_list = ['ankle', 'bones', 'microwave', 'spiral']
chosen_word=random.choice(word_list)
word_length = len(chosen_word)
number_of_lives=6

display = []
for x in range(word_length):
    display += "_"
end=False
while not end:
    guess = str.lower((input("Guess a letter")))
    print(display)
    for position in range(word_length):
        letter=chosen_word[position]
        if guess==letter:
            display[position]=guess
    if guess not in chosen_word:
        number_of_lives-= 1
        if number_of_lives == 0:
            end=True
            print("You have lost")
    print(number_of_lives)
    print(display)
    if "_" not in display:
        end=True
        print("Win")
