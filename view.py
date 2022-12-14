def get_request ():
   input_str = input('Введите 0 если хотите внести данные в справочник и 1 если хотите найти данные в справочнике: ')
   return input_str

def get_data ():
    input_data = input('Введите данные для справочника через запятую в формате: Иванов,Иван,89637892345,рабочий')
    return input_data

def find_data ():
    need_data = input('Введите фамилию для поиска в справочнике в формате "Иванов" без кавычек')
    return need_data
