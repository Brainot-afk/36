import os

products = [
    {"name": "Snack", "price": 10, "stock": 5},
    {"name": "Soda", "price": 15, "stock": 4},
    {"name": "Candy", "price": 5, "stock": 10}
]
user_money = 50
history = []
admin_password = "1234"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    print("\n" + "="*10 + " MENU SẢN PHẨM " + "="*10)
    print(f"{'STT':<5} {'Tên món':<15} {'Giá':<10} {'Tồn kho':<10}")
    print("-" * 45)
    for idx, product in enumerate(products):
        status = product['stock'] if product['stock'] > 0 else "HẾT HÀNG"
        print(f"{idx+1:<5} {product['name']:<15} {product['price']:<10} {status:<10}")
    print("=" * 45)

def add_funds():
    global user_money
    print("\n--- NẠP TIỀN ---")
    try:
        amount = int(input("Nhập số tiền muốn nạp: "))
        if amount > 0:
            user_money += amount
            history.append(f"Nạp tiền (+{amount}đ)")
            print(f"✅ Nạp thành công! Số dư hiện tại: {user_money}đ")
        else:
            print("⚠️ Số tiền nạp phải lớn hơn 0.")
    except ValueError:
        print("⚠️ Vui lòng nhập con số hợp lệ.")
    
    input("\nNhấn Enter để quay lại...") 

def show_history():
    print("\n" + "="*10 + " LỊCH SỬ GIAO DỊCH " + "="*10)
    if not history:
        print("(Chưa có giao dịch nào)")
    else:
        for idx, item in enumerate(reversed(history)): 
            print(f"{idx+1}. {item}")
    print("=" * 45)
    input("\nNhấn Enter để quay lại...")

def admin_mode():
    global admin_password
    clear_screen() 
    print("\n--- KHU VỰC QUẢN TRỊ ---")
    
    while True:
        password = input("Nhập mật khẩu (hoặc nhập '0' để quay lại): ")
        if password == '0': return
        if password == admin_password: break
        else: print("❌ Mật khẩu sai! Vui lòng thử lại.")

    while True:
        clear_screen() 
        print(f"\n--- ADMIN MENU (Pass: {admin_password}) ---")
        print("1. Nhập thêm hàng (Restock)")
        print("2. Thêm món mới vào Menu")
        print("3. Xóa món khỏi Menu")        
        print("4. Đổi mật khẩu Admin")
        print("5. Quay lại Menu chính")
        
        choice = input("Admin chọn: ")
        
        if choice == '1':
            show_menu()
            try:
                p_idx = int(input("Chọn STT sản phẩm cần nhập thêm: ")) - 1
                if 0 <= p_idx < len(products):
                    qty = int(input(f"Nhập số lượng thêm cho {products[p_idx]['name']}: "))
                    if qty > 0:
                        products[p_idx]['stock'] += qty
                        print(f"✅ Đã thêm {qty} cái vào kho.")
                    else: print("⚠️ Số lượng phải dương.")
                else: print("⚠️ Sản phẩm không tồn tại.")
            except ValueError: print("⚠️ Nhập sai định dạng.")
            input("\nNhấn Enter để tiếp tục...") 

        elif choice == '2':
            name = input("Tên món mới: ")
            try:
                price = int(input("Giá bán: "))
                stock = int(input("Số lượng ban đầu: "))
                products.append({"name": name, "price": price, "stock": stock})
                print(f"✅ Đã thêm món '{name}' vào menu.")
            except ValueError: print("⚠️ Giá và số lượng phải là số.")
            input("\nNhấn Enter để tiếp tục...")

        elif choice == '3':
            show_menu()
            try:
                p_idx = int(input("🗑️ Chọn STT sản phẩm muốn XÓA: ")) - 1
                if 0 <= p_idx < len(products):
                    deleted_item = products.pop(p_idx) 
                    print(f"✅ Đã xóa vĩnh viễn món '{deleted_item['name']}' khỏi menu.")
                else:
                    print("⚠️ STT không tồn tại.")
            except ValueError:
                print("⚠️ Vui lòng nhập số.")
            input("\nNhấn Enter để tiếp tục...") 

        elif choice == '4':
            new_pass = input("Nhập mật khẩu mới: ")
            if len(new_pass) > 0:
                if input("Xác nhận lại mật khẩu: ") == new_pass:
                    admin_password = new_pass
                    print("✅ Đổi mật khẩu thành công!")
                else: print("❌ Xác nhận không khớp.")
            else: print("⚠️ Mật khẩu không được trống.")
            input("\nNhấn Enter để tiếp tục...") 

        elif choice == '5': break
        else: 
            print("⚠️ Lựa chọn không hợp lệ.")
            input("\nNhấn Enter...")

def buy_product():
    global user_money
    cart = {} 
    
    while True:
        clear_screen()
        show_menu()
        
        current_total = 0
        if cart:
            print("\n🛒 GIỎ HÀNG CỦA BẠN:")
            for p_idx, qty in cart.items():
                p = products[p_idx]
                subtotal = p['price'] * qty
                current_total += subtotal
                print(f"   - {p['name']} (x{qty}): {subtotal}đ")
            print(f"   --------------------")
            print(f"   👉 TỔNG TẠM TÍNH: {current_total}đ (Ví: {user_money}đ)")
        
        try:
            print("\n(Nhập '0' để THANH TOÁN, '-1' để XÓA giỏ hàng và thoát)")
            choice_str = input(">>> Chọn STT sản phẩm muốn thêm vào giỏ: ")
            
            if not choice_str: continue 
            choice = int(choice_str)
            
            if choice == -1: 
                return 
            
            if choice == 0: 
                if not cart:
                    print("⚠️ Giỏ hàng đang trống!")
                    input("Nhấn Enter...")
                    continue
                break 

            p_idx = choice - 1
            if 0 <= p_idx < len(products):
                product = products[p_idx]
                
                current_in_cart = cart.get(p_idx, 0)
                available_stock = product['stock'] - current_in_cart
                
                if available_stock <= 0:
                    print("❌ Sản phẩm này đã hết hàng (hoặc bạn đã lấy hết trong giỏ).")
                    input("Nhấn Enter...") 
                    continue

                try:
                    qty = int(input(f"Nhập số lượng {product['name']} (Còn {available_stock}): "))
                except ValueError:
                    print("⚠️ Vui lòng nhập số.")
                    input("Nhấn Enter...")
                    continue
                
                if qty <= 0:
                    print("⚠️ Số lượng phải > 0")
                    input("Nhấn Enter...")
                elif qty > available_stock:
                    print(f"❌ Không đủ hàng! Chỉ còn {available_stock} cái.")
                    input("Nhấn Enter...") 
                else:
                    if p_idx in cart:
                        cart[p_idx] += qty
                    else:
                        cart[p_idx] = qty
                    print("✅ Đã thêm vào giỏ!")
                    input("Nhấn Enter để tiếp tục mua...")
            else:
                print("⚠️ STT không tồn tại.")
                input("Nhấn Enter...")
                
        except ValueError:
            print("⚠️ Nhập sai định dạng.")
            input("Nhấn Enter...")

    if current_total > user_money:
        print(f"\n❌ THANH TOÁN THẤT BẠI! Tổng {current_total}đ nhưng ví chỉ có {user_money}đ.")
        print(f"Thiếu {current_total - user_money}đ.")
    else:
        user_money -= current_total
        
        details = []
        for p_idx, qty in cart.items():
            products[p_idx]['stock'] -= qty
            details.append(f"{qty}x {products[p_idx]['name']}")
        
        history_str = f"Mua Combo: {', '.join(details)} (-{current_total}đ)"
        history.append(history_str)
        
        print(f"\n✅ MUA HÀNG THÀNH CÔNG! Đã trừ {current_total}đ.")
        print(f"Số dư còn lại: {user_money}đ")
    
    input("Nhấn Enter để về menu chính...")

def main():
    while True:
        clear_screen()
        print(f"\n💰 VÍ TIỀN: {user_money}đ")
        print("1. Mua hàng (Giỏ hàng) | 2. Nạp tiền | 3. Lịch sử | 4. Admin | 5. Thoát")
        choice = input("👉 Chọn (1-5): ")
        
        if choice == '1': buy_product()
        elif choice == '2': add_funds()
        elif choice == '3': show_history()
        elif choice == '4': admin_mode()
        elif choice == '5':
            print("Cảm ơn và hẹn gặp lại!")
            break
        else:
            print("⚠️ Lựa chọn không hợp lệ.")
            input("Nhấn Enter...")

if __name__ == "__main__":
    main()
