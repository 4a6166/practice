import numpy as np
import pandas as pd

# pd.set_option('display.float_format', lambda x: '%{0:,.2f}'.format(int(x)))

# If a player hits on a single in an American game, that player wins 35 times the bet

frenchWheel = ['0', '32', '15', '19', '4', '23', '2', '25', '17', '34', '6', '27', '13', '36', '11', '30', '8', '23', '10', '5', '24', '16', '33', '1', '20', '14', '31', '9', '22', '18', '29', '7', '28', '12', '35', '3', '26']
americanWheel = ['0', '28', '9', '26', '30', '11', '7', '20', '32', '17', '5', '22', '34', '15', '3', '24', '36', '13', '1', '00', '27', '10', '25', '29', '12', '8', '19', '31', '18', '6', '21', '33', '16', '4', '23', '35', '14', '2']
sandsWheel = ['0', '000', '00', '32', '15', '19', '4', '21', '2', '25', '17', '34', '6', '27', '13', '36', '11', '30', '8', '23', '10', '5', '24', '16', '33', '1', '20', '14', '31', '9', '22', '18', '29', '7', '28', '12', '35', '3', '26']

payouts = [  # Bet, Winning Spaces, Payout Multiplier (winnings = wager + wager*multiplier), Game Type
           ('0', ['0'], 35, 'All'),
           ('00', ['00'], 35, 'American'),
           ('000', ['000'], 35, 'Sands'),  # TODO: Check value
           ('Straight', ['1..36'], 35, 'All'),
           # Inside
           ('Row', ['0', '00'], 17, 'American'),
           ('Split', ['two adjoining numbers'], 17, 'All'),
           ('Street', ['3 horizontal numbers'], 11, 'All'),
           ('Square', ['4 numbers in a block'], 8, 'All'),
           ('Basket-Fr', ['0', '1', '2', '3'], 8, 'French'),
           ('Basket-Am', ['0', '00', '1', '2', '3'], 6, 'American'),
           ('Double Street', ['2 rows or 3 numbers'], 5, 'All'),
           # Outside
           ('Column', ['Every third number (1,4,7...)'], 2, 'All'),
           ('Dozen', ['12 continuous numbers (1-12, 13-24, 25-36)'], 2, 'All'),
           ('Snake', [1, 5, 9, 12, 14, 16, 19, 23, 27, 30, 32, 34], 2, "All"),
           ('Impiar (Odd)', ['1, 3, 5 ...35'], 1, 'All'),
           ('Pair (Even)', ['2, 4, 6 ...36'], 1, 'All'),
           ('Red', [32, 19, 21, 25, 34, 27, 36, 30, 23, 5, 16, 1, 14, 9, 18, 7, 12, 3], 1, "All"),
           ('Black', [15, 4, 2, 17, 6, 13, 11, 8, 10, 24, 33, 20, 31, 22, 29, 28, 35, 26], 1, "All"),
           ('Manque (Low)', ['1-18'], 1, "All"),
           ('Passe (High)', ['19-36'], 1, "All"),
           ]  # TODO: break Winning Spaces into usable field


class RouletteGame():
    def __init__(self):
        self.pockets = ['0', '1']  # French 37, American 38, Sands 39
        # self.pockets = americanWheel
        self.hitPocket = None
        self.possibleBets = []  # TODO: Set to accept other bets, only accepts Single bets currently

    def spin(self):
        self.hitPocket = np.random.choice(self.pockets)

    def getResult(self, bet, wager):
        if str(bet) == str(self.hitPocket):  # TODO: only set up for single bets right now
            # return wager * 35
            return wager * (35 + 1)
        return bet * -1

    def __str__(self):
        return 'Base Game'


class FrenchRoulette(RouletteGame):
    def __init__(self):
        self.pockets = frenchWheel

    def __str__(self):
        return 'French Roulette'


class AmericanRoulette(RouletteGame):
    def __init__(self):
        self.pockets = americanWheel

    def __str__(self):
        return 'American Roulette'


class SandsRoulette(RouletteGame):
    def __init__(self):
        self.pockets = sandsWheel

    def __str__(self):
        return 'Sands Roulette'


dfmapper = {'Game': '',
            'Plays': '{0:.2f}%',
            '% Winnings': '{0:.2f}%'
            }


def playGame(game, plays, bet, wager):
    totalWinnings = 0
    for i in range(plays):
        game.spin()
        totalWinnings += game.getResult(bet, wager)
    df = pd.DataFrame(
            data={
                'Game':[game.__str__()],
                'Plays':[plays],
                'Bet':[bet],
                'Wager':[wager],
                'Total Wagered':[wager*plays],
                'Winnings':[totalWinnings - wager*plays],
                '% Winnings':[(totalWinnings - wager*plays)/(wager*plays) * 100],
                'Take Home':[totalWinnings],
                '% of Wagered':[totalWinnings/(wager*plays) * 100]
            },
            )
    # df.style.format(dfmapper)
    df.style.format({'Total Wagered': '${0:}%'})
    return df.transpose()


print(playGame(
    FrenchRoulette(),
    100_000,  # Plays
    1,  # Number bet on
    10   # Amount wagered per play
    ),
  )

print(playGame(
    AmericanRoulette(),
    100_000,  # Plays
    1,  # Number bet on
    10   # Amount wagered per play
    ),
  )

print(playGame(
    SandsRoulette(),
    100_000,  # Plays
    1,  # Number bet on
    10   # Amount wagered per play
    ),
  )
