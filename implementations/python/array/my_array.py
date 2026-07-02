class MyArray:
    def __init__(self):
        self._data = []

    def get(self, i):
        return self._data[i]

    def set(self, i, value):
        self._data[i] = value

    def insert(self, i, value):
        # TODO: 뒤 원소를 한 칸씩 밀고 i 자리에 value를 넣기
        # [1,2,3,4,5]가 있다고 생각하고
        # 모든 자리를 뒤로 밀고 0에 값 넣기
        self._data.append(0)          # (1,2,3,4,5,0)
        t_len = len(self._data)-2 # 6-2 (0,1,2,3,4,5)
        for r in range(t_len , i-1 , -1):
            self._data[r+1] = self._data[r]
        self._data[i] = value
        print(f"{i}번째 인덱스에 추가됨: {self.get(i)}")
        print(self._data)

    def delete(self, i):
        # TODO: i 자리를 지우고 뒤 원소를 한 칸씩 당기기
        # [1,2,3,4,5]가 있다고 생각하고
        # (0,1,2,3,4)
        # 3을 지워보자
        # [1,2,4,5]
        # (0,1,2,3)
        # 옮기고 맨 뒤에 삭제
        t_len = len(self._data)-1 # 4
        for r in range(i, t_len ): # 2, 4(3)
            self._data[r] = self._data[r+1]
        self._data.pop()
        print(f'삭제된 후 array {self._data}')


arr = MyArray()
for v in [1,2,3,4,5]:
    arr._data.append(v)
arr.insert(2,99)
    