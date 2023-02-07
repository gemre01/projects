import random as r
from numpy.linalg import norm
from numpy import dot
from numpy import array
from numpy import mean
from numpy import array
import pandas as pd
import sys
from sklearn.metrics import mean_squared_error



def main():
    next_10_moves(sys.argv[1], sys.argv[2], sys.argv[3])



def next_10_moves(data, y, tsc=0.7):
    
    # Read file
    csv_ = pd.read_csv(data)
    file = list(csv_["Close"])
    
    # How many days of data to use (5950 is the optimal result based on tests)
    n_of_days = -5950
    data = file[n_of_days:]
    
    y = int(y)
    tsc = float(tsc)


    # Size of chunks
    if y < 10:
        x = 10 
    else:
        x = y 


    percentages = []

    # Convert data to moving percentages
    for i in range(0, len(data)-1):
        percentages.append(round((data[i+1] - data[i]) / data[i], 3))

    last_x = percentages[-x:] # the last x days of data

    percentages = percentages[:-x] # percentages without the last x days of data
    
    
    # Divide the percentages into x long chunks
    chunks = list(divide_chunks(percentages, x))
    
    
    indices = []
    
    # Examine all chunk and select those with higher cosine similarity than treshold
    # Default cosine similarity threshold is 0.7
    for chunk in chunks:
        if len(last_x) == len(chunk):    
            cos_sim = dot(last_x, chunk) / (norm(last_x) * norm(chunk))

            if cos_sim > tsc:
                indices.append(percentages.index(chunk[0]))
    
    # If no similarities found, return 0
    if len(indices) == 0:
        print("empty indices, tsc might be too high")
        return 0
    
    sequences = []

    # Collects the next y moves after the similar sequences
    for index in indices:
        if index not in percentages[-x:]:
            seq = percentages[index + 1 + x : index + 1 + x + y]
            sequences.append(seq)
    
    # Average the next moves to get an average sequence
    avg_sequence = mean(sequences, axis=0)

    
    y_next_moves = []
    
    # Predict the next y moves
    today = data[-1]
    for i in avg_sequence:
        y_next_moves.append(today * (1 + i))
        today = y_next_moves[-1]

    
    actual = file[-y:]
    predicted = y_next_moves

    # Calculate root mean squared error
    rmse = (mean_squared_error(actual, predicted) ** 0.5)
    
    # Outputs the predicted numbers into a txt file
    with open("pred.txt", "w") as f:
        for item in y_next_moves:
            f.write("%f\n" % item)

    # Returns the rmse and predicted numbers
    return rmse, predicted



# Divide input list into x long chunks
def divide_chunks(lst, x):
    for i in range(0, len(lst), x):
        yield lst[i:i + (int(x))]


if __name__ == "__main__":
    main()