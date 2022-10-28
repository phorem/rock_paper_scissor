def rpsWinner(player1, player2):
    player1 = player1.lower()
    player2 = player2.lower()

    if player1 == "rock":
        player1 = 0
    elif player1 == "paper":
        player1 = 1
    elif player1 == "scissors":
        player1 = 2
        
    if player2 == "rock":
        player2 = 0
    elif player2 == "paper":
        player2 = 1
    elif player2 == "scissors":
        player2 = 2 
    
    if player1 == player2:
        return "tie"

    elif player1 == 0 and player2 == 2:
        return "player one"
    
    elif player1 == 2 and player2 == 0:
        return "player two"

    elif player1 > player2:
        return "player one"

    elif player1 < player2:
        return "player two"

#print(rpsWinner("scissor", "scissor"))
    
assert rpsWinner('rock', 'paper') == 'player two'

assert rpsWinner('rock', 'scissors') == 'player one'

assert rpsWinner('paper', 'scissors') == 'player two'

assert rpsWinner('paper', 'rock') == 'player one'

assert rpsWinner('scissors', 'rock') == 'player two'

assert rpsWinner('scissors', 'paper') == 'player one'

assert rpsWinner('rock', 'rock') == 'tie'

assert rpsWinner('paper', 'paper') == 'tie'

assert rpsWinner('scissors', 'scissors') == 'tie'
      