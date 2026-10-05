#Задача 1. Переменные и типы. Заведи переменные для результата теста: test_name (строка), 
# duration (дробное), passed (bool), retries (целое), error (None). 
# Выведи каждую вместе с её типом через type().

test_name = 'login_flow'
print(f"{test_name} {type(test_name)}")

duration = 1.5
print(f"{duration} {type(duration)}")

passed = False
print(f"{passed} {type(passed)}")

retries = 0
print(f"{retries} {type(retries)}")

error = None
print(f"{error} {type(error)}")

#Задача 2. f-строки. 
# Выведи строку вида Test login_flow: PASSED in 1.24s. 
# Статус должен быть заглавными буквами и зависеть от passed, 
# длительность — ровно 2 знака после запятой, даже если duration = 1.2.

status = 'PASSED' if passed else 'FAILED'
print(f"Test {test_name}: {status} in {duration:.2f}s")

#Задача 3. Арифметика. Есть 137 тестов и 4 воркера. 
# Посчитай через // и %, сколько тестов получит каждый воркер поровну 
# и сколько останется лишних. Выведи результат одной f-строкой.

tests = 137
workers = 4

tests_per_worker = tests // workers
remainder = tests % workers

print(f'tests for workers: {tests_per_worker} and tests left: {remainder}')

#Задача 4. Сначала угадай, потом проверь. Напиши в комментариях, что вернёт каждое выражение, и только потом запусти:


# 0.1 + 0.2 == 0.3 # false
# [] == [] # true
# [] is [] # false
# None == False # false
# bool("False") # true
# bool(0), bool(""), bool([]), bool("0") #true

#Где ошиблась, разберём почему. Это любимые вопросы на интервью.

#Задача 5. Условия. Есть переменная pass_rate (процент прошедших тестов). 
# Выведи release OK, если он 95 или выше; 
# needs review, если от 80 до 95; 
# release blocked, если ниже 80;
#  invalid data, если меньше 0 или больше 100. 
# Проверь на значениях 100, 95, 94.9, 80, 79, -1 и 150.

pass_rate = -1


if pass_rate > 100 or pass_rate < 0:
    print('invalid data')
elif pass_rate >= 95:
    print('release OK')
elif pass_rate >= 80 and pass_rate < 95:
    print('needs review')
else:
    print('release blocked')


     