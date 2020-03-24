FROM python:3
ADD reflect.py /app/
CMD [ "python", "/app/reflect.py" ]
