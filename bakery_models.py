# 🧁 Sia's Bakery - 烘焙品模型
# 這個檔案用來練習物件導向程式設計 (OOP) 的基礎概念
# 重點：類別 (class)、建構子 (__init__)、繼承 (inheritance)

from datetime import datetime, timedelta
from bakery_art import get_product_art, DIVIDER_SIMPLE


# ============================================
# 基礎類別：BakedGoods（烘焙品）- 已完成
# ============================================

class BakedGoods:
    """
    烘焙品的基礎類別（已完成，供參考）
    
    學習重點：
    - __init__ 是建構子，用來初始化物件
    - self 代表物件本身
    - self.xxx 是物件的屬性
    """
    
    def __init__(self, name: str, price: int):
        """初始化烘焙品"""
        self.name = name          # 名稱
        self.price = price        # 價格
        self.production_date = datetime.now()  # 製造日期
        self.shelf_life_days = 3  # 保存天數
    
    def is_fresh(self) -> bool:
        """判斷是否新鮮"""
        expiry_date = self.production_date + timedelta(days=self.shelf_life_days)
        return datetime.now() <= expiry_date
    
    def get_description(self) -> str:
        """回傳商品描述"""
        return f"美味的{self.name}"
    
    def get_calories(self) -> int:
        """回傳熱量"""
        return 200
    
    def __str__(self):
        """印出物件時顯示的文字"""
        status = "🟢 新鮮" if self.is_fresh() else "🔴 過期"
        return f"{self.name} - ${self.price} ({self.get_calories()} 大卡) [{status}]"


# ============================================
# 蛋糕類別：Cake（繼承 BakedGoods）- 已完成
# ============================================

class Cake(BakedGoods):
    """
    蛋糕類別（已完成，供參考）
    
    學習重點：
    - 使用 super().__init__() 呼叫父類別的建構子
    - 子類別可以新增自己的屬性
    """
    
    SIZE_CALORIES = {"small": 200, "medium": 350, "large": 500}
    
    def __init__(self, name: str, price: int, size: str = "medium"):
        super().__init__(name, price)  # 呼叫父類別的 __init__
        self.size = size               # 新增尺寸屬性
        self.toppings = []             # 新增配料列表
    
    def add_topping(self, topping: str):
        """新增配料"""
        self.toppings.append(topping)
    
    def get_calories(self) -> int:
        """計算熱量：基礎熱量 + 配料熱量"""
        base = self.SIZE_CALORIES.get(self.size, 350)
        return base + len(self.toppings) * 30
    
    def get_description(self) -> str:
        if self.toppings:
            return f"{self.size} 尺寸的{self.name}，配料：{'、'.join(self.toppings)}"
        return f"{self.size} 尺寸的{self.name}"


# ============================================
# 練習：特定蛋糕類別（繼承 Cake）
# ============================================

class StrawberryCake(Cake):
    """
    草莓蛋糕
    
    TODO: 完成 __init__ 方法
    
    完成後應有的屬性：
    - self.name = "草莓蛋糕"
    - self.price = (傳入的 price)
    - self.size = (傳入的 size)
    - self.toppings = ["草莓", "鮮奶油"]
    """
    
    def __init__(self, price: int, size: str = "medium"):
        # TODO: 請在這裡完成
        pass
    
    def get_description(self) -> str:
        return "新鮮酸甜的草莓蛋糕，鋪滿當季草莓與鮮奶油"
    
    def get_calories(self) -> int:
        return super().get_calories() + 80


class MatchaCake(Cake):
    """
    抹茶蛋糕
    
    TODO: 完成 __init__ 方法
    
    完成後應有的屬性：
    - self.name = "抹茶蛋糕"
    - self.price = (傳入的 price)
    - self.size = (傳入的 size)
    - self.matcha_level = (傳入的 matcha_level)
    - self.toppings = ["紅豆"]
    """
    
    def __init__(self, price: int, size: str = "medium", matcha_level: int = 3):
        # TODO: 請在這裡完成
        pass
    
    def get_description(self) -> str:
        return f"濃度 {self.matcha_level} 級的抹茶蛋糕，搭配香甜紅豆"
    
    def get_calories(self) -> int:
        return super().get_calories() + 50 + (self.matcha_level * 10)


class MilleCrepe(Cake):
    """
    千層蛋糕
    
    TODO: 完成 __init__ 方法
    
    完成後應有的屬性：
    - self.name = "千層蛋糕"
    - self.price = (傳入的 price)
    - self.size = (傳入的 size)
    - self.cream_flavor = (傳入的 cream_flavor)
    - self.shelf_life_days = 2（千層蛋糕保存期較短）
    """
    
    def __init__(self, price: int, size: str = "medium", cream_flavor: str = "原味"):
        # TODO: 請在這裡完成
        pass
    
    def get_description(self) -> str:
        return f"{self.cream_flavor}口味的千層蛋糕，層層綿密"
    
    def get_calories(self) -> int:
        return super().get_calories() + 100


# ============================================
# 糕點類別（已完成，供參考）
# ============================================

class Pastry(BakedGoods):
    """糕點類別（已完成，供參考）"""
    
    def __init__(self, name: str, price: int, is_glazed: bool = False):
        super().__init__(name, price)
        self.is_glazed = is_glazed
    
    def get_calories(self) -> int:
        return 180 + (60 if self.is_glazed else 0)
    
    def get_description(self) -> str:
        return f"{self.name}（{'有糖霜' if self.is_glazed else '無糖霜'}）"


class CinnamonRoll(Pastry):
    """
    肉桂捲
    
    TODO: 完成 __init__ 方法
    
    完成後應有的屬性：
    - self.name = "肉桂捲"
    - self.price = (傳入的 price)
    - self.is_glazed = True（肉桂捲預設有糖霜）
    - self.cinnamon_intensity = (傳入的 cinnamon_intensity)
    """
    
    CINNAMON_CALORIES = {"light": 20, "medium": 35, "strong": 50}
    
    def __init__(self, price: int, cinnamon_intensity: str = "medium"):
        # TODO: 請在這裡完成
        pass
    
    def get_description(self) -> str:
        return f"肉桂濃度 {self.cinnamon_intensity} 的經典肉桂捲"
    
    def get_calories(self) -> int:
        extra = self.CINNAMON_CALORIES.get(self.cinnamon_intensity, 35)
        return super().get_calories() + extra


# ============================================
# 輔助函數
# ============================================

def display_product_info(product: BakedGoods):
    """顯示商品資訊（已完成）"""
    art = get_product_art(product.name)
    print(art)
    print(f"📛 {product.name}")
    print(f"📝 {product.get_description()}")
    print(f"🔥 {product.get_calories()} 大卡")
    print(f"💰 ${product.price}")
    print(f"{'🟢 新鮮' if product.is_fresh() else '🔴 過期'}")
    print(DIVIDER_SIMPLE)


def calculate_total_calories(products: list) -> int:
    """
    TODO: 計算多個商品的總熱量
    
    預期輸出範例：
    >>> products = [StrawberryCake(350), MatchaCake(380)]
    >>> calculate_total_calories(products)
    960
    
    （回傳所有商品 get_calories() 的總和）
    """
    # TODO: 請在這裡完成
    pass


# ============================================
# 測試區域 - 完成 TODO 後執行此檔案可看到結果
# ============================================

if __name__ == "__main__":
    from bakery_art import BAKERY_BANNER
    
    print(BAKERY_BANNER)
    print("🧁 Sia's Bakery - 模型測試")
    print("=" * 40)
    
    # 測試草莓蛋糕
    print("\n【草莓蛋糕】")
    strawberry = StrawberryCake(price=350)
    display_product_info(strawberry)
    
    # 測試抹茶蛋糕
    print("\n【抹茶蛋糕】")
    matcha = MatchaCake(price=380, matcha_level=4)
    display_product_info(matcha)
    
    # 測試千層蛋糕
    print("\n【千層蛋糕】")
    mille = MilleCrepe(price=420, cream_flavor="芋頭")
    display_product_info(mille)
    
    # 測試肉桂捲
    print("\n【肉桂捲】")
    cinnamon = CinnamonRoll(price=85, cinnamon_intensity="strong")
    display_product_info(cinnamon)
    
    # 測試總熱量
    print("\n【總熱量計算】")
    products = [strawberry, matcha, mille, cinnamon]
    print(f"所有商品總熱量: {calculate_total_calories(products)} 大卡")
