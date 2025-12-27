# 🏪 Sia's Bakery - 烘焙房管理系統
# 這個檔案用來練習類別的實際應用

from datetime import datetime
from bakery_models import (
    BakedGoods, Cake, Pastry,
    StrawberryCake, MatchaCake, MilleCrepe, CinnamonRoll
)
from bakery_art import (
    BAKERY_BANNER, WELCOME_ART, THANK_YOU_ART,
    DIVIDER_CAKE, DIVIDER_SIMPLE,
    get_product_art
)


class Bakery:
    """
    烘焙房類別 - 管理所有烘焙品
    
    屬性：
    - name: 烘焙房名稱
    - _products: 商品列表（私有屬性）
    - _daily_sales: 當日銷售額（私有屬性）
    """
    
    def __init__(self, name: str):
        """初始化烘焙房"""
        self.name = name
        self._products = []
        self._daily_sales = 0
    
    # ============================================
    # 商品管理方法（已完成）
    # ============================================
    
    def add_product(self, product: BakedGoods):
        """新增商品到烘焙房"""
        if isinstance(product, BakedGoods):
            self._products.append(product)
            print(f"✓ 已新增商品：{product.name}")
        else:
            print("✗ 錯誤：只能新增烘焙品！")
    
    def get_products(self) -> list:
        """回傳商品列表的副本"""
        return self._products.copy()
    
    def get_product_count(self) -> int:
        """回傳商品數量"""
        return len(self._products)
    
    # ============================================
    # 查詢方法（含練習）
    # ============================================
    
    def find_products_by_type(self, product_type: type) -> list:
        """根據類型尋找商品"""
        result = []
        for product in self._products:
            if isinstance(product, product_type):
                result.append(product)
        return result
    
    def find_products_by_price_range(self, min_price: int, max_price: int) -> list:
        """根據價格範圍尋找商品"""
        result = []
        for product in self._products:
            if min_price <= product.price <= max_price:
                result.append(product)
        return result
    
    def find_fresh_products(self) -> list:
        """
        TODO: 尋找所有新鮮的商品
        
        預期輸出範例：
        >>> bakery.find_fresh_products()
        [<草莓蛋糕>, <抹茶蛋糕>, ...]  # 回傳所有 is_fresh() 為 True 的商品列表
        """
        # TODO: 請在這裡完成
        result=[]
        for product in self._products:
            if product.is_fresh():
                result.append(product)
        return result
    
    # ============================================
    # 銷售方法（已完成）
    # ============================================
    
    def sell_product(self, product: BakedGoods) -> bool:
        """販售商品"""
        if product not in self._products:
            print("✗ 商品不在庫存中！")
            return False
        
        if not product.is_fresh():
            print("✗ 商品已過期，無法販售！")
            return False
        
        self._products.remove(product)
        self._daily_sales += product.price
        print(f"✓ 已售出：{product.name}，價格 ${product.price}")
        return True
    
    def get_daily_sales(self) -> int:
        """回傳當日銷售額"""
        return self._daily_sales
    
    # ============================================
    # 練習：統計方法
    # ============================================
    
    def get_total_inventory_value(self) -> int:
        """計算庫存總價值"""
        total = 0
        for product in self._products:
            total += product.price
        return total
    
    def get_average_price(self) -> float:
        """
        TODO: 計算平均價格
        
        預期輸出範例：
        >>> bakery.get_average_price()
        308.75  # 回傳所有商品的平均價格（四捨五入到小數點後 2 位）
        
        >>> empty_bakery.get_average_price()
        0  # 如果沒有商品，回傳 0
        """
        # TODO: 請在這裡完成
        if not self._products:
            return 0
        
        total=0
        for product in self._products:
            total += product.price
        
        average=total/len(self._products)
        return round(average,2)
    
    # ============================================
    # 練習：顯示方法
    # ============================================
    
    def display_menu(self):
        """顯示菜單"""
        print(DIVIDER_CAKE)
        print(f"🧁 {self.name} 菜單")
        print(DIVIDER_CAKE)
        
        if not self._products:
            print("目前沒有商品")
        else:
            for i, product in enumerate(self._products, 1):
                art = get_product_art(product.name, small=True)
                print(f"\n{i}. {product.name} - ${product.price} ({product.get_calories()} 大卡)")
                print(art)
                print(f"   {product.get_description()}")
                print(DIVIDER_SIMPLE)
        
        print(f"\n共 {len(self._products)} 項商品 | 庫存總價值: ${self.get_total_inventory_value()}")
        print(DIVIDER_CAKE)
    
    def display_sales_report(self):
        """
        TODO: 顯示銷售報告
        
        預期輸出：
        🍰═══════════════════════════════🍰
        📊 銷售報告
        🍰═══════════════════════════════🍰
        今日銷售額: $350
        🍰═══════════════════════════════🍰
        """
        # TODO: 請在這裡完成
        print(DIVIDER_CAKE)
        print("📊 銷售報告")
        print(DIVIDER_CAKE)
        print(f"今日銷售額：{self._daily_sales}")
        print(DIVIDER_CAKE)


    
    def __str__(self):
        """
        TODO: 回傳烘焙房的簡短描述
        
        預期輸出範例：
        >>> print(bakery)
        Sia's Bakery - 共 4 項商品
        """
        # TODO: 請在這裡完成
        return f"{self.name}-共{len(self._products)}項商品。"


# ============================================
# 主程式
# ============================================

def main():
    """主程式 - 烘焙房互動介面"""
    
    # 建立烘焙房
    bakery = Bakery("Sia's Bakery")
    
    # 預先加入一些商品
    bakery.add_product(StrawberryCake(price=350))
    bakery.add_product(MatchaCake(price=380, matcha_level=4))
    bakery.add_product(MilleCrepe(price=420, cream_flavor="芋頭"))
    bakery.add_product(CinnamonRoll(price=85))
    
    # 顯示歡迎畫面
    print(BAKERY_BANNER)
    print(WELCOME_ART)
    
    while True:
        print(DIVIDER_SIMPLE)
        print("\n請選擇操作：")
        print("1. 查看菜單")
        print("2. 購買商品")
        print("3. 查看銷售報告")
        print("4. 查看新鮮商品")
        print("5. 依價格搜尋")
        print("6. 離開")
        
        choice = input("\n請輸入選項 (1-6): ").strip()
        
        if choice == "1":
            bakery.display_menu()
        
        elif choice == "2":
            # 購買商品
            products = bakery.get_products()
            if not products:
                print("目前沒有商品可購買！")
                continue
            
            print("\n可購買的商品：")
            for i, product in enumerate(products, 1):
                print(f"{i}. {product.name} - ${product.price}")
            
            try:
                idx = int(input("請輸入要購買的商品編號: ")) - 1
                if 0 <= idx < len(products):
                    bakery.sell_product(products[idx])
                else:
                    print("無效的編號！")
            except ValueError:
                print("請輸入有效的數字！")
        
        elif choice == "3":
            # TODO: 完成 display_sales_report() 後，這個功能才會正常運作
            bakery.display_sales_report()
        
        elif choice == "4":
            # TODO: 完成 find_fresh_products() 後，這個功能才會正常運作
            fresh = bakery.find_fresh_products()
            if fresh:
                print(f"\n🟢 新鮮商品 ({len(fresh)} 項)：")
                for product in fresh:
                    print(f"  - {product}")
            else:
                print("\n（請先完成 find_fresh_products 方法）")
        
        elif choice == "5":
            # 依價格搜尋
            try:
                min_p = int(input("最低價格: "))
                max_p = int(input("最高價格: "))
                found = bakery.find_products_by_price_range(min_p, max_p)
                print(f"\n價格 ${min_p} ~ ${max_p} 的商品：")
                for product in found:
                    print(f"  - {product}")
            except ValueError:
                print("請輸入有效的數字！")
        
        elif choice == "6":
            print(THANK_YOU_ART)
            break
        
        else:
            print("無效的選項，請重新輸入。")


if __name__ == "__main__":
    main()
ㄏ