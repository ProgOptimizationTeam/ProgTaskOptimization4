import bisection
import gradient_ascent
import golden_section

# before running this file, download all 4 files and run the following command in the terminal:
# python3 main.py

if __name__ == "__main__":
    print("Bisection Method")
    bisection.call()
    print("Golden Section Method")
    golden_section.call()
    print("Gradient Ascent Method")
    gradient_ascent.call()