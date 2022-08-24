FROM python:3.9.13

WORKDIR /home/
# RUN echo $(ls /home/)
RUN echo "testing_image0.3"

#gitlab access token
#https://lab.ssafy.com/s07-webmobile2-sub2/S07P12B209/-/settings/access_tokens
RUN git clone -b master https://<gitlab_id>:<access_tokens>@lab.ssafy.com/s07-webmobile2-sub2/S07P12B209.git

# RUN echo $(pwd /home/)

WORKDIR /home/S07P12B209/BE
RUN echo $(pwd /home/)

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient



EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=apiserver.settings.deploy && python manage.py migrate --settings=apiserver.settings.deploy &&gunicorn apiserver.wsgi --env DJANGO_SETTINGS_MODULE=apiserver.settings.deploy --bind 0.0.0.0:8000"]