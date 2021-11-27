def preorder(tree, now):
    global res
    res[0] += now
    for next in tree[now]:
        if next != '.':
            preorder(tree, next)
            
def inorder(tree, now):
    global res
    if tree[now][0] != '.':
        inorder(tree, tree[now][0])
    res[1] += now
    if tree[now][1] != '.':
        inorder(tree, tree[now][1])

def postorder(tree, now):
    global res
    for next in tree[now]:
        if next != '.':
            postorder(tree, next)
    res[2] += now


n = int(input())
graph = dict()
for i in range(n):
    parent, left, right = input().split()
    graph[parent] = [left, right]

res = ['','','']
for traversal in [preorder, inorder, postorder]:
    traversal(graph, 'A')
print('\n'.join(res))