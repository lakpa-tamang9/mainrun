# Usage

## Exploratory Data Analysis (EDA)
From the root directory go to ```mainrun/notebook/some_eda.ipynb``` to check the dataset and do some EDA.

## Training

To train the model with consistency regularization with cyclic padding.
```python train.py cr cyclic```

1. Simply change the system arguments ```cr``` to `no_cr` for training without consistency regularization. and 
2. Change `cyclic` to either `edge`, or `token` to change the padding type.

## Plotting

To plot the learning curves go to ```mainrun/notebook/post_hoc_analysis.ipynb```, where the logfiles are loaded and the validation loss curve is plotted using matplotlib library.