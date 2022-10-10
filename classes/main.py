# Do not modify these lines
__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'

# Add your code after this line

# Part 1: Players

from turtle import speed


class Player():
    def __init__(self, name, speed, endurance, accuracy):
        self.name = name
        self.speed = speed
        self.endurance = endurance
        self.accuracy = accuracy

        list = [speed, endurance, accuracy]
        for input in list:
            if input < 0 or input > 1: 
                raise ValueError("value should be between 0 and 1")
          

    def introduce(self):
        return f"Hello everyone, my name is {self.name}."
    

    def strength(self):
        if self.speed >= self.endurance and self.accuracy:
            return "speed", self.speed
        elif self.endurance >= self.accuracy:
            return "endurance", self.endurance
        else:
            return "accuracy", self.accuracy
        

# Part 2 Commentators


class Commentator():
    def __init__(self, name):
        self.name = name


    def sum_player(self, player):
        return player.speed + player.endurance + player.accuracy


    def compare_players(self, player_1, player_2, skill):
        compare_player_1 = getattr(player_1, skill)
        compare_player_2 = getattr(player_2, skill)
        
        strenght_player_1 = player_1.strength() 
        strenght_player_2 = player_2.strength()

        sum_player_1 = self.sum_player(player_1)
        sum_player_2 = self.sum_player(player_2)

        if compare_player_1 > compare_player_2:
            return player_1.name
        elif compare_player_1 < compare_player_2:
            return player_2.name
        
        else:
            if strenght_player_1 > strenght_player_2:
                return player_1.name
            elif strenght_player_1 < strenght_player_2:
                return player_2.name
            
            else:
                if sum_player_1 > sum_player_2:
                    return player_1.name
                elif sum_player_1 < sum_player_2:
                    return player_2.name
        
                else:
                    return "These two players might as well be twins!"

ray = Commentator('Ray Hudson')
# print(ray.name)


player_1 = Player("Hans van Breukelen", 0.8, 0.7, 0.5)
# print(player_1.__dict__)
# print(player_1.introduce())

player_2 = Player("Frank de Boer", 0.8, 0.7, 0.5)
# print(player_2.__dict__)
# print(player_2.strength())

player_3 = Player("Ronald de Boer", 0.7, 0.8, 0.9)
# print(player_3.__dict__)

ray = Commentator("Ray Hudson")
print(ray.sum_player(player_2))
print(ray.compare_players(player_1, player_2, "accuracy"))

