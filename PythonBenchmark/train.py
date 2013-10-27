import data_io
import sys
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
train_file = sys.argv[1]
model_file  = sys.argv[2]
def main():
	print("Reading training data")
	train = pd.read_csv(
			train_file,
			header    = 0,
			chunksize = 100000,
			index_col = 0
		)
	print dir(train)
	"""
	feature_names = list(train_sample.columns)
	feature_names.remove("click_bool")
	feature_names.remove("booking_bool")
	feature_names.remove("gross_bookings_usd")
	feature_names.remove("date_time")
	feature_names.remove("position")
	"""
	feature_names = [
			'prop_brand_bool',
			'srch_saturday_night_bool',
			'random_bool',
			'promotion_flag',
			'comp1_inv',
			'comp2_inv',
			'comp3_inv',
			'comp4_inv',
			'comp5_inv',
			'comp6_inv',
			'comp7_inv',
			'comp8_inv',
		]
	#feature_names.remove("booking_bool")

	for train_sample in train:
		train_sample.fillna(0.5,inplace=True)
		features = train_sample[feature_names].values
		for f in features:
			print f

if __name__=="__main__":
	main()
