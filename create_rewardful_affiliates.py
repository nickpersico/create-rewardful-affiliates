import requests
import csv
import sys

# Get auth from command line
CSV_FILE = sys.argv[1]
REWARDFUL_API_KEY = sys.argv[2]
CAMPAIGN_ID = sys.argv[3]


# Create affiliate in Rewardful
def create_affiliate(first_name, last_name, email, token, campaign_id, api_key):

	# build JSON affiliate payload
	payload = {
		"first_name": first_name,
		"last_name": last_name,
		"email": email,
		"token": token,
		"campaign_id": campaign_id
	}

	base_url = 'https://api.getrewardful.com/v1/affiliates'
	post_affiliate = requests.post(base_url, auth=(api_key, ''), data=payload)

	return post_affiliate.text

# Import CSV and read it
with open(CSV_FILE, mode='rU') as csv_data:
	csv_reader = csv.reader(csv_data)
	next(csv_reader, None)  # skip the headers
	for row in csv_reader:

			# Create affiliate
			ca = create_affiliate(
				first_name=row[0],
				last_name=row[1],
				token=row[2],
				email=row[3],
				campaign_id=CAMPAIGN_ID,
				api_key=REWARDFUL_API_KEY
			)

			print ca