class Candidate:
    def __init__(self, name, votes):
        self.name = name
        self.votes = votes

    def __del__(self):
        print(f"Кандидат {self.name} видалений з пам'яті.")

    def get_name(self):
        return self.name

    def get_votes(self):
        return self.votes

    def display_info(self):
        print(f"Кандидат: {self.name}")
        print(f"Голоси: {self.votes}")

class Elections:
    def __init__(self):
        self.candidates = []

    def add_candidate(self, candidate):
        self.candidates.append(candidate)

    def total_votes(self):
        return sum(c.get_votes() for c in self.candidates)

    def winner(self):
        find_winner = max(self.candidates, key=lambda c: c.get_votes())
        if not self.candidates:
           find_winner = None
        return find_winner

    def display_results(self):
        total = self.total_votes()
        for c in self.candidates:
            percent = (c.get_votes() / total * 100) if total > 0 else 0
            print(f"{c.get_name()} - {c.get_votes()} голосів - {percent: }%")

def main():
    elections = Elections()

    for i in range(5):
        name = input("Введіть прізвище кандидата: ")

        while True:
            try:
                votes = int(input(f"Кількість голосів для {name}: "))
                if votes < 0:
                    print("Кількість голосів не може бути від'ємною. Спробуйте ще раз.")
                else:
                    break
            except ValueError:
                print("Будь ласка, введіть ціле число для голосів.")

        candidate = Candidate(name, votes)
        elections.add_candidate(candidate)

    print("результати виборів:")
    elections.display_results()

    winner = elections.winner()
    if winner:
        print(f"переможець: {winner.get_name()} з {winner.get_votes()} голосами")

if __name__ == "__main__":
    main()
