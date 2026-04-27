import random

num, guess, count = random.randint(1, 10), 0, 0

while count < 3:
    try:
        count += 1
        guess = int(input(f"Adivinhe um número entre 1 e 10! "))
        if guess == num:
            print(f"Você acertou! 🎉")
            break
        elif count == 3:
            print(f"Você perdeu 😿")
        elif guess > num:
            print(f"Você errou! O número é menor que seu palpite.")
        elif guess < num:
            print(f"Você errou! O número é maior que seu palpite.")
    except ValueError:
        print(f"Este não é um número 🥹")
