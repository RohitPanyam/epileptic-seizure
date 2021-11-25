# Detection of Epileptical eeg waves
Using the eeg waves we predict if they are epileptic or not 

## Dataset : https://archive.ics.uci.edu/ml/datasets/Epileptic+Seizure+Recognition
  ## The data points are categorizer as following :
    5 - eyes open, means when they were recording the EEG signal of the brain the patient had their eyes open
    4 - eyes closed, means when they were recording the EEG signal the patient had their eyes closed
    3 - Yes they identify where the region of the tumor was in the brain and recording the EEG activity from the healthy brain area
    2 - They recorded the EEG from the area where the tumor was located
    1 - Recording of seizure activity
  
## Final Result : 
  Eplileptical - 1; 
  Not Epileptical - 0
  
- The sample we want to predict should be placed in the test_reso dir.
- Then we run the run.py in ther terminal. (which would predict the output using the model "Epilepsy.h5" and changes the out.json respectively)
- By running the result_o we can view the predection of the given test data.
