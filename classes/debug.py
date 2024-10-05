class Debug:
    def print_user(message):
        print(message.from_user.first_name or None, message.from_user.last_name or None, message.from_user.username or None, message.from_user.id)