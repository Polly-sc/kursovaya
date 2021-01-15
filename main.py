import unittest
from NewsPageTests.testNews import TestNews
from NewsPageTests.testNewsFavorites import TestNewsFavorites
from UserPageTests.testRegistration import TestRegistration
from UserPageTests.testSingIn import TestSingIn
from testCarusel import TestCarusel
from testHeader import TestHeader
from testProfile import TestProfile


def runTests(testClasses):
    loader = unittest.TestLoader()
    suitesList = []
    for testClass in testClasses:
        suite = loader.loadTestsFromTestCase(testClass)
        suitesList.append(suite)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(unittest.TestSuite(suitesList))

def main():
    runTests([TestNews, TestNewsFavorites])
    runTests([TestRegistration, TestSingIn])
    runTests([TestCarusel])
    runTests([TestHeader])
    runTests([TestProfile])

if __name__ == '__main__':
    main()
