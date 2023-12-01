costs = {'Philadelphia':{'Chicago':227, 'Dallas':289},
         'Chicago':{'Philadelphia':227, 'Dallas':105, 'Las Vegas':56},
         'Dallas':{'Philadelphia':289, 'Houston':173, 'Chicago':105,
                   'Las Vegas':44, 'San Diego':303},
         'Houston':{'Dallas':173},
         'Las Vegas':{'Chicago':56, 'Dallas':44, 'San Diego':74,
                      'Los Angeles':44, 'San Francisco':56},
         'Los Angeles':{'Las Vegas':44, 'San Diego':157,
                        'San Francisco':111},
         'San Diego':{'Las Vegas':44, 'Los Angeles':157, 'Dallas':303},
         'San Francisco':{'Las Vegas':56, 'Los Angeles':111}}


def cheapest(costs: dict, origin: str, destination: str):
    total_cost = []
    for city in costs[origin]:
        if destination == city:
            total_cost.append(costs[origin][city])
        elif destination in costs[city]:
            total_cost.append(costs[origin][city] + costs[city][destination])
    if len(total_cost) == 0:
        return float('inf')
    return min(total_cost)

def main():
    total = costs['Chicago']['Las Vegas'] + costs['Las Vegas']['Dallas']
    print(total)
    print(cheapest(costs, 'San Francisco', 'Philadelphia'))
    print(cheapest(costs, 'Chicago', 'Dallas'))
    print(cheapest(costs, 'Las Vegas', 'Los Angeles'))


if __name__ == '__main__':
    main()