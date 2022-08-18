class Inventory:
    sku_no = ""          # SKU (stock-keeping unit) number as ID
    brand = ""           # such as Toshiba
    product_name = ""    # such as Awesome-112 Laptop
    price = None         # float
    disc_app = None      # boolean, to check if discount is applicable
    stock_avail = None   # int to keep track of stock available
    
    def __init__(self, sku, brand, pname, price, disc, stock):
        self.sku_no = sku
        self.brand = brand
        self.product_name = pname
        self.price = price
        self.disc_app = disc
        self.stock_avail = stock
        
    def display_attributes(self):
        print("\n")
        print("The SKU Code is:", self.sku_no)
        print("The brand is:", self.brand)
        print("The product name is:", self.product_name)
        print("The price is:", self.price)
        print("The discount applicability is:", self.disc_app)
        print("The unit(s) of stock available is:", self.stock_avail)
        
    def display_promo(self, percent):  # Display a promo message based on percentage
        print("\nWelcome to Awesome Electronics!")
        print(f"{self.brand} {self.product_name}")
        originalDollar = "{:.2f}".format(self.price)
        if self.disc_app:
            # Discount message
            print(f"Now at {percent}% discount!!")
            discountedPrice = ((100 - percent) / 100) * self.price
            discountedDollar = "{:.2f}".format(discountedPrice)
            print(f"    ONLY ${discountedDollar} !!")
            print(f"Original Price: ${originalDollar} //")
            
            # Giving rough idea of stocks left to create urgency to buy
            left = self.stock_avail
            if left < 20:
                print("\nLess than 20 units left! Hurry!\n")
            elif left < 30:
                print("\nLess than 30 units left! What are you waiting for?\n")
            elif left < 50:
                print("\nLess than 50 units left! Get your promo code from our app!\n")
            
        else:
            print(f"Now at: ${originalDollar}")
            print("Download our app to check out our latest products and promotion!\n")



# Build and display objects:

mouse_MOSDEL1234 = Inventory("MOS-DEL-1234", "Dell", "Wireless Mouse Model 1234", 15.50, False, 34)
mouse_MOSDEL1234.display_attributes()

keyb_KEBTOS3310 = Inventory("KEB-TOS-3310", "Toshiba", "Wireless Keyboard Model 3310", 27.80, True, 26)
keyb_KEBTOS3310.display_attributes()

thud_THDKST2688_128 = Inventory("THD-KST-2688", "Kingston", "Thumb Drive 128GB Model 2688", 58.80, True, 43)
thud_THDKST2688_128.display_attributes()

tabl_TABWAC4730 = Inventory("TAB-WAC-4730", "Wacom", "Drawing Tablet Model 4730", 670.70, True, 16)
tabl_TABWAC4730.display_attributes()




# No discount
mouse_MOSDEL1234.display_promo(0)

# 10% discount for relatively cheap items
keyb_KEBTOS3310.display_promo(10)
thud_THDKST2688_128.display_promo(10)

# 15% discount for big ticket purchase, clearing stock for new product release.
tabl_TABWAC4730.display_promo(15)

