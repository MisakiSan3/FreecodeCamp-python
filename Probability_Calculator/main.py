import prob_calcuator
from unittest import main

hat = prob_calcuator.Hat(blue=4, red=2, green=6)
probability = prob_calcuator.experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)

# Run unit tests automatically
main(module='test_module', exit=False)