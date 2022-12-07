import json

if __name__ == '__main__':

    filename = 'file.json'

    # countries = []
    countries = json.load(open(filename))

    a = ' '

    while a != '0':

        print('1) Delete country')
        print('2) Add new country')
        print('3) Edit existing country')
        print('4) Print country info')
        print('5) Sort countries by filed')
        print('6) Save countries to file')
        print('0) Exit')

        # print(countries)

        a = input('select task ')

        if a == "1":
            name = input('input name ')
            countries = [c for c in countries if c[0] != name]
            out_file = open(filename, "w")
            json.dump(countries, out_file)

        if a == "2":
            name = input('input name ')
            gov = input('input form of goverment ')
            area = input('input area ')
            people_count = input('input people count ')
            GDP = input('input GDP ')
            lang = input('input count language')

            c = [name, gov, area, people_count, GDP, lang]
            countries.append(c)

        if a == '3':

            name = input('input name ')
            gov = input('input form of goverment ')
            area = input('input area ')
            people_count = input('input people count ')
            GDP = input('input GDP ')
            lang = input('input count language')

            c = [name, gov, area, people_count, GDP, lang]

            new_countries = []
            for country in countries:
                if country[0] == name:
                    new_countries.append(c)
                else:
                    new_countries.append(country)

            countries = new_countries

        if a == '4':

            name = input('input name ')
            for country in countries:
                if country[0] == name:
                    name, gov, area, people, GDP, lang = country
                    print('country name', name)
                    print('country form of goverment', gov)
                    print('country area', area)
                    print('country people count', people)
                    print('country GDP', GDP)
                    print('country language', lang)
                    print()

        if a == '5':

            print(' 1) Sort by name ')
            print(' 2) Sort by goverment ')
            print(' 3) Sort by area ')
            print(' 4) Sort by GDP ')
            b = input('select task ')
            key_func = lambda x: x[0]
            if b == '1':
                key_func = lambda x: x[0]
            if b == '2':
                key_func = lambda x: x[1]
            if b == '3':
                key_func = lambda x: x[2]
            if b == '4':
                key_func = lambda x: x[4]

            countries = sorted(countries, key=key_func)

        if a == '6':
            fname = input('input output filename ')

            out_file = open(fname, "w")
            json.dump(countries, out_file)

            key_func = lambda x: x[4]

            min_GDP_country = sorted(countries, key=key_func)[0]

            name, gov, area, people, GDP, lang = min_GDP_country
            print('country with minimap GDP')
            print('country name', name)
            print('country form of goverment', gov)
            print('country area', area)
            print('country people count', people)
            print('country GDP', GDP)
            print('country language', lang)
            print()
