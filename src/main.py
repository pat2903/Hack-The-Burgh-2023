from training import run_test_harness
from prediction import predict_test_image
from database_creation import create_database


def main():
    # # train model and test model accuracy
    # run_test_harness()

    # predict the value of a given image (1 - panda, 0 - other animal)
    predict_test_image('../prediction_images/cat_image.jpeg')
    predict_test_image('../prediction_images/panda_image.jpeg')

    # # create database of simulated drone data
    # create_database()


if __name__ == "__main__":
    main()
