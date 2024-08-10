class User:
    def __str__(self):
        return f'Логин: {self.nickname}, пароль: {self.password}, возраст: {self.age}'

    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = password
        password_h = hash(password)
        self.age = int(age)


class Video:
    def __str__(self):
        return f'Название: "{self.title}", продолжительность: {self.duration} сек, секунда остановки: {self.time_now}, подходит для детей: {self.ad_mode}'

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = str(title)
        self.duration = int(duration)
        self.time_now = int(time_now)
        self.adult_mode = bool(adult_mode)
        if not self.adult_mode:
            self.ad_mode = 'нет'
        else:
            self.ad_mode = 'да'


class UrTube:

    def __init__(self, users=None, videos=None, current_user=User):
        self.users = users
        if self.users is None:
            self.users = []
        self.videos = videos
        if self.videos is None:
            self.videos = []
        self.current_user = current_user

    def log_in(self, nickname, password):
        if nickname in self.users and hash(password) in self.users:
            self.current_user = nickname

    def register(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
        if [nickname, password, age] not in self.users:
            self.users.append([nickname, password, age])
            self.current_user = nickname
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self, nickname):
        self.nickname = nickname
        self.current_user = None

    def add(self, *args):
        self.videos.append(args)

    def get_videos(self, search_word):
        self.search_word = search_word


ur = UrTube()
v1 = Video('белый конь', 111)
v2 = Video('белки', 59)
v3 = Video('Полосатый в белую полоску', 59)
v4 = Video('Snow', 59)

ur.add(v1, v2, v3, v4)
ur.get_videos('бел')
