import pandas as pd

data = [['tom', 10], ['nick', 15], ['juli', 14]]

df = pd.DataFrame(data, columns=['Name', 'Age'])

df.style.format({'Age': '{:$.2f}'})

print(df)
