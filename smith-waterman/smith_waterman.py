def smith_waterman(seq1: str, seq2: str, match_score: int = 2, mismatch_penalty: int = -1, gap_penalty: int = -1) -> list[list]:
    m = len(seq1)
    n = len(seq2)
    
    score = [[0 for j in range(n + 1)] for i in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                diagonal_score = score[i - 1][j - 1] + match_score
            else:
                diagonal_score = score[i - 1][j - 1] + mismatch_penalty
            
            # Score from coming from above (gap in seq2)
            from_above = score[i-1][j] + gap_penalty
            
            # Score from coming from left (gap in seq1)
            from_left = score[i][j-1] + gap_penalty


            score[i][j] = max(0, diagonal_score, from_above, from_left)
    
    return score