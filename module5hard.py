import hashlib
import time


class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = self._hash_password(password)
        self.age = age

    def _hash_password(self, password: str) -> int:
        """Метод для хэширования пароля"""
        return int(hashlib.sha256(password.encode()).hexdigest(), 16)

    def check_password(self, password: str) -> bool:
        """Метод для проверки пароля"""
        return self.password == self._hash_password(password)

    def __repr__(self):
        return f"User(nickname={self.nickname}, age={self.age})"

    def __eq__(self, other):
        """Сравнение пользователей по их никам"""
        return self.nickname == other.nickname


class Video:
    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __repr__(self):
        return f"Video(title={self.title}, duration={self.duration}, adult_mode={self.adult_mode})"

    def __eq__(self, other):
        """Сравнение видео по названию"""
        return self.title == other.title

    def __contains__(self, keyword: str):
        """Поиск ключевого слова в названии видео (без учета регистра)"""
        return keyword.lower() in self.title.lower()


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname: str, password: str):
        """Метод для авторизации пользователя"""
        for user in self.users:
            if user.nickname == nickname and user.check_password(password):
                self.current_user = user
                print(f"Вы вошли как {nickname}")
                return
        print("Неправильное имя пользователя или пароль")

    def register(self, nickname: str, password: str, age: int):
        """Метод для регистрации пользователя"""
        if any(user.nickname == nickname for user in self.users):
            print(f"Пользователь {nickname} уже существует")
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user
            print(f"Регистрация успешна. Вы вошли как {nickname}")

    def log_out(self):
        """Метод для выхода из аккаунта"""
        if self.current_user:
            print(f"Вы вышли из аккаунта {self.current_user.nickname}")
            self.current_user = None
        else:
            print("Никто не вошел в систему")

    def add(self, *videos):
        """Метод для добавления видео на платформу"""
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)
                print(f"Видео '{video.title}' добавлено")
            else:
                print(f"Видео '{video.title}' уже существует")

    def get_videos(self, search_word: str):
        """Метод для поиска видео по ключевому слову"""
        search_word = search_word.lower()
        return [video.title for video in self.videos if search_word in video]

    def watch_video(self, title: str):
        """Метод для просмотра видео"""
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        video = next((v for v in self.videos if v.title == title), None)

        if video is None:
            print("Видео не найдено")
            return

        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        print(f"Вы смотрите '{video.title}'")
        for second in range(video.time_now, video.duration):
            print(f"{second + 1}", end=" ")
            time.sleep(1)  # Пауза между секундами для имитации проигрывания
        print("Конец видео")
        video.time_now = 0

    def __repr__(self):
        return f"UrTube(users={self.users}, videos={self.videos}, current_user={self.current_user})"


# Код для проверки
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
