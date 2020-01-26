"""This code calculates the difference of
TEST_CASE_NUMBERS in multiple folders."""

from os import listdir
import re
import TestData


class Delta:

    location = ""

    def __init__(self, location):
        self.location = location

    def calculate_delta(self):
        """Calculate the difference in test_case_nmubers."""

        # list folder names
        folders = listdir(self.location)

        test_case_num_folderwise = []
        testDataDetails = []
        expr = "NS-[0-9]+"
        # list file name in each folder
        for folder in folders:
            test_case_num_lst = []
            for file_ in listdir(self.location+"\\"+folder):
                # Extract numbers
                with open(self.location+"\\"+folder+"\\"+file_) as f:
                    for line in f:
                        for testNum in re.findall(expr, line):
                            testData = TestData.TestData(
                                testNum, folder, file_)
                            testDataDetails.append(testData)
                            test_case_num_lst.append(testData.testCaseNum)
            test_case_num_folderwise.append(test_case_num_lst)
        # calculate difference
        diff1 = list(
            set(test_case_num_folderwise[0]) - set(test_case_num_folderwise[1])
            )
        diff2 = list(
            set(test_case_num_folderwise[1]) - set(test_case_num_folderwise[0])
            )
        result = diff1 + diff2
        for rslt in result:
            for obj in testDataDetails:
                if rslt == obj.testCaseNum:
                    print(
                        obj.testCaseNum+"  "+obj.folderName+"  "+obj.fileName
                    )
