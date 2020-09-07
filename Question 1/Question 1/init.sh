sleep 90s

/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P $SA_PASSWORD -i 01-create-database.sql

/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P $SA_PASSWORD -i 02-create-table.sql

/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P $SA_PASSWORD -i 03-insert-data.sql