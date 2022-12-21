public class Main {
    public static void main(String[] args) {
        Main main = new Main();
    }

    private Kattio io;
    private CircularList list;
    private CircularList copyList;

    public Main() {
        this.io = new Kattio(System.in, System.out);
        this.list = new CircularList();
        this.copyList = new CircularList();
    }

    public void closeIO() {
        this.io.close();
    }

    public void read() {
        while (io.hasMoreTokens()) {
            int val = io.getInt();
            list.addNode(val);
            copyList.addNode(val);
        }
    }
}

class Node {
    private int index;
    private int value;
    private Node next;

    public int getIndex() {
        return index;
    }

    public int getValue() {
        return value;
    }

    public Node getNext() {
        return next;
    }

    public Node(int value, int index) {
        this.index = index;
        this.value = value;
    }

    public void setNext(Node next) {
        this.next = next;
    }
}

class CircularList {
    private int size;
    private Node head;
    private Node tail;

    public CircularList() {
        this.size = 0;
        this.head = null;
        this.tail = null;
    }

    public int getSize() {
        return size;
    }

    public Node getHead() {
        return head;
    }

    public Node getTail() {
        return tail;
    }

    public void addNode(int value) {
        Node node = new Node(value, size);

        if (head == null) {
            head = node;
        } else {
            tail.setNext(node);
        }

        tail = node;
        tail.setNext(head);
        size++;
    }
}