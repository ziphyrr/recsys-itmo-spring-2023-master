# Инструкция по запуску

1. Клонируем репозиторий
2. [Устанавливаем docker](https://www.docker.com/products/docker-desktop)
3. Собираем образы и запускаем контейнеры
   ```
   docker-compose up -d --build 
   ```   
4. Смотрим логи рекомендера
   ```
   docker logs recommender-container
   ```
5. Переходим в папку sim

6. Создаем чистый env с python 3.7
7. Устанавливаем зависимости
   ```
   pip install -r requirements.txt
   ``` 
8. Добавляем текущую директорию в $PYTHONPATH
   ```
   export PYTHONPATH=${PYTHONPATH}:.
   ```
9. Запускаем симулятор в режиме "трафика" в многопоточном режиме.
   ```
   python sim/run.py --episodes 2000 --config config/env.yml multi --processes 2
   ```
10. Скачиваем логи пользовательских сессии с контейнера
```
docker cp recommender-container:/app/log/ /tmp/
```
