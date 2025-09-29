def give_hint(guess, number):
    if guess < number:
        return "Try higher"
    elif guess > number:
        return "Try lower"
    return "Correct!"