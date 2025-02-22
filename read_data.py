with open("carp.csv") as file:
   	 for line in file:
       	    row = line.rstrip().split(",")
print(f"In year {row[0]}, the carp was is Region {row[1]}")
