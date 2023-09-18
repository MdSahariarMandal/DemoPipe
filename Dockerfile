FROM python:3.9-slim
COPY Hello.py /
CMD ["python","/Hello.py"]
