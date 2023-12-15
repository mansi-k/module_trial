

print("HELLO!")

from clarifai.client.input import Inputs
input_obj = Inputs(user_id = 'mansi_k', app_id = 'ui_modules', pat="95978ef1e65e4e1ab8b268e94a49b1e9")
input_obj.upload_from_url(input_id='demo', image_url='https://samples.clarifai.com/metro-north.jpg')


