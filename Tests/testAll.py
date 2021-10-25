from Tests.testCRUD import testAdaugaRezervare, testStergeRezervare, testModificaRezervare
from Tests.testDomain import testRezervare
from Tests.testfunctionalitate2 import *
from Tests.testFunctionalitate3 import *


def runAllTests():
    testRezervare()
    testAdaugaRezervare()
    testStergeRezervare()
    testModificaRezervare()
    testTrecereClasaSuperioasa()