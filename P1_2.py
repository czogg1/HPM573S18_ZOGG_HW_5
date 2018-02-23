import Working_Model as GameOfChance
import scr.FigureSupport as FigSupport  # calling histogram from the support library

# run trial of 1000 games to calculate expected reward
games = GameOfChance.SetOfGames(prob_head=0.5, n_games=1000)
# print the average reward
print("The average expected reward is:", games.get_ave_reward())   # holdover from HW4


# Problem 1: create a histogram of game rewards
FigSupport.graph_histogram(observations=games.get_reward(), title="Histogram of Game Rewards",
                           x_label="Game Rewards (USD)", y_label="Count", x_range=(-260, 260))

print("The maximum expected reward is:", games.get_max_reward())
print("The minimum expected reward is:", games.get_min_reward())


# Problem 2: calculate the probability of a loss
print("The probability of a loss is:", games.get_loss_probability())
