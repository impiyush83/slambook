from slambook_restful.resource.customer_create_secret_key import CustomerCreateSecretKey
from slambook_restful.resource.customer_data_transfer import CustomerDataTransfer
from slambook_restful.resource.customer_enter_secret_key import CustomerEnterSecretKey
from slambook_restful.resource.customer_homepage import CustomerHomepage
from slambook_restful.resource.customer_login import CustomerLogin
from slambook_restful.resource.customer_logout import CustomerLogout
from slambook_restful.resource.customer_register_friend import OnSpotRegisterFriend
from slambook_restful.resource.customer_save_new_friend import SaveFriend
from slambook_restful.resource.customer_signup import CustomerSignUp
from slambook_restful.resource.index import Index
from slambook_restful.utils import URLS

urls = [
    URLS(resource=Index, endpoint=['/'], name="showcases_homepage"),
    URLS(resource=CustomerSignUp, endpoint=['user/signup'], name="signup_user"),
    URLS(resource=CustomerLogin, endpoint=['user/login'], name="customer_login"),
    URLS(resource=CustomerHomepage, endpoint=['user/home'], name="customer_homepage"),
    URLS(resource=CustomerLogout, endpoint=['user/logout'], name="unsets_jwt_cookie"),
    URLS(resource=CustomerCreateSecretKey, endpoint=['user/secret-key'], name="create_secret_key"),
    URLS(resource=OnSpotRegisterFriend, endpoint=['user/register-friend'], name="onspot_register_friend"),
    URLS(resource=SaveFriend, endpoint=['user/save'], name="save_friend_to_db"),
    URLS(resource=CustomerEnterSecretKey, endpoint=['user/enter-secret-key'], name="renders_web_page"),
    URLS(resource=CustomerDataTransfer, endpoint=['user/transfer'], name="give_user_data_to_secret_key_bearer"),
]
