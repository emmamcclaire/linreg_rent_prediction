# Predicting Bay Area Rent Prices

Using data on four bay area counties (San Francisco County, Alameda County, San Mateo County, and Santa Clara County), predict the price of rent using a linear regression model. The data was primarily scraped from compass.com with additional walk score data scraped from walkscore.com.

**Target:** rent price ($)

**Features:**
- bedrooms
- bathrooms
- sqare footage
- year built
- has address 2 (ex. 123 A Street, **Unit 4**)
- city
- parking
- laundry
- unit type (house, apartment, townhouse, etc.)
- walk score (based on address)

**Data Used**

All features except walk score were scraped from **compass.com**. The rental data was pulled mid-January 2021 so the predictions are based on that snapshot of the rental market. 

Walk score data was scraped from **walkscore.com**. The input for each walk score was the first line of each unit's address.

**Tools Used**

- BeautifulSoup
- Scikit-learn
- Pandas
- Numpy
- Seaborn
- Matplotlib

**Possible Impacts of this Project**

This model can be implemented in the form of a web application to be used for rental property investors where for-sale properties can be inputted, scraped for features, and fed through the model to output the estimated gross rental income for the property of interest.
