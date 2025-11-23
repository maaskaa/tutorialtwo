import pytest
from user.user_manager import User, UserManager

def test_add_user():
    manager = UserManager()
    user = manager.add_user('alice', 'alice@example.com')
    assert user.username == 'alice'
    assert user.email == 'alice@example.com'
    assert manager.get_user('alice') == user

def test_add_duplicate_user():
    manager = UserManager()
    manager.add_user('bob', 'bob@example.com')
    with pytest.raises(ValueError):
        manager.add_user('bob', 'bob@example.com')

def test_remove_user():
    manager = UserManager()
    user = manager.add_user('charlie', 'charlie@example.com')
    assert manager.remove_user('charlie') is True
    assert manager.get_user('charlie') is None

def test_change_email():
    user = User('david', 'david@example.com')       
    user.change_email('new@example.com')
    assert user.email == 'new@example.com'
