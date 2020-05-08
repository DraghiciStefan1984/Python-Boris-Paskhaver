languages=['python', 'java', 'c++', 'typescript', 'c#']

lengths1={language: len(language) for language in languages}
print(lengths1)

lengths2={language: len(language) for language in languages if 'c' in language}
print(lengths2)

long_word='Lopadotemachoselachogaleokranioleipsanodrimhypotrimmatosilphioparaomelitokatakechymenokichlepikossyphophattoperisteralektryonoptekephalliokigklopeleiolagoiosiraiobaphetraganopterygon'
letter_count={letter: long_word.count(letter) for letter in long_word}
print(letter_count)


capitals={'Romania': 'Bucharest', 'UK':'London', 'USA': 'Washington', 'France': 'Paris', 'Italy':'Rome'}
inverted_capitals={capital: state for state, capital in capitals.items()}
print(inverted_capitals)