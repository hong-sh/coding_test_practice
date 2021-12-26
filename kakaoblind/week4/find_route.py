'''
https://programmers.co.kr/learn/courses/30/lessons/42892
[[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]	[[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]
'''

class Node:
    def __init__(self, node:tuple):
        self.value = node
        self.left = None
        self.right = None 

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key_idx:int, node:tuple):
        if self.root is None:
            self.root = Node(node)
        else:
            current = self.root
            while True:
                if current.value[key_idx] < node[key_idx]:
                    if current.right is None:
                        current.right = Node(node)
                        break
                    else:
                        current = current.right
                elif current.value[key_idx] > node[key_idx]:
                    if current.left is None:
                        current.left = Node(node)
                        break
                    else:
                        current = current.left

def pre_order(current:Node, pre_order_list:list):
    if current is not None:
        pre_order_list.append(current.value[0])
        pre_order(current.left, pre_order_list)
        pre_order(current.right, pre_order_list)

def post_order(current:Node, post_order_list:list):
    if current is not None:
        post_order(current.left, post_order_list)
        post_order(current.right, post_order_list)
        post_order_list.append(current.value[0])

def solution(nodeinfo):
    answer = [[],[]]

    graphs = []
    for i in range(len(nodeinfo)):
        graphs.append((i+1, nodeinfo[i][0], nodeinfo[i][1]))
    
    graphs.sort(key= lambda x : x[2], reverse=True)

    binary_tree = BinaryTree()
    for node in graphs:
        binary_tree.insert(1, node)

    pre_order(binary_tree.root, answer[0])
    post_order(binary_tree.root, answer[1])

    return answer

if __name__ == "__main__":
    nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
    print(solution(nodeinfo))