from bandits import BanditAPI

PUBLIC_KEY = 'public_key'
PRIVATE_KEY = 'private_key'

B = BanditAPI(
    'my_test2',
    PUBLIC_KEY,
    PRIVATE_KEY
    )

# get the info
print B.info()

# Select an arm
arm = B.select_arm()
print arm

# update with a successful conversion.
print B.update(arm['arm'], 1.0).json

# print the info again
print B.info()
