class Node {
    int key;
    int value;
    Node prev;
    Node next;
    public Node(int key, int value) {
        this.key = key;
        this.value = value;
        this.prev = this.next = null;
    }
}
class DLL {
    Node head;
    Node tail;
    public DLL() {
        this.head = this.tail = null;
    }
}
class LRUCache {
    DLL dll;
    HashMap<Integer, Node> hmp;
    int size;
    int capacity;
    public LRUCache(int capacity) {
        this.dll = new DLL();
        this.hmp = new HashMap<>();
        this.size = 0;
        this.capacity = capacity;
    }
    
    public int get(int key) {
        if (!hmp.containsKey(key)) {
            return -1;
        }
        Node currentNode = hmp.get(key);
        if (currentNode != dll.head) {
            // Remove it from it's current position in dll
            currentNode.prev.next = currentNode.next;
            if (currentNode.next != null) {
                currentNode.next.prev = currentNode.prev;
            }
            else {
                dll.tail = currentNode.prev;
            }
            // append it to the front (head)
            currentNode.next = dll.head;
            dll.head.prev = currentNode;
            dll.head = currentNode;
        }
        return currentNode.value;
    }
    
    public void put(int key, int value) {
        // Step - 1: check if the key is already in hashmap
        if (hmp.containsKey(key)) {
            Node currentNode = hmp.get(key);
            // Update it's value id DLL
            currentNode.value = value;
            if (currentNode != dll.head) {
                // Remove it from it's current position in dll
                currentNode.prev.next = currentNode.next;
                if (currentNode.next != null) {
                    currentNode.next.prev = currentNode.prev;
                }
                else {
                    dll.tail = currentNode.prev;
                }
                // append it to the front (head)
                currentNode.next = dll.head;
                dll.head.prev = currentNode;
                dll.head = currentNode;
            }
        }
        else {
            // Make a new node
            Node newNode = new Node(key, value);
            // Add it to hashmap
            hmp.put(key, newNode);
            // Add it to dll at head
            if (dll.head == null && dll.tail == null) {
                dll.head = dll.tail = newNode;
            }
            else {
                dll.head.prev = newNode;
                newNode.next = dll.head;
                dll.head = newNode;
            }
            size++;
        }
        // Check if size exceeds capacity and evict from tail
        if (size > capacity) {
            // Remove from dll tail
            Node removed = dll.tail;
            if (dll.head == dll.tail) {
                dll.head = dll.tail = null;
            }
            else {
                dll.tail = dll.tail.prev;
                dll.tail.next = null;
            }
            // Remove it from hashmap
            hmp.remove(removed.key);
            size--;
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */