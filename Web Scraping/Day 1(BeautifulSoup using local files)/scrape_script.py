from bs4 import BeautifulSoup

# with open('index.html','r') as fp:
#     content = fp.read()
    
#     soup = BeautifulSoup(content,'lxml')
#     boxes_list = soup.find_all('div',class_='box')
    
#     for box in boxes_list:
#         print(box.h3.text)
        
        
        
with open('index.html','r') as fp:
    content = fp.read()
    
    soup = BeautifulSoup(content,'lxml')
    Title = soup.find_all('title')
    product_Name = soup.find_all('h2',class_='product-name')
    product_price = soup.find_all('p',class_='price')
    
    footer = soup.find('footer')
    
    product_count = 0
    print(Title.text)
    for name,price in zip(product_Name,product_price):
        product_count += 1
        print(f'product name is {name.text} and price is {price.text}')
        print(f'product count is {product_count}')
    
    print(f'footer text is {footer.p.text}')
    

    