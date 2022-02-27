import random


class TicTac():
    PRIORITY_CELLS = {"1" : 2, "2" : 1, "3" : 2, "4" : 1, "5" : 3, "6" : 1, "7" : 2, "8" : 1, "9" : 2}
    board = [" " for i in range(1,10)]
    whose_move = "X"
    count = 0

    def start_game(self):
        win = False
        self.game_view()
        while win == False:
            self.game_logick()
            win_bot = self.check_win()
            self.game_view()
            self.count += 1
            if win_bot:
                print(f'Компьютер играющий за {win_bot}, победил!')
                win = True
            elif self.count == 9:
                print("Ничья!")
                win = True

    def game_view(self):
        print("-" * 13)
        for i in range(3):
            print("|", self.board[0+i*3], "|", self.board[1+i*3], "|", self.board[2+i*3], "|")
            print("-" * 13)
    
    def game_logick(self):
        future_win = self.check_future_win()
        if type(future_win) == int:   #Выигрышная комбинация
            self.board[future_win] = self.whose_move
        elif type(future_win) == str: #Комбинаця которую нужно закрыть
            self.board[int(future_win)] = self.whose_move
        #если выигрышных нет ставим по порядку с учетом важности клеток
        else:
            price_cell = 0
            future_win = 0
            for i in range(len(self.board)):
                if self.board[i] == " ":
                    if price_cell < self.PRIORITY_CELLS[str(i + 1)]:
                        price_cell = self.PRIORITY_CELLS[str(i + 1)]
                        future_win = i


            rand_check = False
            while rand_check == False:
                if price_cell == 2:
                    future_win = random.choice([0, 2, 6, 8, 1, 3, 5, 7])
                    if self.board[future_win] == " ":
                        rand_check = True
                elif price_cell == 0:
                    future_win = random.choice([1, 3, 5, 7])
                    if self.board[future_win] == " ":
                        rand_check = True
                elif price_cell == 3:
                    rand_check = True

            self.board[future_win] = self.whose_move
        
        if self.whose_move == "X":
            self.whose_move = "O"
        else:
            self.whose_move = "X"
        

    def check_win(self):
        win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
        for i in win_coord:
            if self.board[i[0]] == self.board[i[1]] == self.board[i[2]] != " ":
                return self.board[i[0]]
        return False

    def check_future_win(self):
        posible_win_coord = {
                (0,1) : 2, (0,2) : 1, (0,3) : 6, (0,6) : 3,
                (1,2) : 0, (1,4) : 7, (1,7) : 4, (2,5) : 8,
                (2,8) : 5, (2,4) : 6, (2,6) : 4, (3,4) : 5,
                (3,5) : 4, (3,6) : 0, (0,4) : 8, (0,8) : 4,
                (4,5) : 3, (4,7) : 1, (4,6) : 2, (4,8) : 0,
                (5,8) : 2, (6,7) : 8, (6,8) : 7, (7,8) : 6,
            }
        if self.whose_move == "X":
            for i in posible_win_coord.keys():
                if self.board[i[0]] == self.board[i[1]] == "X":
                    if self.board[posible_win_coord.get(i)] == " ":
                        return posible_win_coord.get(i)
            
            for i in posible_win_coord.keys():
                if self.board[i[0]] == self.board[i[1]] == "O":
                    if self.board[posible_win_coord.get(i)] == " ":
                        return posible_win_coord.get(i)

        if self.whose_move == "O":
            for i in posible_win_coord.keys():
                if self.board[i[0]] == self.board[i[1]] == "O":
                    if self.board[posible_win_coord.get(i)] == " ":
                        return posible_win_coord.get(i)
            
            for i in posible_win_coord.keys():
                if self.board[i[0]] == self.board[i[1]] == "X":
                    if self.board[posible_win_coord.get(i)] == " ":
                        return posible_win_coord.get(i)

        return None
            


if __name__ == "__main__":
    tictac = TicTac()
    tictac.start_game()