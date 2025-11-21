import utils
import random

FILE_1 = "POL0005_beczkowska_kedy-droga.xml"
FILE_2 = "POL0006_beczkowska_w-mieszczanskim-gniezdzie.xml"


def main():
    try:
        words_1 = utils.parse_text(FILE_1)
        words_2 = utils.parse_text(FILE_2)

    except FileNotFoundError:
        print(f"Files were not found on paths {FILE_1} and {FILE_2}")
        exit()


    min_len = min(len(words_1), len(words_2))
    words_1 = words_1[:min_len]
    words_2 = words_2[:min_len]

    bigrams_1 = utils.ngrams(words_1, 2)
    bigrams_2 = utils.ngrams(words_2, 2)
    trigrams_1 = utils.ngrams(words_1, 3)
    trigrams_2 = utils.ngrams(words_2, 3)

    words_random = random.choices(words_1, k=len(words_1))

    bigrams_random = utils.ngrams(words_random, 2)
    trigrams_random = utils.ngrams(words_random, 3)

    overlap_2_12, len_2_1, len_2_2 = utils.overlap(bigrams_1, bigrams_2)
    overlap_3_12, len_3_1, len_3_2 = utils.overlap(trigrams_1, trigrams_2)
    
    overlap_2_1_random, _, _ = utils.overlap(bigrams_1, bigrams_random)
    overlap_3_1_random, _, _ = utils.overlap(trigrams_1, trigrams_random)


    print("Results:")
    
    print(f"\n1. Real 1 vs Real 1 ({FILE_1} vs {FILE_2})")
    print(f"   Common unique bigrams: {overlap_2_12} (around {overlap_2_12/len(set(bigrams_1))*100:.2f}%)")
    print(f"   Common unique trigrams: {overlap_3_12} (around {overlap_3_12/len(set(trigrams_1))*100:.2f}%)")
    
    print(f"\n2. Real 1 vs Random 1")
    print(f"   Common unique bigrams: {overlap_2_1_random} (around {overlap_2_1_random/len(set(bigrams_1))*100:.2f}%)")
    print(f"   Common unique trigrams: {overlap_3_1_random} (around {overlap_3_1_random/len(set(trigrams_1))*100:.2f}%)")

if __name__ == "__main__":
    main()