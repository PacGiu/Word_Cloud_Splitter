import pandas as pd

class Cluster:
    
    """
    Create tree cluster out of DataFrame.
    The class contains
    
    self.df
    self.node_id
    self.parent_node_list
    self.list_left
    self.node_id_left
    self.list_right
    self.node_id_right
    """
    
    def __init__(self, tree_dataframe):
        
        print('Root Node')
        print('---------')
        
        self.df=tree_dataframe
        
        self.node_id = -1
        self.parent_node_list=[x for x in list(self.df['Child_1'])+list(self.df['Child_2'])\
                        if not isinstance(x, int)]
        
        self.list_left=[]
        self.list_right=[]
        self.node_id_left=0
        self.node_id_right=0
        
        self._get_next_clusters()
        
    
    def display_clouds(self,top=10):
        
        
        if type(self.list_left[0])==str:
            print('node_id Left:','Leaf')
            display(pd.DataFrame(self.list_left).T.rename(columns={0:"Topic",1:"Size"}))
        else:
            print('node_id Left:',self.node_id_left)
            display(pd.DataFrame(self.list_left).sort_values(1,ascending=False)[:top]\
                    .reset_index(drop=True).rename(columns={0:"Topic",1:"Size"}))
        
        
        if type(self.list_right[0])==str:
            print('node_id Right:','Leaf')
            display(pd.DataFrame(self.list_right).T.rename(columns={0:"Topic",1:"Size"}))
        else:
            print('node_id Right:',self.node_id_right)
            display(pd.DataFrame(self.list_right).sort_values(1,ascending=False)[:top]\
                    .reset_index(drop=True).rename(columns={0:"Topic",1:"Size"}))

    def click_left(self):
        
        print('click!')
        
        if type(self.list_left[0])==str:
            print('Leaf Node - No more Splits')
        else:    
            self.node_id=self.node_id_left
            self.parent_node_list=self.list_left

            self._get_next_clusters()
        
        
    def click_right(self):
        
        print('click!')
        
        if type(self.list_right[0])==str:
            print('Leaf Node - No more Splits')
        else:
            self.node_id=self.node_id_right
            self.parent_node_list=self.list_right

            self._get_next_clusters()
        
        
    def _word_cloud(self,node_id,df):
        leaf=[]
        def leafing(node_id,df):
            temp=df[df['node_id']==node_id][['node_id','Child_1','Child_2']]

            if type(temp['Child_1'].values[0])==list:
                leaf.append(temp['Child_1'].values[0])
            else:
                leafing(int(temp['Child_1']),df)

            if type(temp['Child_2'].values[0])==list:
                leaf.append(temp['Child_2'].values[0])
            else:
                leafing(int(temp['Child_2']),df)
        leafing(node_id,df)
        return leaf
    
    def _get_next_clusters(self,):
        '''
        Output (list_left, node_id_left, list_right, node_id_right)
        '''   
        temp=self.df[self.df['node_id']==self.node_id][['node_id','Child_1','Child_2']]

        if type(temp['Child_1'].values[0])!=list:
            list_left=self._word_cloud(int(temp['Child_1'].values),self.df)
            print('len_list_left:',len(list_left))
        else:
            list_left=temp['Child_1'].values[0]
            print('len_list_left:',1)

        if type(temp['Child_2'].values[0])!=list:
            list_right=self._word_cloud(int(temp['Child_2'].values),self.df)
            print('len_list_right:',len(list_right))
        else:
            list_right=temp['Child_2'].values[0]
            print('len_list_right:',1)

        next_indexes=temp[['Child_1','Child_2']].values[0]
        node_id_left=next_indexes[0]
        node_id_right=next_indexes[1]
        print('\b')
        print('node_id Left:', node_id_left ,' node_id Right:', node_id_right)
        
        self.list_left=list_left
        self.node_id_left=node_id_left
        self.list_right=list_right
        self.node_id_right=node_id_right