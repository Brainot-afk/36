products = [
    {"name": "snack", "price": 10, "stock": 5},
    {"name": "soda", "price": 15, "stock": 3},
    {"name": "candy", "price": 5, "stock": 10}
]
user_money = 50

def show_menu():
    print("\n=== Menu Sản Phẩm ===")
    for idx, product in enumerate(products):
        print(f"{idx+1}:{product['name']} - Giá: {product['price']} - Số lượng còn: {product['stock']}")

def buy_product():
    global user_money
    show_menu()
    try:
        choice = int(input("Chọn số thứ tự của sản phẩm muốn mua: "))
        if choice < 1 or choice > len(products):
            print("Chọn sản phẩm không hợp lệ.")
            return
        product = products[choice - 1]
        if product['stock'] <= 0:
            print("Sản phẩm đã hết hàng.")
            return
        if user_money < product['price']:
            print("Bạn không đủ tiền để mua sản phẩm này.")
            return
        user_money -= product['price']
        product['stock'] -= 1
        print(f"Đã mua thành công {product['name']}! Số tiền còn lại của bạn: {user_money}đ")
    except ValueError:
        print("Vui lòng nhập số hợp lệ.")

def main():
    print("Chào mừng bạn đến với máy bán hàng!")
    while True:
        print(f"\nSố tiền của bạn: {user_money}đ")
        print("1. Mua sản phẩm")
        print("2. Thoát")
        choice = input("Chọn chức năng (1-2): ")
        if choice == '1':
            buy_product()
        elif choice == '2':
            print("Cảm ơn bạn đã sử dụng máy bán hàng!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")

if __name__ == "__main__":
    main()