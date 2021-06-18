# diabetes

Structure and usage

data
    |__ raw -> contains the original data without being processed
    |__ processed -> contains the dataset modified on the EDA notebook and the train/test files. Generated predictions of diabetes.py will be saved here.

models -> contains best model of the first iteration.

notebooks -> contains the notebooks for EDA and the making of the predictive models.

source -> contains diabetes.py file. It contains several methods of interest for this example. If you call this file you'll see the parameters of the best model and it will generate a file of predictions on data/processed.

utils -> contains some useful resources. For eample an HTML version of the EDA report.

