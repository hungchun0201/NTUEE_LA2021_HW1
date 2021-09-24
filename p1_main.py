import sys
import time
from graph_gen import *
from p1 import p1_has_cycle
import networkx as nx


def main():
    start_time = time.time()
    p1_list = list()
    if len(sys.argv) <= 1:
        p1_list = get_p1('r07')
    else:
        p1_list = get_p1(sys.argv[1])
        
    p1_list_converted = convert_p1(p1_list)
    for i in range(len(p1_list)):
        # if(i!=230):
        #     continue
        graph = nx.DiGraph(p1_list[i])
        has_cycle = True
        try:
            res = nx.find_cycle(graph)
        except:
            has_cycle = False
        if p1_has_cycle(p1_list_converted[i]) != has_cycle:
            print('Bug in the {}th graph. P1.'.format(i))
    # print("--- Execution time for p1: %7f seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()
