'''
Created on 11/06/2013

@author: victor
'''
import unittest
from pyproclust.clustering.metrics.test.data import CH_table1
from pyproclust.clustering.metrics.CalinskiHarabasz import CalinskiHarabaszCalculator
from pyproclust.clustering.clustering import Clustering
from pyproclust.clustering.cluster import Cluster
from pyRMSD.condensedMatrix import CondensedMatrix


class Test(unittest.TestCase):


    def test_evaluation(self):
        clusterings = [
                       {
                        "clustering": Clustering([Cluster(None, [0,1,2,3]),Cluster(None, [4,5])]),
                        "result": 3.74
                        },
                       ]
        
        calculator = CalinskiHarabaszCalculator()
        matrix = CondensedMatrix(CH_table1)
        
        for i in range(len(clusterings)):
            self.assertEqual(clusterings[i]["result"], calculator.evaluate(clusterings[i]["clustering"], matrix))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()