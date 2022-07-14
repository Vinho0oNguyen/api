FROM node:12

WORKDIR /usr/src/app

COPY yarn.lock .
COPY .env .


COPY . .
RUN yarn 
EXPOSE 5000
CMD [ "yarn", "start" ]
