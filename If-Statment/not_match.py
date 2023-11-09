name = str(input('Enter your team name: '))

match name:
    case 'Manchester':
        print('Is English team')
    case 'Real Madrid':
        print('Is Spanish team')
    case 'Rom':
        print('Is Italia team')
    case 'Byren Munchen':
        print('Is German team')
    case 'Los Angles':
        print('Is not EU team')
    case _:
        print('The team not exisit, try again')