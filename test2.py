import unittest
from test_do_quiz.test_quiz_session import TestQuizSession 
from test_do_quiz.test_quiz_timer import TestQuizTimer
def test_suite2():
    suite = unittest.TestSuite()
    result = unittest.TestResult() 
    suite.addTest(TestQuizSession('test_start_quiz'))
    suite.addTest(TestQuizSession('test_submit_answers')) 
    suite.addTest(TestQuizSession('test_score_wrong_answer')) 
    suite.addTest(TestQuizTimer('test_start_timer'))
    suite.addTest(TestQuizTimer('test_check_time_remaining'))
    runner = unittest.TextTestRunner() 
    print(runner.run(suite))
test_suite2()