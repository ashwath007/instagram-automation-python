from alright import WhatsApp
messenger = WhatsApp()
messenger.find_user('91-6364250724')
messages = ['Morning my love', 'I wish you a good night!']
for message in messages:
    messenger.send_message(message)   