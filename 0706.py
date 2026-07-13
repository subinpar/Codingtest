def solution(n, w, num):
    row = (num - 1) // w
    pos = (num - 1) % w
    
    if row % 2 == 0:  
        col = pos + 1
    else:             
        col = w - pos
    
    full_rows = n // w
    rem = n % w
    
    if rem == 0:
        top_row = full_rows - 1
    else:
        if full_rows % 2 == 0:
        
            exists_in_last_row = (col <= rem)
        else:
         
            exists_in_last_row = (col >= w - rem + 1)
        
        top_row = full_rows if exists_in_last_row else full_rows - 1

    return top_row - row + 1