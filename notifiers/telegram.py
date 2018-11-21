import telepot

class TelegramNotifier:
    def __init__(self, telegram_token, chat_id):
        self.telegram_token = telegram_token
        self.chat_id = chat_id

    def notify(self, system, replication_name, status, short_msg, long_msg, time_string):
        bot = telepot.Bot(token=self.telegram_token)
        msg = '''
        System: *%s*
        Replication name: *%s*
        Status: *%s*
        Message: `%s`
        Description: ```%s```
        Time: `%s`
        ''' % (system, replication_name, status, short_msg, long_msg, time_string)
        bot.sendMessage(self.chat_id, msg, parse_mode='Markdown')