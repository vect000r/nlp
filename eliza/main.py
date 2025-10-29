from eliza import Eliza


def main():
    
    eliza = Eliza('patterns.json')
    eliza.start()



if __name__ == "__main__":
    main()
