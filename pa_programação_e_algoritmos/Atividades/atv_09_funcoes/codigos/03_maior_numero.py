from functions import find_max


def maior_numero():
    nums = []

    for i in range(3):
        nums.append(int(input(f"Digite o {i + 1} número: ")))

    print("O maior número é: ", find_max(nums))
