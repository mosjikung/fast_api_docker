FROM python:3.9.13-slim

# 
WORKDIR /code
# 
COPY ./requirment.txt /code/requirment.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirment.txt

#
COPY . .

EXPOSE 8000
# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]