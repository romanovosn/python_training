# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application
import time

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_t2(app):
    app.session.login("admin", "secret")
    app.group.create(Group(name="123", header="1234", footer="12345"))
    app.session.logout()

def test_t1(app):
    app.session.login("admin", "secret")
    app.group.create(Group(name="sdf", header="sdf", footer="sdffd"))
    app.session.logout()
    time.sleep(3)

