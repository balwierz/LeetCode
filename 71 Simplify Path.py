class Solution:
    def simplifyPath(self, path: str) -> str:
        p = []
        for f in path.split(r"/"):
            if not f or f == ".":
                continue
            if f == ".." :
                if p: p.pop()
                continue
            p.append(f)
        return "/" + "/".join(p)
