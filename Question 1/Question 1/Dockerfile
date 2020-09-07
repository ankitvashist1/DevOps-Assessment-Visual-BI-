FROM mcr.microsoft.com/mssql/server:2017-latest

#create working directory
ENV SA_PASSWORD Qwerty123

ENV ACCEPT_EULA Y

WORKDIR /DBScripts

COPY ./ ./

RUN chmod +x /DBScripts/entrypoint.sh

EXPOSE 1433

CMD [ "/bin/bash", "./entrypoint.sh" ]