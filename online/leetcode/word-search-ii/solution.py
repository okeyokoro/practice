from collections import defaultdict


def boggleBoard(board, words):
    letter_coords = defaultdict(list)
    
    max_row = len(board)
    max_col = len(board[0])
    
    for row in range(max_row):
        for col in range(max_col):
            letter = board[row][col]
            letter_coords[letter].append( (row, col) )
    
    def foundmatch(word, coord, idx=0, visited=None) -> bool:
        if not visited:
            visited = set()
        
        if word[idx] == board[coord[0]][coord[1]]:
            
            if idx == len(word)-1:
                return True

            new_idx = idx+1
            new_visited = visited | {coord}
            options = []
            
            # up; row + 1
            up = (coord[0]+1, coord[1])
            if up[0] < max_row and up not in visited:
                options.append(foundmatch(word, up, new_idx, new_visited))
                
            # down; row - 1
            down = (coord[0]-1, coord[1])
            if down[0] > -1 and down not in visited:
                options.append(foundmatch(word, down, new_idx, new_visited))
                
            # left; col - 1
            left = (coord[0], coord[1]-1)
            if left[1] > -1 and left not in visited:
                options.append(foundmatch(word, left, new_idx, new_visited))
            
            # right; col + 1
            right = (coord[0], coord[1]+1)
            if right[1] < max_col and right not in visited:
                options.append(foundmatch(word, right, new_idx, new_visited))
            
            """
                # top-left; row+1, col-1
                topleft = (coord[0]+1, coord[1]-1)
                if topleft[0] < max_row and topleft[1] > -1 and topleft not in visited:
                    options.append(foundmatch(word, topleft, new_idx, new_visited))
                    
                # top-right; row+1, col+1
                topright = (coord[0]+1, coord[1]+1)
                if topright[0] < max_row and topright[1] < max_col and topright not in visited:
                    options.append(foundmatch(word, topright, new_idx, new_visited))
                    
                # bottom-left; row-1, col-1
                bottomleft = (coord[0]-1, coord[1]-1)
                if bottomleft[0] > -1 and bottomleft[1] > -1 and bottomleft not in visited:
                    options.append(foundmatch(word, bottomleft, new_idx, new_visited))
                    
                # bottom-right; row-1, col+1
                bottomright = (coord[0]-1, coord[1]+1)
                if bottomright[0] > -1 and bottomright[1] < max_col and bottomright not in visited:
                    options.append(foundmatch(word, bottomright, new_idx, new_visited))
            """
                
            return any(options)
            
        return False
    
    def found(word, starting_coords) -> bool:
        for coord in starting_coords:
            if foundmatch(word, coord):
                return True
        return False
    
    return [ 
        word for word in words
        if found(word, letter_coords[ word[0] ])
    ]



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        return boggleBoard(board, words)
