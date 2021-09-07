import copy
def solution(tickets):
    N = len(tickets)
    hubo = []
    
    def dfs(tickets,path,start):
        if len(path) == N+1:
            hubo.append(path)
            return 

        for i,p in enumerate(tickets):
            if p[0] == start:
                rest_ticket = copy.deepcopy(tickets)
                rest_ticket.pop(i)
                dfs(rest_ticket, path+[p[1]], p[1])
                
    dfs(tickets,['ICN'],'ICN')
    hubo.sort()
    return hubo[0]