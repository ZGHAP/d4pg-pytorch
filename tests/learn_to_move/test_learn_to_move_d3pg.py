import unittest
from scripts.train import train, read_config


class TestsLearnToMoveD3PG(unittest.TestCase):

    # def test_d3pg_train_single_process(self):
    #     config = read_config("tests/pendulum/config.yml")
    #     config['model'] = 'd3pg'
    #     train(config)

    def test_d3pg_train_multiprocessing(self):
        CONFIG_PATH = 'tests/learn_to_move/config.yml'
        config = read_config(CONFIG_PATH)
        config['model'] = 'd3pg'
        train(CONFIG_PATH, config=config)