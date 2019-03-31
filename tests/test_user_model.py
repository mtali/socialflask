import unittest

from app.models import User, Role, AnonymousUser
from app.permissions import SitePermission as Permission
from flask import current_app
from app import create_app, db

class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_setter(self):
        user = User(password="cat")
        self.assertTrue(user.password_hash is not None)

    def test_no_password_getter(self):
        user = User(password="cat")
        with self.assertRaises(AttributeError):
            user.password

    def test_password_verification(self):
        user = User(password="cat")
        self.assertTrue(user.verify_password("cat"))
        self.assertFalse(user.verify_password("dog"))

    def test_password_salts_are_random(self):
        user1 = User(password="cat")
        user2 = User(password="cat")
        self.assertTrue(user1.password_hash != user2.password_hash)

    def test_roles_and_permissions(self):
        Role.insert_roles()
        u = User(email="john@example.com", password="cat")
        self.assertTrue(u.can(Permission.WRITE_ARTICLE))
        self.assertFalse(u.can(Permission.MODERATE_COMMENTS))

    def test_anonymous_user(self):
        u = AnonymousUser()
        self.assertFalse(u.can(Permission.FOLLOW))
