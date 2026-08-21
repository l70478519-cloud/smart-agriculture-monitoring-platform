import sys
sys.path.insert(0,'.')
from src.domain import evaluate
def test_threshold():
 assert evaluate(75,50)["flagged"] is True
 assert evaluate(25,50)["flagged"] is False
