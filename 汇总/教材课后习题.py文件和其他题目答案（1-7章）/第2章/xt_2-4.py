PRODUCT_RATE = 35 / 50
totalMaterial = 10.5e3
print(f"产出的面粉数量为{totalMaterial * PRODUCT_RATE:.2f}kg，；浪费的面粉数量为{totalMaterial * (1 - PRODUCT_RATE):.2f}kg")