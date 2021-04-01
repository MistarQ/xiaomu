# 加油
# pull request text

def dfs(arr,depth):
    for i in range(len(arr[depth])):
        #print(result[depth])
        result[depth]=arr[depth][i]
        if depth<len(arr)-1:
            dfs(arr,depth+1)
        else:
            print("-".join(result))

n=3
result = [None] * n
results = [] * n
arr=[
    ["i","he","she"],
    ["is","am","are"],
    ["pig","dog","cat"]
]

dfs(arr,0)
