from fabric.api import local


def test():
    local('coverage run --source=btsync,test $(which nosetests)')


def coverage():
    test()
    local('coverage report -m')


def test_integration():
    pass