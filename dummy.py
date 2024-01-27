import requests
from bs4 import BeautifulSoup
import csv
import re
urls=[
'https://www.dugdugmotorcycles.com/diamond-cushion-seat-cover-with-rider-and-pillion-backrest-for-royal-enfield-hunter-350',
'https://www.dugdugmotorcycles.com/new-hunter-350-seat-cover-with-stripes-black',
'https://www.dugdugmotorcycles.com/royal-enfield-classic-reborn-seat-cover-type-6',
'https://www.dugdugmotorcycles.com/royal-enfield-reborn-seat-cover-type-5',
'https://www.dugdugmotorcycles.com/royal-enfield-reborn-seat-cover-type-4',
'https://www.dugdugmotorcycles.com/royal-enfield-reborn-seat-cover-type-3',
'https://www.dugdugmotorcycles.com/royal-enfield-reborn-seat-cover-type-2',
'https://www.dugdugmotorcycles.com/royal-enfield-reborn-seat-cover-type-1', 
'https://www.dugdugmotorcycles.com/cushion-seat-cover-with-backrest-for-royal-enfield-hunter-350',
'https://www.dugdugmotorcycles.com/royal-enfield-seat-cover-with-padding-brown-copy',
'https://www.dugdugmotorcycles.com/royal-enfield-standard-350-seat-cover-black',
'https://www.dugdugmotorcycles.com/royal-enfield-seat-cover-with-padding-black-copy',
'https://www.dugdugmotorcycles.com/product/royal-enfield-seat-cover/comfortable-cushion-seat-covers-for-royal-enfield-classic-black/',
'https://www.dugdugmotorcycles.com/royal-enfield-seat-cover-with-padding-black',
'https://www.dugdugmotorcycles.com/dug-dug-cross-stitch-brown-seat-cover-with-back-support-for-royal-enfield-brown',
'https://www.dugdugmotorcycles.com/dug-dug-cross-stitch-black-seat-cover-with-back-support-for-royal-enfield',
]
all_products = []
for url in urls:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    product = soup.select('div.col-inner')
    print(type(product))
    if len(product)>0:
        name = product[0].select('div.product-title-container')
        if len(name)==0:
            nm='-'
        else:
            nm=name[0].text.strip()
    else:nm='-'
#     print(nm)
    if len(product)>0:
        description = product[0].select('div.tab-panels')
        if len(description)==0:
            des='-'
        else:
            des=description[0].text.strip()
    else:
        des='-'
#     print(des)
    if len(product)>0:
        sku = product[0].select('span.sku')
        sk=sku[0].text
#     print(sku[0].text)
    else:
        sk='-'
    if len(product)>0:
        brand = product[0].select('div.product-short-description')
#     print(brand)
        if len(brand)>0:
            table_rows = brand[0].find_all('tr')

        # Extracting text from each row
            row_text=''# Finding all cells in the row (<td> tags)
            if len(table_rows)>0:
                cells = table_rows[0].find_all('td') 
                span_text = cells[1].find('span').text.strip() if cells[1].find('span') else ''
                row_text += span_text + ' '
                
                brandd=row_text.strip()
            else:brandd='-'
        else:
            brandd='-'
    else:
            brandd='-'


#     print(cells)  # Print text from the row, removing extra spaces
# 
    # price = product[0].find_all('div',class_="col-inner")
    price = soup.find('span', class_='product-price')
    possible_classes = ['product-price', 'woocommerce-Price-amount']  # Possible classes containing price

    product_price = None

    for class_name in possible_classes:
        price_element = soup.find('span', class_=class_name)
        if price_element:
            product_price = price_element.text.strip()
            break  # Exit loop if price is found
    # print(product_price)


    slider_container = soup.find('div', class_='slider')  # Adjust the selector as per your webpage

    if slider_container:
        # Find all image elements within the slider container
        images = slider_container.find_all('img')

        # Extract image URLs
        image_urls = [img['src'] for img in images if 'src' in img.attrs]

        if image_urls:
            for idx, img_url in enumerate(image_urls, start=1):
                # print(f"Image {idx}: {img_url}")
                print()
        else:
            # print("No images found in the slider.")
            print()
        # print(image_urls)
    else:
        # print("Slider container not found.")
        print()

        
    sale_price_pattern = re.compile(r'₹\d{1,3}(?:,\d{3})*(?:\.\d+)?')  # Regular expression for ₹15,500.00 format

    product_sale_price = None

    # Find all matches of the price pattern in the HTML content
    matches = soup.find_all(text=sale_price_pattern)

    if matches:
        product_sale_price = matches[0].strip()

    # print(product_sale_price)
    if len(product)>0:
        weight = product[0].select('div.product-short-description')
    #     print(brand)
        if len(weight)>0:
            table_rows1 = weight[0].find_all('tr')

        # Extracting text from each row
            row_text1=''# Finding all cells in the row (<td> tags)
            if len(table_rows1)==6:
                cells1 = table_rows1[5].find_all('td') 
                span_text1 = cells1[1].find('span').text.strip() if cells1[1].find('span') else ''
                row_text1 += span_text1 + ' '

                weightt=row_text1.strip()  
            else:weightt='-'
        else:
            weightt='-'
    else:
            weightt='-'


    all_products.append({
        "Product name": nm,
        "Description": des,
        "Slug": '-',
        "SKU": sk,
        "Auto Generate SKU": '-',
        "Categories": '-',
        "Status": '-',
        "Is featured?": '-',
        "Brand": brandd,
        "Product collections": '-',
        "Labels": '-',
        "Taxes": '-',
        "Images": image_urls,
        "Price": product_price,
        "Product attributes": '-',
        "Import type": '-',
        "Is variation default?": '-',
        "Stock status": '-',
        "With storehouse management": '-',
        "Quantity": '-',
        "Allow checkout when out of stock": '-',
        "Sale price": product_sale_price,
        "Start date sale price": '-',
        "End date sale price": '-',
        "Weight":weightt,
        "Length": '-',
        "Wide": '-',
        "Height": '-',
        "Cost per item": '-',
        "Barcode": '-',
        "Content": '-',
        "Tags": '-',
        "Vendor": '-',
    })

# print(all_products)

keys = all_products[0].keys()
# print('keys',keys,all_products)
with open('Seat_Covers.csv', 'w', newline='', encoding='utf-8') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(all_products)
