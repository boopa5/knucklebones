import random
import functools

class Game:
    def __init__(self):

        self.turn = "p1"

        # Board contains array of each column of each player NOT ROW
        self.board = {
            "p1": [[], [], []],
            "p2": [[], [], []]
        }

        self.dice_val = self.roll_dice()


    def reset_game(self) -> None:
        self.board = {
            "p1": [[], [], []],
            "p2": [[], [], []]
        }
        self.turn = "p1"
        self.dice_val = self.roll_dice()


    def roll_dice(self) -> int:
        return random.choice([i for i in range(1, 7)])


    def place_in_column(self, player: str, column: int, val: int) -> bool:
        # Column already full
        if len(self.board[player][column]) == 3:
            return False

        self.board[player][column].append(val)

        # Remove same value from opponent board
        self.board["p1" if player == "p2" else "p2"][column] = [i for i in self.board["p1" if player == "p2" else "p2"][column] if i != val]

        return True # Used to break out of take_turn


    def take_turn(self, column) -> None:
        if not self.place_in_column(self.turn, column, self.dice_val):
            return
        
        # Alternate Turn
        self.turn = "p1" if self.turn == "p2" else "p2"
        self.dice_val = self.roll_dice()
    

    def points(self) -> tuple:
        # Return tuple with each players points
        res1, res2 = 0, 0
        for i in range(3):
            res1 += sum(self.board["p1"][i])
            res2 += sum(self.board["p2"][i])
        return (res1, res2)

    
    def game_over(self) -> bool:
        res1, res2 = 0, 0
        for i in range(3):
            res1 += len(self.board["p1"][i])
            res2 += len(self.board["p2"][i])
        return res1 == 9 or res2 == 9
        
    
    def winner(self) -> str:
        return "p1" if self.points()[0] > self.points()[1] else "p2"