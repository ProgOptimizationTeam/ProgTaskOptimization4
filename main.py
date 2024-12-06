import bisection
import gradient_ascent
import golden_section



if __name__ == "__main__":
    print("Bisection Method")
    bisection.call()
    print("Golden Section Method")
    golden_section.call()
    print("Gradient Ascent Method")
    gradient_ascent.call()