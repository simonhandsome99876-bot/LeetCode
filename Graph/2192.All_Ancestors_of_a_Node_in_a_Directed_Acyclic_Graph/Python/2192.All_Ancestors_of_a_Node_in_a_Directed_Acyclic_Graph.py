class Solution(object):
    def getAncestors(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        #===========================================#
        # Depth-first search based traversal method #
        #===========================================#

        ############
        #Initialize
        ##### Length of edges array #####
        len_edges = len(edges)

        ##### Root-child array #####
        root_child_arry = [[] for _ in range(n)]

        ##### Result array #####
        res_arry = [[] for _ in range(n)]


        #############################################################
        #Depth-first search based loop traversal with recorded array
        ##### Step 1: Record indexed-nodes informations with array #####
        for edges_idx in range(len_edges):
            (root_child_arry[(edges[edges_idx])[0]]).append((edges[edges_idx])[1]) #Keep updating/recording

        ##### Step 2: Looped-traversal with recorded array #####
        for n_idx in range(n):
            self.dfsTraversal(n_idx, n_idx, root_child_arry, res_arry) #Recursion function call

        return res_arry


    def dfsTraversal(self, curr_node, curr_value, root_child_arry, res_arry):
        """
        :type curr_node: int
        :type curr_value: int
        :type root_child_arry: List[List[int]]
        :type res_arry: List[List[int]]
        :rtype: None, void
        """
        #=============================================#
        # Depth-first search based traversal function #
        #=============================================#

        ####################
        #Whole process/flow
        for next_node in root_child_arry[curr_node]:

            ##### Check if the current-next nodes matched conditions or not #####
            if ((not res_arry[next_node]) or ((res_arry[next_node])[(-1)] != curr_value)):
                (res_arry[next_node]).append(curr_value) #Keep updating/recording

                self.dfsTraversal(next_node, curr_value, root_child_arry, res_arry) #Recursion function call
