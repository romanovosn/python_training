# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application
import time

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_t2(app):
    app.login("admin", "secret")
    app.create_group(Group(name="123", header="1234", footer="12345"))
    app.logout()

def test_t1(app):
    app.login("admin", "secret")
    app.create_group(Group(name="sdf", header="sdf", footer="sdffd"))
    app.logout()
    time.sleep(3)

