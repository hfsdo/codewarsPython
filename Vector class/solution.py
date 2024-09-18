class Vector:
    def __init__(self, arr) -> None:
        self.arr = arr

    def __str__(self) -> str:
        return '('+','.join(str(a) for a in self.arr)+')'
    
    def equals(self, vec):
        print(f'compare self:{str(self.arr)}, vec:{str(vec.arr)}')
        if len(self.arr) != len(vec.arr):
            return False
        for i in range(len(self.arr)):
            if self.arr[i] != vec.arr[i]:
                return False
        return True

    def add(self, vec):
        result = []
        if len(self.arr) != len(vec.arr):
            raise BaseException
        for i in range(len(self.arr)):
            result.append(self.arr[i] + vec.arr[i])
        return Vector(result)
        
    def subtract(self, vec):
        result = []
        if len(self.arr) != len(vec.arr):
            raise BaseException
        for i in range(len(self.arr)):
            result.append(self.arr[i] - vec.arr[i])
        return Vector(result)
    
    def dot(self, vec):
        result = 0
        if len(self.arr) != len(vec.arr):
            raise BaseException
        for i in range(len(self.arr)):
            result += self.arr[i] * vec.arr[i]
        return result
    
    def norm(self):
        result = 0
        for i in range(len(self.arr)):
            result += self.arr[i] ** 2
        return result ** 0.5