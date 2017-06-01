"""
    Tests for the snoozy package.
"""

import unittest

import snoozy

class TestSnoozy(unittest.TestCase):
    def test_evaluate(self):
        # Attributes should be evaluated on access.
        called = []

        class Foo(object):
            @snoozy.lazy_property
            def foo(self):
                called.append(True)
                return True

        foo = Foo()
        self.assertEqual(foo.foo, True)
        self.assertEqual(len(called), 1)

    def test_evaluate_once(self):
        # Attributes should be evaluated only once.
        called = []

        class Foo(object):
            @snoozy.lazy_property
            def foo(self):
                called.append('foo')
                return 1

        foo = Foo()
        self.assertEqual(foo.foo, 1)
        self.assertEqual(foo.foo, 1)
        self.assertEqual(foo.foo, 1)
        self.assertEqual(len(called), 1)

    def test_private_attribute(self):
        # Create private lazy attributes.
        called = []

        class Foo(object):
            @snoozy.lazy_property
            def __foo(self):
                called.append('foo')
                return 1

            def get_foo(self):
                return self.__foo

        foo = Foo()
        self.assertEqual(foo.get_foo(), 1)
        self.assertEqual(foo.get_foo(), 1)
        self.assertEqual(foo.get_foo(), 1)
        self.assertEqual(len(called), 1)

    def test_reserved_attribute(self):
        # Create reserved lazy attributes.
        called = []

        class Foo(object):
            @snoozy.lazy_property
            def __foo__(self):
                called.append('foo')
                return 1

        foo = Foo()
        self.assertEqual(foo.__foo__, 1)
        self.assertEqual(foo.__foo__, 1)
        self.assertEqual(foo.__foo__, 1)
        self.assertEqual(len(called), 1)

    def test_introspection(self):
        # Supports basic introspection.
        class Foo(object):
            def foo(self):
                """foo func doc"""

            @snoozy.lazy_property
            def bar(self):
                """bar func doc"""

        self.assertEqual(Foo.foo.__name__, "foo")
        self.assertEqual(Foo.foo.__doc__, "foo func doc")
        self.assertEqual(Foo.foo.__module__, "snoozy.tests.test_snoozy")

        self.assertEqual(Foo.bar.__name__, "bar")
        self.assertEqual(Foo.bar.__doc__, "bar func doc")
        self.assertEqual(Foo.bar.__module__, "snoozy.tests.test_snoozy")
