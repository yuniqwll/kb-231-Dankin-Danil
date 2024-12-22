import random

def play_rps():
    options = ["stone", "scissor", "paper"]
    user_choice = input("Введіть свій вибір (stone, scissor, paper): ").lower()
    
    if user_choice not in options:
        print("Некоректний вибір. Спробуйте ще раз.")
        return

    computer_choice = random.choice(options)
    print(f"Вибір комп'ютера: {computer_choice}")

    if user_choice == computer_choice:
        print("Нічия!")
    elif (user_choice == "stone" and computer_choice == "scissor") or \
         (user_choice == "scissor" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "stone"):
        print("Ви виграли!")
    else:
        print("Комп'ютер виграв!")

play_rps()
