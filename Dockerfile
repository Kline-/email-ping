FROM python:3-alpine
WORKDIR /usr/src/app
HEALTHCHECK --interval=10m CMD /usr/src/app/hc.sh
COPY email-ping.py hc.sh ./
CMD [ "python", "./email-ping.py" ]
