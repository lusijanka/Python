person = {
    'name': 'Ola',
    'surname':'Brzęczkowska',
    'city': 'Warszawa',
    }

print (person['name'])
formula = '{} jest z  {} '
sentence = formula.format(person['name'], person['city'])
print(sentence)


print('*****')

# business card
def card(**kwargs):
    # generating data
    data = []
    max_row_len = 0
    for key, value in kwargs.items():
        row = '{}: {}'.format(key,value)
        data.append(row)

        row_len = len(row)
        if row_len > max_row_len:
            max_row_len = row_len

    # print
    print('+' + '-' *(max_row_len +2) + '+')
    for row in data:
        spaces= max_row_len - len(row)
        print('|',row, ' ' * spaces + '|') 
    print('+' + '-' *(max_row_len +2) + '+')

def get_user():
    user = {}
    user['name'] = input('Enter your name: ')
    user['surname'] = input('Enter your surname: ')
    user['job'] = input('Enter your job: ')
    user['age'] = input('Enter your age: ')
    user['city'] = input('Enter your city: ')
    return user

users = []
quit =False
while not quit:
    print('[1] Add person ')
    print('[q] End ')

    choice = input('Choice')

    if choice == '1':
        user = get_user()
        users.append(user)
    elif choice == 'q':
        quit = True
    else:
        print('No way')
    print()

for user in users:
    card(**user)
    
print(card)

