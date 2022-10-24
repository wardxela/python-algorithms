import json
import bcrypt


class DB:
    def __init__(self, src: str):
        self.src = src
        self.data = self.__read__()

    def __read__(self):
        data = []
        try:
            file = open(self.src, 'r')
            data = json.load(file)
            file.close()
        except:
            pass
        return data

    def add(self, login: str, password: str):
        salt = bcrypt.gensalt()
        hashedpw = bcrypt.hashpw(password.encode('utf-8'), salt)
        self.data.append({
            'login': login,
            'password': hashedpw.decode('utf-8')
        })

    def find(self, login: str, password: str):
        for user in self.data:
            if user['login'] == login:
                if bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
                    return True, 'Пользователь найден'
                return False, 'Неверный пароль'
        return False, f'Пользователь с логином `{login}` не существует'

    def save(self):
        file = open(self.src, 'w')
        json.dump(self.data, file)
        file.close()


def get_user_credentials():
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    return login, password


db = DB('./data/users.json')
while True:
    branch = input('Войти(1) / Зарегистрироваться(2)? - ')
    if branch == '1':
        login, password = get_user_credentials()
        status, message = db.find(login, password)
        if status:
            print(message)
            print('Вы успешно вошли в систему')
        else:
            print('Ошибка авторизации:')
            print(message)
        break
    elif branch == '2':
        login, password = get_user_credentials()
        db.add(login, password)
        db.save()
        print('Пользователь успешно добавлен')
        break
    else:
        print('Я тебя не понял, попробуй еще раз')
