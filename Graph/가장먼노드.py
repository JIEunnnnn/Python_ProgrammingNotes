===================================================================================
#1

#f = sorted(e, key = lambda x : (x[0], -x[1]))
# 아이템 첫 번째 인자를 기준으로 오름차순으로 먼저 정렬하고,
# 그리고 그 안에서 다음 두 번째 인자를 기준으로 내림차순으로 정렬하게 하려면, 다음과 같이 할 수 있다.


def solution(n, edge):
    
    visited = [0] * n #방문노드체크하기
    
    dic_edge = {}
    for i in edge :
        if i[0] < i[1] :
            dic_edge[i[0]] = dic_edge.get(i[0], []) + [i[1]]
        else :
            dic_edge[i[1]] = dic_edge.get(i[1], []) + [i[0]]
            
    #dic_edge.sort() => 딕셔너리는 정렬X for문으로
    for i in dic_edge :
        dic_edge[i].sort()
    print(dic_edge)
    
    stack = [1,]
    count_list = {}
    count = 0
    tmp_count = 0
    
    while stack  :
        
            top = stack[-1]
            if top in dic_edge and visited[top-1] == 0 :
                
                stack.append(dic_edge[top][-1])
                dic_edge[top] = dic_edge[top][:-1]
                tmp_count += 1 
                visited[top -1] = 1
                print("#1")
                print(tmp_count)
                print(dic_edge)
                print(visited)
                print(stack)
                
                
            else :
                if top not in dic_edge or len(dic_edge[top]) == 0 :
                    visited[top -1] = 1
                    count_list[tmp_count] = count_list.get(tmp_count, []) + [top]
                    stack.pop()
                    tmp_count -= 1
                    
                    
                    print("#2")
                    print(tmp_count)
                    print(dic_edge)
                    print(visited)
                    print(stack)
                    print(count_list)
                    
                    
                    
                    
            
                
                else :
                    if len(dic_edge[top]) != 0 :#이미 방문한 노드임..
                        
                        if dic_edge[top][-1] in dic_edge :
                            print("테스트중")
                            print(top)
                            print(dic_edge[top])
                            
                            break 
                            
                        tmp_count += 1 
                        stack.append(dic_edge[top][-1])
                        dic_edge[top] = dic_edge[top][:-1]
                        print("#3")
                        print(tmp_count)
                        print(dic_edge)
                        print(visited)
                        print(stack)
                        #break
                         

                        
    print(count_list)        
    answer = 0

    return answer
