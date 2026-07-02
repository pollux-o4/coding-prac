public class MyArray {
    private int[] data;
    private int size; // 실제로 채워진 원소 개수 (data.length는 "용량")

    public MyArray() {
        data = new int[10];
        size = 0;
    }

    public int get(int i) {
        // TODO: i번째 원소를 반환하기 (O(1))
        return data[i];
    }

    public void set(int i, int value) {
        // TODO: i번째 자리를 value로 덮어쓰기 (O(1))
        data[i] = value;
    }

    public void insert(int i, int value) {
        if (size == data.length) {
            grow();
        }
        for (int r = size; r > i; r--) {
            data[r] = data[r - 1];
        }
        data[i] = value;
        size++;
    }

    public void delete(int i) {
        // TODO: i번째를 지우고 뒤 원소들을 한 칸씩 당기기 (O(n))
        // insert와 반대 방향 - 여기서는 앞에서 뒤로 당기면 됨
        // [1,2,3,4,5], size=5 에서 인덱스 2를 지우면 [1,2,4,5], size=4
        for (int r = i; r < size - 1; r++) {
            data[r] = data[r+1];
        }
        size--;
    }

    private void grow() {
        int[] bigger = new int[data.length * 2];
        for (int r = 0; r < data.length; r++) {
            bigger[r] = data[r];
        }
        data = bigger;
    }

    public static void main(String[] args) {
        MyArray arr = new MyArray();
        for (int v : new int[] {1, 2, 3, 4, 5}) {
            arr.insert(arr.size, v);
        }
        arr.insert(2, 11);
        for (int r = 0; r < arr.size; r++) {
            System.out.print(arr.get(r) + " ");
        }
        System.out.println();
    }
}
