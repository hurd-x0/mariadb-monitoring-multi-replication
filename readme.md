# Monitoring Multi Replication on MariaDB 

Python app monitoring MariaDB Multi Replication with Telegram and Slack notifications

# How to use
- Copy `config.yml.template` to config.yml and update information in file
- Install dependencies: 
    `bash init.sh`
- Need set schedule following command:
```
python run.py
```
Example monitoring replication every 5 minutes:
```
*/5 * * * * python /path/to/repo/mariadb-monitoring-multi-replication/run.py
```
- View log: `replication.log`