class Node<T>(value: T){
    var value:T = value
    var next: Node<T>? = null
    var previous:Node<T>? = null
}

class LinkedList<T> {
    private var head:Node<T>? = null
    
    var isEmpty:Boolean = (head == null)
    
    fun first():Node<T>? = head
    
    fun last(): Node<T>? {
        var node = head
        if (node != null){
            while (node?.next != null) {
                node = node?.next
			}
            return node
        } else {
            return null
        }
    }
    
    fun count():Int {
        var node = head
        if (node != null){
            var counter = 1
            while (node?.next != null){
                node = node?.next
                counter += 1
            }
            return counter
        } else {
            return 0
        }
    }
    
    fun add(value: T) {
        var newNode = Node(value)
        var lastNode = this.last()
        if (lastNode != null) {
            newNode.previous = lastNode
            lastNode.next = newNode
        } else {
            head = newNode
        }
    }
    
    override fun toString(): String {
        var s = "["
        var node = head
        while (node != null) {
            s += "${node.value}"
            node = node.next
            if (node != null) { s += ", " }
        }
        return s + "]"
    }
}

fun main() {
    var ll = LinkedList<String>()
    ll.add("Hello")
	ll.add("and")
    ll.add("Welcome")
    ll.add("To")
    ll.add("Hacktoberfest")
    ll.add("2019")
    print(ll)
}