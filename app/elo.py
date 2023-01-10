# r1 winning, r2 losing
def calculate_elo(r1, r2):
    return 1 / (1 + pow(10, (r2 - r1)/400))
