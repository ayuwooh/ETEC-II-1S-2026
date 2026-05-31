import random

num, guess, count = random.randint(1, 10), 0, 0

while count < 3:
    try:
        count += 1
        guess = int(input("Adivinhe um número entre 1 e 10! "))
        if guess == num:
            print("Você acertou! 🎉")
            break
        elif count == 3:
            print("Você perdeu 😿")
        elif guess > num:
            print("Você errou! O número é menor que seu palpite.")
        elif guess < num:
            print("Você errou! O número é maior que seu palpite.")
    except ValueError:
        print("Este não é um número 🥹")
