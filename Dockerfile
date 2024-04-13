FROM python:3-alpine

WORKDIR /app

COPY src/update_save_ip_api.py .
COPY src/requirements.txt ./

RUN pip install -r requirements.txt

CMD ["python", "-u", "./update_save_ip_api.py"]
