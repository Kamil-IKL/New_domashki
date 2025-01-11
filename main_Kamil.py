class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = str(nickname)
        self.password = hash(password)
        self.age = int(age)

    # def __str__(self):
    #     return f'хеш пароль: {self.password}'


class Video:
    def __init__(self, title: str, duration: int, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = bool(adult_mode)


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        password = hash(password)
        for user in self.users:
            if user.nickname == nickname and user.password == password:
                self.current_user = user
                print(f'{nickname} - Вы успешно вошли аккаунт')
                return True
        print(f'Неверный логин или пароль')
        return False

    def register(self, nickname, password, age):
        # проверяю, существует ли уже данный Пользователь или нет
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь с логином "{nickname}" -  уже существует')
                return
                # return f'Такой пользователь уже существует'

        # добавляю нового пользователя
        new_user = User(nickname, password, age)  # создал нового Пользователя
        self.users.append(new_user)  # добавил в список Пользователей
        self.current_user = new_user  # присвоил статус текущего Пользователя
        print(f'{nickname} - Вы успешно зарегистрировались и вошли в аккаунт')
        # return self.current_user

    def log_out(self):
        self.current_user = None
        print(f'Вы вышли из аккаунта')
        # return None

    def add(self, *videos):
        for video in videos:
            if video.title in self.videos:
                print(f'Видео: "{video.title}" уже существует')
            else:
                self.videos.append(video.title)  # ОБРАТИ ВНИМАНИЕ ! МОЖЕТ СДЕЛАТЬ ЧЕРЕЗ not В УСЛОВИИ (Т.Е. НАОБОРОТ)?
                print(f'Видео: "{video.title}" добавлено')

    def get_videos(self, search_word: str):
        for video in self.videos:
            if search_word.lower() in video.lower():
                print(video)
                # return


    def watch_video(self, title):
        if self.current_user == None:
            print(f'Войдите в аккаунт, чтобы смотреть видео')
            return



if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    print(f'\nДобавление видео'.upper())
    ur.add(v1, v2)
    print(ur.videos)  # проверка списка видео

    print(f'\nПроверка на дублирование видео'.upper())
    v3 = Video('Лучший язык программирования 2024 года', 150)
    ur.add(v3)
    print(ur.videos)  # проверка списка видео

    print(f'\nПроверка поиска'.upper())
    # print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))
    # print(ur.get_videos('ПаР'))
    #
    # print(f'\nПроверка на вход пользователя и возрастное ограничение')
    # ur.watch_video('Для чего девушкам парень программист?')
    # ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    # ur.watch_video('Для чего девушкам парень программист?')
    # ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    # ur.watch_video('Для чего девушкам парень программист?')
    #
    print(f'\nПроверка входа в другой аккаунт'.upper())
    ur.register('urban_pythonist', 'F8098FM8fjm9jmi', 55)
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    ur.log_in('vasya_pupkin', 'F8098')
    ur.log_in('urban_pythonist', 'F8098')

    print(ur.current_user)
    #
    # print(f'\nПопытка воспроизведения несуществующего видео')
    # ur.watch_video('Лучший язык программирования 2024 года!')
