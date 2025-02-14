def rotation(row, col, direction):
    global index
    if index == N**2 + 1:
        return matrix
    
    if direction == 'right':
        matrix[row][col] = index
        index += 1
        # 오른쪽 끝 예외처리
        if matrix[row][col+1] != 0:
            return rotation(row+1,col,'down')
        else:
            return rotation(row,col+1,'right')

    elif direction == 'down':
        matrix[row][col] = index
        index += 1
        # 아래 끝 예외처리
        if matrix[row+1][col] != 0:
            return rotation(row,col-1,'left')
        else:            
            return rotation(row+1,col,'down')
    
    elif direction == 'left':
        matrix[row][col] = index
        index += 1
        # 왼쪽 끝 예외처리
        if matrix[row][col-1] != 0:  
            return rotation(row-1,col,'up')
        else:
            return rotation(row,col-1,'left')
        
    else: # direction == 'up'
        matrix[row][col] = index
        index += 1
        # 위 끝 예외처리
        if matrix[row-1][col] != 0:
            return rotation(row,col+1, 'right')
        else:
            return rotation(row-1,col, 'up')
    
    

T = int(input())
for tc in range(T):
    N = int(input())
    matrix = [[1 for _ in range(N+2)] for _ in range(N+2)]
    
    # 0 행렬의 테두리를 1로 감싸기
    for i in range(1,N+1):
        for j in range(1,N+1):
            matrix[i][j] = 0
    
    index = 1
    matrix2 = rotation(1,1,'right')
    print(f'#{tc+1}')
    for i in range(1,N+1):
        for j in range(1, N+1):
            print(matrix[i][j],end=' ')
        print()