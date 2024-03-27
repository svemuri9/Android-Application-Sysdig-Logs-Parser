import sys
from collections import defaultdict
import graphviz


def createDotFileFromAdjacencyList(nodes,adj_list,file_path):

    f = graphviz.Digraph(filename=file_path)

    for node in nodes:
        f.node(node, shape="oval")

    for node1,values in adj_list.items():
        for key in values:
            node2 = key[0]
            in_time = key[1]
            out_time = key[2]
            label = "[" + str(in_time) + "-" + str(out_time) + "]"
            f.edge(node1,node2, label=label)

    f.save()



def backtrackBasedOnTimes(adj_list,poi):
    visited = defaultdict(bool)
    nodes = set()
    result_adj_list = defaultdict(set)

    queue = []
    queue.append(poi)

    prev_max_end_time = 1000000000000
    cnt = 0
    while len(queue) > 0:
        cnt += 1
        temp_queue = []
        cur_max_end_time = -1
        print("BackTrack Level - {}".format(cnt))
        for node1 in queue:
            if node1 not in visited:
                visited[node1] = True
                for key in adj_list[node1]:
                    node2 = key[0]
                    in_time = key[1]
                    out_time = key[2]
                    if int(in_time) < prev_max_end_time:
                        temp_queue.append(node2)
                        cur_max_end_time = max(cur_max_end_time,int(out_time))
                        nodes.add(node1)
                        nodes.add(node2)
                        result_adj_list[node2].add((node1,in_time,out_time))

        prev_max_end_time = cur_max_end_time
        queue = temp_queue

    return nodes, result_adj_list


def read_log_file(file_path):

    nodes=set()
    adj_list=defaultdict(set)
    rev_adj_list = defaultdict(set)

    in_time = defaultdict(int)
    out_time = defaultdict(int)

    with open(file_path) as fp:
        while True:
            line = fp.readline()

            if not line:
                break

            #print("Line{}: {}".format(count, line.strip()))
            process_name_index = line.find("process-name")
            process_name = line[process_name_index:].split(" ")[0].split("=")[-1]
            #process_id_index = line.find("process-id")
            #process_id = line[process_id_index:].split(" ")[0].split("=")[-1]
            event_type_index = line.find("event-type")
            event_type = line[event_type_index:].split(" ")[0].split("=")[-1]
            object_name_index = line.find(" name")
            object_name = line[object_name_index+1:].split(" ")[0].split("=")[-1]
            event_time_index = line.find("event-time")
            event_time = line[event_time_index:].split(" ")[0].split("=")[-1].split(".")[0]
            in_event_dir_index = line.find(" > ")

            in_event_dir = False

            if in_event_dir_index != -1:
                in_event_dir = True

            object_name="".join(l for l in object_name.splitlines() if l)
            if len(object_name)>0:
                print("process name :"+process_name, ", event type :" +event_type, ", Object name :"+object_name)
                if event_type=="write" or event_type=="recvmsg":
                    if in_event_dir==True:
                        if (process_name,object_name) not in in_time:
                            in_time[(process_name,object_name)]=event_time
                    else:
                        out_time[(process_name,object_name)]=event_time
                else:
                    if in_event_dir==True:
                        if (object_name,process_name) not in in_time:
                            in_time[(object_name,process_name)] = event_time
                    else:
                        out_time[(object_name,process_name)] = event_time

                #print(process_name,process_id,event_type,object_name,event_time)

    for key,value in in_time.items():
        if key in out_time:
            adj_list[key[0]].add((key[1],value,out_time[key]))
            rev_adj_list[key[1]].add((key[0],value,out_time[key]))
            nodes.add(key[0])
            nodes.add(key[1])

    return nodes,adj_list,rev_adj_list


#python3 parse_log_file.py -input logfile.txt -poi "string" -output test.dot
def main():

    log_file_path = sys.argv[2]

    nodes,adj_list,rev_adj_list=read_log_file(log_file_path)

    if sys.argv[3] == "-poi":

        poi = sys.argv[4]

        output_file_path = sys.argv[6]

        print("Starting backtracking.... : ")

        nodes, adj_list = backtrackBasedOnTimes(rev_adj_list, poi)

        print("Creating the dot file : {}".format(output_file_path))

        createDotFileFromAdjacencyList(nodes, adj_list, output_file_path)

        print("{} file created.".format(output_file_path))

    else:
        output_file_path = sys.argv[4]

        print("Creating the dot file : {}".format(output_file_path))

        createDotFileFromAdjacencyList(nodes ,adj_list, output_file_path)

        print("{} file created at given location".format(output_file_path))


if __name__ == "__main__":
    main()