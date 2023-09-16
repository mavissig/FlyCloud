FROM node:18-alpine

WORKDIR /client

RUN npm install -g npm

COPY ./package*.json .

RUN npm install

COPY . .

EXPOSE 5173

CMD [ "npm", "run", "dev" ]