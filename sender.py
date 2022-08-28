import requests

group_message_api = 'http://47.93.40.173:5701/send_group_msg'
private_message_api = 'http://47.93.40.173:5701/send_private_msg'


class QQSender():
    def __init__(self, access_token: str):
        self.access_token = access_token

    def send_group_message(self, group_id: str, message: str):
        params = {
            'group_id': group_id,
            'message': message,
            'access_token': self.access_token
        }
        return requests.get(group_message_api, params=params)

    def send_private_message(self, user_id: str, message: str):
        params = {
            'user_id': user_id,
            'message': message,
            'access_token': self.access_token
        }
        return requests.get(private_message_api, params=params)

