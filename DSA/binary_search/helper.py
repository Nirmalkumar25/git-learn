# from bin_search import locate_card
import bin_search
import time
import datetime

test_case = [{
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
}]

def evalute_test_cases(func,test_cases):
    test_results = list()
    for test in test_cases:
        start_time = datetime.datetime.now()
        res = func(test['input']['cards'], test['input']['query'])
        end_time = datetime.datetime.now()
        if res == test['output']:
            test['result'] = "Passed"
        else:
            test['result'] = "Failed"
        
        print("Input: \n", test['input']['cards'])
        print("Expected Output: \n", test['input']['query'])
        print("Actual Output: \n", res)
        print("Runtime: \n", end_time -  start_time)
        print("Test Result: \n", test['result'])
        print("#"*100)
        
        test_results.append(test)
    return test_results


if __name__ == "__main__":
    results = evalute_test_cases(bin_search.locate_card,test_case)
    # for res in results:
    #     print(res)