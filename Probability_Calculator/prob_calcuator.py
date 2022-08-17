import copy
import random
# Consider using the modules imported above.

class Hat(object):
  def __init__(self, **balls):
    self.contents = []
    for ball_color, number_of_balls in balls.items():
      self.contents.extend([ball_color] * number_of_balls)
  
  def draw(self, balls):
    """ Draws a number of balls out of the hat, and returns those as a list
    """
    results = []
    if balls >= len(self.contents):
      results = copy.deepcopy(self.contents)
      random.shuffle(results)
      self.contents = []
    else:
      for i in range(balls):
        pickedBall = random.choice(self.contents)
        self.contents.remove(pickedBall)
        results.append(pickedBall)
    return results
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  M_successes = 0
  for experiment_number in range(num_experiments):
    experimental_hat = copy.deepcopy(hat)
    experiment_test = copy.deepcopy(expected_balls)
    balls_out = experimental_hat.draw(num_balls_drawn)
    # review the results of the experiment
    for ball in balls_out:
      if ball in experiment_test.keys():
        experiment_test[ball] = experiment_test[ball] - 1
    # determine if experiment was a success
    for test_ball in experiment_test:
      if experiment_test[test_ball] > 0:
        break
    else:
      M_successes += 1
  return M_successes / num_experiments