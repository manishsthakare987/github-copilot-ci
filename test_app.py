#use pytest to test the add and substract  function in app.py
from app import add 


def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0   
    assert add(-1, -1) == -2
    assert add(1.5, 2.5) == 4.0 
    assert add(-1.5, -2.5) == -4.0
    assert add(1, -1) == 0
    assert add(-1, 1) == 0  
    assert add(0, 1) == 1
    assert add(1, 0) == 1
    assert add(0, -1) == -1
    assert add(-1, 0) == -1    

def test_subtract():
    from app import subtract
    assert subtract(1, 2) == -1
    assert subtract(-1, 1) == -2
    assert subtract(0, 0) == 0   
    assert subtract(-1, -1) == 0 
    assert subtract(1.5, 2.5) == -1.0 
    assert subtract(-1.5, -2.5) == 1.0
    assert subtract(1, -1) == 2  
    assert subtract(-1, 1) == -2
    assert subtract(0, 1) == -1
    assert subtract(1, 0) == 1
    assert subtract(0, -1) == 1
    assert subtract(-1, 0) == -1    

#add main function to run the tests
if __name__ == "__main__":
    test_add()
    test_subtract()
                    
    print("All tests passed!")
