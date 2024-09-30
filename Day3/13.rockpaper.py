from rockpaper import ComputerPlayer, HumanPlayer, Game, GamePlay

pc =  ComputerPlayer()
myself = HumanPlayer("Silviu")

gp = GamePlay(myself, pc)
gp.play()