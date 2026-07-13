import pandas as pd
record = [(1,"manish","HR",300000),
          (2,"rahul","IT",20000),
          (3,"akhilesh","sales",25000),
          (4,"shivam","IT",33000),
          (5,"Dev","IT",40000)]
df = pd.read_csv("record.csv")
print(df)


print(df[df["salary"]>30000])


average = df["salary"].mean()
print(average)

df["happiness"] = [100000,200000,300000,400000,500000]
print(df)

df.to_csv("updated_data.xlsx",index=False)
