import codewars_test as test
from solution import valid_ISBN10

@test.describe("Sample tests")
def tests():
    @test.it("Some examples")
    def tests():
        test.assert_equals(valid_ISBN10('1112223339'), True)
        test.assert_equals(valid_ISBN10('048665088X'), True)
        test.assert_equals(valid_ISBN10('1293000000'), True)
        test.assert_equals(valid_ISBN10('1234554321'), True)
        test.assert_equals(valid_ISBN10('1234512345'), False)
        test.assert_equals(valid_ISBN10('1293'), False)
        test.assert_equals(valid_ISBN10('X123456788'), False)
        test.assert_equals(valid_ISBN10('ABCDEFGHIJ'), False)
        test.assert_equals(valid_ISBN10('XXXXXXXXXX'), False)
        test.assert_equals(valid_ISBN10('123456789T'), False)