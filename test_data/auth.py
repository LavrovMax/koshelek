from dataclasses import dataclass


# Пустые поля
@dataclass
class Auth:
    name: str
    email: str
    password: str
    referral_code: str


# @dataclass
# class ValidDate:
#     name: str = "LavrovMax"
#     email: str = "test_autotest@autotest.ru"
#     password: str = "password123$%^"
#     referral_code: str = "http:"

# Имя меньше 3-х символов
@dataclass()
class InvalidLendingName:
    name: str = "Max"
    email: str = "test_autotest@autotest.ru"
    password: str = "passWord123$%^"
    referral_code: str = ""


# Имя больше 32 символов
@dataclass()
class InvalidLendingNameTwo:
    name: str = "MaxMaxMaxMaxMaxMaxMaxMaxMaxMaxMaxMaxMaxMaxMaxMax"
    email: str = "test_autotest@autotest.ru"
    password: str = "passWord123$%^"
    referral_code: str = ""


# Имя начинающиеся с цифры
@dataclass
class InvalidSymbolsName:
    name: str = "123lavrovMax"
    email: str = "test_autotest@autotest.ru"
    password: str = "passWord123$%^"
    referral_code: str = ""


# Имя содержащие пробел и спецсимвол
@dataclass
class InvalidSymbolsNameTwo:
    name: str = "lavrv M@x"
    email: str = "test_autotest@autotest.ru"
    password: str = "passWord123$%^"
    referral_code: str = ""


# Емейл без @
@dataclass()
class InvalidEmailOne:
    name: str = "LavrovMax"
    email: str = "test_autotest"
    password: str = "passWord123$%^"
    referral_code: str = ""


# Емейл без домена
@dataclass()
class InvalidEmailTwo:
    name: str = "LavrovMax"
    email: str = "test_autotest@.py"
    password: str = "passWord123$%^"
    referral_code: str = ""


# Емейл с спец. символами
@dataclass()
class InvalidEmailThree:
    name: str = "LavrovMax"
    email: str = "aut%tes^@.py"
    password: str = "passWord123$%^"
    referral_code: str = ""


# Пароль <6 символов
@dataclass()
class InvalidPasswordOne:
    name: str = "LavrovMax"
    email: str = "test_autotest@autotest.ru"
    password: str = "pass"
    referral_code: str = ""


# Пароль только из цифр
@dataclass()
class InvalidPasswordTwo:
    name: str = "LavrovMax"
    email: str = "test_autotest@autotest.ru"
    password: str = "12341234"
    referral_code: str = ""


# Пароль без заглавных букв
@dataclass()
class InvalidPasswordThree:
    name: str = "LavrovMax"
    email: str = "test_autotest@autotest.ru"
    password: str = "password123"
    referral_code: str = ""


# пароль более 64 символов
@dataclass()
class InvalidPasswordAgain:
    name: str = "LavrovMax"
    email: str = "test_autotest@autotest.ru"
    password: str = """Буря мглою небо кроет,
Вихри снежные крутя;
То, как зверь, она завоет,
То заплачет, как дитя,
То по кровле обветшалой
Вдруг соломой зашумит,
То, как путник запоздалый,
К нам в окошко застучит.
Наша ветхая лачужка
И печальна и темна.
Что же ты, моя старушка,
Приумолкла у окна?
Или бури завываньем
Ты, мой друг, утомлена,
Или дремлешь под жужжаньем
Своего веретена?
Выпьем, добрая подружка
Бедной юности моей,
Выпьем с горя; где же кружка?
Сердцу будет веселей.
Спой мне песню, как синица
Тихо за морем жила;
Спой мне песню, как девица
За водой поутру шла."""
    referral_code: str = ""


@dataclass
class InvalidReferralKode:
    name: str = "LavrovMax"
    email: str = "test_autotest@autotest.ru"
    password: str = "passWord123$%^"
    referral_code: str = "www"
