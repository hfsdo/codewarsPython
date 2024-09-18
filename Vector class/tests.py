from solution import Vector
import codewars_test as test

@test.describe("Vector tests")
def vector_tests():
    
    @test.it("addtests")
    def addtests():
        a = Vector([1, 2])
        b = Vector([3, 4])
        test.expect(a.add(b).equals(Vector([4, 6])))

    @test.it("subtracttests")
    def subtests():
        a = Vector([1, 2, 3])
        b = Vector([3, 4, 5])
        
        test.expect(a.add(b).equals(Vector([4, 6, 8]))) 

    @test.it("Example tests")
    def example_tests():
        
        a = Vector([1, 2])
        b = Vector([3, 4])
        
        test.expect(a.add(b).equals(Vector([4, 6])))
        
        
        a = Vector([1, 2, 3])
        b = Vector([3, 4, 5])
        
        test.expect(a.add(b).equals(Vector([4, 6, 8])))
        test.expect(a.subtract(b).equals(Vector([-2, -2, -2])))
        test.assert_equals(a.dot(b), 26)
        test.assert_equals(a.norm(), 14 ** 0.5)