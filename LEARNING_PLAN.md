# 📚 План обучения для студента DjangoFirstShop

## Цель плана
Систематическое изучение тем, в которых были допущены ошибки при разработке проекта DjangoFirstShop. План составлен на основе code review и охватывает как фундаментальные концепции Python, так и специфику Django/DRF разработки.

---

## 🔴 Модуль 1: Безопасность Django-приложений (Критический приоритет)

### 1.1 Управление секретами и конфигурацией
**Проблема в проекте:** SECRET_KEY и пароли БД захардкожены в коде

**Что изучить:**
- Переменные окружения в Python (os.environ, os.getenv)
- Библиотеки для управления конфигурацией:
  - `python-decouple`
  - `django-environ`
  - `python-dotenv`
- Файл `.env` и его структура
- Различия между dev/staging/prod окружениями

**Практика:**
1. Создать `.env` файл с переменными:
   ```
   SECRET_KEY=your-secret-key
   DEBUG=False
   DATABASE_URL=postgresql://user:pass@localhost/db
   ```
2. Переписать `settings.py` с использованием `python-decouple`
3. Добавить `.env` в `.gitignore`
4. Создать `.env.example` с шаблоном переменных

**Ресурсы:**
- Django documentation: "Settings" → "Security"
- OWASP Top 10 (A02:2021 – Cryptographic Failures)
- 12-Factor App methodology (Config section)

**Время:** 3-4 часа

---

### 1.2 Django Security Best Practices
**Проблема в проекте:** DEBUG=True, пустой ALLOWED_HOSTS, отсутствие HTTPS настроек

**Что изучить:**
- `DEBUG`, `ALLOWED_HOSTS`, `SECRET_KEY` — назначение и настройка
- HTTPS и SSL/TLS в Django:
  - `SECURE_SSL_REDIRECT`
  - `SESSION_COOKIE_SECURE`
  - `CSRF_COOKIE_SECURE`
  - `SECURE_HSTS_SECONDS`
- CSRF protection в Django
- Защита от SQL injection (Django ORM автоматически защищает, но нужно понимать как)
- XSS protection и Django templates

**Практика:**
1. Настроить production-ready `settings.py`
2. Пройти Django Security Checklist
3. Использовать `python manage.py check --deploy`

**Ресурсы:**
- Django Security documentation
- Django deployment checklist
- OWASP Django Security Cheat Sheet

**Время:** 4-5 часов

---

## 🟠 Модуль 2: Git и контроль версий

### 2.1 Продвинутый .gitignore
**Проблема в проекте:** db.sqlite3 попал в репозиторий, tmp_my.py не игнорируется

**Что изучить:**
- Как работает `.gitignore` (паттерны, приоритеты)
- Что никогда не должно попадать в git:
  - Базы данных (*.sqlite3, *.db)
  - Логи (*.log)
  - Виртуальные окружения (venv/, .venv/)
  - IDE настройки (.idea/, .vscode/)
  - Секреты (.env, *.pem, *.key)
  - Временные файлы (__pycache__, *.pyc)
  - Медиафайлы (media/)
- Удаление уже отслеживаемых файлов: `git rm --cached`
- Глобальный `.gitignore` для всех проектов

**Практика:**
1. Создать полный `.gitignore` для Django проектов
2. Удалить db.sqlite3 из истории (если нужно — `git filter-branch`)
3. Настроить глобальный `.gitignore` в `~/.gitignore_global`

**Ресурсы:**
- GitHub Python .gitignore template
- gitignore.io для генерации

**Время:** 2 часа

---

### 2.2 Git workflow и commit messages
**Проблема в проекте:** Закомментированный код вместо удаления, отладочные print в коммитах

**Что изучить:**
- Git best practices для команд
- Semantic commit messages (conventional commits)
- Когда делать commit (atomic commits)
- Git hooks для автоматических проверок (pre-commit)
- Code review процесс

**Практика:**
1. Установить pre-commit hooks:
   ```bash
   pip install pre-commit
   pre-commit install
   ```
2. Настроить проверки:
   - ruff для линтинга
   - черный список слов (print, TODO без issue)
3. Переписать 5 последних коммитов с правильными сообщениями

**Время:** 2-3 часа

---

## 🟡 Модуль 3: Django REST Framework

### 3.1 Базовая настройка и конфигурация DRF
**Проблема в проекте:** DRF не добавлен в INSTALLED_APPS, отсутствует в requirements.txt

**Что изучить:**
- Установка и подключение DRF
- Основные компоненты:
  - Serializers
  - ViewSets и Generic Views
  - Routers
- Настройка в `settings.py`:
  ```python
  REST_FRAMEWORK = {
      'DEFAULT_AUTHENTICATION_CLASSES': [...],
      'DEFAULT_PERMISSION_CLASSES': [...],
      'DEFAULT_PAGINATION_CLASS': '...',
  }
  ```
- Различия между APIView, GenericAPIView, ViewSet

**Практика:**
1. Правильно подключить DRF в проект
2. Создать простой API для модели Product:
   - Serializer
   - ViewSet
   - Router
3. Протестировать через DRF Browsable API

**Ресурсы:**
- DRF Official Tutorial (все части)
- DRF documentation: Quickstart

**Время:** 6-8 часов

---

### 3.2 Аутентификация и JWT в DRF
**Проблема в проекте:** JWT реализован вручную с ошибками, не используется djangorestframework-simplejwt

**Что изучить:**
- Виды аутентификации в DRF:
  - Session Authentication
  - Token Authentication
  - JWT Authentication
- Библиотека `djangorestframework-simplejwt`:
  - Установка и настройка
  - Token obtain/refresh endpoints
  - Custom claims
  - Token blacklisting
- Разница между access и refresh токенов
- Где хранить токены на фронтенде (безопасность)

**Практика:**
1. Удалить самописную JWT реализацию
2. Установить `djangorestframework-simplejwt`
3. Настроить:
   ```python
   REST_FRAMEWORK = {
       'DEFAULT_AUTHENTICATION_CLASSES': [
           'rest_framework_simplejwt.authentication.JWTAuthentication',
       ],
   }
   ```
4. Создать endpoints для login/refresh/logout
5. Протестировать через Postman/curl

**Ресурсы:**
- DRF-SimpleJWT documentation
- JWT.io для понимания структуры токенов
- OWASP JWT Security Cheat Sheet

**Время:** 5-6 часов

---

### 3.3 Permissions и Authorization
**Проблема в проекте:** Нет проверки прав доступа для создания продукта

**Что изучить:**
- Встроенные permission classes:
  - `IsAuthenticated`
  - `IsAdminUser`
  - `IsAuthenticatedOrReadOnly`
- Создание custom permissions
- Object-level permissions
- Различие между authentication и authorization

**Практика:**
1. Добавить `@permission_classes([IsAuthenticated])` на нужные views
2. Создать custom permission `IsOwnerOrReadOnly`
3. Применить к Product CRUD операциям
4. Написать тесты для проверки прав доступа

**Время:** 4-5 часов

---

## 🟢 Модуль 4: Django Models и ORM

### 4.1 Продвинутые возможности моделей
**Проблема в проекте:** Нет auto_now_add, хранится вычисляемое значение average_rating

**Что изучить:**
- Auto-поля:
  - `auto_now_add` — устанавливается при создании
  - `auto_now` — обновляется при каждом save()
- Вычисляемые поля vs хранимые:
  - `@property` для динамических полей
  - `annotate()` для агрегаций
  - Денормализация и когда она оправдана
- Сигналы Django:
  - `pre_save`, `post_save`
  - Когда использовать, а когда избегать
- Методы моделей и менеджеры

**Практика:**
1. Исправить `Product.created` на `auto_now_add=True`
2. Переделать `average_rating` на property:
   ```python
   @property
   def average_rating(self):
       return self.ratings.aggregate(Avg('score'))['score__avg'] or 0
   ```
3. Если нужна оптимизация — использовать `select_related` и `prefetch_related`

**Ресурсы:**
- Django Models documentation
- Django ORM optimization
- Two Scoops of Django (Models chapter)

**Время:** 5-6 часов

---

### 4.2 Django ORM: оптимизация запросов
**Проблема в проекте:** Нет пагинации, возможны N+1 запросы

**Что изучить:**
- Проблема N+1 запросов
- `select_related()` для ForeignKey
- `prefetch_related()` для ManyToMany и обратных ForeignKey
- `only()` и `defer()` для выбора полей
- `annotate()` и `aggregate()`
- Django Debug Toolbar для анализа запросов
- Индексы в БД (`db_index=True`)

**Практика:**
1. Установить Django Debug Toolbar
2. Найти N+1 запросы в проекте
3. Оптимизировать с помощью `select_related`/`prefetch_related`
4. Добавить пагинацию для списка продуктов:
   ```python
   from django.core.paginator import Paginator
   ```

**Ресурсы:**
- Django ORM Cookbook
- Django documentation: Database access optimization
- Query optimization guide

**Время:** 6-7 часов

---

## 🔵 Модуль 5: Тестирование Django-приложений

### 5.1 Основы тестирования
**Проблема в проекте:** Пустые tests.py во всех приложениях

**Что изучить:**
- Виды тестов:
  - Unit tests (изолированные тесты функций/методов)
  - Integration tests (тесты взаимодействия компонентов)
  - Functional tests (end-to-end тесты)
- Django TestCase vs unittest.TestCase
- Фикстуры и test database
- `setUp()`, `tearDown()`, `setUpTestData()`
- Запуск тестов: `python manage.py test`

**Практика:**
1. Написать тесты для модели Product:
   ```python
   from django.test import TestCase
   
   class ProductModelTest(TestCase):
       def setUp(self):
           self.product = Product.objects.create(...)
       
       def test_str_representation(self):
           ...
       
       def test_average_rating_calculation(self):
           ...
   ```
2. Написать тесты для views (аутентификация, рейтинг)
3. Достичь coverage > 70%

**Ресурсы:**
- Django Testing documentation
- Test-Driven Development with Python (Harry Percival)
- pytest-django (альтернатива встроенному тестировщику)

**Время:** 8-10 часов

---

### 5.2 Тестирование API (DRF)
**Что изучить:**
- `APITestCase` vs `TestCase`
- `APIClient` для тестирования endpoints
- Тестирование аутентификации (JWT tokens)
- Моки и фикстуры для API тестов
- Status codes (200, 201, 400, 401, 403, 404)

**Практика:**
1. Написать тесты для API:
   ```python
   from rest_framework.test import APITestCase
   
   class ProductAPITest(APITestCase):
       def test_create_product_authenticated(self):
           self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
           response = self.client.post('/api/products/', data)
           self.assertEqual(response.status_code, 201)
       
       def test_create_product_unauthenticated(self):
           response = self.client.post('/api/products/', data)
           self.assertEqual(response.status_code, 401)
   ```
2. Тесты для рейтинга (проверка диапазона 1-5, повторное голосование)
3. Использовать `factory_boy` для создания тестовых данных

**Ресурсы:**
- DRF Testing documentation
- factory_boy documentation
- Coverage.py для измерения покрытия

**Время:** 6-8 часов

---

## 🟣 Модуль 6: Python Best Practices

### 6.1 Работа с датой и временем
**Проблема в проекте:** Использование datetime.now() без timezone

**Что изучить:**
- Модуль `datetime`:
  - `datetime.now()` vs `datetime.now(timezone.utc)`
  - `datetime.utcnow()` — почему deprecated
- Timezone-aware vs naive datetime
- Django настройки:
  - `USE_TZ = True`
  - `TIME_ZONE = 'UTC'`
- Библиотека `pytz` (в старых проектах) vs `zoneinfo` (Python 3.9+)
- Работа с UTC в БД, конвертация в локальные зоны на фронте

**Практика:**
1. Исправить все `datetime.now()` на `datetime.now(timezone.utc)`
2. Проверить, что `USE_TZ = True` в settings
3. Написать функцию для конвертации UTC → user timezone

**Ресурсы:**
- Python datetime documentation
- Django timezone documentation
- pytz vs zoneinfo comparison

**Время:** 3-4 часа

---

### 6.2 Принципы SOLID, DRY, KISS, YAGNI
**Проблема в проекте:** Дублирование кода между user и user_auth, неиспользуемое приложение user

**Что изучить:**
- **SOLID**:
  - Single Responsibility Principle (один класс = одна ответственность)
  - Open/Closed Principle (открыт для расширения, закрыт для изменения)
  - Liskov Substitution Principle
  - Interface Segregation Principle
  - Dependency Inversion Principle
- **DRY** (Don't Repeat Yourself):
  - Вынесение общего кода в функции/классы
  - Наследование и миксины в Django
- **KISS** (Keep It Simple, Stupid):
  - Простота > сложность
  - Не переусложнять архитектуру
- **YAGNI** (You Aren't Gonna Need It):
  - Не писать код "на будущее"

**Практика:**
1. Удалить приложение `user` (полностью неиспользуемое)
2. Убрать дублирование функций между модулями
3. Рефакторинг: создать базовые классы для повторяющейся логики
4. Code review своего кода через призму SOLID

**Ресурсы:**
- Clean Code (Robert Martin)
- Refactoring: Improving the Design of Existing Code (Martin Fowler)
- SOLID principles in Python examples

**Время:** 6-8 часов

---

### 6.3 Отладка и логирование
**Проблема в проекте:** print() для отладки, закомментированный debug-код

**Что изучить:**
- Почему `print()` это плохо в production
- Модуль `logging`:
  - Уровни: DEBUG, INFO, WARNING, ERROR, CRITICAL
  - Handlers (console, file, email)
  - Formatters
- Django logging конфигурация в settings.py
- Structured logging (JSON logs)
- Debugging tools:
  - `pdb` (Python debugger)
  - Django Debug Toolbar
  - `ipdb` (улучшенный pdb)

**Практика:**
1. Настроить logging в Django:
   ```python
   LOGGING = {
       'version': 1,
       'handlers': {
           'file': {
               'level': 'INFO',
               'class': 'logging.FileHandler',
               'filename': 'debug.log',
           },
       },
       'loggers': {
           'django': {
               'handlers': ['file'],
               'level': 'INFO',
           },
       },
   }
   ```
2. Заменить все `print()` на `logger.info()`, `logger.error()`
3. Удалить закомментированный debug-код
4. Научиться использовать `pdb.set_trace()` для отладки

**Ресурсы:**
- Python logging documentation
- Django logging documentation
- Real Python: Logging in Python

**Время:** 4-5 часов

---

## 🟤 Модуль 7: Django архитектура и паттерны

### 7.1 Разделение settings на окружения
**Что изучить:**
- Структура `settings/`:
  ```
  settings/
    __init__.py
    base.py      # Общие настройки
    dev.py       # Development
    test.py      # Testing
    prod.py      # Production
  ```
- Переменная окружения `DJANGO_SETTINGS_MODULE`
- Различия между окружениями:
  - Dev: DEBUG=True, sqlite, less security
  - Prod: DEBUG=False, PostgreSQL, HTTPS, strict security

**Практика:**
1. Создать структуру `settings/`
2. Вынести общие настройки в `base.py`
3. Настроить dev/prod с наследованием от base
4. Обновить `manage.py` и `wsgi.py`

**Ресурсы:**
- Two Scoops of Django (Settings chapter)
- Django Cookiecutter template (пример структуры)

**Время:** 3-4 часа

---

### 7.2 Static и Media files
**Проблема в проекте:** Не настроен STATIC_ROOT

**Что изучить:**
- Различия:
  - `STATIC_FILES` — CSS/JS/images в коде
  - `MEDIA_FILES` — файлы пользователей (uploads)
- Настройки:
  - `STATIC_URL`, `STATIC_ROOT`, `STATICFILES_DIRS`
  - `MEDIA_URL`, `MEDIA_ROOT`
- Команда `collectstatic`
- Раздача статики в production (nginx/whitenoise)

**Практика:**
1. Настроить в settings:
   ```python
   STATIC_ROOT = BASE_DIR / 'staticfiles'
   MEDIA_ROOT = BASE_DIR / 'media'
   ```
2. Добавить в urls.py для development:
   ```python
   from django.conf.urls.static import static
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   ```
3. Установить `whitenoise` для production

**Время:** 2-3 часа

---

### 7.3 Django Views: Function-Based vs Class-Based
**Что изучить:**
- Function-Based Views (FBV):
  - Простота
  - Явный контроль flow
- Class-Based Views (CBV):
  - Наследование и переиспользование
  - Generic views (ListView, DetailView, CreateView, etc.)
  - Миксины (LoginRequiredMixin, etc.)
- Когда использовать FBV vs CBV

**Практика:**
1. Переписать 2-3 FBV на CBV с использованием Generic Views
2. Создать custom mixin для проверки владельца объекта
3. Сравнить количество кода (до/после)

**Ресурсы:**
- Classy Class-Based Views (ccbv.co.uk)
- Django CBV documentation
- Two Scoops of Django (Views chapter)

**Время:** 5-6 часов

---

## ⚫ Модуль 8: DevOps и Deployment

### 8.1 Docker best practices
**Проблема в проекте:** Закомментированный код в Dockerfile, пароли в docker-compose

**Что изучить:**
- Multi-stage builds
- Слои и кеширование в Docker
- `.dockerignore`
- Docker secrets для паролей
- Docker Compose:
  - Environment variables
  - Volumes для данных
  - Depends_on и health checks

**Практика:**
1. Оптимизировать Dockerfile:
   ```dockerfile
   FROM python:3.11-slim as builder
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install --user -r requirements.txt
   
   FROM python:3.11-slim
   COPY --from=builder /root/.local /root/.local
   ...
   ```
2. Вынести пароли БД в `.env`
3. Создать `.dockerignore`

**Ресурсы:**
- Docker Best Practices
- Docker Compose documentation
- Docker for Django developers

**Время:** 4-5 часов

---

### 8.2 CI/CD и автоматизация
**Что изучить:**
- GitHub Actions / GitLab CI
- Автоматический запуск тестов при push
- Линтинг (ruff, black, mypy)
- Coverage reports
- Автоматический deploy

**Практика:**
1. Создать `.github/workflows/tests.yml`:
   ```yaml
   name: Tests
   on: [push, pull_request]
   jobs:
     test:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v2
         - name: Run tests
           run: |
             pip install -r requirements.txt
             python manage.py test
   ```
2. Добавить badge со статусом тестов в README

**Время:** 3-4 часа

---

## 📊 Итоговый проект: Рефакторинг DjangoFirstShop

После прохождения всех модулей — полный рефакторинг проекта:

### Checklist:
- [ ] Все секреты вынесены в `.env`
- [ ] DRF правильно настроен с JWT
- [ ] Добавлены permissions на все endpoints
- [ ] Написаны тесты (coverage > 80%)
- [ ] Удалено дублирование кода
- [ ] Убран весь debug-код
- [ ] Настроены dev/prod settings
- [ ] Документация в README.md
- [ ] API документация (Swagger/ReDoc)
- [ ] Docker оптимизирован
- [ ] CI/CD pipeline работает
- [ ] Pre-commit hooks настроены
- [ ] Все замечания из code review исправлены

**Время на рефакторинг:** 10-15 часов

---

## 📈 Оценка прогресса

### Этап 1 (Критический) — 2 недели
- Модуль 1: Безопасность
- Модуль 2: Git
- Модуль 3.1-3.2: DRF + JWT

### Этап 2 (Основной) — 3 недели
- Модуль 3.3: Permissions
- Модуль 4: Models и ORM
- Модуль 5: Тестирование

### Этап 3 (Продвинутый) — 2 недели
- Модуль 6: Python Best Practices
- Модуль 7: Django архитектура
- Модуль 8: DevOps

### Этап 4 (Итоговый) — 1 неделя
- Полный рефакторинг проекта

**Общее время:** 8 недель (при 10-15 часах в неделю)

---

## 🎯 Дополнительные ресурсы

### Книги:
1. **Two Scoops of Django** — must-read для Django разработчиков
2. **Django for APIs** by William Vincent
3. **Clean Code** by Robert Martin
4. **Test-Driven Development with Python** by Harry Percival

### Онлайн-курсы:
1. Django REST Framework официальный туториал
2. TestDriven.io — Django курсы
3. Real Python — Django треки

### Инструменты:
1. **Postman** — тестирование API
2. **Django Debug Toolbar** — оптимизация запросов
3. **Coverage.py** — измерение покрытия тестами
4. **pre-commit** — автоматические проверки
5. **Black** — автоформатирование кода
6. **mypy** — статическая типизация

---

## ✅ Критерии завершения обучения

Студент готов к работе над реальными проектами, если умеет:
1. ✅ Настроить Django проект с нуля (security, settings, DB)
2. ✅ Создать полноценный REST API с аутентификацией
3. ✅ Написать тесты с покрытием >80%
4. ✅ Оптимизировать ORM запросы
5. ✅ Работать с Git профессионально
6. ✅ Контейнеризовать приложение
7. ✅ Применять SOLID принципы
8. ✅ Деплоить приложение в production

**Удачи в обучении!** 🚀
