from Tests.testCRUD import testAdaugaRezervare, testStergeRezervare, testModificaRezervare
from Tests.testDomain import testRezervare
from Tests.testFunctionalitate4 import testPretMaxim
from Tests.testFunctionalitate5 import testOrdonareDescrescatoare
from Tests.testFunctionalitate6 import testSumaPreturilor
from Tests.testfunctionalitate2 import *
from Tests.testFunctionalitate3 import *


def runAllTests():
    testRezervare()
    testAdaugaRezervare()
    testStergeRezervare()
    testModificaRezervare()
    testTrecereClasaSuperioasa()

    testOrdonareDescrescatoare()
    testSumaPreturilor()