from C04 import LinkedListQueue

# 链表式队列测试
print("=====链表式队列测试=========")
link_list_queue= LinkedListQueue.LinkedListQueue()
link_list_queue.push(2)
link_list_queue.push(3)
link_list_queue.push(5)
link_list_queue.push(7)

print(link_list_queue.size())
print(link_list_queue.to_list())

link_list_queue.pop()
link_list_queue.pop()
print(link_list_queue.size())
print(link_list_queue.to_list())

link_list_queue.push(11)
link_list_queue.push(13)
print(link_list_queue.size())
print(link_list_queue.to_list())