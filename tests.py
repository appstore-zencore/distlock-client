import unittest
from distlock_client import Lock
from distlock_client import distlock
from distlock_client import get_app_unique_name


class TestDistLockClient(unittest.TestCase):

    def test_api(self):
        lock = Lock("app01", "http://127.0.0.1:8000/")
        locked = lock.safe_acquire("lock01")
        assert locked
        released = lock.safe_release("lock01")
        assert released

    def test_with(self):
        lock = Lock("app01", "http://127.0.0.1:8000/")
        with distlock(lock, "app01") as locked:
            assert locked

    def test_app_unique_name(self):
        name1 = get_app_unique_name()
        name2 = get_app_unique_name()
        assert name1 == name2

if __name__ == '__main__':
    unittest.main()
