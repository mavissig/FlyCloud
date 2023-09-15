FROM node:18-alpine

ARG PROJ_DIR=/front

RUN mkdir -p ${PROJ_DIR}
COPY ./client ${PROJ_DIR}

WORKDIR ${PROJ_DIR}

RUN npm install -g npm

COPY ./client/package.json ${PROJ_DIR}
COPY ./client/package-lock.json ${PROJ_DIR}

RUN npm install

CMD [ "npm", "run", "serve" ]