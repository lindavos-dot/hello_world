# Leave these lines untouched
__winc_id__ = "8c2e6882503c4baa9ce2e050497c3f2f"
__human_name__ = "stds"

# Your code here

# imports
import sys



def main():
    # read text from stdin
    text = sys.stdin.read() # read text in given file

    # Filter character given as an argument from the text
    character = sys.argv[1] # get passed in argument [1] python main.py = [0]
    filter_character = text.replace(character, "") # for stdout
    number_character_removed = text.count(character) # for stderr

    # Print the result to stdout
    sys.stdout.write(f'{filter_character}')

    # Print the total number of removed characters to stderr
    sys.stderr.write(f'{str(number_character_removed)}')



if __name__ == "__main__":
    main()

# C:\Users\Linda Vos\Desktop\hello-world\stds> echo 'abc' | python main.py a


