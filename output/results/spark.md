# Results Of All Models On Spark

## On Train-test Set
|#|Model| Score1| Score2| Score3| Score4 | Overall Score |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | WordFrequencyModel | 0.4285 | 0.5933 | 0.6724 | 0.6902 | **0.5961** |
| 2 | WordConditionalModel | 0.4285 | 0.5133 | 0.5862 | 0.6168 | **0.5362** |


## On Train-train Set
|#|Model| Score1| Score2| Score3| Score4| Overall Score|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | WordFrequencyModel | 0.7951 | 0.8327 | 0.8604 | 0.8567 | **0.8362**|


## Cross Validation On Spark-train-train Set
|#|Model| Score1| Score2| Score3| Score4| Overall Score|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | WordFrequencyModel | 0.6145 |  0.7141 | 0.7829  | 0.8062 | **0.7294**|
| 2 | WordConditionalModel | 0.2951 |  0.4747 | 0.5564  | 0.5971 | **0.4808**|

