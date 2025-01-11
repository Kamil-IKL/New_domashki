class User:

    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = str(nickname)
        self.password = hash(password)  # хеширую пароль (все в число)
        self.age = int(age)


class Video:

    def __init__(self, title: str, duration: int, adult_mode=False):
        self.title = str(title)
        self.duration = int(duration)
        self.time_now = 0
        self.adult_mode = bool(adult_mode)


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname: str, password: str):
        '''
        Вход в аккаунт Пользователя, предварительно проверяет Пользователя по логину и паролю
        :param nickname: логин (строка)
        :param password: пароль (строка), в дальнейшем автоматически хешируется в число
        :return: True - вход выполнен, False - вход не выполнен
        '''
        password = hash(password)  # хеширую пароль (все в число)
        for user in self.users:
            if user.nickname == nickname and user.password == password:
                self.current_user = user
                print(f'{self.current_user} - Вы успешно вошли аккаунт')
                return True
        print(f'Неверный логин или пароль')
        return False

    def register(self, nickname: str, password: str, age: int):
        '''
        Регистрация Пользователя, предварительно осуществляется проверка на существующего Пользователя
        :param nickname: логин (строка)
        :param password: пароль (строка), в дальнейшем автоматически хешируется в число
        :param age: возраст (число)
        :return: добавляет нового Пользователя
        '''
        # проверяю, существует ли такой логин(Пользователь) или нет
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')

        # добавляю нового Пользователя
        new_user = User(nickname, password, age)  # создал нового Пользователя
        self.users.append(new_user)  # добавил в список Пользователей
        self.current_user = new_user  # присвоил статус текущего Пользователя
        print(f'Пользователь {self.current_user} успешно зарегистрирован и вошел в аккаунт')
        return new_user

    def log_out(self):
        '''
        Выход из аккаунта Пользователя
        :return: None
        '''
        self.current_user = None  # "обнуляю" текущего Пользователя
        return f'Пользователь {self.current_user} вышел из аккаунта'

    # Добавление видео из класса Video
    def add(self, *videos):
        # проверяю, существует ли такое видео Пользователя в списке(базе) и добавляю, если нет
        for video in videos:
            if video.title in self.videos:
                print(f'"{video.title}" уже существует в базе "Видео"')
        self.videos.append(videos)  # ОБРАТИ ВНИМАНИЕ, МОЖЕТ СДЕЛАТЬ ЧЕРЕЗ not В УСЛОВИИ (Т.Е. НАОБОРОТ)
        print(f'Ваше {video.title} добавлено в базу "Видео"')

    def get_videos(self, search_word: str):
        for video in self.videos:
            if search_word.upper() in video.title.upper(): # верхний регистр (метод upper())
                return [video]

    def watch_video(self):
        pass
