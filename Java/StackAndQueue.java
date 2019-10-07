import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

class StackAndQueue {

    // create Stack Class.
    // Stack use First in - Last out System
    // Example is stack of plates in your kitchen.
    // When you use a plate, you get a plate from the top one first.
    public static class Stack {

        protected ArrayList<String> list = new ArrayList<String>();

        @Override
        public String toString() {
            return "" + list;
        }

        public Stack() {
        }

        // use to push data into Stack.
        public void push(String element) {
            list.add(element);
        }

        // use to show and remove a data at the top of the Stack.
        public String pop() {
            String data = list.get(list.size() - 1);
            list.remove(data);
            return data;
        }

        // use to show a data at the top of the Stack.
        public String top() {
            return list.get(list.size() - 1);
        }

        // use to check if Stack is empty
        public boolean isEmpty() {
            return list.isEmpty();
        }

        // use to show the Stack size.
        public int size() {
            return list.size();
        }

    }

    // create Queue Class.
    // Queue use First in - First out System
    // Example is queue at a food shop. First person will get a food first.
    public static class Queue {

        protected ArrayList<String> list = new ArrayList<String>();

        @Override
        public String toString() {
            return "" + list;
        }

        public Queue() {
        }

        // use to add data into Queue.
        public void enqueue(String element) {
            list.add(element);
        }

        // use to show and remove a data at the front of the Queue.
        public String dequeue() {
            String data = list.get(0);
            list.remove(data);
            return data;
        }

        // use to show a data at the front of the Queue.
        public String front() {
            return list.get(0);
        }

        // use to check if Queue is empty
        public boolean isEmpty() {
            return list.isEmpty();
        }

        // use to show the Queue size.
        public int size() {
            return list.size();
        }

    }

    public static String[] shuffle(String[] array) {
        Integer[] shuffle = new Integer[array.length];
        for (int i = 0; i < array.length; i++) {
            shuffle[i] = i;
        }
        Collections.shuffle(Arrays.asList(shuffle));
        String[] shuffleArr = new String[shuffle.length];
        for (int i = 0; i < shuffle.length; i++) {
            shuffleArr[i] = array[shuffle[i]];
        }
        ;
        return shuffleArr;
    }

    public static void main(String[] args) {

        Stack breadInstock = new Stack();
        Queue breadCustomer = new Queue();

        String[] breads = { "Eggette", "Tortilla", "Croissant", "Lagana", "Muffin", "Pretzel", "Baguette" };
        String[] customers = { "Altair", "Ezio", "Connor", "Edward", "Arno" };

        // shuffle breads and customer.
        // so everytime you run this program, you can get differenct result.
        breads = shuffle(breads);
        customers = shuffle(customers);

        // push every bread into Stack.
        for (int i = 0; i < breads.length; i++) {
            breadInstock.push(breads[i]);
        }
        // enqueue every customer into Queue.
        for (int i = 0; i < customers.length; i++) {
            breadCustomer.enqueue(customers[i]);
        }

        // Print out the result.
        System.out.println("----- Balance of Flour -----");
        System.out.println("Balance of Flour's order today:");
        System.out.println("Bread Instock (" + breadInstock.size() + ") : " + breadInstock);
        System.out.println("Queue of Customer (" + breadCustomer.size() + ") : " + breadCustomer);
        System.out.println("Latest Bread : " + breadInstock.top());
        System.out.println("First Queue : " + breadCustomer.front());
        System.out.println("----------------------------");
        while (!breadInstock.isEmpty() && !breadCustomer.isEmpty()) {
            System.out.println("* " + breadCustomer.dequeue() + " buys a " + breadInstock.pop() + ".");
        }
        System.out.println("----------------------------");
        System.out.println("Bread Remain (" + breadInstock.size() + ") : " + breadInstock);
        System.out.println("Customer Remain (" + breadCustomer.size() + ") : " + breadCustomer);
        System.out.println("----------------------------");
    }

}
