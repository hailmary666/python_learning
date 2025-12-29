def describe_city(name, country='russia'):
    print(name.title() + " is in " + country.title())

describe_city('moscow')
describe_city('voronezh')
describe_city('paris', 'france')
describe_city(country='united kingdom', name='london')


