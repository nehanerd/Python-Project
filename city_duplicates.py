#Prints out the cities that are listed more than twice


def main():
    cities = ["Austin", "Dallas", "Houston", "Houston", "Austin", "Corpus Christi", "Waco", "Houston"]
    duplicate_cities = []
    count = 0
    for i in cities:
        for j in cities:
            if i == j:
                count += 1
        if (count > 1) and (i not in duplicate_cities):
            duplicate_cities.append(i)
        count = 0
    print(duplicate_cities)

main()
