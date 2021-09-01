def solution(info, query):
    answer = []
    info_df = [x.split() for x in info]
    query_df = [x.replace('and', '').split() for x in query]
    my_dict = dict()

    for a in ['cpp', 'java', 'python','-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    my_dict[(a, b, c, d)] = []

    for info in info_df:
        for a in [info[0], '-']:
            for b in [info[1], '-']:
                for c in [info[2], '-']:
                    for d in [info[3], '-']:
                        my_dict[(a,b,c,d)].append(int(info[4]))

    for k in my_dict:
        my_dict[k].sort()

    for query in query_df:
        hubo = my_dict[(query[0],query[1],query[2],query[3])]
        index = index_of_greater_equal_than_x(my_dict[(query[0],query[1],query[2],query[3])],int(query[4]))
        answer.append(len(hubo) - index)

    return answer