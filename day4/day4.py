with open("input.txt") as f:
    input_data = f.read().split("\n\n")

draws = [int(draw) for draw in input_data[0].split(",")]
boards = [
    [[int(cell) for cell in row.split()] for row in board.split("\n") if row]
    for board in input_data[1:]
]

# Part 1


def transpose(board: list[list[int]]) -> list[list[int]]:
    return list(map(list, zip(*board)))


def is_winner(board: list[list[int]], draws: list[int]):
    row_winner = any(set(row).issubset(set(draws)) for row in board)
    col_winner = any(set(col).issubset(set(draws)) for col in transpose(board))
    return row_winner or col_winner


def calculate_winner_score(boards: list[list[list[int]]], draws: list[int]):
    for i in range(len(draws)):
        current_draws = draws[:i]
        for board in boards:
            if is_winner(board, current_draws):
                board_score = sum(
                    cell for row in board for cell in row if cell not in current_draws
                )
                draw_score = current_draws[-1]
                return board_score * draw_score


score = calculate_winner_score(boards, draws)
print(score)


# Part 2


def calculate_loser_score(boards: list[list[list[int]]], draws: list[int]):
    candidate_boards = boards
    for i in range(len(draws)):
        current_draws = draws[:i]
        for board in boards:
            if is_winner(board, current_draws):
                boards.remove(board)
            if len(boards) == 0:
                board_score = sum(
                    cell for row in board for cell in row if cell not in current_draws
                )
                draw_score = current_draws[-1]
                return board_score * draw_score


score = calculate_loser_score(boards, draws)
print(score)
