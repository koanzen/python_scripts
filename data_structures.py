import pprint

#data structure organize and can represent real world objects
#creating data structure for a tic tac toe game
#for this data structure we will use the dictionary data
dsboard = {
    'ul':' ',
    'um':' ',
    'ur':' ',
    'ml':' ',
    'mm':' ',
    'mr':' ',
    'll':' ',
    'lm':' ',
    'lr':' '
    }

#This function will represent the data structure in a presentable view
def showBoard(board):
    print(f"{board['ul']}|{board['um']}|{board['ur']}")
    print("-----")
    print(f"{board['ml']}|{board['mm']}|{board['mr']}")
    print("-----")
    print(f"{board['ll']}|{board['lm']}|{board['lr']}")

print(showBoard(dsboard)) #prints the view of the data structure