from lib.cat_facts import *
from unittest.mock import Mock

def test_provide_cat_facts():
    requester_mock = Mock(name="requester")
    response_mock = Mock(name="response")

    requester_mock.get.return_value = response_mock

    response_mock.json.return_value = {'fact': 'Statistics indicate that animal lovers in recent years have shown a preference for cats over dogs!',
                                    'length': 98}
    
    cat_facts = CatFacts(requester_mock)

    assert cat_facts.provide() == 'Cat fact: Statistics indicate that animal lovers in recent years have shown a preference for cats over dogs!'
    
    
