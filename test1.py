import unittest
from test_question_bank.test_question_loader import TestQuestionLoader
from test_question_bank.test_question_manager import TestQuestionManager

def test_suite1():
    suite1 = unittest.TestSuite()
    result1 = unittest.TestResult()
    suite1.addTest(TestQuestionLoader('test_category'))
    suite1.addTest(TestQuestionLoader('test_difficulty'))
    suite1.addTest(TestQuestionManager('test_add_question'))
    suite1.addTest(TestQuestionManager('test_remove_question'))
    runner = unittest.TextTestRunner()
    print(runner.run(suite1))

test_suite1()