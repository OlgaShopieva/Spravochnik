import view

def upload_data ():
    with open('log.csv', 'a') as file:
        file.write(f'\n{view.get_data()}')





