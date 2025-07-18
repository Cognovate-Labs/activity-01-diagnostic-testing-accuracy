"""
Simulate diagnostic test results
"""
import numpy as np
import pandas as pd

class DiagnosticSimulator:
    def __init__(self, n_patients=1000, prevalence=0.384):
        """
        Arguments:
        n_patients:: Number of patients
        n_patients:: int
        """
        # number of people actually with disease
        self.n_patients = n_patients
        self.prevalence = prevalence
        self.with_disease_count = int(self.n_patients*self.prevalence)

        self.s1 = self._random_rate()
        self.s2 = self._random_rate()

    def _random_rate(self, low=0.9, high=0.999):
        """
        Randomly generate value between (0.9,0.999)
        """
        return np.random.uniform(low, high)

    
    def simulate(self):
        """
        Simulate the experiment.
        """
        # true disease status: (1 = has disease, 0 = no disease)
        true_disease = np.zeros(self.n_patients)
        true_disease[:self.with_disease_count] = 1
        np.random.shuffle(true_disease)

        # generate test results based on true disease status
        test_result = []
        for status in true_disease:
            if status == 1:
                # Has disease -> test positive with probability = sensitivity
                test_result.append(np.random.rand() < self.s1)
            else:
                # No disease -> test negative with probability = specificity
                test_result.append(np.random.rand() > (1 - self.s2))
        
        # convert boolean to int
        test_result = np.array(test_result).astype(int)
        
        # create DataFrame
        df = pd.DataFrame({
            'PatientID': range(1, self.n_patients+1),
            'TrueDisease': true_disease.astype(int),
            'TestResult': test_result
        })
        
        return df