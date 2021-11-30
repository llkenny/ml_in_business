## API для предсказания диабета на ранних стадиях.

- Датасет обучения: diabetes_data_upload.csv
- Метод POST: '/predict'

##### HTTP BODY SAMPLE:
```
{
  "Age": 40,
  "Alopecia": "Yes",
  "Gender": "Male",
  "Genital thrush": "Yes",
  "Irritability": "Yes",
  "Itching": "Yes",
  "Obesity": "Yes",
  "Polydipsia": "Yes",
  "Polyphagia": "Yes",
  "Polyuria": "No",
  "delayed healing": "Yes",
  "muscle stiffness": "Yes",
  "partial paresis": "No",
  "sudden weight loss": "No",
  "visual blurring": "No",
  "weakness": "Yes"
}
```

### Использование:
1. Активировать venv: source venv/bin/activate
2. Установить зависимости: pip install -r requirements.txt
3. Запустить локальный сервер: python app/app.py
4. Создать запрос http://127.0.0.1:8180/predict с HTTP BODY

### Docker:
1. Создание образа: docker build -t ml_in_business:v0.1 9/
2. Запуск: docker run -d -p 8180:8180 -p 8181:8181 ml_in_business:v0.1
3. Проверка активности образа: docker ps (параметр -a для показа всех)
4. Доступ: http://0.0.0.0:8180/predict
5. Остановка: docker stop <id>

### Файлы:
- app/model/pipeline.dill - предобученная модель (+ pipeline)
- app/app.py - API
- diabetes_data_upload.csv - датасет
- request_sample.request - тестовый запрос для использования в приложении Rested
- Homework 9.ipynb - Jupyter Notebook подготовки модели
- Dockerfile - настройки Docker образа
