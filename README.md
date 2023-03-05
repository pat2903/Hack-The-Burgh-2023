# Hack The Burgh 2023 SDG Task

This is a solution to the Sustainable Development Goals challenge.

The aim of this solution is to track endangered species using a machine learning model and a heatmap, in accordance with Sustainable Development Goal 15 'Life on Land'.

The model is trained using a supervised learning approach where it is presented with input training data using labels. In this case, we have used Pandas; while they are not 
endangered anymore, this model can be adapted to any animal (land or sea) as long as the model can be provided with a dataset of reasonable size.

During evaluation, the model is presented with new unseen images of animals and it predicts whether or not the image is a specific animal and it 
outputs a probability. In this case, if the score is closer to a 1, then the model predicts that the image is a Panda.

The idea is that this can be used to identify animals in specific locations which can then be translated into a heatmap. 
This can then be used to track the distribution of the animal and their population over time to aid with conservation efforts.

Linked is the dataset that was used to train the model (~20 GB):
[dataset.](https://www.kaggle.com/datasets/utkarshsaxenadn/animal-image-classification-dataset)


**Table of probabilities**

| % Pandas Identified |      |
|---------------------| ---- |
| 0.9285714           | **panda** |
| 0.125               | beetle |
| 0.10891089          | butterfly |
| 0.1493671           | cat |
| 0.25153375          | cow |
| 0.08988764          | dogs |
| 0.33714285          | elephants |
| 0.7096774           | gorilla |
| 0.37931034          | hippo |
| 0.13861386          | lizard |
| 0.3783784           | monkey |
| 0.25742576          | mouse |
| 0.34653464          | spider |
| 0.23030303          | tiger |
| 0.05904059          | zebra |
| 0.3598485           | sheep |
| 0.33128834          | squirrels |

**Preview of Heatmap**

![Heatmap](heatmap_preview.png)