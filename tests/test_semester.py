from semester import app, db
from semester.models import User


class TestView:

    def setup(self):
        app.testing = True
        self.client = app.test_client()
        print('setup')

    def login(self, username, password):
        return app.post('/auth/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return app.get('/auth/logout', follow_redirects=True)

    def test_index(self):
        response = self.client.get('/')
        result = response.status_code
        assert result == 200

    def test_login(self):
        response = self.client.get('/auth/login')
        result = response.status_code
        assert result == 200

    def test_register(self):
        response = self.client.get('/auth/register')
        result = response.status_code
        assert result == 200

    def test_about(self):
        response = self.client.get('/about')
        result = response.status_code
        assert result == 200

    def test_basket(self):
        response = self.client.get('/basket')
        result = response.status_code
        assert result == 401

    def test_contacts(self):
        response = self.client.get('/contacts')
        result = response.status_code
        assert result == 200

    def test_burgers(self):
        response = self.client.get('/burgers')
        result = response.status_code
        assert result == 200

    def test_pizza(self):
        response = self.client.get('/pizza')
        result = response.status_code
        assert result == 200

    def test_snacks(self):
        response = self.client.get('/snacks')
        result = response.status_code
        assert result == 200

    def test_sauces(self):
        response = self.client.get('/sauces')
        result = response.status_code
        assert result == 200

    def test_drinks(self):
        response = self.client.get('/drinks')
        result = response.status_code
        assert result == 200

    def test_profile(self):
        response = self.client.get('/user_profile/profile')
        result = response.status_code
        assert result == 401

    def test_edit(self):
        response = self.client.get('/user_profile/edit')
        result = response.status_code
        assert result == 401

    def test_pass_edit(self):
        response = self.client.get('/user_profile/edit_pass')
        result = response.status_code
        assert result == 401

    def test_index_authed(self):
        sent = {
            'email': "test@mail.ru",
            'password': "Roman_2002",
            'rememberme': 'y'
        }
        self.client.post(
            '/auth/login',
            data=sent
        )
        response = self.client.get('/')
        result = response.status_code
        assert result == 200

    def test_login_authed(self):
        sent = {
            'email': "test@mail.ru",
            'password': "Roman_2002",
            'rememberme': 'y'
        }
        self.client.post(
            '/auth/login',
            data=sent
        )
        response = self.client.get('/auth/login')
        result = response.status_code
        assert result == 200

    def test_register_authed(self):
        sent = {
            'email': "test@mail.ru",
            'password': "Roman_2002",
            'rememberme': 'y'
        }
        self.client.post(
            '/auth/login',
            data=sent
        )
        response = self.client.get('/auth/register')
        result = response.status_code
        assert result == 200

    def test_about_authed(self):
        sent = {
            'email': "test@mail.ru",
            'password': "Roman_2002",
            'rememberme': 'y'
        }
        self.client.post(
            '/auth/login',
            data=sent
        )
        response = self.client.get('/about')
        result = response.status_code
        assert result == 200

    def test_basket_authed(self):
        sent = {
            'email': "test@mail.ru",
            'password': "Roman_2002",
            'rememberme': 'y'
        }
        self.client.post(
            '/auth/login',
            data=sent
        )
        response = self.client.get('/basket')
        result = response.status_code
        assert result == 200

    def test_contacts_authed(self):
        sent = {
            'email': "test@mail.ru",
            'password': "Roman_2002",
            'rememberme': 'y'
        }
        self.client.post(
            '/auth/login',
            data=sent
        )
        response = self.client.get('/contacts')
        result = response.status_code
        assert result == 200

    def test_burgers_authed(self):
        sent = {
            'email': "test@mail.ru",
            'password': "Roman_2002",
            'rememberme': 'y'
        }
        self.client.post(
            '/auth/login',
            data=sent
        )
        response = self.client.get('/burgers')
        result = response.status_code
        assert result == 200

    def test_pizza_authed(self):
        sent = {
            'email': "test@mail.ru",
            'password': "Roman_2002",
            'rememberme': 'y'
        }
        self.client.post(
            '/auth/login',
            data=sent
        )
        response = self.client.get('/pizza')
        result = response.status_code
        assert result == 200

    def test_snacks_authed(self):
        sent = {
            'email': "test@mail.ru",
            'password': "Roman_2002",
            'rememberme': 'y'
        }
        self.client.post(
            '/auth/login',
            data=sent
        )
        response = self.client.get('/snacks')
        result = response.status_code
        assert result == 200

    def test_sauces_authed(self):
        sent = {
            'email': "test@mail.ru",
            'password': "Roman_2002",
            'rememberme': 'y'
        }
        self.client.post(
            '/auth/login',
            data=sent
        )
        response = self.client.get('/sauces')
        result = response.status_code
        assert result == 200

    def test_drinks_authed(self):
        sent = {
            'email': "test@mail.ru",
            'password': "Roman_2002",
            'rememberme': 'y'
        }
        self.client.post(
            '/auth/login',
            data=sent
        )
        response = self.client.get('/drinks')
        result = response.status_code
        assert result == 200

    def test_profile_authed(self):
        sent = {
            'email': "test@mail.ru",
            'password': "Roman_2002",
            'rememberme': 'y'
        }
        self.client.post(
            '/auth/login',
            data=sent
        )
        response = self.client.get('/user_profile/profile')
        result = response.status_code
        assert result == 200

    def test_edit_authed(self):
        sent = {
            'email': "test@mail.ru",
            'password': "Roman_2002",
            'rememberme': 'y'
        }
        self.client.post(
            '/auth/login',
            data=sent
        )
        response = self.client.get('/user_profile/edit')
        result = response.status_code
        assert result == 200

    def test_pass_edit_authed(self):
        sent = {
            'email': "test@mail.ru",
            'password': "Roman_2002",
            'rememberme': 'y'
        }
        self.client.post(
            '/auth/login',
            data=sent
        )
        response = self.client.get('/user_profile/edit_pass')
        result = response.status_code
        assert result == 200

    def test_login_post(self):
        sent = {
            'email': "test@mail.ru",
            'password': "Roman_2002",
            'rememberme': 'y'
        }
        result = self.client.post(
            '/auth/login',
            data=sent
        ).status_code

        assert result == 302

    def test_login_pass_mistake(self):
        sent = {
            'email': "test@mail.ru",
            'password': "Roman_202",
            'rememberme': 'y'
        }
        result = self.client.post(
            '/auth/login',
            data=sent
        ).status_code

        assert result == 200

    def test_login_email_wrong(self):
        sent = {
            'email': "tes@mail.ru",
            'password': "Roman_2002",
            'rememberme': 'y'
        }
        result = self.client.post(
            '/auth/login',
            data=sent
        ).status_code

        assert result == 200

    def test_login_not_email(self):
        sent = {
            'email': "",
            'password': "Roman_2002",
            'rememberme': 'y'
        }
        result = self.client.post(
            '/auth/login',
            data=sent
        ).status_code

        assert result == 200

    def test_login_not_pass(self):
        sent = {
            'email': "tes@mail.ru",
            'password': "",
            'rememberme': 'y'
        }
        result = self.client.post(
            '/auth/login',
            data=sent
        ).status_code

        assert result == 200

    def test_login_email_mistake(self):
        sent = {
            'email': "tesmailru",
            'password': "",
            'rememberme': 'y'
        }
        result = self.client.post(
            '/auth/login',
            data=sent
        ).status_code

        assert result == 200

    def test_register_post(self):
        sent = {
            'name': "Роман",
            'email': "test11@mail.ru",
            'password': "Roman_2002",
            'repeat': 'Roman_2002'
        }
        result = self.client.post(
            '/auth/register',
            data=sent
        ).status_code

        assert result == 302

    def test_register_post_not_email(self):
        sent = {
            'name': "Роман",
            'email': "",
            'password': "Roman_2002",
            'repeat': 'Roman_2002'
        }
        result = self.client.post(
            '/auth/register',
            data=sent
        ).status_code

        assert result == 200

    def test_register_post_email_wrong(self):
        sent = {
            'name': "Роман",
            'email': "test11mailru",
            'password': "Roman_2002",
            'repeat': 'Roman_2002'
        }
        result = self.client.post(
            '/auth/register',
            data=sent
        ).status_code

        assert result == 200

    def test_register_post_same_email(self):
        sent = {
            'name': "Роман",
            'email': "test1@mail.ru",
            'password': "Roman_2002",
            'repeat': 'Roman_2002'
        }
        result = self.client.post(
            '/auth/register',
            data=sent
        ).status_code

        assert result == 200

    def test_register_post_not_pass(self):
        sent = {
            'name': "Роман",
            'email': "test11@mail.ru",
            'password': "",
            'repeat': 'Roman_2002'
        }
        result = self.client.post(
            '/auth/register',
            data=sent
        ).status_code

        assert result == 200

    def test_register_not_same_pass(self):
        sent = {
            'name': "Роман",
            'email': "test11@mail.ru",
            'password': "Roman_2002",
            'repeat': 'Roman_2003'
        }
        result = self.client.post(
            '/auth/register',
            data=sent
        ).status_code

        assert result == 200

    def test_register_post_pass_hard(self):
        sent = {
            'name': "Роман",
            'email': "test11@mail.ru",
            'password': "Roman2002",
            'repeat': 'Roman2002'
        }
        result = self.client.post(
            '/auth/register',
            data=sent
        ).status_code

        assert result == 200

    def test_edit_post(self):
        sent = {
            'email': "test@mail.ru",
            'password': "Roman_2002",
            'rememberme': 'y'
        }
        self.client.post(
            '/auth/login',
            data=sent
        )

        sent = {
            'name': "Егор",
            'email': "edit_test@mail.ru",
            'number': "8945874242",
            'address': 'Тольятти, 40 лет победы, 15д'
        }
        result = self.client.post(
            '/user_profile/edit',
            data=sent
        ).status_code

        sent = {
            'name': "Роман",
            'email': "test@mail.ru",
            'number': "89270271234",
            'address': 'Казань, Деревня Универсиады, 18'
        }

        self.client.post(
            '/user_profile/edit',
            data=sent
        )

        assert result == 302

    def test_edit_post_(self):
        sent = {
            'email': "test@mail.ru",
            'password': "Roman_2002",
            'rememberme': 'y'
        }
        self.client.post(
            '/auth/login',
            data=sent
        )

        sent = {
            'name': "",
            'email': "",
            'number': "",
            'address': ""
        }
        result = self.client.post(
            '/user_profile/edit',
            data=sent
        ).status_code

        assert result == 200

    def test_edit_post_email_wrong(self):
        sent = {
            'email': "test@mail.ru",
            'password': "Roman_2002",
            'rememberme': 'y'
        }
        self.client.post(
            '/auth/login',
            data=sent
        )

        sent = {
            'name': "Егор",
            'email': "edit_testmailru",
            'number': "8945874242",
            'address': 'Тольятти, 40 лет победы, 15д'
        }
        result = self.client.post(
            '/user_profile/edit',
            data=sent
        ).status_code

        assert result == 200

    def test_edit_post_same_email(self):
        sent = {
            'email': "test1@mail.ru",
            'password': "Roman_2002",
            'rememberme': 'y'
        }
        self.client.post(
            '/auth/login',
            data=sent
        )

        sent = {
            'name': "Егор",
            'email': "test1@mailru",
            'number': "8945874242",
            'address': 'Тольятти, 40 лет победы, 15д'
        }
        result = self.client.post(
            '/user_profile/edit',
            data=sent
        ).status_code

        assert result == 200

    def test_edit_post_name_wrong(self):
        sent = {
            'email': "test@mail.ru",
            'password': "Roman_2002",
            'rememberme': 'y'
        }
        self.client.post(
            '/auth/login',
            data=sent
        )

        sent = {
            'name': "88005553535",
            'email': "edit_testmailru",
            'number': "8945874242",
            'address': 'Тольятти, 40 лет победы, 15д'
        }
        result = self.client.post(
            '/user_profile/edit',
            data=sent
        ).status_code

        assert result == 200

    def test_edit_post_wrong_number(self):
        sent = {
            'email': "test@mail.ru",
            'password': "Roman_2002",
            'rememberme': 'y'
        }
        self.client.post(
            '/auth/login',
            data=sent
        )

        sent = {
            'name': "Егор",
            'email': "edit_testmailru",
            'number': "hurt other people",
            'address': 'Тольятти, 40 лет победы, 15д'
        }
        result = self.client.post(
            '/user_profile/edit',
            data=sent
        ).status_code

        assert result == 200

    def test_edit_pass(self):
        sent = {
            'email': "test@mail.ru",
            'password': "Roman_2002",
            'rememberme': 'y'
        }
        self.client.post(
            '/auth/login',
            data=sent
        )

        sent = {
            'old_pass': "Roman_2002",
            'new_pass': "Egor_2009",
            'new_pass2': "Egor_2009"
        }
        result = self.client.post(
            '/user_profile/edit_pass',
            data=sent
        ).status_code

        sent = {
            'old_pass': "Egor_2009",
            'new_pass': "Roman_2002",
            'new_pass2': "Roman_2002"
        }

        self.client.post(
            '/user_profile/edit_pass',
            data=sent
        )

        assert result == 302

    def test_edit_pass_not_pass(self):
        sent = {
            'email': "test@mail.ru",
            'password': "Roman_2002",
            'rememberme': 'y'
        }
        self.client.post(
            '/auth/login',
            data=sent
        )

        sent = {
            'old_pass': "",
            'new_pass': "",
            'new_pass2': ""
        }
        result = self.client.post(
            '/user_profile/edit_pass',
            data=sent
        ).status_code

        assert result == 200

    def test_edit_pass_pass_wrong(self):
        sent = {
            'email': "test@mail.ru",
            'password': "Roman_2002",
            'rememberme': 'y'
        }
        self.client.post(
            '/auth/login',
            data=sent
        )

        sent = {
            'old_pass': "Roman2002",
            'new_pass': "Egor_2009",
            'new_pass2': "Egor_2009"
        }
        result = self.client.post(
            '/user_profile/edit_pass',
            data=sent
        ).status_code

        assert result == 200

    def test_edit_pass_not_same_pass(self):
        sent = {
            'email': "test@mail.ru",
            'password': "Roman_2002",
            'rememberme': 'y'
        }
        self.client.post(
            '/auth/login',
            data=sent
        )

        sent = {
            'old_pass': "Roman_2002",
            'new_pass': "Durak_2009",
            'new_pass2': "Egor_2009"
        }
        result = self.client.post(
            '/user_profile/edit_pass',
            data=sent
        ).status_code

        assert result == 200

    def test_edit_pass_hard_pass(self):
        sent = {
            'email': "test@mail.ru",
            'password': "Roman_2002",
            'rememberme': 'y'
        }
        self.client.post(
            '/auth/login',
            data=sent
        )

        sent = {
            'old_pass': "Roman_2002",
            'new_pass': "egor2009",
            'new_pass2': "egor2009"
        }
        result = self.client.post(
            '/user_profile/edit_pass',
            data=sent
        ).status_code

        assert result == 200

    def test_index_post(self):
        sent = {
            'town': "Казань"
        }
        result = self.client.post(
            '/',
            data=sent
        ).status_code

        assert result == 200

    def test_index_post_wrong(self):
        sent = {
            'town': "Москва"
        }
        result = self.client.post(
            '/',
            data=sent
        ).status_code

        assert result == 200
