"""
Note this file contains _NO_ flask functionality.
Instead it makes a file that takes the input dictionary Flask gives us,
and returns the desired result.

This allows us to test if our modeling is working, without having to worry
about whether Flask is working. A short check is run at the bottom of the file.
"""

import pickle as pickle
from sklearn.metrics import pairwise_distances

with open("./files/doc_topic.pickle", "rb") as f:
    doc_topic = pickle.load(f)
with open("./files/story_and_topic.pickle", "rb") as f:
    story_and_topic = pickle.load(f)


def make_recommendation(dictionary):
    """
    Input:
    feature_dict: a dictionary of the form {"feature_name": "value"}

    Output:

    """
    if (len(dictionary) == 0):
        return (0, 0)


    input_story = dictionary.get('story')
    story = story_and_topic[story_and_topic.title == input_story]
    num_story_requested = int(dictionary.get('num_story'))

    distance_array = pairwise_distances(doc_topic[story.index].reshape(1,-1),doc_topic,metric='cosine')[0]
    sorted_distance = distance_array.argsort()
    recommend_index = sorted_distance[1: num_story_requested + 1]
    # recommend_df = pd.DataFrame(columns = ['Title','Continent','Author'])
    recommend_list = []
    for i in recommend_index:
        title = story_and_topic.loc[i,].title
        # continent = story_and_topic.loc[i,].continent_name
        author = story_and_topic.loc[i,].author
        # recommend_df = recommend_df.append({'Title': title,
        #                     'Continent': continent,
        #                     'Author': author}, ignore_index = True)
        recommend_story = title +' by '+ author
        recommend_list.append(recommend_story)

    x_userinput = []
    for x in dictionary.values():
        x_userinput.append(x)
    x_userinput = x_userinput[::-1]
    return x_userinput, recommend_list


if __name__ == '__main__':

    print('No error')
