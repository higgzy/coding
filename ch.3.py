games = ['battlefield','terraria','blox']
#variable                #list
print(games)
    #variable
print(games[0])
    #list index
print(games[1])
    #list index
print(games[2].title())
 #list index + title
print(games[-1])
#list index reversed
print(games[-2].title())
#list index reversed + title
print(games[0].title() + " " + "is a fun game")
#list index + title + string
games[0] = 'WOW'
#list value switch
print(games)
    #variable
games.append('battlefront')
    #append new value
print(games)
    #variable
games.insert(1, 'smite')
  #insering new value
print(games)
    #variable
del games[0]
#delete value
print(games)
    #variable
popped_games = games.pop()
     #popped values
print(popped_games)
 #poped last value
games.remove('terraria')
 #remove values
print(games)
    #variable
games.sort()
#sorts values
print(games)
    #variable

