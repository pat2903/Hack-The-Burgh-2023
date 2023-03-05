from training import run_test_harness
from prediction import predict_test_image, predict_test_images


def main():
    # train model and test model accuracy
    # run_test_harness()

    # predict the value of a given image (1 - panda, 0 - other animal)
    predict_test_image('prediction_images/panda_image.jpeg')


if __name__ == "__main__":
    main()
