I created an API for running website tests using bandit algorithms. There is much more info at [http://banditapi.herokuapp.com](http://banditapi.herokuapp.com). This is a python client library for accessing the API.

Features that work so far:

* getting info on a running test
* selecting an arm to display
* updating the algorithm with the test results

Features that haven't been implemented yet:

* create a new test

### Usage

```{python}
B = bandits.BanditAPI('my_test_id', 'my_public_key', 'my_private_key')
B.info()
# {u'algorithm': u'epsilon_greedy', u'epsilon': 0.6, u'n_arms': 3, 
# u'values': [0.24324324324324326, 0.3399999999999999, 0.11538461538461538], 
# u'owner': u'youremail@youremail.com', u'counts': [37, 50, 26], 
# u'test_id': u'my_test2'}

chosen_arm = B.select_arm()
# {u'arm': 1}

B.update(chosen_arm['arm'], 0.0)
# {u'total_arm_value': 0.26315789473684215, u'arm': 1, u'pull_count': 38}
```

### Installing

Just include the `bandits.py` file wherever you need it.
