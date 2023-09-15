FROM python:3.11.1-alpine

ENV PYTHONDONTWHRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

ARG PROJ_DIR=/back

RUN mkdir -p ${PROJ_DIR}
COPY ./server ${PROJ_DIR}

WORKDIR ${PROJ_DIR}

RUN pip install -U pip \
    pip install -r requirements.txt

COPY ./compose/server/entry.sh /entry.sh
RUN chmod +x /entry.sh
ENTRYPOINT [ "/entry.sh" ]