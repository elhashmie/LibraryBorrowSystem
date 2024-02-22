from login import loginadmin
from login import loginuser

def test_loginadmin():
   assert loginadmin('1','123')
def test_loginuser():
   assert loginuser('456','741')

         