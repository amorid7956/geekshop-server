import requests
from .models import UserProfile
from datetime import datetime
from django.utils.timezone import now
from social_core.exceptions import AuthForbidden

def save_user_profile(backend, user, response, *args, **kwargs):
    if backend != 'vk-oauth2':
        return

    api_url = f'https://api.vk.com/method/users.get?fields=bdate,sex,about&access_token={response["access_token"]}'

    vk_response = requests.get(api_url)
    if vk_response.status_code != 200:
        return
    vk_data = vk_response.json()['response'][0]
    if vk_data['sex']:
        if vk_data['sex'] == 2:
            user.userprofile.gender = UserProfile.MALE
        elif vk_data['sex'] == 1:
            user.userprofile.gender = UserProfile.FEMALE

    if vk_data['about']:
        user.userprofile.about_me = vk_data['about']

    if vk_data['bdate']:
        b_date = datetime.strptime(vk_data['bdate'], '%d.%m.%Y').date()
        age = now().date().year - b_date.year
        if age < 18:
            user.delete()
            raise AuthForbidden('social_core.backends.vk.VKOAuth2')
        user.age = age

    user.save()

