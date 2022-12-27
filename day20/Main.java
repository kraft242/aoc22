public class Main {
    public static void main(String[] args) {
        Main main = new Main();
        main.read();
        main.printInitalList();
        main.list.execute();
        main.printResult();
        main.closeIO();
    }

    private Kattio io;
    private CircularList list;
    private CircularList copyList;

    public Main() {
        this.io = new Kattio(System.in, System.out);
        this.list = new CircularList();
        this.copyList = new CircularList();
    }

    public void printInitalList() {
        System.out.println("Initial arrangement: \n" + list.toString() + "\n");
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

    public void printListSize() {
        int size = list.getSize();
        io.println(size);
    }

    public void printResult() {
        int res = list.getResult();
        io.println(res);
    }

    public void printList() {
        io.println(getListAsString());
    }

    private String getListAsString() {
        return list.toString();
    }
}

class Node {
    private int index;
    private final int order;
    private final int value;
    private Node next;
    private Node prev;

    public int getIndex() {
        return index;
    }

    public int getValue() {
        return value;
    }

    public Node getNext() {
        return next;
    }

    public int getOrder() {
        return order;
    }

    public Node getPrev() {
        return prev;
    }

    public void incrementIndex() {
        this.index++;
    }

    public void decrementIndex() {
        this.index--;
    }

    public void setPrev(Node prev) {
        this.prev = prev;
    }

    public void setIndex(int index) {
        this.index = index;
    }

    public Node(int value, int index) {
        this.index = index;
        this.order = index;
        this.value = value;
    }

    public void setNext(Node next) {
        this.next = next;
    }

    @Override
    public String toString() {
        return "(v: " + value + ", o:" + order + ", i: " + index + ")";
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

    private int modSize(int value) {
        return value % size;
    }

    private int mod(int numerator, int denominator) {
        int res = numerator % denominator;
        // Dunno why I subtract one, but it works.
        if (res < 0)
            res += denominator - 1;
        return res;
    }

    private int calculateSteps(Node node) {
        int value = node.getValue();
        int index = node.getIndex();
        int steps = modSize(value);

        /*
         * if (isNegative(index + steps)) {
         * steps--;
         * } else if (isPositive(index + steps)) {
         * steps++;
         * }
         */

        return steps;
    }

    private int calculateGoalIndex(Node node) {
        int index = node.getIndex();
        int value = node.getValue();
        return ((index + value) % size) - 1;
    }

    public void execute() {
        for (int order = 0; order < size; order++) {
            Node node = getNodeByOrder(order);
            moveNodeToGoal(node);
            printDebug(node);
        }
    }

    public void printDebug(Node node) {
        int value = node.getValue();
        int prev = node.getPrev().getValue();
        int next = node.getNext().getValue();
        System.out.println(value + " moves between " + prev + " and " + next);
        System.out.println(this.toString() + "\n");

    }

    private int abs(int value) {
        return Math.abs(value);
    }

    private int getSign(int value) {
        int negative = -1;
        int nonNegative = 1;
        if (value < 0)
            return negative;
        return nonNegative;
    }

    private void moveNodeToGoal(Node node) {
        int steps = calculateSteps(node);
        int numSteps = abs(steps);
        int direction = getSign(steps);
        for (int i = 0; i < numSteps; i++) {
            stepNode(node, direction);
        }
    }

    private boolean hasWrappedLeft(Node node) {
        return node.getNext() == head;
    }

    private boolean hasWrappedRight(Node node) {
        return node.getPrev() == tail;
    }

    private boolean isNegative(int value) {
        return value < 0;
    }

    private boolean isPositive(int value) {
        return value > 0;
    }

    /**
     * Original configuration:
     * (pPrev) <-> (prev) <-> (node) <-> (next) <-> (nNext)
     */
    private void stepNode(Node node, int direction) {
        if (isPositive(direction)) {
            stepNodeForwards(node);
        } else if (isNegative(direction)) {
            stepNodeBackwards(node);
        }
        return;
    }

    private void stepNodeBackwards(Node node) {
        Node next = node.getNext();
        Node prev = node.getPrev();
        Node prevPrev = prev.getPrev();

        /*
         * Step to the left:
         * (pPrev) <-> (node) <-> (prev) <-> (next) <-> (nNext)
         */

        // Move (prev) one step to the right
        prev.setNext(next);
        next.setPrev(prev);
        prev.incrementIndex();

        // Move (node) one step to the left
        node.setNext(prev);
        prev.setPrev(node);
        node.setPrev(prevPrev);
        prevPrev.setNext(node);
        node.decrementIndex();

        if (prev == head)
            head = node;
        if (next == tail)
            tail = node;
    }

    private void stepNodeForwards(Node node) {
        Node next = node.getNext();
        Node prev = node.getPrev();
        Node nextNext = next.getNext();
        /*
         * Step to the right:
         * (pPrev) <-> (prev) <-> (next) <-> (node) <-> (nNext)
         */

        // Move (next) one step to the left
        prev.setNext(next);
        next.setPrev(prev);
        next.decrementIndex();

        // Move (node) one step to the right
        next.setNext(node);
        node.setPrev(next);
        node.setNext(nextNext);
        nextNext.setPrev(node);
        node.incrementIndex();

        if (next == head)
            head = node;
        if (prev == tail)
            tail = node;
    }

    private int getValueAfterSteps(Node node, int steps) {
        Node curr = node;
        for (int i = 0; i < steps; i++)
            curr = curr.getNext();
        return curr.getValue();
    }

    public int getResult() {
        int zero = 0;
        int one = 1000 % size;
        int two = 2000 % size;
        int three = 3000 % size;
        Node zeroNode = getNodeWithValue(zero);
        int oneRes = getValueAfterSteps(zeroNode, one);
        int twoRes = getValueAfterSteps(zeroNode, two);
        int threeRes = getValueAfterSteps(zeroNode, three);
        return oneRes + twoRes + threeRes;
    }

    private Node getNodeByOrder(int order) {
        Node curr = head;
        while (curr.getOrder() != order)
            curr = curr.getNext();
        return curr;
    }

    private Node getNodeWithValue(int value) {
        Node curr = head;
        while (curr.getValue() != value)
            curr = curr.getNext();
        return curr;
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
            head.setNext(head);
            head.setPrev(head);
        } else {
            tail.setNext(node);
            node.setPrev(tail);
            node.setNext(head);
            head.setPrev(node);
        }

        tail = node;
        size++;
    }

    @Override
    public String toString() {
        String sep = ", ";
        Node curr = head;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < size; i++) {
            sb.append(curr.getValue());
            curr = curr.getNext();
            sb.append(sep);
        }
        String s = sb.substring(0, sb.length() - 2);
        return s;
    }
}