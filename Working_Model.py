import numpy as np


class Game(object):
    def __init__(self, id, prob_head):
        self._id = id
        self._rnd = np.random
        self._rnd.seed(id)
        self._probHead = prob_head  # probability of flipping a head
        self._countWins = 0  # number of wins, set to 0 to begin

    def simulate(self, n_of_flips):

        count_tails = 0  # number of consecutive tails so far, set to 0 to begin

        # flip the coin 20 times
        for i in range(n_of_flips):

            # in the case of flipping a heads
            if self._rnd.random_sample() < self._probHead:
                if count_tails >= 2:  # if the series is ..., T, T, H
                    self._countWins += 1  # increase the number of wins by 1
                count_tails = 0  # the tails counter needs to be reset to 0 because a heads was flipped

            # in the case of flipping a tails
            else:
                count_tails += 1  # increase tails count by one

    def get_reward(self):
        # calculate the reward from playing a single game
        return 100*self._countWins - 250


class SetOfGames:
    def __init__(self, prob_head, n_games):
        self._gameRewards = []      # create an empty list where rewards will be stored

        self._n_losses = 0          # number of losses
        self._n_games = n_games     # number of total games

        self._max_reward = 0        # maximum game reward
        self._min_reward = 0        # minimum game reward

        # simulate the games
        for n in range(n_games):
            # create a new game
            game = Game(id=n, prob_head=prob_head)
            # simulate the game with 20 flips
            game.simulate(20)
            # store the reward
            self._gameRewards.append(game.get_reward())

    def get_ave_reward(self):
        """ returns the average reward from all games"""
        return sum(self._gameRewards) / len(self._gameRewards)

    def get_reward(self):
        """ returns the list of rewards"""
        return self._gameRewards

    def get_max_reward(self):
        """ returns the maximum reward"""
        for reward in self._gameRewards:
            if reward > self._max_reward:
                self._max_reward = reward
        return self._max_reward

    def get_min_reward(self):
        """ returns the minimum reward"""
        for reward in self._gameRewards:
            if reward < self._min_reward:
                self._min_reward = reward
        return self._min_reward

    def get_loss_probability(self):
        """ returns the probability of a loss, reward < $0"""
        for reward in self._gameRewards:
            if reward < 0:
                self._n_losses += 1
        return self._n_losses/self._n_games
