import sys
sys.path.append('../')
import Read_data_and_Write_results as rw
from evaluate import match_m
import data_helpers as dh


def linear_regression():
    _, _, _, _, _, train_x, train_y, train_pos2Id, _ = dh.read("../datasets/s-train-train-split.txt")
        _, _, _, _, _, test_x, _, test_pos2Id, _ = dh.read("../datasets/s-train-test-split.txt")
    one_hot_train_x = dh.get_one_hot_matrix(train_x, len(train_pos2Id))
    one_hot_train_y = dh.get_one_hot_matrix(train_y, len(train_pos2Id))
    one_hot_test_x = dh.get_one_hot_matrix(test_x, len(test_pos2Id))
    model = linear_regression_model()
    x_r, y_r, p4 = model.fit(one_hot_train_x, one_hot_train_y)
    x_m = model.predict(one_hot_test_x)
    plt.scatter(x_r, y_r)
    plt.plot(x_m, p4(x_m), c = 'r')
    results = convert_matrix_to_2D_array("../datasets/s-train-test-split.txt", test_pos2Id, p4, x_m)
    results["overal"] = (results[1] + results[2] + results[3] + results[4])/4
    print(results)



def convert_matrix_to_2D_array(path, pos2Id, p4, x_m):
    _, _, _, _, truth, pos_lsts = rw.read_data(path)
    predictions = []
    for i in range(len(pos_lsts)):
        prediction = []
        for j in range(len(pos_lsts[i])):
            if pos_lsts[i][j] in pos2Id.keys():
                tem = pos2Id[pos_lsts[i][j]]
                prediction.append(p4(x_m[tem]))
        predictions.append(prediction)
    return match_m(predictions, truth)

if __name__ == "__main__":
    linear_regression()