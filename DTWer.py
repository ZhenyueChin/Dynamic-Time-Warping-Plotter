import numpy as np
import file_processor as fp
from dtw import dtw
from matplotlib import pyplot


class DTWProcessor:
    def __init__(self, x, y):
        if not isinstance(x, list):
            x = x.reshape(-1, 1)
        else:
            x = np.array(x).reshape(-1, 1)
        self.x = x

        if not isinstance(y, list):
            y = y.reshape(-1, 1)
        else:
            y = np.array(y).reshape(-1, 1)
        self.y = y

        self.dist, self.cost, self.acc, self.path = dtw(x, y, dist=lambda x, y: np.linalg.norm(x - y, ord=1))

        self.path_matrix = []
        for i in range(len(self.x)):
            a_path = []
            for j in range(len(y)):
                a_path.append((i, j))
            self.path_matrix.append(a_path)

    def get_index_dist(self):
        return np.mean(np.fabs(self.path[0] - self.path[1]))

    def generate_critical_point_lists(self):
        x_s = []
        y_s = []
        for i in range(len(self.path[0])):
            # tmp = [(path[0][i], x[i][0]), (path[1][i], y[i][0])]
            start_idx = self.path_matrix[self.path[0][i]][self.path[1][i]]
            # print("x ravel: ", self.x.ravel().shape)
            start = (self.x.ravel()[start_idx[0]], self.y.ravel()[start_idx[1]])
            x_s.append(start[0])
            y_s.append(start[1])
        return x_s, y_s

    def plot_paths(self):
        pyplot.plot(self.x, marker='x')
        pyplot.plot(self.y, marker='x')
        # pyplot.scatter(path[0], path[1])

        a_tuple_list = []
        for i in range(len(self.path[0])):
            # tmp = [(path[0][i], x[i][0]), (path[1][i], y[i][0])]
            start_idx = self.path_matrix[self.path[0][i]][self.path[1][i]]
            start = (self.x.ravel()[start_idx[0]], self.y.ravel()[start_idx[1]])
            left = (start_idx[0], start[0])
            right = (start_idx[1], start[1])
            a_tuple_list.append([left, right])
        fp.plot_a_list_of_tuples(a_tuple_list, use_scatter=False)