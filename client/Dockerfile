FROM node:18-alpine

WORKDIR /client

RUN npm install -g npm

COPY ./client/package*.json ./

RUN npm install

COPY . .

EXPOSE 8080

CMD [ "npm", "run", "serve" ]