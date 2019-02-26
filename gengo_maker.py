import pandas as pd


def main():
	df = pd.DataFrame()
	res1 = pd.read_csv("joyo2010.csv", header=None, usecols=[0])
	res2 = pd.read_csv("joyo2010.csv", header=None, usecols=[0])

	print(len(res1))
	for i in range(len(res1)):
		df[str(i)] = res1[0].str.cat(res2[0])
		tmp = res2.iloc[-1]
		res2 = res2.shift(1)
		res2.at[0] = tmp
	df.to_csv("gengo_list.csv", header=False, index=False)


if __name__ == "__main__":
	main()