FROM ubuntu

RUN apt update
RUN apt install python3 python3-pip -y

RUN pip install flask
RUN pip install flask_sqlalchemy
RUN pip install flask-login

COPY . /Documents/proj_Tania/WebAppFlask/WebAppFlaskPyTest/website

EXPOSE 5000

CMD python3 /Documents/proj_Tania/WebAppFlask/WebAppFlaskPyTest/website/main.py
