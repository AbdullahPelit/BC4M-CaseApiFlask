FROM python
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY app.py /usr/src/app/
COPY requirements.txt /usr/src/app/
COPY . ./
RUN pip install -r requirements.txt
ENTRYPOINT [ "python3", "app.py" ]
EXPOSE 5000