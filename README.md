## fastener_shop
## API for fastener shop

Проект выполнен в рамках технического задания. Описание <a href='test_task.txt'> здесь</a>.

Подробнее об эндпойнтах:
- /category/ - вернет список всех категорий и для каждой категории все дочерние.
get-Запрос: http://127.0.0.1:8000/api/category/ 
- /category/{id}/ - вернет все карточки, входящие в эту секцию/группу/подгруппу
Пример get-запроса: http://127.0.0.1:8000/api/category/2/
- /card_details/{id}/ - вернет карточку товара по id c детальной информацией, в случае отсутвия карточки (например, если в передать id не карточки, а подгруппы), вернет 404
Пример get-запроса: http://127.0.0.1:8000/api/card_details/11/
- /card_products/{id}/ - вернет все продукты, относящиеся к этой карточкеб в случае отсутвия карточки вернет 404
Пример get-запроса: http://127.0.0.1:8000/api/card_products/4/

## Чтобы развернуть проект локально:
### Клонируйте данный репозиторий
```
git clone https://github.com/Viktrols/fastener_shop.git
 ```
### Создайте и активируйте виртуальное окружение
```
python -m venv venv
source ./venv/Scripts/activate  #для Windows
source ./venv/bin/activate      #для Linux и macOS
```
### Установите требуемые зависимости
```
pip install -r requirements.txt
```
### Запустите проект
```
python shop/manage.py runserver
```
#### Приложение будет доступно по адресу: http://127.0.0.1:8000/
#### Посмотреть и протестировать доступные эндпойнты можно в доке: http://127.0.0.1:8000/api/swagger/
#### Зайти в админку http://127.0.0.1:8000/admin/  (login: test, password: test)