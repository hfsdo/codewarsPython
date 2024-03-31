import codewars_test as test
from solution import parse

@test.describe("Sample tests")
def fixed_tests():
    @test.it("Some examples")
    def tests():
        test.assert_equals(parse("ooo"), [0,0,0])
        test.assert_equals(parse("ioioio"), [1,2,3])
        test.assert_equals(parse("idoiido"), [0,1])
        test.assert_equals(parse("isoisoiso"), [1,4,25])
        test.assert_equals(parse("codewars"), [0])
