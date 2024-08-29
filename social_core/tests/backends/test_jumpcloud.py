import json

from .oauth import OAuth2Test


class DripOAuthTest(OAuth2Test):
    backend_path = "social_core.backends.jumpcloud.JumpCloudOAuth2"
    user_data_url = "https://oauth.id.jumpcloud.com/userinfo"
    expected_username = "other@example.com"
    access_token_body = json.dumps(
        {"access_token": "822bbf7cd12243df", "token_type": "bearer", "scope": "public"}
    )

    user_data_body = json.dumps(
        {"users": [{"email": "other@example.com", "name": "Foo Bar", "given_name": "Foo", "family_name": "Bar", "preferred_username": "Toto", "sub": "101010101010101010101"}]}
    )

    def test_login(self):
        self.do_login()

    def test_partial_pipeline(self):
        self.do_partial_pipeline()
