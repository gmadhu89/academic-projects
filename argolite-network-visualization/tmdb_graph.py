import http.client
import json
import csv


class Graph:

    # Do not modify
    def __init__(self, with_nodes_file=None, with_edges_file=None):
        """
        option 1:  init as an empty graph and add nodes
        option 2: init by specifying a path to nodes & edges files
        """
        self.nodes = []
        self.edges = []
        if with_nodes_file and with_edges_file:
            nodes_CSV = csv.reader(open(with_nodes_file))
            nodes_CSV = list(nodes_CSV)[1:]
            self.nodes = [(n[0],n[1]) for n in nodes_CSV]

            edges_CSV = csv.reader(open(with_edges_file))
            edges_CSV = list(edges_CSV)[1:]
            self.edges = [(e[0],e[1]) for e in edges_CSV]


    def add_node(self, id: str, name: str)->None:
        """
        add a tuple (id, name) representing a node to self.nodes if it does not already exist
        The graph should not contain any duplicate nodes
        """
        if (id,name) not in self.nodes:
            self.nodes.append((id,name))


    def add_edge(self, source: str, target: str)->None:
        """
        Add an edge between two nodes if it does not already exist.
        An edge is represented by a tuple containing two strings: e.g.: ('source', 'target').
        Where 'source' is the id of the source node and 'target' is the id of the target node
        e.g., for two nodes with ids 'a' and 'b' respectively, add the tuple ('a', 'b') to self.edges
        """
        if (source,target) not in self.edges and (target,source) not in self.edges:
            self.edges.append((source,target))


    def total_nodes(self)->int:
        """
        Returns an integer value for the total number of nodes in the graph
        """
        return len(self.nodes)


    def total_edges(self)->int:
        """
        Returns an integer value for the total number of edges in the graph
        """
        return len(self.edges)


    def max_degree_nodes(self)->dict:
        """
        Return the node(s) with the highest degree
        Return multiple nodes in the event of a tie
        Format is a dict where the key is the node_id and the value is an integer for the node degree
        e.g. {'a': 8}
        or {'a': 22, 'b': 22}
        """
        #Initializing an empty dictionary to store the degree of nodes
        all_edges = {}

        '''
        Loading all the edges for each node in a dictionary without double counting.
        '''
        for nodes in self.edges:
            if nodes[0] in all_edges:
                if not isinstance(all_edges[nodes[0]],list):
                    all_edges[nodes[0]] = [all_edges[nodes[0]]]
                all_edges[nodes[0]].append(nodes[1])
            else:
                all_edges[nodes[0]] = nodes[1]

            if nodes[1] in all_edges:
                if not isinstance(all_edges[nodes[1]],list):
                    all_edges[nodes[1]] = [all_edges[nodes[1]]]
                all_edges[nodes[1]].append(nodes[0])
            else:
                all_edges[nodes[1]] = nodes[0]

        '''
        Extracting the degree of each node to get the nodes with max degree
        '''
        all_edges = {k:(len(set(v)) if isinstance(v,list) else 1) for k,v in all_edges.items()}

        '''
        Evaluating and returning the nodes with max degree
        '''
        return {k:v for k,v in all_edges.items() if v == all_edges[max(all_edges,key=all_edges.get)]}


    def print_nodes(self):
        """
        No further implementation required
        May be used for de-bugging if necessary
        """
        print(self.nodes)


    def print_edges(self):
        """
        No further implementation required
        May be used for de-bugging if necessary
        """
        print(self.edges)


    # Do not modify
    def write_edges_file(self, path="edges.csv")->None:
        """
        write all edges out as .csv
        :param path: string
        :return: None
        """
        edges_path = path
        edges_file = open(edges_path, 'w', encoding='utf-8')

        edges_file.write("source" + "," + "target" + "\n")

        for e in self.edges:
            edges_file.write(e[0] + "," + e[1] + "\n")

        edges_file.close()
        print("finished writing edges to csv")


    # Do not modify
    def write_nodes_file(self, path="nodes.csv")->None:
        """
        write all nodes out as .csv
        :param path: string
        :return: None
        """
        nodes_path = path
        nodes_file = open(nodes_path, 'w', encoding='utf-8')

        nodes_file.write("id,name" + "\n")
        for n in self.nodes:
            nodes_file.write(n[0] + "," + n[1] + "\n")
        nodes_file.close()
        print("finished writing nodes to csv")


    #Utility function to count number of leaf nodes (nodes with degree =1)
    def count_leaf_nodes(self)->int:
        all_edges = {}

        for nodes in edges:
            if nodes[0] in all_edges:
                if not isinstance(all_edges[nodes[0]],list):
                    all_edges[nodes[0]] = [all_edges[nodes[0]]]
                all_edges[nodes[0]].append(nodes[1])
            else:
                all_edges[nodes[0]] = nodes[1]

            if nodes[1] in all_edges:
                if not isinstance(all_edges[nodes[1]],list):
                    all_edges[nodes[1]] = [all_edges[nodes[1]]]

                all_edges[nodes[1]].append(nodes[0])
            else:
                all_edges[nodes[1]] = nodes[0]

        all_edges = {k:(len(set(v)) if isinstance(v,list) else 1) for k,v in all_edges.items()}

        return len({k:v for k,v in all_edges.items() if v == 1})


class  TMDBAPIUtils:

    # Do not modify
    def __init__(self, api_key:str):
        self.api_key=api_key


    def get_movie_cast(self, movie_id:str, limit:int=None, exclude_ids:list=None) -> list:
        """
        Get the movie cast for a given movie id, with optional parameters to exclude an cast member
        from being returned and/or to limit the number of returned cast members
        documentation url: https://developers.themoviedb.org/3/movies/get-movie-credits

        :param integer movie_id: a movie_id
        :param integer limit: maximum number of returned cast members by their 'order' attribute
            e.g., limit=5 will attempt to return the 5 cast members having 'order' attribute values between 0-4
            If after exluding, there are fewer cast members than the specified limit or the limit not specified, return all cast members.
            If cast members with 'order' attribute in the specified limit range have been excluded, do not include more cast members to reach the limit.
            e.g., if limit=5 and the actor whose id corresponds to cast member with order=1 is to be excluded,
            return cast members with order values [0, 2, 3, 4], not [0, 2, 3, 4, 5]
        :param list exclude_ids: a list of ints containing ids (not cast_ids) of cast members  that should be excluded from the returned result
            e.g., if exclude_ids are [353, 455] then exclude these from any result.
        :rtype: list
            return a list of dicts, one dict per cast member with the following structure:
                [{'id': '97909' # the id of the cast member
                'character': 'John Doe' # the name of the character played
                'credit_id': '52fe4249c3a36847f8012927' # id of the credit, ...}, ... ]
                Note that this is an example of the structure of the list and some of the fields returned by the API.
                The result of the API call will include many more fields for each cast member.
        """

        #Asserting input variables to the required datatypes (limit->int, exclude_ids->list)
        limit = int(0 if limit is None else limit)
        exclude_ids = [ ] if exclude_ids is None else exclude_ids


        #Storing the number of casts to be limited in a list
        cast_limit = [int(i) for i in range(limit)]

        #Initializing final_list which will return a list of dicts of each cast member
        final_list = [ ]
        cast_order = [ ]


        #Setting the variables to connect to Movie Database API
        get_cast = F"/3/movie/{movie_id}/credits?api_key={self.api_key}&language=en-US"
        movie_url = "api.themoviedb.org"


        #Setting up the HTTP connection and getting the response from API
        conn = http.client.HTTPSConnection(movie_url)
        conn.request("GET", get_cast)
        data = conn.getresponse().read().decode('utf-8')
        data_dict = json.loads(data)


        #Getting the cast members per the limit and exclusion criteria
        if (limit == 0) or ((limit-len(set(exclude_ids))) > len(data_dict['cast'])):
            for cast in data_dict['cast']:
                if int(cast['id']) not in exclude_ids:
                    final_list.append(cast)
        else:
            for cast in data_dict['cast'][:]:
                if int(cast['order']) in cast_limit:
                    cast_order.append(cast['order'])
                    if int(cast['id']) not in exclude_ids:
                        final_list.append(cast)
                    if sorted(cast_order) == cast_limit:
                        break

        return final_list


    def get_movie_credits_for_person(self, person_id:str, vote_avg_threshold:float=None)->list:

        """
        Using the TMDb API, get the movie credits for a person serving in a cast role
        documentation url: https://developers.themoviedb.org/3/people/get-person-movie-credits

        :param string person_id: the id of a person
        :param vote_avg_threshold: optional parameter to return the movie credit if it is >=
            the specified threshold.
            e.g., if the vote_avg_threshold is 5.0, then only return credits with a vote_avg >= 5.0
        :rtype: list
            return a list of dicts, one dict per movie credit with the following structure:
                [{'id': '97909' # the id of the movie credit
                'title': 'Long, Stock and Two Smoking Barrels' # the title (not original title) of the credit
                'vote_avg': 5.0 # the float value of the vote average value for the credit}, ... ]
        """

        #Declaring a list to hold the final list of dicts for every movie credit
        final_list = []

        #Setting the variables to connect to Movie Database API
        get_credits = F"/3/person/{person_id}/movie_credits?api_key={self.api_key}&language=en-US"
        movie_url = "api.themoviedb.org"


        #Setting up the HTTP connection and getting the response from API
        conn = http.client.HTTPSConnection(movie_url)
        conn.request("GET", get_credits)
        data = conn.getresponse().read().decode('utf-8')
        data_dict = json.loads(data)

        if vote_avg_threshold == None:
            final_list = data_dict['cast'][:]
        else:
            for credit in data_dict['cast'][:]:
                if float(credit['vote_average']) >= vote_avg_threshold:
                    final_list.append(credit)

        return final_list


# BEGIN BUILD CO-ACTOR NETWORK
#
# INITIALIZE GRAPH
#   Initialize a Graph object with a single node representing Laurence Fishburne
#
# BEGIN BUILD BASE GRAPH:
#   Find all of Laurence Fishburne's movie credits that have a vote average >= 8.0
#   FOR each movie credit:
#   |   get the movie cast members having an 'order' value between 0-2 (these are the co-actors)
#   |
#   |   FOR each movie cast member:
#   |   |   using graph.add_node(), add the movie cast member as a node (keep track of all new nodes added to the graph)
#   |   |   using graph.add_edge(), add an edge between the Laurence Fishburne (actress) node
#   |   |   and each new node (co-actor/co-actress)
#   |   END FOR
#   END FOR
# END BUILD BASE GRAPH
#
#
# BEGIN LOOP - DO 2 TIMES:
#   IF first iteration of loop:
#   |   nodes = The nodes added in the BUILD BASE GRAPH (this excludes the original node of Laurence Fishburne!)
#   ELSE
#   |    nodes = The nodes added in the previous iteration:
#   ENDIF
#
#   FOR each node in nodes:
#   |  get the movie credits for the actor that have a vote average >= 8.0
#   |
#   |   FOR each movie credit:
#   |   |   try to get the 3 movie cast members having an 'order' value between 0-2
#   |   |
#   |   |   FOR each movie cast member:
#   |   |   |   IF the node doesn't already exist:
#   |   |   |   |    add the node to the graph (track all new nodes added to the graph)
#   |   |   |   ENDIF
#   |   |   |
#   |   |   |   IF the edge does not exist:
#   |   |   |   |   add an edge between the node (actor) and the new node (co-actor/co-actress)
#   |   |   |   ENDIF
#   |   |   END FOR
#   |   END FOR
#   END FOR
# END LOOP
#
# Your graph should not have any duplicate edges or nodes
# Write out your finished graph as a nodes file and an edges file using:
#   graph.write_edges_file()
#   graph.write_nodes_file()
#
# END BUILD CO-ACTOR NETWORK
# ----------------------------------------------------------------------------------------------------------------------


def return_name()->str:
    """
    Return a string containing your GT Username
    e.g., gburdell3
    Do not return your 9 digit GTId
    """
    return 'mganesan7'


def return_argo_lite_snapshot()->str:
    """
    Return the shared URL of your published graph in Argo-Lite
    """
    return 'https://poloclub.github.io/argo-graph-lite/#fb015d5e-4934-4f3e-83be-73e899e9cdd1'


#Function to build graph
def build_graph(node, vote_avg_threshold):
    nodes_list = []               #Initializing an empty list to hold co-actors per actor
    credits = tmdb_api_utils.get_movie_credits_for_person(node, vote_avg_threshold)

#Getting the Top 3 co-actors for every movie credit
    for credit in credits:
        movie_id = credit['id']
        exclude_id = int(node)

        casts = tmdb_api_utils.get_movie_cast(movie_id,3,[exclude_id])

        for cast in casts:                              #Iterating for every movie cast and adding them to the graph
            graph.add_node(str(cast['id']),cast['original_name'].replace(",",""))
            graph.add_edge(str(exclude_id), str(cast['id']))
            if cast['id'] not in nodes_list: nodes_list.append(cast['id'])

    #Returning the nodes added in this iteration for the next pass.
    return nodes_list



# You should modify __main__ as you see fit to build/test your graph using  the TMDBAPIUtils & Graph classes.
# Some boilerplate/sample code is provided for demonstration. We will not call __main__ during grading.

if __name__ == "__main__":

    graph = Graph()
    graph.add_node(id='2975', name='Laurence Fishburne')
    tmdb_api_utils = TMDBAPIUtils(api_key='################################')

    # call functions or place code here to build graph (graph building code not graded)
    # Suggestion: code should contain steps outlined above in BUILD CO-ACTOR NETWORK


    #Initializing lists to hold all new nodes added as part of co-actor network within and outside iteration
    #Iterating our code 3 times
    #1. Will build the base graph with Laurence Fishburne's
    #2. Will Build graph for nodes added from Base Graph
    #3. WIll Build Graph for nodes added from step 2.

    new_nodes = []
    nodes_added = []

#Running code 3 times
#This will get the nodes from the previous iteration, assert if it exists
#Building the base graph with Laurence Fishburne's
# Clearing nodes_added for the next iteration
#Iterating through all the co-actors that were added as part of the previous iteration
#Each node(actor's) list of co-actors will be appended to the list
    #Eliminating the older nodes from the new nodes list
    for i in range(3):
        if graph.total_nodes() == 1:
            new_nodes = ['2975']
            vote_avg_threshold = 8.0
        else:
            new_nodes = nodes_added
            nodes_added = []
            vote_avg_threshold = 8.0


        for node in new_nodes:
            nodes_added.extend(build_graph(node,vote_avg_threshold))
        nodes_added = list(set(nodes_added).difference(set(new_nodes)))


    graph.write_edges_file()
    graph.write_nodes_file()

    # If you have already built & written out your graph, you could read in your nodes & edges files
    # to perform testing on your graph.
    # graph = Graph(with_edges_file="edges.csv", with_nodes_file="nodes.csv")
