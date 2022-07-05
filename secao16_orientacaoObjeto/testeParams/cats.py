cats = {'Tom': {'color': 'white', 'weight': 8}, 'Klakier': {'color': 'black', 'weight': 10}}
cat_attr = {}
for cat in cats:
    for attr in cats[cat]:
        print(cats[cat][attr])