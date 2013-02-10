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

    def select_arm(self, user_id=None, default_value=None, lifetime=None):
        params = {'test_id': self.test_id}
        if user_id is not None:
            params['user_id'] = user_id
        try:
            default_value = float(default_value)
            params['default_value'] = default_value
        except:
            pass

        try:
            lifetime = float(lifetime)
            params['lifetime'] = lifetime
        except:
            pass

        return requests.get(self.SELECT_ARM_ROUTE, params=params).json

    def info(self):
        return requests.get(self.INFO_ROUTE, params={'test_id': self.test_id}).json

    def update(self, arm, reward):
        params = self.__authenticate()
        params['reward'] = reward
        params['chosen_arm'] = arm
        params['test_id'] = self.test_id
        return requests.post(self.UPDATE_ROUTE, params=params).json

    def epsilon_greedy(self, test_id, n_arms, epsilon):
        """
        Initializes an epsilon greedy test.

        Inputs:
        -------
        test_id - string
            The ID for the test.
        n_arms - integer
            The number of arms for the test.
        epsilon - float between 0 and 1
            Epsilon parameter.
        """
        n_arms = int(n_arms)
        epsilon = float(epsilon)
        if epsilon < 0.0 or epsilon > 1.0:
            return
        params = {
            'algorithm': 'epsilon_greedy',
            'test_id': test_id,
            'n_arms': n_arms,
            'epsilon': epsilon
        }
        return self._initialize_test(params)

    def a_b(self, test_id, n_arms):
        """
        Initializes an A/B greedy test.

        Inputs:
        -------
        test_id - string
            The ID for the test.
        n_arms - integer
            The number of arms for the test.
        """
        n_arms = int(n_arms)
        params = {
            'algorithm': 'epsilon_greedy',
            'test_id': test_id,
            'n_arms': n_arms,
            'epsilon': 0.0
        }
        return self._initialize_test(params)

    def annealing_epsilon_greedy(self, test_id, n_arms):
        """
        Initializes an annealing epsilon greedy test.

        Inputs:
        -------
        test_id - string
            The ID for the test.
        n_arms - integer
            The number of arms for the test.
        """
        n_arms = int(n_arms)
        params = {
            'algorithm': 'annealing_epsilon_greedy',
            'test_id': test_id,
            'n_arms': n_arms,
        }
        return self._initialize_test(params)

    def exp3(self, test_id, n_arms, gamma):
        """
        Initializes an EXP3 test.

        Inputs:
        -------
        test_id - string
            The ID for the test.
        n_arms - integer
            The number of arms for the test.
        gamma - float between 0 and 1
            Gamma parameter.
        """
        n_arms = int(n_arms)
        gamma = float(gamma)
        if gamma < 0.0 or gamma > 1.0:
            return
        params = {
            'algorithm': 'exp3',
            'test_id': test_id,
            'n_arms': n_arms,
            'gamma': gamma
        }
        return self._initialize_test(params)

    def _initialize_test(self, params):
        """
        Initializes a test with the given test-specific parameters.
        """
        auth_params = self.__authenticate()
        for k, v in auth_params:
            params[k] = v
        return requests.post(self.INIT_ROUTE, params=params).json
