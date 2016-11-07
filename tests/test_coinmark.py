import os
import pytest
import tempfile
from coinmark import coinmark

@pytest.fixture                                              
def client(request):                                         
    """I just stole this from flaskr. I don't know what it does."""
    db_fd, coinmark.app.config['DATABASE'] = tempfile.mkstemp()
    coinmark.app.config['TESTING'] = True                      
    client = coinmark.app.test_client()                        
    with coinmark.app.app_context():                           
        coinmark.init_db()                                     
                                                             
    def teardown():                                          
        os.close(db_fd)                                      
        os.unlink(coinmark.app.config['DATABASE'])             
    request.addfinalizer(teardown)                           
                                                             
    return client                                            

def test_empty_db(client):
    rv = client.get('/')
    assert b'Hello' in rv.data
