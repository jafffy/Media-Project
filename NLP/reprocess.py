#	Caution:
#	- Must excute with Python3
#
#	Description:
#	- Re-process movie reviews json file to txt file
#	- Only positive, negative reviews included
#	- Process for training and testing classification model


import json
import classifier as cf


def export_txt(fname, data):
	with open(fname, "w") as f:
		for d in data:
			f.write("{0:}\n" .format(d))


if __name__ == "__main__":
	raw = cf.parse_json("./review/review_2.json")
	
	review_pos = []
	review_neg = []

	for r in raw:
		if   r[0] > 8: review_pos.append(r[1])
		elif r[0] < 3: review_neg.append(r[1])

	export_txt("./review/review_pos", review_pos)
	export_txt("./review/review_neg", review_neg)


