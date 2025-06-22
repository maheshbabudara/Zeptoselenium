import pytest

from POM.test_blog import test
from time import sleep

@pytest.mark.blog
def test_blog(tes):
    t=test(tes)
    t.det("Mahesh Babu",'maheshrony@gmail.com','8639563301','Nandyala')
    # t.drop_down()
    # t.calender()
    # t.switch_window()
    # sleep(2)
    # t.web()
    # sleep(2)
    # t.condition_based_data()
    # sleep(1)
    # t.chek()
    # sleep(1)
    # t.pops('HOBBIT')
    # t.ACTIONS()
    # t.fames('mahesh@gmail.com','test123','test123')

import pytest

# from POM.practise import practise
# from time import sleep
#
# def test_check(b):
#     p=practise(b)
#     p.prac("mahesh",'mahesh@gmail;.com',"8639563301","13/Nov/2026","mahesh")

