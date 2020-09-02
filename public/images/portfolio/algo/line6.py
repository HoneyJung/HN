from copy import deepcopy

def solution(directory, command):
    # 디렉토리를 dictionary를 이용해 트리 구조로 구현
    root = {}
    
    def mkdir(root, path):
        cur = root
        names = path.split('/')[1:]
        for name in names:
            if name not in cur:
                cur[name] = {}
            cur = cur[name]

    def rm(root, path):
        parent = root
        names = path.split('/')[1:]
        for name in names[:len(names) - 1]:
            parent = parent[name]
        
        del parent[names[-1]]

    def cp(root, src, dst):
        dstdir = root
        if dst != '/':
            for name in dst.split('/')[1:]:
                dstdir = dstdir[name]
        
        srcdir = root
        names = src.split('/')[1:]
        for name in names:
            srcdir = srcdir[name]
        
        # src directory는 deep copy로 복사
        dstdir[names[-1]] = deepcopy(srcdir)

    # 첫 directory 구성
    for path in directory:
        mkdir(root, path)

    # command 실행
    for cmd in command:
        splitted = cmd.split(' ')
        if len(splitted) == 2:
            cmd, path = splitted
        else:
            cmd, src, dst = splitted
        
        if cmd == 'mkdir':
            mkdir(root, path)
        elif cmd == 'rm':
            rm(root, path)
        else:
            cp(root, src, dst)
    
    res = []

    # directory tree를 dfs로 순회하면서 path의 이름을 얻음
    def getNames(root, prefix, res):
        if len(root) == 0:
            return
        for k in sorted(list(root.keys())):
            s = '/' + k
            res.append(prefix + s)
            getNames(root[k], prefix + s, res)
    
    getNames(root, '', res)
    return res