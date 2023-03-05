# Hack The Burgh 2023

This is a solution to the Sustainable Development Goals challenge.

The aim of this solution is to track endangered species using a machine learning model and a heatmap, in accordance with Sustainable Development Goal 15 'Life on Land'.

The model is trained using a supervised learning approach where it is presented with input training data using labels. In this case, we have used Pandas; while they are not 
endangered anymore, this model can be adapted to any animal (land or sea) as long as the model can be provided with a dataset of reasonable size.

During evaluation, the model is presented with new unseen images of animals and it predicts whether or not the image is a specific animal and it 
outputs a probability. In this case, if the score is closer to a 1, then the model predicts that the image is a Panda.

The idea is that this can be used to identify animals in specific locations which can then be translated into a heatmap. 
This can then be used to track the distribution of the animal and their population over time to aid with conservation efforts.

Linked is the dataset that was used to train the model:
[dataset.](https://www.kaggle.com/datasets/utkarshsaxenadn/animal-image-classification-dataset)

