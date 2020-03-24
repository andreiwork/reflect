FROM python:3
ADD reflect.py /app/
CMD [ "python","-u","/app/reflect.py" ]
