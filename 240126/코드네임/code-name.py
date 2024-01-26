class Spy:
    def __init__(self, code ="", score = 0):
        self.code = code
        self.score = score
spys = []
for _ in range(5):
    code, score = tuple(input().split())
    score = int(score)
    spys.append(Spy(code,score))

mincode = ""
minscore = 101
for elem in spys:
    if elem.score < minscore:
        mincode = elem.code
        minscore = elem.score
print(mincode, minscore)