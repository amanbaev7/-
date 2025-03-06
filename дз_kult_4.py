

import random

class Game:
    def __init__(self):
        self.min_num = 1
        self.max_num = 100
        self.secret_number = random.randint(self.min_num, self.max_num)
        self.attempts = 0

    def set_range(self, min_num, max_num):
        """Устанавливает диапазон и загадывает новое число"""
        self.min_num = min_num
        self.max_num = max_num
        self.secret_number = random.randint(min_num, max_num)
        self.attempts = 0

    def check_guess(self, guess):
        """Проверяет, угадал ли игрок число"""
        self.attempts += 1
        if guess < self.secret_number:
            return "Число больше!"
        elif guess > self.secret_number:
            return "Число меньше!"
        else:
            return f"Поздравляю! Вы угадали число {self.secret_number} за {self.attempts} попыток."

    def reset_game(self):
        """Перезапускает игру"""
        self.secret_number = random.randint(self.min_num, self.max_num)
        self.attempts = 0

class Player:
    @staticmethod
    def guess_number():
        """Запрашивает ввод числа у игрока"""
        while True:
            try:
                return int(input("Введите число: "))
            except ValueError:
                print("Ошибка! Введите целое число.")

def main():
    print("Добро пожаловать в игру 'Угадай число'!")

    game = Game()

    difficulty = input("Выберите уровень сложности (1 - Легкий (1-50), 2 - Средний (1-100), 3 - Сложный (1-1000)): ")
    if difficulty == "1":
        game.set_range(1, 50)
    elif difficulty == "3":
        game.set_range(1, 1000)
    else:
        game.set_range(1, 100)

    while True:
        guess = Player.guess_number()
        result = game.check_guess(guess)
        print(result)
        
        if "Поздравляю" in result:
            again = input("Хотите сыграть еще раз? (да/нет): ").strip().lower()
            if again == "да":
                game.reset_game()
                print("Новая игра началась!")
            else:
                print("Спасибо за игру!")
                break

if __name__ == "__main__":
    main()
    
    