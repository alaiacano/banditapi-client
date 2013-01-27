from bandits import BanditAPI

PUBLIC_KEY = '83e4f11db51ab7b274d60f3c0d99ca8166a1fe18'
PRIVATE_KEY = '6c3bede5e48427356ee08d80aaf16114e7314417'

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