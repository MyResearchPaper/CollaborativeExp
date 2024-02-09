# Learning Content and Structure aware Representations for Collaborative Expert Discovery

This repository provides a standard training and testing framework for 'Learning Content and Structure aware Representations for Collaborative Expert Discovery'.

## Performance Analysis

We provide detailed results from the top five methods for each test question, highlighting differences in $\texttt{NDCG}$ ($\Delta\texttt{NDCG}$) and $\texttt{MAP}$ ($\Delta\texttt{MAP}$) between our approach and the best baselines, as shown in the help-hurt plots in the following figure. In the figure, positive values indicate the superiority of our method. In contrast, negative values demonstrate the better performance of the corresponding baseline. The summary of our observations is as follows: (1) our method produces 148\% superior ranks in terms of $\texttt{NDCG}$ compared to the best baseline, i.e., $\texttt{EnC}$; (2) our proposed approach improves the results of our best baseline, i.e., $\texttt{EnC}$, in terms of $\texttt{MAP}$ by 35.46\%; (3) as expected all methods show a better performance on $\texttt{MAP}$ compared to $\texttt{NDCG}$. The reason is that $\texttt{MAP}$ ignores the order of experts in the ranking list, and takes only their relevance to the questions into account.

![Alt text](/ndcg_map_help.png )

## Usage

#### Installation

- Clone this repo. or download and unzip the code
- Enter the directory, and run the following code
    ```
    pip install .
    or
    pip install CollaborativeExp
    ```


#### Examples
##### e.g. 1 data preprocessing
 ```python
# import the class
from  CollaborativeExp.preprocessing import  datapreprocessing 
# run preprocessing by passing the location and dataset
datapreprocessing.createdata("./data/","android") 
 ```
The datasets are publicly available at https://archive.org/details/stackexchange. For each dataset, three files as  Posts.xml, Tags.xml, and Users.xml are required for the data preprocessing phase. 

 ##### e.g. 2 generate train and test data 
```python 
#import CollaborativeExp class to run the framework
from  CollaborativeExp.framework import  CollaborativeExp
#generate train and test data  
CollaborativeExp.prepare_train_test("data/android")
```
 ##### e.g. 3 model training
 ```python
# import CollaborativeExp class to run the framework
from  CollaborativeExp.framework import  CollaborativeExp
#perform  function run_train to train the model 
#   parameters: 
#  "data/android": dataset name and location,
#  dim_node=32,dim_word=300  node and word embedding dimentions ,
#  epochs=10,batch_size=16   the number of epochs and batch size
#  returns: trainded model is stored in ./data/android/parsed/model/
model=CollaborativeExp.run_train("data/android",dim_node=32,dim_word=32
                         ,epochs=1,batch_size=16)
# save node and word embedding vectors
model.saveembedings()
#save the model
CollaborativeExp.saveModel("data/android/parsed/model/","model",model)
#load the model
loadedModle=CollaborativeExp.loadModel("data/android/parsed/model/","model")
 ```
 
 ##### e.g. 4 perform expert finding 
 ```python
# import CollaborativeExp class to run the framework
from  CollaborativeExp.framework import  CollaborativeExp
#load the model
loadedModle=CollaborativeExp.loadModel("data/android/parsed/model/","model")
#find topk related experts for a given question
q={"title":"How Can I fix GPS in my Samsung Galaxy S?","tags":["gps","samsung-galaxy-s"],"askerID":1089}
top10=CollaborativeExp.findTopKexperts(question=q,model=loadedModle,topk=10)
print(top10)
print("done!")
 ```

