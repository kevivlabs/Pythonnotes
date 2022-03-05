# dfs + keeping track of path:
def dfs(root, path):
    if root is None:
        return
    else:
        print(root.val)
        path.append(root)
        dfs(root.left, path)
        dfs(root.right, path)
        path.pop()
        
        
# get path from root:
def get_path_from_root(root, val):
    def dfs(root, val, path):
        if root is None:
            return False
        else:
            path.append(root)
            if root.val == val or dfs(root.left, val, path) or dfs(root.right, val, path):
                return True
            path.pop()
            return False
    path = []
    dfs(root, val, path)
    return path
  
  
# kth ancestor:
def kth_ancestor(root, val, k):
    path = get_path_from_root(root, val)
    if k >= len(path):
        return None
    else:
        return path[len(path)-k-1]
    
    
# lowest common ancestor:
def lca(root, val1, val2):
    path1 = get_path_from_root(root, val1)
    path2 = get_path_from_root(root, val2)
    last_common = None
    i = j = 0
    while i < len(path1) and j < len(path2):
        if path1[i] == path2[j]:
            last_common = path1[i]
            i += 1
            j += 1
        else:
            break
    return last_common
  
  
# root to leaf paths:
def get_root_to_leaf_paths(root):
    def dfs(root, path, paths):
        if root is None:
            return
        else:
            path.append(root)
            if root.left is None and root.right is None:
                paths.append(path.copy())
            dfs(root.left, path, paths)
            dfs(root.right, path, paths)
            path.pop()
    paths = []
    path = []
    dfs(root, path, paths)
    return paths
