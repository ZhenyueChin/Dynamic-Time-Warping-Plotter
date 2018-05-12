import pickle

import matplotlib.pyplot as plt
import os


def plot_a_list_of_tuples(tuple_lists, labels=None, specials=None, use_scatter=True):
    if specials is None:
        specials = []
    markers = ['x', 'o']
    colors = ['r', 'b', 'g']

    if not (labels is None):
        for idx in range(len(tuple_lists)):
            if use_scatter:
                plt.scatter(*zip(*tuple_lists[idx]), marker=markers[idx % len(markers)], c=colors[idx % len(colors)])
            else:
                plt.plot(*zip(*tuple_lists[idx]), linestyle='--', marker='o', c=colors[idx % len(colors)], linewidth=2.0)
    else:
        for idx in range(len(tuple_lists)):
            if use_scatter:
                plt.scatter(*zip(*tuple_lists[idx]))
            else:
                plt.plot(*zip(*tuple_lists[idx]), linestyle='--', marker='o', c='r', linewidth=2.0)
    try:
        if specials is not None and specials != [[]]:
            for idx in range(len(specials)):
                plt.scatter(*zip(*specials[idx]), marker='D', c='black')
    except TypeError:
        pass
    # plt.gca().set_aspect('equal', adjustable='box')

    plt.show()


def save_2d_lists_graph(lists, labels=None, path="", file_name=""):
    if labels is None:
        labels = []
    fig, ax0 = plt.subplots(nrows=1, figsize=(8, 3))

    markers = ['x', 'o']
    colors = ['r', 'b', 'g', 'y']

    for a_list_idx in range(len(lists)):
        a_reduced_list = []
        for x in lists[a_list_idx]:
            a_reduced_list.append((x, 0))
        if labels:
            ax0.scatter(*zip(*a_reduced_list), label=labels[a_list_idx], marker=markers[a_list_idx % len(markers)],
                        c=colors[a_list_idx % len(colors)])
        else:
            ax0.scatter(*zip(*a_reduced_list), marker='x', c='b')
        ax0.legend()

    if path and file_name:
        plt.savefig(path + os.sep + file_name, dpi=200)
    else:
        plt.show()
    plt.clf()
    plt.close()


def save_lists_graph(lists, labels=None, path="", file_name=""):
    fig, ax0 = plt.subplots(nrows=1, figsize=(16, 10))

    for a_list_idx in range(len(lists)):
        if not (labels is None):
            ax0.plot(lists[a_list_idx], linewidth=1.5, label=labels[a_list_idx])
        else:
            ax0.plot(lists[a_list_idx], linewidth=1.5)
        ax0.legend()

    if path and file_name:
        plt.savefig(path + os.sep + file_name, dpi=200)
    else:
        plt.show()
    plt.clf()
    plt.close()


def save_pickle_f(target, name):
    with open(('pkls' + os.sep + name + '.pkl'), 'wb') as output:
        pickle.dump(target, output, pickle.HIGHEST_PROTOCOL)

def load_pickle_f(name):
    with open(('pkls' + os.sep + name + '.pkl'), 'rb') as input:
        return pickle.load(input)
