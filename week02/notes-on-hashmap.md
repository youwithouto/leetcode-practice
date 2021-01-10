# HashMap 总结

HashMap 基于 Hash Table 实现了 `java.util.Map` 接口。

JDK 1.8 中的 HashMap 通过数组和链表实现其底层存储，并用红黑树优化长链表。HashMap 在存储某键值对（key 和 value）时，使用 key 的哈希值确定该键值对在数组中的位置，即 bin 的位置。确定该位置后，该键值对被插入到该位置中的数据结构中。这个数据结构可能是链表，也可能红黑树，由已经在该位置存储的键值对个数决定。在使用过程中，这个数据结构可以在链表和红黑树间不断转换。

### 特点

- 允许 `null` 键和 `null` 值
- 操作线程不安全
- 不保证键值对顺序不变
- 运行效率主要由 capacity 和 load factor 两个参数决定


### 主要方法

- 查找 `public V get(Object key)`
  - 主要工作由 `final Node<K,V> getNode(int hash, Object key)` 完成
    - 首先确定给定的键 key，所在的 bin 的位置，即数组的 index
      - 如果该位置不存在，则所查找的键值对不存在，返回 `null`
      - 否则，继续在确定的 bin 中查找
        - 判断确定的 bin 使用的是何种数据结构
          - 如果是红黑树，则调用其相应方法查找
          - 如果是链表，则遍历链表查找 hash 与 key 均满足条件的键值对




- 插入 `public V put(K key, V value)`
  - 主要工作由 `final V putVal(int hash, K key, V value, boolean onlyIfAbsent, boolean evict)` 完成
    - 首先确定给定的键 key，所在的 bin 的位置，即数组的 index
      - 如果该 bin 为空，则直接将键值对存入，作为链表的第一个元素
      - 如果不为空，判断确定的 bin 使用的是何种数据结构
        - 如果是红黑树，则调用红黑树的插入方法
        - 如果是链表，需要判断该键值对是否存在于链表中（需要判断是否扩容）
          - 如果不存在，则将该键值对插入到链表的末尾，作为链表的最后一个元素
          - 如果存在，则更新键值对