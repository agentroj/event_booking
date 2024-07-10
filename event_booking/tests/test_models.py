import os
import django
import pytest
from django.contrib.auth.models import User
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

fake = Faker()


@pytest.mark.django_db
def test_user_creation():
    username = fake.user_name()
    email = fake.email()
    password = fake.password()

    user = User.objects.create_user(username, email, password)
    assert user.username == username
    assert user.email == email


@pytest.mark.django_db
def test_user_profile():
    first_name = fake.first_name()
    last_name = fake.last_name()
    username = fake.user_name()
    email = fake.email()
    password = fake.password()

    user = User.objects.create_user(username, email, password)
    user.first_name = first_name
    user.last_name = last_name
    user.save()

    assert user.first_name == first_name
    assert user.last_name == last_name


@pytest.mark.django_db
def test_multiple_users():
    for _ in range(10):
        username = fake.user_name()
        email = fake.email()
        password = fake.password()

        user = User.objects.create_user(username, email, password)
        assert user.username == username
        assert user.email == email
