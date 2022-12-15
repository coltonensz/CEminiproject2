# importing pandas library
import pandas as pd
# importing matplotlib library
import matplotlib.pyplot as plt

# creating dataframe
df = pd.DataFrame({
    'person': [1, 2, 3, 4, 5],
    'age': [2, 42, 6, 30, 15]
})

# plotting a line graph
print("Line graph: ")
plt.plot(df["person"], df["age"])
plt.savefig('charts.png')

