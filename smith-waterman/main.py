from utils import parse_letter, compare_versions

def main():
    versions = parse_letter('grimm-letters.txt')
    
    comparisons = [
        (1, 2, "Manual vs OCR"),
        (1, 3, "Manual vs Automatic"),
        (2, 3, "OCR vs Automatic")
    ]
    
    for v1, v2, label in comparisons:
        print(f"\n=== {label} ===")

        common_ids = set(versions[v1].keys()) & set(versions[v2].keys())
        
        for line_id in sorted(common_ids):
            text1 = versions[v1][line_id]
            text2 = versions[v2][line_id]
            
            if text1 != text2:
                print(f"\nLine {line_id}:")
                differences = compare_versions(text1, text2)

                for diff in differences:
                    diff1, diff2 = diff['diff']
                    position = diff['position']
                    print(f"  {{{diff1}, {diff2}}} at position {position}")
                
                print(f"  Version {v1}: {text1}")
                print(f"  Version {v2}: {text2}")




if __name__ == '__main__':
    main()