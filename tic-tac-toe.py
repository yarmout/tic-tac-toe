import turtle

shelly = turtle.Turtle()
playerOneTurn = True
playerTwoTurn = True
chosenTiles = {'X':[], 'O':[]}
gameOver = False
turnCounter = 0

def drawBoard():
    shelly.penup()
    shelly.right(90)
    shelly.forward(100)
    shelly.right(90)
    shelly.backward(300)
    shelly.pendown()
    shelly.forward(600)
    shelly.penup()
    shelly.right(90)
    shelly.forward(200)
    shelly.right(90)
    shelly.pendown()
    shelly.forward(600)
    shelly.penup()
    shelly.right(180)
    shelly.forward(200)
    shelly.right(90)
    shelly.forward(200)
    shelly.right(180)
    shelly.pendown()
    shelly.forward(600)
    shelly.penup()
    shelly.right(90)
    shelly.forward(200)
    shelly.right(90)
    shelly.pendown()
    shelly.forward(600)
    shelly.penup()
    
def drawX():
    shelly.penup()
    shelly.left(135)
    shelly.forward(66.4215)
    shelly.pendown()
    shelly.forward(150)
    shelly.penup()
    shelly.right(135)
    shelly.forward(106.066)
    shelly.right(135)
    shelly.pendown()
    shelly.forward(150)
    shelly.penup()
    shelly.right(180)
    shelly.forward(75)
    shelly.right(90)
    shelly.forward(141.4215)
    shelly.left(45)

def drawO():
    shelly.penup()
    shelly.right(180)
    shelly.forward(200)
    shelly.right(90)
    shelly.forward(100)
    shelly.right(90)
    shelly.forward(46.967)
    shelly.right(90)
    shelly.pendown()
    shelly.circle(53.033)
    shelly.penup()
    shelly.right(90)
    shelly.forward(46.967)
    shelly.left(90)
    shelly.forward(100)
    shelly.left(90)
    shelly.forward(200)

def drawLetter(tileLetter):
    if tileLetter == 'X':
        drawX()
    if tileLetter == 'O':
        drawO()

def goToTile(tileNumber, tileLetter):
    if tileNumber == 1:
        shelly.backward(400)
        drawLetter(tileLetter)
        shelly.forward(400)

    if tileNumber == 2:
        shelly.backward(400)
        shelly.right(90)
        shelly.forward(200)
        shelly.left(90)
        drawLetter(tileLetter)
        shelly.forward(400)
        shelly.left(90)
        shelly.forward(200)
        shelly.right(90)

    if tileNumber == 3:
        shelly.backward(400)
        shelly.right(90)
        shelly.forward(400)
        shelly.left(90)
        drawLetter(tileLetter)
        shelly.forward(400)
        shelly.left(90)
        shelly.forward(400)
        shelly.right(90)

    if tileNumber == 4:
        shelly.backward(200)
        drawLetter(tileLetter)
        shelly.forward(200)
    
    if tileNumber == 5:
        shelly.backward(200)
        shelly.right(90)
        shelly.forward(200)
        shelly.left(90)
        drawLetter(tileLetter)
        shelly.forward(200)
        shelly.left(90)
        shelly.forward(200)
        shelly.right(90)

    if tileNumber == 6:
        shelly.backward(200)
        shelly.right(90)
        shelly.forward(400)
        shelly.left(90)
        drawLetter(tileLetter)
        shelly.forward(200)
        shelly.left(90)
        shelly.forward(400)
        shelly.right(90)

    if tileNumber == 7:
        drawLetter(tileLetter)

    if tileNumber == 8:
        shelly.right(90)
        shelly.forward(200)
        shelly.left(90)
        drawLetter(tileLetter)
        shelly.left(90)
        shelly.forward(200)
        shelly.right(90)

    if tileNumber == 9:
        shelly.right(90)
        shelly.forward(400)
        shelly.left(90)
        drawLetter(tileLetter)
        shelly.left(90)
        shelly.forward(400)
        shelly.right(90)

def winCondition(tileLetter):
    if 1 in chosenTiles[tileLetter] and 2 in chosenTiles[tileLetter] and 3 in chosenTiles[tileLetter]:
        return True
    if 4 in chosenTiles[tileLetter] and 5 in chosenTiles[tileLetter] and 6 in chosenTiles[tileLetter]:
        return True
    if 7 in chosenTiles[tileLetter] and 8 in chosenTiles[tileLetter] and 9 in chosenTiles[tileLetter]:
        return True
    if 1 in chosenTiles[tileLetter] and 4 in chosenTiles[tileLetter] and 7 in chosenTiles[tileLetter]:
        return True
    if 2 in chosenTiles[tileLetter] and 5 in chosenTiles[tileLetter] and 8 in chosenTiles[tileLetter]:
        return True
    if 3 in chosenTiles[tileLetter] and 6 in chosenTiles[tileLetter] and 9 in chosenTiles[tileLetter]:
        return True
    if 1 in chosenTiles[tileLetter] and 5 in chosenTiles[tileLetter] and 9 in chosenTiles[tileLetter]:
        return True
    if 3 in chosenTiles[tileLetter] and 5 in chosenTiles[tileLetter] and 7 in chosenTiles[tileLetter]:
        return True


drawBoard()
while(gameOver == False):
    while(playerOneTurn == True):
        tileNumber = int(input('Player 1\'s turn: '))
        if tileNumber not in chosenTiles['X'] and tileNumber not in chosenTiles['O'] and tileNumber > 0 and tileNumber < 10:
            goToTile(tileNumber, 'X')
            chosenTiles['X'].append(tileNumber)
            turnCounter += 1
            playerOneTurn = False
            if winCondition('X') == True:
                print('Game Over! Player 1 Wins!')
                playerTwoTurn = False
                gameOver = True
        elif tileNumber < 1 or tileNumber > 9:
            print('Invalid input! Tile does not exist.')
        else:
            print('That tile has already been chosen!')
    playerOneTurn = True

    if turnCounter == 9 and gameOver == False:
        print('Game Over! Draw!')
        playerTwoTurn = False
        gameOver = True
        
    while(playerTwoTurn == True):
        tileNumber = int(input('Player 2\'s turn: '))
        if tileNumber not in chosenTiles['X'] and tileNumber not in chosenTiles['O'] and tileNumber > 0 and tileNumber < 10:
            goToTile(tileNumber, 'O')
            chosenTiles['O'].append(tileNumber)
            turnCounter += 1
            playerTwoTurn = False
            if winCondition('O') == True:
                print('Game Over! Player 2 Wins!')
                gameOver = True
        elif tileNumber < 1 or tileNumber > 9:
            print('Invalid input! Tile does not exist.')
        else:
            print('That tile has already been chosen!')
    playerTwoTurn = True
                
turtle.done()



## To do list
## Draw a thick line through the winning tiles?
## Single player vs bot
## Hard mode, perfect game
## Easy mode, random spots
## Medium mode, random spot within one tile of the player's last move
