# 🧁 Sia's Bakery - Python OOP 練習專案

歡迎來到 Sia 的烘焙房！這個專案將幫助你練習 Python 的物件導向程式設計 (OOP)。

## 📁 專案結構

```
python-project-bakery/
├── bakery_models.py   # 烘焙品模型（練習繼承）
├── bakery_app.py      # 烘焙房管理系統（練習類別方法）
├── bakery_art.py      # ASCII 藝術圖案（已完成）
└── readme.md          # 說明文件
```

## 🎯 學習目標

完成這個專案後，你將學會：

- [ ] 類別 (Class) 與物件 (Object) 的概念
- [ ] 建構子 `__init__` 的使用
- [ ] 屬性 (Attributes) 與方法 (Methods)
- [ ] 繼承 (Inheritance) - 使用 `super().__init__()`
- [ ] 基本的迴圈與條件判斷
- [ ] Git 版本控制與分支管理

---

## 📝 TODO 清單

### `bakery_models.py` (5 個 TODO)

| 類別/函數 | 方法 | 說明 |
|----------|------|------|
| `StrawberryCake` | `__init__` | 呼叫父類別 + 加入配料 |
| `MatchaCake` | `__init__` | 呼叫父類別 + 設定屬性 + 加入配料 |
| `MilleCrepe` | `__init__` | 呼叫父類別 + 設定屬性 + 修改保存天數 |
| `CinnamonRoll` | `__init__` | 呼叫父類別（含參數）+ 設定屬性 |
| `calculate_total_calories` | 函數 | 用 for 迴圈計算總熱量 |

### `bakery_app.py` (4 個 TODO)

| 類別 | 方法 | 說明 |
|------|------|------|
| `Bakery` | `find_fresh_products()` | 用 for 迴圈篩選新鮮商品 |
| `Bakery` | `get_average_price()` | 計算平均價格 |
| `Bakery` | `display_sales_report()` | 印出銷售報告 |
| `Bakery` | `__str__()` | 回傳格式化字串 |

---

## 🌿 Git 練習流程

### 步驟 1: 初始化專案

```bash
# 初始化 Git 儲存庫
git init

# 查看目前狀態
git status

# 將所有檔案加入暫存區
git add .

# 建立第一個 commit
git commit -m "Initial commit: 專案初始化"
```

### 步驟 2: 建立分支開發

```bash
# 建立並切換到新分支
git checkout -b feature/bakery-models

# 確認目前在哪個分支
git branch
```

### 步驟 3: 開發 bakery_models.py

```bash
# 完成 StrawberryCake 後：
git add bakery_models.py
git commit -m "feat(models): 完成 StrawberryCake"

# 完成 MatchaCake 後：
git commit -am "feat(models): 完成 MatchaCake"

# 完成 MilleCrepe 後：
git commit -am "feat(models): 完成 MilleCrepe"

# 完成 CinnamonRoll 後：
git commit -am "feat(models): 完成 CinnamonRoll"

# 完成 calculate_total_calories 後：
git commit -am "feat(models): 完成 calculate_total_calories"
```

### 步驟 4: 合併回 main

```bash
# 切換回 main 分支
git checkout main

# 合併分支
git merge feature/bakery-models

# 查看 log
git log --oneline
```

### 步驟 5: 開發 bakery_app.py

```bash
# 建立新分支
git checkout -b feature/bakery-app

# 完成各個 TODO 後分別 commit
git commit -am "feat(app): 完成 find_fresh_products"
git commit -am "feat(app): 完成 get_average_price"
git commit -am "feat(app): 完成 display_sales_report"
git commit -am "feat(app): 完成 __str__"
```

### 步驟 6: 最終合併

```bash
git checkout main
git merge feature/bakery-app
git log --oneline --graph
```

---

## 📋 Git 指令速查表

| 指令 | 說明 |
|------|------|
| `git init` | 初始化儲存庫 |
| `git status` | 查看目前狀態 |
| `git add <file>` | 將檔案加入暫存區 |
| `git add .` | 將所有變更加入暫存區 |
| `git commit -m "訊息"` | 建立 commit |
| `git commit -am "訊息"` | 加入暫存並 commit |
| `git branch` | 列出所有分支 |
| `git checkout -b <name>` | 建立並切換到新分支 |
| `git checkout <branch>` | 切換分支 |
| `git merge <branch>` | 合併指定分支 |
| `git log --oneline` | 查看簡潔的 commit 歷史 |

---

## 🧪 測試你的程式

### 測試 bakery_models.py

```bash
python bakery_models.py
```

完成所有 TODO 後，應該會看到：
```
╔══════════════════════════════════════════╗
║  🥐  🍰  🧁  Sia's Bakery  🧁  🍰  🥐   ║
║        每一口都是幸福的滋味              ║
╚══════════════════════════════════════════╝

🧁 Sia's Bakery - 模型測試
========================================

【草莓蛋糕】
📛 草莓蛋糕
📝 新鮮酸甜的草莓蛋糕，鋪滿當季草莓與鮮奶油
🔥 490 大卡
💰 $350
🟢 新鮮
...
```

### 測試 bakery_app.py

```bash
python bakery_app.py
```

會啟動互動式選單，可以：
1. 查看菜單
2. 購買商品
3. 查看銷售報告
4. 查看新鮮商品
5. 依價格搜尋
6. 離開

---

## 💡 提示與技巧

### 1. 使用 `super()` 呼叫父類別

```python
class StrawberryCake(Cake):
    def __init__(self, price, size="medium"):
        super().__init__("草莓蛋糕", price, size)  # 呼叫父類別
        self.add_topping("草莓")  # 加入配料
```

### 2. for 迴圈篩選

```python
def find_fresh_products(self):
    result = []
    for product in self._products:
        if product.is_fresh():
            result.append(product)
    return result
```

### 3. 計算平均值

```python
def get_average_price(self):
    if len(self._products) == 0:
        return 0
    total = self.get_total_inventory_value()
    return round(total / len(self._products), 2)
```

### 4. 格式化字串

```python
def __str__(self):
    return f"{self.name} - 共 {len(self._products)} 項商品"
```

---

## 🎨 商品資訊

### 蛋糕 (Cake)

| 品項 | 建議價格 | 特色 |
|------|----------|------|
| 草莓蛋糕 | $350 | 預設配料：草莓、鮮奶油 |
| 抹茶蛋糕 | $380 | 可調整抹茶濃度 1-5 |
| 千層蛋糕 | $420 | 保存期較短（2天） |

### 糕點 (Pastry)

| 品項 | 建議價格 | 特色 |
|------|----------|------|
| 肉桂捲 | $85 | 預設有糖霜，可調整肉桂濃度 |

---

## 🐛 常見錯誤

### 1. 忘記呼叫 `super().__init__()`

```python
# ❌ 錯誤
class StrawberryCake(Cake):
    def __init__(self, price, size="medium"):
        self.add_topping("草莓")  # 會出錯！因為 self.toppings 還不存在

# ✅ 正確
class StrawberryCake(Cake):
    def __init__(self, price, size="medium"):
        super().__init__("草莓蛋糕", price, size)  # 先呼叫父類別
        self.add_topping("草莓")  # 現在可以了
```

### 2. 忘記 return

```python
# ❌ 錯誤
def find_fresh_products(self):
    result = []
    for product in self._products:
        if product.is_fresh():
            result.append(product)
    # 忘記 return！

# ✅ 正確
def find_fresh_products(self):
    result = []
    for product in self._products:
        if product.is_fresh():
            result.append(product)
    return result  # 記得回傳
```

### 3. 除以零

```python
# ❌ 錯誤
def get_average_price(self):
    return self.get_total_inventory_value() / len(self._products)  # 如果沒商品會出錯

# ✅ 正確
def get_average_price(self):
    if len(self._products) == 0:
        return 0  # 先檢查
    return self.get_total_inventory_value() / len(self._products)
```

---

## 🏆 進階挑戰

完成基本練習後，可以嘗試：

1. **新增更多商品類型** - 麵包類、餅乾類
2. **新增折扣功能** - 滿額折扣、會員優惠
3. **儲存資料到檔案** - 程式重啟後保留記錄

---

祝你學習愉快！🎉 有問題隨時可以問喔！
