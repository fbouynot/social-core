"""
Jumpcloud backends, docs at:
    https://python-social-auth.readthedocs.io/en/latest/backends/jumpcloud.html
"""

from .oauth import BaseOAuth2

class BaseJumpCloud:
    def get_user_id(self, details, response):
        return response["sub"]
        
    def get_user_details(self, response):
        name, given_name, family_name = (
            response.get("name", ""),
            response.get("given_name", ""),
            response.get("family_name", ""),
        )

        fullname, first_name, last_name = self.get_user_names(
            name, given_name, family_name
        )
        
        return {
            "username": response.get("preferred_username", ""),
            "email": response.get("email", ""),
            "fullname": fullname,
            "first_name": first_name,
            "last_name": last_name,
        }
        
    def user_data(self, access_token, *args, **kwargs):
        """return user data from JumpCloud API"""
        return self.get_json(
            "https://oauth.id.jumpcloud.com/userinfo",
            headers={"Authorization": "Bearer %s" % access_token},
        )
    
class JumpCloudOauth2
    """Jumpcloud Oauth2 authentication backend"""
    name = "jumpcloud-oauth2"
    AUTHORIZATION_URL = "https://oauth.id.jumpcloud.com/oauth2/auth"
    ACCESS_TOKEN_URL = "https://oauth.id.jumpcloud.com/oauth2/token"
    ACCESS_TOKEN_METHOD = "POST"
    REDIRECT_STATE = False
