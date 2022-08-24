FROM node:12.18
WORKDIR /home/

RUN echo "fe_test:0.1"

#gitlab access token
#https://lab.ssafy.com/s07-webmobile2-sub2/S07P12B209/-/settings/access_tokens

RUN git clone -b master https://<gitlab_id>:<access_tokens>@lab.ssafy.com/s07-webmobile2-sub2/S07P12B209.git

RUN echo "testing_image0.3"

RUN echo "fe_test:0.1"
# RUN echo $(pwd /home/)

WORKDIR /home/S07P12B209/FE/blaa

RUN npm install
RUN npm install --save @popperjs/core

EXPOSE 3000

CMD ["npm", "run", "serve"]