import smith_waterman

def main():
    A = "AGCT"
    B = 'ACT'
    
    
    smith_waterman(2, -1, -1, len(A), len(B))



if __name__ == '__main__':
    main()