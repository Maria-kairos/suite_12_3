import unittest
import turnament
import runner

baseST = unittest.TestSuite()
baseST.addTest(unittest.TestLoader().loadTestsFromTestCase(turnament.TournamentTest))
baseST.addTest(unittest.TestLoader().loadTestsFromTestCase(runner.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(baseST)