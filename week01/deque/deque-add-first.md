# 用 add first 或 add last 这套新的 API 改写 Deque 的代码

---

```java
public static void demoOriginalDeque() {
    Deque<String> deque = new LinkedList<String>();

    deque.push("a");
    deque.push("b");
    deque.push("c");
    System.out.println(deque);

    String str = deque.peek();
    System.out.println(str);
    System.out.println(deque);

    while (deque.size() > 0) {
        System.out.println(deque.pop());
    }
    System.out.println(deque);
}

public static void demoNewDeque() {
    Deque<String> deque = new LinkedList<>();

    deque.addFirst("a");
    deque.addFirst("b");
    deque.addFirst("c");
    System.out.println(deque);

    String str = deque.peek();
    System.out.println(str);
    System.out.println(deque);

    while (deque.size() > 0) {
        System.out.println(deque.removeFirst());
    }
    System.out.println(deque);
}
```