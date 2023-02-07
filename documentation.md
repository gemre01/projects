Cosine Similarity Algorithm

next_y_moves(data, y, tsc)

Returns predicted stock prices and root mean squared error for y days ahead based on the input file.

Parameters:
    data : historical stock movement data, only compatible with yahoo.finance historical data yet

    y : number of predicted next y moves

    tsc : treshold of cosine similarity, how big of a similarity is needed between 0 and 1



Theory behind the Algorithm:

“Those who do not remember the past are condemned to repeat it.”
                                - George Santayana


How much does history repeat itself? 

I'm a big fan of history and patterns. While studying, distinct patterns were observable in wars, revolutions, rises and falls of civilizations. Marcus Aurelius once said that whatever problems and situations you face, it had already happened to thousands of others before you. The situations repeat itself, only the variables change.

Is it true to the stock market?

Is the situation of today already happened in the past in a similar form, and if yes, what happened afterwards? How good of a prediction can we form based on this theory? That's where the Cosine Similarity Algorithm comes into play.

The basic overview of the algorithm:

1. Load the input dataset
2. Transform the dataset into moving percentages
3. Take the last x item of the list [x = 10 if y < 10 else y] (The     last x days)
4. Deconstruct the dataset into x size chunks
5. Compare the chunks to the last x days and save those chunks that have a cosine similarity larger than the treshold (more on cosine similarity: https://en.wikipedia.org/wiki/Cosine_similarity)
6. Take the next y sequences after the similar chunks and average its elements
7. Calculate predictions based on the average sequence
8. Return prediction and root mean squared error



