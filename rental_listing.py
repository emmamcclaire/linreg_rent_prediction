def get_location_vars(soup):
    location_soup = soup.find('div', class_='app__StyledLocation-sc-1qqu9tk-20 jbSvSQ section-padding')
    location = [i.text.split(', ') for i in location_soup.find_all('li')]
    if len(location[-1]) == 2:
        location.append(location[-1])
        location[-2] = [location[-2][0]]
        location[-1] = [location[-1][1]]
    else:
        location.append(['N/A'])
    location = [i[0] for i in location]
    return location

def get_price_bed_bath(soup):
    price_bed_bath = [i.find('div', class_ = 'textIntent-title2').text
                       for i in soup.find_all(class_='summary__StyledSummaryDetailUnit-e4c4ok-13 dsPYTb')]
    price_bed_bath[0] = int(price_bed_bath[0][1:].replace(',',''))
    price_bed_bath = [int(i) for i in price_bed_bath]
    return price_bed_bath

def get_sqft(soup):
    sqft_raw = soup.find('div', class_ = 'sc-fzqKVi custom-ranges-hide__CustomRangesHide-sc-19a3hp9-0 fEUcgh u-flexContainer--row')\
    .find('div', class_ = "textIntent-title2").text
    try:
        sqft = int(sqft_raw.replace(',', ''))
    except ValueError:
        sqft = 'NaN'
    return sqft

def parse_main_table(soup): 
    main_table_td = [i.text for i in soup.find('table').find_all('td')]
    main_table_th = [i.text for i in soup.find('table').find_all('th')]
    m_f_mt_y_c = []
    global m_f_mt_y_c_headers
    m_f_mt_y_c_headers = ['MLS #', 'Furnished', 'MLS Type', 'Year Built', 'County']
    for i in zip(main_table_th, main_table_td):
        if i[0] in m_f_mt_y_c_headers:
            m_f_mt_y_c.append(i[1])
    return m_f_mt_y_c

def get_laundry_type(soup):
    desc_puller = soup.text.lower()
    in_unit_terms = ['in-unit', 'in unit', 'laundry: yes', 'laundry: washer/dryer', 'laundry: dryer, washer', 'laundry: washer, dryer']
    laundry_snippet = 'none'
    for term in in_unit_terms:
        if term in desc_puller:
            in_unit = 1
            laundry_snippet = desc_puller[desc_puller.find(term)-25:desc_puller.find(term)+25]
            break
        else:
            in_unit = 0
    return [in_unit, laundry_snippet]

def get_parking(soup):
    all_text = soup.text.lower()
    parking = ''
    #check if the number of parking spaces is listed in standard field
    parking_index_standard_field = all_text.find('num of parking spaces')
    idx_num_parking_spaces = parking_index_standard_field + len('num of parking spaces')

    if parking_index_standard_field >= 0:
        try:
            if int(all_text[idx_num_parking_spaces]) > 0:
                parking = 'parking'
            else:
                parking = 'no_parking'
        except ValueError:
            parking = 'parking_unknown'
    
    snippet = all_text[all_text.find('parking')-10:
                                   all_text.find('parking')+30]
    
    return [parking, snippet]