---
FROM alpine:latest

USER 1001

CMD [ "python", "/usr/src/app/main.py" ]
