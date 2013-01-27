import requests
import time
import sha


class BanditAPI(object):

    # Routes
    BASE_ROUTE = 'http://banditapi.herokuapp.com/api'
    INIT_ROUTE = BASE_ROUTE + '/init'
    INFO_ROUTE = BASE_ROUTE + '/info'
    SELECT_ARM_ROUTE = BASE_ROUTE + '/select_arm'
    UPDATE_ROUTE = BASE_ROUTE + '/update'

    def __init__(self, test_id, public_key, private_key):
        self.public_key = public_key
        self.private_key = private_key
        self.test_id = test_id

    def __authenticate(self):
        now = int(time.time())
        params = {
            'timestamp': now,
            'signature': sha.sha(str(now) + self.private_key).hexdigest(),
            'public_key': self.public_key,
        }
        return params

    def select_arm(self, user_id=None):
        params = {'test_id': self.test_id}
        if user_id is not None:
            params['user_id'] = user_id
        return requests.get(self.SELECT_ARM_ROUTE, params=params).json

    def info(self):
        return requests.get(self.INFO_ROUTE, params={'test_id': self.test_id}).json

    def update(self, arm, reward):
        params = self.__authenticate()
        params['reward'] = reward
        params['chosen_arm'] = arm
        params['test_id'] = self.test_id
        return requests.post(self.UPDATE_ROUTE, params=params)
