favoritos_tres_games = [
  {
    "Name" : "Call of Duty",
    "Units Sold" : 400
  },
  {
    "Name" : "Final Fantasy",
    "Units Sold" : 150
  },
  {
    "Name" : "Mass Effect",
    "Units Sold" : 16
  }
]

for i in range(len(favoritos_tres_games)):
    if favoritos_tres_games[i]["Name"] == 'Call of Duty':
        print(f'Units Sold: {favoritos_tres_games[i]["Units Sold"]} million')