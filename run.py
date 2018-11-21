import yaml
import logging
import datetime
import os
import time
from checkers.replication import ReplicationChecker
from notifiers.telegram import TelegramNotifier

if __name__ == '__main__':
    directory = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    config = yaml.load((open(os.path.join(directory, 'config.yml'), 'r').read()))
    logging.basicConfig(filename = os.path.join(directory, 'replication.log'), level = logging.DEBUG)
    logging.info('Checker started at: ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    notifier = TelegramNotifier(telegram_token=config['telegram']['token'], chat_id=config['telegram']['chat_id'])

    for repl_name in config['mysql']['replication_name']:
        time.sleep(1)
        checker = ReplicationChecker(
            project_directory = directory,
            replication_name = repl_name,
            lag_interval = 300,
            lag_duration = 1800,
            config=config
        )
        checker.add_notifier(notifier)
        checker.check()

    logging.info('Checker ended at: ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))