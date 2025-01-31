import time
from .. import securelink

secureurl = securelink.sign.generate_md5_base64_url(
    "http://local-ssoapi.quadopus.com/secure/", "secret", 20, "127.0.0.1"
)
print('normal sucess validation :',securelink.sign.validate_md5_base64_url(secureurl,'secret','127.0.0.1'))
print('invalid ip validation :',securelink.sign.validate_md5_base64_url(secureurl,'secret','10.44.0.1'))
print('invalid secret validation :',securelink.sign.validate_md5_base64_url(secureurl,'wrong secret','127.0.0.1'))
time.sleep(8)
print('dlayed validation :',securelink.sign.validate_md5_base64_url(secureurl,'secret','127.0.0.1'))
