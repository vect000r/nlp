def smith_waterman(seq1: str, seq2: str, match_score: int = 2, mismatch_penalty: int = -1, gap_penalty: int = -1) -> list[list]:
    """
    Implementation of the Smith-Waterman algorithm. Returns a n x m size matrix of scores where n and m are lenghts of two sequences provided by the user.
    """
    
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



def parse_letter(path: str) -> dict:
    """
    Function that parses the letters. Returns a dictionary: {version_id: {line_id: text}}
    """
    
    versions = {1: {}, 2: {}, 3: {}}

    with open(path, "r") as letter:
        for line in letter:
            parts = line.strip().split('\t')
            if len(parts) >= 2:
                full_id = parts[0]
                text = parts[1]

                version = int(full_id[0])
                line_id = full_id[1:]

                version[version][line_id] = text
    
    return versions 



def traceback(score_matrix: list[list], seq1: str, seq2: str, match_score: int = 2, mismatch_penalty: int = -1, gap_penalty: int = -1):
    """
    Traces back from the maximum score to find the alignment.
    Returns: aligned_seq1, aligned_seq2, and the alignment operations
    """
    # Find the position of maximum score
    m, n = len(seq1), len(seq2)
    max_score = 0
    max_pos = (0, 0)
    
    for i in range(m + 1):
        for j in range(n + 1):
            if score_matrix[i][j] > max_score:
                max_score = score_matrix[i][j]
                max_pos = (i, j)
    
    # Traceback from max_pos until we hit 0
    i, j = max_pos
    aligned_seq1 = []
    aligned_seq2 = []
    
    while i > 0 and j > 0 and score_matrix[i][j] > 0:
        current_score = score_matrix[i][j]
        diagonal = score_matrix[i-1][j-1]
        above = score_matrix[i-1][j]
        left = score_matrix[i][j-1]
        
        # Determine which direction we came from
        if seq1[i-1] == seq2[j-1]:
            match_check = diagonal + match_score
        else:
            match_check = diagonal + mismatch_penalty
            
        if current_score == match_check:
            # diagonal
            aligned_seq1.append(seq1[i-1])
            aligned_seq2.append(seq2[j-1])
            i -= 1
            j -= 1
        elif current_score == above + gap_penalty:
            # gap in seq2
            aligned_seq1.append(seq1[i-1])
            aligned_seq2.append('-')
            i -= 1
        else:
            # gap in seq1
            aligned_seq1.append('-')
            aligned_seq2.append(seq2[j-1])
            j -= 1
    
    return ''.join(reversed(aligned_seq1)), ''.join(reversed(aligned_seq2))



def find_differences(aligned_seq1, aligned_seq2, original_seq1, original_seq2):
    """
    Finds differences and returns them with context
    Format: {text1, text2} : context
    """
    differences = []
    i = 0
    
    while i < len(aligned_seq1):
        if aligned_seq1[i] != aligned_seq2[i]:
            # Collect the differing segment
            diff_start = i
            diff1 = []
            diff2 = []
            
            while i < len(aligned_seq1) and aligned_seq1[i] != aligned_seq2[i]:
                if aligned_seq1[i] != '-':
                    diff1.append(aligned_seq1[i])
                if aligned_seq2[i] != '-':
                    diff2.append(aligned_seq2[i])
                i += 1
            
            # Get context 
            diff1_str = ''.join(diff1) if diff1 else 'x'
            diff2_str = ''.join(diff2) if diff2 else 'x'
            
            differences.append({
                'diff': (diff1_str, diff2_str),
                'position': diff_start
            })
        else:
            i += 1
    
    return differences