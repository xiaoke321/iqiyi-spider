import requests


class Demo():

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14"
        })

    def login(self):
        url = "https://passport.iqiyi.com/apis/reglogin/login.action"
        data = {
            "email": "18191350628",
            "fromSDK": "1",
            "sdk_version": "1.0.0",
            "passwd": "9e0fe7b4ad6ded6abeae175baf6af1574c499737f1ca51b629fe748be2177195f1f48240373d3f2ad63b377f44cd9ffe57227f05f2dccc8d6920a6afe55477f0",
            "agenttype": "1",
            "__NEW": "1",
            "checkExist": "1",
            "lang": "",
            "ptid": "01010021010000000000",
            "nr": "2",
            "verifyPhone": "1",
            "area_code": "86",
            "dfp": "a0f3e74609f2a54750bd56733baa4eb9db599f3f38bcf3c574dd24ac844e6142fb",
        }
        response = self.session.post(url=url, data=data)
        print(response.text)
        print(response.json()['data']['nickname'])

if __name__ == '__main__':
    demo = Demo()
    demo.login()