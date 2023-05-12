def generateParenthesis(n: int) -> list[str]:
    output = []
    class parenthesis:
        def __init__(self, startSign, endSign):
            self.children = []
            self.startSign = startSign
            self.endSign = endSign
        def addChild(self, child):
            self.children.append(child)
        def leaveChild(self, child):
            self.children.remove(child)
        def print(self):
            str = ""
            for i in self.children:
                str += i.print()
            return self.startSign + str + self.endSign
    parents: list[parenthesis] = [parenthesis('', '')] + [parenthesis('(', ')') for _ in range(n)]

    # we have already checked all combinations where parenthesis is inserted into parenthesis[0:excluding]
    def dfs(depth, excluding):
        if depth == len(parents):
            output.append(parents[0].print())
            return
        for i in range(excluding, depth):
            parents[i].addChild(parents[depth])
            dfs(depth + 1, i)
            parents[i].leaveChild(parents[depth])

    dfs(1, 0)
    return output

# Insane
def generateParenthesis_DnC(n: int) -> list[str]:
    intermediateF = ["-"] * (n + 1)
    intermediateF[0] = [""]
    def generateF(n):
        output = []
        if intermediateF[n] != "-":
            return intermediateF[n]
        for leftN in range(n):
            generateF(leftN)
            generateF(n - leftN - 1)
            for l in intermediateF[leftN]:
                for r in intermediateF[n - leftN - 1]:
                    output.append("(" + l + ")" + r)
        intermediateF[n] = output
        return output
    return generateF(n)


print(generateParenthesis_DnC(3))