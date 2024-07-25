import numpy as np


def create_train_data():
    data = [['Sunny', 'Hot', 'High', 'Weak', 'No'], ['Sunny', 'Hot', 'High', 'Strong', 'No'], ['Overcast', 'Hot', 'High', 'Weak', 'Yes'],
            ['Rain', 'Mild', 'High', 'Weak', 'Yes'], ['Rain', 'Cool', 'Normal',
                                                      'Weak', 'Yes'], ['Rain', 'Cool', 'Normal', 'Strong', 'No'],
            ['Overcast', 'Cool', 'Normal', 'Strong', 'Yes'], ['Overcast', 'Mild',
                                                              'High', 'Weak', 'No'], ['Sunny', 'Cool', 'Normal', 'Weak', 'Yes'],
            ['Rain', 'Mild', 'Normal', 'Weak', 'Yes']]
    return np.array(data)


def compute_prior_probablity(train_data):
    y_unique = ['no', 'yes']
    prior_probablity = np.zeros(len(y_unique))
    n_yes = len(train_data[:, -1][train_data[:, -1] == 'Yes'])
    n_no = len(train_data[:, -1][train_data[:, -1] == 'No'])
    prior_probablity[0] = n_no/np.size(train_data[:, -1])
    prior_probablity[1] = n_yes/np.size(train_data[:, -1])
    return prior_probablity


def compute_conditional_probability(train_data):
    conditional_probability = []
    list_x_name = []
    for i in range(0, train_data.shape[1] - 1):
        x_unique = np.unique(data[:, i])
        list_x_name.append(x_unique)
    n_yes = len(train_data[:, -1][train_data[:, -1] == 'Yes'])
    n_no = len(train_data[:, -1][train_data[:, -1] == 'No'])
    for i in range(len(list_x_name)):
        prob_yes = []
        prob_no = []
        for ele in list_x_name[i]:
            prob_yes.append(len(train_data[:, i][(train_data[:, i] == ele) & (
                train_data[:, -1] == 'Yes')])/n_yes)
            prob_no.append(len(train_data[:, i][(train_data[:, i] == ele) & (
                train_data[:, -1] == 'No')])/n_no)
        conditional_probability.append(np.array([prob_no, prob_yes]))
    return conditional_probability, list_x_name


def train_naive_bayes(train_data):
    prior_probability = compute_prior_probablity(train_data)
    conditional_probability, list_x_name = compute_conditional_probability(
        train_data)

    return prior_probability, conditional_probability, list_x_name


def get_index_from_value(feature_name, list_features):
    return np.nonzero(list_features == feature_name)[0][0]


def prediction_play_tennis(x, list_x_name, prior_probability, conditional_probability):
    x1 = get_index_from_value(x[0], list_x_name[0])
    x2 = get_index_from_value(x[1], list_x_name[1])
    x3 = get_index_from_value(x[2], list_x_name[2])
    x4 = get_index_from_value(x[3], list_x_name[3])

    p0 = conditional_probability[0][0, x1] * conditional_probability[1][0, x2] * \
        conditional_probability[2][0, x3] * \
        conditional_probability[3][0, x4] * prior_probability[0]
    p1 = conditional_probability[0][1, x1] * conditional_probability[1][1, x2] * \
        conditional_probability[2][1, x3] * \
        conditional_probability[3][1, x4] * prior_probability[1]

    if p0 > p1:
        y_pred = 0
    else:
        y_pred = 1

    return y_pred


if __name__ == "__main__":
    X = ['Sunny', 'Cool', 'High', 'Strong']
    data = create_train_data()
    prior_probability, conditional_probability, list_x_name = train_naive_bayes(
        data)
    pred = prediction_play_tennis(
        X, list_x_name, prior_probability, conditional_probability)

    if pred:
        print('Ad should go!')
    else:
        print('Ad should not go!')
