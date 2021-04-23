import os

#讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			name, price = line.strip().split(',')
			products.append([name, price])
	return products
	print(products)


#購買者記帳輸入
def user_input(products):
	products = []
	while True:
		name = input('請輸入商品名稱： ')
		if name == 'q':
			break
		price = input('請輸入商品價格： ')
		products.append([name, price])
	return products
	print(products)

#印出所有購買紀錄
def print_products(products):
	for s in products:
		print(s[0], '的商品價格為', s[1])

#寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f: #encoding='utf-8' => 中文字（編碼）
		f.write('品名,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')

#主要程式
def main():
	if os.path.isfile('products.csv'):
		print('有檔案！')
	else:
		print('找不到檔案！')
	filename = 'products.csv'
	products = read_file(filename)
	products = user_input(products)
	print_products(products)
	write_file('products.csv', products) 

main()