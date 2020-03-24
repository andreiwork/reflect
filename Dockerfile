FROM python:3
ADD relfect.py /app
CMD [ "python", "/app/reflect.py" ]
