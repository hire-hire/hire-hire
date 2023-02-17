

# План тестирования
# сайт

<picture>
 <img alt="YOUR-ALT-TEXT" src="photo_2023-02-16_17-09-13.jpg">
</picture>

## Основная информация

| Продукт       | НаймиНайми           |   
| ------------- |:-------------:| 
| Автор      | Арсентьев Константин | 
|Дата |16.02.23 |  
|Версия |1,5 |  
|Статус |В работе |  
       



 Содержание: 
### 1. Введение
#### 1.1. Основная информация
#### 1.2. Цель
### 2. Цели и задачи
### 3. Область тестирования проекта
### 4. Cтратегия тестирования
#### 4.1. Подход к тестированию
#### 4.2. Уровни тестирования
#### 4.3. Функциональное тестирование
#### 4.4. Цикл тестирования
#### 4.5. Группы тестов используемые на проекте
#### 4.6. Отчеты об ошибках
### 5. Ресурсы 
#### 5.1. Инструменты 
#### 5.2. Список браузеров 
#### 5.3. Список устройств
#### 5.4. Список разрешений
### 6. Риски процесса тестирования
	

### 1. Введение
	
#### 1.1. Основная информация
Документ представляет собой описание методов и подходов, которые используются отделом QA для проведения тестирования сайта. Он также содержит общие условия, касающиеся уровня качества выпускаемого программного продукта, которые учитываются тестировщиками.
План тестирования используется как тестировщиками, так и менеджерами и разработчиками.
#### 1.2. Цель
Тест-план проекта преследует следующие цели:
- Анализ существующей информации о проекте и декомпозиция программных компонентов, подлежащих тестированию
- Описать стратегии тестирования, которые будут использоваться.
- Определить критерии готовности взятия в работу продукта
- Определить критерии готовности продукта.
- Описать обязанности участников команды

### 2. Цели и задачи
Цель: [TODO]
 - Задачи: 
    - Внедрить 
        - PR-Review
        - Re-Testing
        - BUG-Tracking
        - BUG-Analysis
        - BUG-Management 
        - Status Dashboard

| Зоны ответственности | Ответственный |Ответственный |Ответственный |
| :---:       |     :---:      |     :---:      |     :---:      |
| PR-Review   | Senior Dev    |[TODO]     |[TODO]     |
| Re-Testing   | отдел QA     |[TODO]     |[TODO]     |
| BUG-Tracking   | Senior Dev     | QA Manager     | Team-/Tech-lead     |
| BUG-Analysis   | Senior Dev     |QA Manager     | Team-/Tech-lead     |
| BUG-Management   | Senior Dev     |QA Manager     | Team-/Tech-lead     |
| Status Dashboard   | QA Engineer     | PO     |PM     |


### 3.Область тестирования сайта

Объект тестирования - web – приложение НаймиНайми находящееся по адресу
http://www. [TODO]

Компоненты делятся на следующие группы:
|Сокращение|Группа|
|:---:|:---:|
|DB|Data Base|
|BE|Back-end logic|
|FE|Front-end logic|
|GI|Graphical interface|

Компоненты приложения:

1. Главная страница:
    1. Хэдер 
        - Логотип  FE/GI
        - Кнопка «Пройти собеседование» FE/GI
        - Наша команда FE/GI
        - Вход/Личный кабинет FE/GI
    2. Боди 
        - О проекте FE/GI
        - Блок «Пройти собеседование» FE/GI
        - Блок «Голодные игры» FE/GI
        - Активен только по параметру включаемому администратором FE/GI
    3. Футер
        - Копирайт FE/GI
        - Соглашение FE/GI
        - Правила сервиса FE/GI
        - Контакты FE/GI

2. Личный кабинет пользователя:
    1. Регистрация FE/BE/GI/DB
    2. Авторизация и аутентификация FE/BE/GI/DB
    3. Выход из учетной записи FE/BE/GI
    4. Изменение данных учетной записи FE/BE/GI/DB

3. Личный Кабинет Супер-Администратора
    1. Авторизация и аутентификация FE/BE/GI/DB
    2. Выход из учетной записи FE/BE/GI
    3. Изменения данных учетной записи FE/BE/GI/DB
    4. Управление командой (Включение юзерам «Голодные игры») FE/BE/GI/DB

4. Пройти собеседование
    1. Выбор специальности FE/BE/GI/DB
        - Список специальностей 
    2. Выбор количество вопросов FE/BE/GI/DB
        - 10 вопросов (по умолчанию) 
        - 20 вопросов 
        - 30 вопросов  
    3. Выбор грейда FE/BE/GI/DB
        - Джун (по умолчанию)
        - Миддл
        - Синьор
    4. Вопрос FE/BE/GI/DB
        - Вопрос
        - Поле для ввода ответа
        - Показать правильный ответ
        - Следующий вопрос
    5. Окончание собеседование FE/GI
    6. Счетчик вопросов BE/DB
        - Вопрос не повторяется у аутентифицированного пользователя
        - Когда выбранное количество вопросов превышает количество оставшихся вопросов у юзера список для пользователя обнуляется
5. Голодные игры FE/BE/GI/DB
    1. Выбор специальности FE/BE/GI/DB
        - Список специальностей
    2. Выбор количество вопросов FE/BE/GI/DB
        - 10 вопросов (по умолчанию)
        - 20 вопросов
        - 30 вопросов
    3. Выбор грейда FE/BE/GI/DB
        - Джун (по умолчанию)
        - Миддл
        - Синьор
    4. Вопрос FE/BE/GI/DB
        - Вопрос
        - Показать правильный ответ
        - Следующий вопрос
        - Radio выбор (Игрок 1, Игрок 2, Неправильный ответ)
    5. Итог «Голодных игр» FE/BE/GI
        - Счетчик количества выбранных radio данных

6. Административная панель
    1. Вход FE/BE/GI/DB
        - Авторизация и аутентификация
        - Выход  из учетной записи
    2. Панель FE/BE/GI/DB
        - Управление разделом «Наша Команда»
            - Просмотр информации
            - Добавление информации
            - Редактирование информации
            - Удаление информации
        -  Управление разделом «Вопросы»
            - Просмотр информации
            - Добавление информации
            - Редактирование информации
            - Удаление информации
        - Управление разделом «Контакты»
            - Просмотр информации
            - Добавление информации
            - Редактирование информации
            - Удаление информации
        - Управление разделом «Личный кабинет»
            - Просмотр информации
            - Добавление информации
            - Редактирование информации
            - Удаление информации
    
### 4. Стратегия тестирования

#### 4.1. Подход к тестированию

##### 1. GI – Graphical interface
- Объекты тестирования: кодовая база, GUI
- Уровни тестирования: Unit Tests, System Integration Tests, System Tests, e2e-testing
- Вид тестирования: Non-Functional, Change-Related
- Техники тестирования: Black-box, Experience-Based
- Степень автоматизации: UT - full auto, ST - manual/semi-automated
- Анализ: статический -  Lint, Code Review

##### 2. FE – Front-end logic
- Объекты тестирования: кодовая база, GUI
- Уровни тестирования: Unit Tests, System Integration Tests, System Tests, e2e-testing
- Вид тестирования: White Box, Functional, Non-Functional, Change-Related
- Техники тестирования: Black-box, White-Box, Experience-Based
- Степень автоматизации: UT - full auto, SIT - Hybrid/semi-automated (Swagger, Postman), ST - manual/semi-automated
- Анализ: статический - Lint, Code Review

##### 3. BE – Back-end logic
- Объекты тестирования: кодовая база, API
- Уровни тестирования: Unit Tests, System Integration Tests, System Tests
- Вид тестирования: White Box, Functional, Non-Functional, Change-Related
- Техники тестирования: Black-box, White-Box, Experience-Based
- Степень автоматизации: UT - full auto, SIT - Hybrid/semi-automated (Swagger, Postman), ST - manual/semi-automated
Анализ: статический - Lint, Code Review

##### 4. DB – Data Base
- Объекты тестирования: кодовая база, API
- Уровни тестирования: Unit Tests, System Integration Tests, System Tests
- Вид тестирования: White Box, Functional, Non-Functional, Change-Related
- Техники тестирования: Black-box, White-Box, Experience-Based
- Степень автоматизации: UT - full auto, SIT - Hybrid/semi-automated (Swagger, Postman)
- Анализ: статический


#### 4.2. Уровни тестирования	
[TODO]
#### 4.3. Функциональное тестирование
[TODO]
#### 4.4. Цикл тестирования
[TODO]
#### 4.5. Группы тестов используемые на проекте
[TODO]


##### 4.6. Сообщения об ошибках
Отчеты об ошибках имеют следующие цели:
- Предоставлять разработчикам и другим сторонам информацию о произошедших негативных событиях, чтобы они могли определить побочные эффекты, изолировать проблему с минимальными затратами на воспроизведение и исправить потенциальные дефекты по мере необходимости, или решать проблемы другими способами
- Обеспечить руководителей тестирования инструментами отслеживания качества продукта и влияния на тестирование (например, если сообщается о большом количестве дефектов, то тестировщики будут вынуждены тратить много времени на отчетность по найденным дефектам вместо того, чтобы запускать тесты; следовательно, нужно больше подтверждающего тестирования)
- Предоставлять команде общую картину текущего уровня качества программного обеспечения.

Степень критичности ошибок:

Серьезность (Severity) бага
Severity — это атрибут, характеризующий влияние бага на общую функциональность тестируемого продукта.

Степень серьезности бага больше касается функциональности, поэтому она присваивается тестировщиком. 

Пример классификации серьезности багов:
|Метка|Название|Описание|
|:---:|:---:|:---:|
|Blocker|Блокирующая ошибка|Она делает невозможной всю последующую работу с программой. Для возобновления работы нужно исправить Blocker. Баги, ведущие к бизнес потерям: критически большое уменьшение количества использования приложения; уменьшение доходов, понижение рейтинга приложения; расхождение реализованного и планов маркетологов|
|Critical|Критическая ошибка|Нарушает работу основного функционала. Баг проявляется постоянно и делает невозможным использование основных функций программы. Нарушения в логике работы бизнес-фич|
|Major|Существенный баг|Затрудняет работу основного функционала или делает невозможным использование дополнительных функций. Нарушения в логике работы бизнес-фич|
|Minor|Незначительный баг|На функционал системы влияет относительно мало, затрудняет использование  дополнительных функций. Для обхода этого бага могут быть очевидные пути. Относится к удобству работы команды и к бизнес-фичам, но не мешает их работе никаким образом|
|Trivial|Тривиальный баг|Не влияет на функционал проекта, но ухудшает общее впечатление от работы с продуктом. Относится к удобству работы команды и к бизнес-фичам, но не мешает их работе никаким образом|


Приоритет (Priority) бага
Приоритет — атрибут, определяющий скорость устранения бага.

Приоритет бага сперва определяет инициатор, но в дальнейшем он корректируется менеджером продукта. 

Виды приоритетов:
|Название|Описание|
|:---:|:---:|
|Blocker||
Top. Наивысший приоритет. Назначается экстренным ситуациям, которые очень отрицательно влияют на продукт или даже бизнес компании. Такие баги нужно устранять немедленно.
High. Высокий приоритет. Назначается багам, которые должны быть устранены в первую очередь.
Normal. Обычный приоритет, назначается по умолчанию. Эти баги устраняются во вторую очередь, в штатном порядке.
Low. Низкий приоритет. Назначается багам, не влияющим на функционал. Исправление таких багов происходит в последнюю очередь, если есть время и ресурсы.

Приоритет
Top/High/Normal/Low
Серьезность
Blocker/Critical/Major/Minor/Trivial

Каждый баг-репорт содержит следующую информацию о дефекте:
|Поле|Важность|
|---|:---:|
|ID|Обязательно|
|Название баг-репорта|Обязательно|
|Краткое описание|Опционально|
|Предусловия|Опционально|
|Шаги для воспроизведения ошибки|Обязательно|
|Ожидаемый результат|Обязательно|
|Фактический результат|Обязательно|
|Дополнительная информация/скриншоты/видеозаписи|Опционально|
|Браузер, в котором проводились тесты|Обязательно|
|OC/Платформа|Обязательно|
|Приоритет|Опционально|
|Серьезность|Обязательно|
|Метка принадлежности ошибки|Обязательно|

Метки:
- front-end
- back-end
- other
- database

### 5. Ресурсы

##### 5.1. Инструменты
Будут использованы следующие инструменты:
| Наименование процесса        | Инструмент           |
| ------------- |:-------------:|
|   Баг-трекинговая система   |Kaiten  |
| Тест кейсы     |Google Documents  | 
|   Захват изображений   | Bandicam / яндекс.диск |

##### 5.2. Список браузеров
| Наименование браузера| Версия браузера|
| ------------- |:-------------:|
|  Chrome   | 110.0.5481 |
|  Firefox  | 110.0 |
|  Opera   | 95.0.4635 |
|  Safari  | 15.0 |


#### 5.3. Список устройств
|Устройство|Операционная система|Версия|
|:---:|:---:|:---:|
|ПК|Windows|10|
|ПК|MacOs|12|
|ПК|Ubuntu|22|
|Смартфон|IOs|12|
|Смартфон|Android|10|
|Планшет|IOs|12|
|Планшет|Android|10|
#### 5.4. Список разрешений
|Платформа|Разрешение|Разрешение|
|:---:|:---:|:---:|
|Desktop Win/MacOs/Ubuntu|1920*1080|1366*768|
|Смартфон Ios|375*812|390*844|
|Смартфон Android|360*800|390*844|
|Планшет Android|768*1024|810*1080|
|Планшет Ios|834*1194|810*1080|

#### 6. Риски процесса тестирования

Следующие проблемы могут повлиять на результаты тестирования:

|Риски|Тип|Степень|Меры|Ответственность|
|:---:|:---:|:---:|:---:|:---:|
|Задержки поставки, выполнения задач, выполнения критериев выхода или критериев готовности|Проектные|[TODO]|[TODO]|[TODO]|
|Поздние изменения могут привести к существенным доработкам|Проектные|[TODO]|[TODO]|[TODO]|
|Недостаток навыков, обучения или численности персонала|Организационные|[TODO]|[TODO]|[TODO]|
|Эксперты предметной области могут быть заняты другими работами|Организационные|[TODO]|[TODO]|[TODO]|
|Тестировщики не могут сообщать о своих потребностях и/или результатах тестирования|Коммуникационные|[TODO]|[TODO]|[TODO]|
|Разработчики и/или тестировщики не могут отслеживать информацию, полученную при тестировании и рецензировании |Коммуникационные|[TODO]|[TODO]|[TODO]|
|Может быть неправильное отношение или ожидания от тестирования (недооценивается важность обнаружения дефектов во время тестирования и т.д.)|Коммуникационные|[TODO]|[TODO]|[TODO]|
|Требования могут быть определены недостаточно хорошо|Технические|[TODO]|[TODO]|[TODO]|
|Требования могут быть невыполнимыми в текущих условиях|Технические|[TODO]|[TODO]|[TODO]|
|Тестовая среда может быть не готова вовремя|Технические|[TODO]|[TODO]|[TODO]|
|Преобразование данных, планирование миграции и их инструментальная поддержка могут быть не готовы вовремя|Технические|[TODO]|[TODO]|[TODO]|
|Слабые стороны процесса разработки могут влиять на согласованность или качество артефактов проекта, таких как дизайн, код, конфигурация, тестовые данные и тестовые сценарии|Технические|[TODO]|[TODO]|[TODO]|
|Проблемы управления дефектами могут привести к накоплению дефектов и росту технического долга|Технические|[TODO]|[TODO]|[TODO]|











