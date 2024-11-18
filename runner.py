import unittest
import base

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        walk_ = base.Runner('a')
        for i in range(10):
            walk_.walk()
        self.assertEqual(walk_.distance, 50)
        print ('Test "walk" OK')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        run_ = base.Runner('a')
        for i in range(10):
            run_.run()
        self.assertEqual(run_.distance, 100)
        print('Test "run" OK')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        challenge1 = base.Runner('a')
        challenge2 = base.Runner('b')
        for i in range(10):
            challenge1.run()
            challenge2.walk()
        self.assertNotEqual(challenge1.distance, challenge2.distance)
        print('Test "challenge" OK')

if __name__ == '__main__':
    unittest.main()