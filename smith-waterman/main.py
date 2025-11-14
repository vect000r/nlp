from smith_waterman import smith_waterman

def main():
    A = "AGCT"
    B = 'ACT'
    
    score = smith_waterman(A, B)

    print(score)



if __name__ == '__main__':
    main()