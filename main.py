import secrets
import string

# Определение длины пароля
password_length = 12

# Определение набора символов для генерации пароля
alphabet = string.ascii_letters + string.digits + string.punctuation

# Создание генератора случайных байтов
generator = secrets.SystemRandom()

# Генерация пароля
password = ''.join(generator.choice(alphabet) for _ in range(password_length))

# Проверка сложности пароля
if not (any(char.islower() for char in password)
        and any(char.isupper() for char in password)
        and any(char.isdigit() for char in password)
        and any(char in string.punctuation for char in password)):
    # Если пароль не соответствует минимальным требованиям сложности, перегенерируем его
    password = ''.join(generator.choice(alphabet) for _ in range(password_length))

# Вывод сгенерированного пароля
print("Сгенерированный пароль: ", password)



















