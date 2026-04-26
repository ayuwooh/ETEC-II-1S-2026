import random

num, guess, count = random.randint(1, 10), 0, 0

while count < 3:
    try:
        guess = int(input(f"Adivinhe um número entre 1 e 10! "))
        if count == 2 and guess != num:
            print(f"Você perdeu 😿")
            break
        elif guess > num and guess != num:
            print(f"Você errou! O número é menor que seu palpite.")
            count += 1
        elif guess < num and guess != num:
            print(f"Você errou! O número é maior que seu palpite.")
            count += 1
        else:
            if guess == num:
                print(f"Você acertou! 🎉")
                break
    except ValueError:
        print(f"Este não é um número 🥹")
