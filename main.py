from replit import clear
import random
import hangman_art
import hangman_words

print(hangman_art.logo)
print("Welcome to Hangman!")

end_of_game = False
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
lives = 6

display = []
for _ in range(word_length):
  display += "_"
  
while not end_of_game:
  guess = input("Guess a letter:\n").lower()

  clear()
  
  if guess in display:
    print(f"Psst, you have already guessed the letter {guess}. Try another letter.")
  for position in range(word_length):
    letter = chosen_word[position]
    if guess == letter:
      display[position] = letter
    
  if guess not in chosen_word:
    lives -= 1
    print(f"{guess} is not in the word so you lose a life. You now have {lives} life left.")
    if lives == 0:
      end_of_game = True
      print(f"You lose...the word was {chosen_word}")
    
  print(f"{' '.join(display)}")
  
  if "_" not in display:
    print("You win!")
  print(hangman_art.stages[lives])