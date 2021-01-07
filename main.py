from apis import XinJieAPIS

print('----------start----------')
xj_api = XinJieAPIS()
xj_api.login()
xj_api.checkin()
xj_api.logout()
print("----------finish---------")
