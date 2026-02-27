import json
from flask import Flask, request, render_template, jsonify
from flask_mail import Mail, Message
from checkout import *

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'khlokrathana02@gmail.com'
app.config['MAIL_PASSWORD'] = 'hglt kzfx zmfl gcsi'

mail = Mail(app)


@app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'

@app.get('/home')
def home():
    products = [
        {
            "id": 1,
            "title": "Espresso",
            "price": 3.00,
            "description": "Espresso is a concentrated coffee beverage brewed by forcing hot water through finely-ground coffee beans under high pressure.",
            "category": "hot coffee",
            "image": "/static/product/espresso-hot.png"
        },
        {
            "id": 2,
            "title": "Espresso Macchiato",
            "price": 3.75,
            "description": "An espresso macchiato is a strong coffee drink consisting of espresso stained or marked with a small amount of steamed milk foam.",
            "category": "hot coffee",
            "image": "/static/product/espresso-macchiato-hot.png"
        },
        {
            "id": 3,
            "title": "Espresso Con Panna",
            "price": 3.75,
            "description": "Espresso con panna is a simple yet elegant coffee drink consisting of a shot of espresso topped with a dollop of whipped cream.",
            "category": "hot coffee",
            "image": "/static/product/espresso_con_panna_hot.png"
        },
        {
            "id": 4,
            "title": "Americano",
            "price": 3.00,
            "description": "An Americano is a coffee drink made by diluting a shot of espresso with hot water.",
            "category": "hot coffee",
            "image": "/static/product/americano_hot.png"
        },
        {
            "id": 5,
            "title": "Cafe Latte",
            "price": 3.75,
            "description": "A café latte is a coffee drink made with espresso and steamed milk, typically topped with a thin layer of foamed milk.",
            "category": "hot coffee",
            "image": "/static/product/cafe_latte_hot.png"
        },
        {
            "id": 6,
            "title": "Cappuccino",
            "price": 3.50,
            "description": "A cappuccino is a classic coffee drink made with espresso, steamed milk, and foamed milk, typically in equal parts.",
            "category": "hot coffee",
            "image": "/static/product/cappuccino_hot.png"
        },
        {
            "id": 7,
            "title": "Cafe Mocha",
            "price": 3.50,
            "description": "A cafe mocha, also known as caffè mocha or mocha, is a chocolate-flavored warm coffee drink.",
            "category": "hot coffee",
            "image": "/static/product/cafe_mocha_hot.png"
        },
        {
            "id": 8,
            "title": "Caramel Macchiato",
            "price": 4.00,
            "description": "A Caramel Macchiato is a coffee beverage typically consisting of steamed milk, vanilla-flavored syrup, espresso, and a caramel drizzle.",
            "category": "hot coffee",
            "image": "/static/product/caramel_macchiato_hot.png"
        },
        {
            "id": 9,
            "title": "Iced Caramel Cappuccino",
            "price": 4.00,
            "description": "An iced caramel cappuccino is a refreshing coffee beverage that combines the rich flavors of espresso, steamed milk, and caramel, all served cold over ice.",
            "category": "iced coffee",
            "image": "/static/product/iced caramel cappuccino.png"
        },
        {
            "id": 10,
            "title": "Iced Americano",
            "price": 3.25,
            "description": "An Iced Americano is a refreshing coffee drink made by combining espresso with cold water and ice.",
            "category": "iced coffee",
            "image": "/static/product/iced americano.png"
        },
        {
            "id": 11,
            "title": "Iced Latte",
            "price": 4.00,
            "description": "An iced latte is a refreshing, cold coffee drink made with espresso, milk, and ice.",
            "category": "iced coffee",
            "image": "/static/product/iced latte.png"
        },
        {
            "id": 12,
            "title": "Iced Cappuccino",
            "price": 3.75,
            "description": "An iced cappuccino is a refreshing twist on the classic cappuccino, featuring espresso, milk, and a layer of cold, frothy foam, all served over ice.",
            "category": "iced coffee",
            "image": "/static/product/iced cappuccino.png",
        },
        {
            "id": 13,
            "title": "Iced Mocha",
            "price": 3.75,
            "description": "An iced mocha is a cold coffee drink made with espresso, milk, and chocolate syrup, typically served over ice.",
            "category": "iced coffee",
            "image": "/static/product/iced mocha.png"
        },
        {
            "id": 14,
            "title": "Brown Sugar Milk Tea",
            "price": 3.00,
            "description": "Brown sugar milk tea, also known as brown sugar boba or tiger milk tea, is a popular Taiwanese bubble tea drink made with fresh milk, brown sugar syrup, and tapioca pearls.",
            "category": "non coffee",
            "image": "/static/product/brown sugar milk tea.png"
        },
        {
            "id": 15,
            "title": "Milk Tea",
            "price": 3.00,
            "description": "Milk tea is a beverage made by adding milk to brewed tea.",
            "category": "non coffee",
            "image": "/static/product/milk tea.png"
        },
        {
            "id": 16,
            "title": "Green Tea",
            "price": 2.50,
            "description": "Green tea is a type of tea made from the leaves of the Camellia sinensis plant, processed to avoid oxidation or fermentation, thus preserving its green color and a high concentration of beneficial compounds like antioxidants.",
            "category": "non coffee",
            "image": "/static/product/green tea.png"
        },
        {
            "id": 17,
            "title": "Matcha Latte",
            "price": 3.00,
            "description": "A matcha latte is a vibrant green, tea-based beverage made from matcha powder, hot water, and milk (or a milk alternative).",
            "category": "non coffee",
            "image": "/static/product/green tea.png"
        },
        {
            "id": 18,
            "title": "Iced Chocolate",
            "price": 2.50,
            "description": "An iced chocolate is a chilled chocolate beverage, often described as a richer, more decadent version of chocolate milk, typically served over ice.",
            "category": "non coffee",
            "image": "/static/product/green tea.png"
        },
        {
            "id": 19,
            "title": "Iced Coconut Water Matcha Cream",
            "price": 2.00,
            "description": "Coconut matcha cream refers to a beverage or dessert that combines the earthy flavor of matcha green tea with the creamy and slightly sweet taste of coconut.",
            "category": "non coffee",
            "image": "/static/product/coconut matcha.png"
        },
        {
            "id": 20,
            "title": "Iced Blue Milk",
            "price": 2.00,
            "description": "Iced Blue Latte is a refreshing and visually stunning drink that's perfect for hot summer days.",
            "category": "non coffee",
            "image": "/static/product/iced blue milk.png"
        },
        {
            "id": 21,
            "title": "Iced Strawberry Milk",
            "price": 2.00,
            "description": "Iced strawberry milk is a refreshing beverage made with milk and strawberries, often featuring a combination of sweet and creamy flavors.",
            "category": "non coffee",
            "image": "/static/product/iced strawberry milk.png"
        },
        {
            "id": 22,
            "title": "Matcha Frappe",
            "price": 2.50,
            "description": "A matcha frappe is a blended, iced beverage typically made with matcha green tea powder, milk, sweetener, and ice, often topped with whipped cream.",
            "category": "frappe",
            "image": "/static/product/matcha frappe.png"
        },
        {
            "id": 23,
            "title": "Strawberry Frappe",
            "price": 2.50,
            "description": "A strawberry frappe is a blended, chilled beverage featuring the sweet and refreshing taste of strawberries.",
            "category": "frappe",
            "image": "/static/product/strawberry frappe.png"
        },
        {
            "id": 24,
            "title": "Blueberry Frappe",
            "price": 2.50,
            "description": "A blueberry frappe is a blended iced drink, often featuring the sweet and tangy taste of blueberries, combined with a creamy base like milk or yogurt, and often includes ice for a refreshing, slushy texture.",
            "category": "frappe",
            "image": "/static/product/blueberry frappe.png"
        },
        {
            "id": 25,
            "title": "chocolate frappe",
            "price": 2.50,
            "description": "A chocolate frappe is a blended iced coffee drink, typically made with chocolate, ice, milk, and often flavored with chocolate syrup or sauce.",
            "category": "frappe",
            "image": "/static/product/chocolate frappe.png"
        },
        {
            "id": 26,
            "title": "Caramel frappe",
            "price": 2.50,
            "description": "A caramel frappé is a blended iced coffee drink known for its creamy, sweet, and cool caramel flavor.",
            "category": "frappe",
            "image": "/static/product/caramel frappe.png"
        },
        {
            "id": 27,
            "title": "Vanilla frappe",
            "price": 2.50,
            "description": "A vanilla frappe is a blended iced drink, typically featuring a creamy, vanilla-flavored base, often made with milk, ice, and vanilla extract or vanilla bean.",
            "category": "frappe",
            "image": "/static/product/vanilla frappe.png"
        },
        {
            "id": 28,
            "title": "Mocha Frappe",
            "price": 2.50,
            "description": "A Mocha Frappe is a blended, iced coffee drink that combines chocolate and coffee flavors.",
            "category": "frappe",
            "image": "/static/product/mocha frappe.png"
        },
        {
            "id": 29,
            "title": "Strawberry Soda",
            "price": 2.50,
            "description": "Strawberry Soda will delight your taste buds and quench your warm-weather thirst with the natural flavor of fresh strawberries.",
            "category": "soda",
            "image": "/static/product/strawberry soda.png"
        },
        {
            "id": 30,
            "title": "Blue Hawaii Soda",
            "price": 2.50,
            "description": "Blue Hawaiian is a cocktail and a soda flavor known for its tropical taste and vibrant blue color.",
            "category": "soda",
            "image": "/static/product/blue hawaii soda.png"
        },
        {
            "id": 31,
            "title": "Lemon Soda",
            "price": 2.50,
            "description": "Lemon soda is a refreshing, carbonated beverage typically made with lemon juice, sugar (or another sweetener), and soda water.",
            "category": "soda",
            "image": "/static/product/lemon soda.png"
        },
        {
            "id": 32,
            "title": "Watermelon Soda",
            "price": 2.50,
            "description": "Watermelon soda is a refreshing, sweet, and bubbly beverage that captures the flavor of watermelon in a fizzy drink.",
            "category": "soda",
            "image": "/static/product/watermelon soda.png"
        },
        {
            "id": 33,
            "title": "Orange Juice",
            "price": 2.00,
            "description": "Orange juice is a refreshing beverage made from the liquid extracted from oranges.",
            "category": "juice",
            "image": "/static/product/orange juice.png"
        },
        {
            "id": 34,
            "title": "Strawberry Juice",
            "price": 2.00,
            "description": "Strawberry Juice is a refreshing fresh fruit juice that is full of vitamin C and antioxidants and lot of invigorating flavor.",
            "category": "juice",
            "image": "/static/product/strawberry juice.png"
        },
        {
            "id": 35,
            "title": "watermelon juice",
            "price": 2.00,
            "description": "Watermelon juice is so simple to make with a blender. Refreshingly sweet and hydrating, it's perfect for a hot summer day.",
            "category": "juice",
            "image": "/static/product/watermelon juice.png"
        },
        {
            "id": 36,
            "title": "Apple Juice",
            "price": 2.00,
            "description": "Apple juice is a refreshing beverage made from the pressed and filtered juice of apples.",
            "category": "juice",
            "image": "/static/product/apple juice.png"
        },
        {
            "id": 37,
            "title": "Pineapple Juice",
            "price": 2.00,
            "description": "Pineapple juice is a sweet and tangy tropical beverage made from the juice extracted from fresh or canned pineapples.",
            "category": "juice",
            "image": "/static/product/pineapple juice.png"
        },
        {
            "id": 38,
            "title": "Cookies",
            "price": 2.50,
            "description": "A cookies is a small piece of data that a website stores on a user's computer, typically used to remember information about the user or their browsing activity.",
            "category": "cake",
            "image": "/static/product/cookies.png"
        },
        {
            "id": 39,
            "title": "Cake Chocolate",
            "price": 2.50,
            "description": "Chocolate cake is a delicious dessert made from chocolate or cocoa, often enjoyed by both children and adults.",
            "category": "cake",
            "image": "/static/product/cake chocolate.png"
        },
        {
            "id": 40,
            "title": "Cake Strawberry",
            "price": 2.50,
            "description": "Strawberry cake is a cake that uses strawberry as a primary ingredient. Strawberries may be used in the cake batter, atop the cake, and in the frosting.",
            "category": "cake",
            "image": "/static/product/cake strawberry.png"
        },
        {
            "id": 41,
            "title": "Cake Blueberry",
            "price": 2.50,
            "description": "Blueberry cake is easy to put together, has the most moist and tender crumb and is dotted with heaps of juicy blueberries throughout.",
            "category": "cake",
            "image": "/static/product/cake blueberry.png"
        },
        {
            "id": 42,
            "title": "Tiramisu Chocolate",
            "price": 3.00,
            "description": "Chocolate Tiramisu is a decadent layered dessert made up of mascarpone cream, chocolate pastry cream and coffee soaked biscuits.",
            "category": "cake",
            "image": "/static/product/tiramisu chocolate.png"
        },
        {
            "id": 43,
            "title": "Tiramisu Matcha",
            "price": 3.00,
            "description": "Matcha Tiramisu is the perfect fusion no-bake dessert made with layers of rich, velvety matcha mascarpone cream and spongy matcha-soaked ladyfingers.",
            "category": "cake",
            "image": "/static/product/tiramisu matcha.png"
        }

    ]
    return render_template('home.html', products=products)


@app.get('/about')
def about():
    return render_template('about.html')


@app.get('/contact')
def contact():
    return render_template('contact.html')


@app.get('/cart_list')
def cart_list():
    return render_template('cart_list.html')


@app.get('/check')
def check():
    return render_template('check.html')


@app.get('/hot')
def hot():
    products = [
        {
            "id": 1,
            "title": "Espresso",
            "price": 3.00,
            "description": "Espresso is a concentrated coffee beverage brewed by forcing hot water through finely-ground coffee beans under high pressure.",
            "category": "hot coffee",
            "image": "/static/product/espresso-hot.png"
        },
        {
            "id": 2,
            "title": "Espresso Macchiato",
            "price": 3.75,
            "description": "An espresso macchiato is a strong coffee drink consisting of espresso stained or marked with a small amount of steamed milk foam.",
            "category": "hot coffee",
            "image": "/static/product/espresso-macchiato-hot.png"
        },
        {
            "id": 3,
            "title": "Espresso Con Panna",
            "price": 3.75,
            "description": "Espresso con panna is a simple yet elegant coffee drink consisting of a shot of espresso topped with a dollop of whipped cream.",
            "category": "hot coffee",
            "image": "/static/product/espresso_con_panna_hot.png"
        },
        {
            "id": 4,
            "title": "Americano",
            "price": 3.00,
            "description": "An Americano is a coffee drink made by diluting a shot of espresso with hot water.",
            "category": "hot coffee",
            "image": "/static/product/americano_hot.png"
        },
        {
            "id": 5,
            "title": "Cafe Latte",
            "price": 3.75,
            "description": "A café latte is a coffee drink made with espresso and steamed milk, typically topped with a thin layer of foamed milk.",
            "category": "hot coffee",
            "image": "/static/product/cafe_latte_hot.png"
        },
        {
            "id": 6,
            "title": "Cappuccino",
            "price": 3.50,
            "description": "A cappuccino is a classic coffee drink made with espresso, steamed milk, and foamed milk, typically in equal parts.",
            "category": "hot coffee",
            "image": "/static/product/cappuccino_hot.png"
        },
        {
            "id": 7,
            "title": "Cafe Mocha",
            "price": 3.50,
            "description": "A cafe mocha, also known as caffè mocha or mocha, is a chocolate-flavored warm coffee drink.",
            "category": "hot coffee",
            "image": "/static/product/cafe_mocha_hot.png"
        },
        {
            "id": 8,
            "title": "Caramel Macchiato",
            "price": 4.00,
            "description": "A Caramel Macchiato is a coffee beverage typically consisting of steamed milk, vanilla-flavored syrup, espresso, and a caramel drizzle.",
            "category": "hot coffee",
            "image": "/static/product/caramel_macchiato_hot.png"
        },
        {
            "id": 9,
            "title": "Iced Caramel Cappuccino",
            "price": 4.00,
            "description": "An iced caramel cappuccino is a refreshing coffee beverage that combines the rich flavors of espresso, steamed milk, and caramel, all served cold over ice.",
            "category": "iced coffee",
            "image": "/static/product/iced caramel cappuccino.png"
        },
        {
            "id": 10,
            "title": "Iced Americano",
            "price": 3.25,
            "description": "An Iced Americano is a refreshing coffee drink made by combining espresso with cold water and ice.",
            "category": "iced coffee",
            "image": "/static/product/iced americano.png"
        },
        {
            "id": 11,
            "title": "Iced Latte",
            "price": 4.00,
            "description": "An iced latte is a refreshing, cold coffee drink made with espresso, milk, and ice.",
            "category": "iced coffee",
            "image": "/static/product/iced latte.png"
        },
        {
            "id": 12,
            "title": "Iced Cappuccino",
            "price": 3.75,
            "description": "An iced cappuccino is a refreshing twist on the classic cappuccino, featuring espresso, milk, and a layer of cold, frothy foam, all served over ice.",
            "category": "iced coffee",
            "image": "/static/product/iced cappuccino.png",
        },
        {
            "id": 13,
            "title": "Iced Mocha",
            "price": 3.75,
            "description": "An iced mocha is a cold coffee drink made with espresso, milk, and chocolate syrup, typically served over ice.",
            "category": "iced coffee",
            "image": "/static/product/iced mocha.png"
        },
        {
            "id": 14,
            "title": "Brown Sugar Milk Tea",
            "price": 3.00,
            "description": "Brown sugar milk tea, also known as brown sugar boba or tiger milk tea, is a popular Taiwanese bubble tea drink made with fresh milk, brown sugar syrup, and tapioca pearls.",
            "category": "non coffee",
            "image": "/static/product/brown sugar milk tea.png"
        },
        {
            "id": 15,
            "title": "Milk Tea",
            "price": 3.00,
            "description": "Milk tea is a beverage made by adding milk to brewed tea.",
            "category": "non coffee",
            "image": "/static/product/milk tea.png"
        },
        {
            "id": 16,
            "title": "Green Tea",
            "price": 2.50,
            "description": "Green tea is a type of tea made from the leaves of the Camellia sinensis plant, processed to avoid oxidation or fermentation, thus preserving its green color and a high concentration of beneficial compounds like antioxidants.",
            "category": "non coffee",
            "image": "/static/product/green tea.png"
        },
        {
            "id": 17,
            "title": "Matcha Latte",
            "price": 3.00,
            "description": "A matcha latte is a vibrant green, tea-based beverage made from matcha powder, hot water, and milk (or a milk alternative).",
            "category": "non coffee",
            "image": "/static/product/matcha latte.png"
        },
        {
            "id": 18,
            "title": "Iced Chocolate",
            "price": 2.50,
            "description": "An iced chocolate is a chilled chocolate beverage, often described as a richer, more decadent version of chocolate milk, typically served over ice.",
            "category": "non coffee",
            "image": "/static/product/iced chocolate.png"
        },
        {
            "id": 19,
            "title": "Iced Coconut Water Matcha Cream",
            "price": 2.00,
            "description": "Coconut matcha cream refers to a beverage or dessert that combines the earthy flavor of matcha green tea with the creamy and slightly sweet taste of coconut.",
            "category": "non coffee",
            "image": "/static/product/coconut matcha.png"
        },
        {
            "id": 20,
            "title": "Iced Blue Milk",
            "price": 2.00,
            "description": "Iced Blue Latte is a refreshing and visually stunning drink that's perfect for hot summer days.",
            "category": "non coffee",
            "image": "/static/product/iced blue milk.png"
        },
        {
            "id": 21,
            "title": "Iced Strawberry Milk",
            "price": 2.00,
            "description": "Iced strawberry milk is a refreshing beverage made with milk and strawberries, often featuring a combination of sweet and creamy flavors.",
            "category": "non coffee",
            "image": "/static/product/iced strawberry milk.png"
        },
        {
            "id": 22,
            "title": "Matcha Frappe",
            "price": 2.50,
            "description": "A matcha frappe is a blended, iced beverage typically made with matcha green tea powder, milk, sweetener, and ice, often topped with whipped cream.",
            "category": "frappe",
            "image": "/static/product/matcha frappe.png"
        },
        {
            "id": 23,
            "title": "Strawberry Frappe",
            "price": 2.50,
            "description": "A strawberry frappe is a blended, chilled beverage featuring the sweet and refreshing taste of strawberries.",
            "category": "frappe",
            "image": "/static/product/strawberry frappe.png"
        },
        {
            "id": 24,
            "title": "Blueberry Frappe",
            "price": 2.50,
            "description": "A blueberry frappe is a blended iced drink, often featuring the sweet and tangy taste of blueberries, combined with a creamy base like milk or yogurt, and often includes ice for a refreshing, slushy texture.",
            "category": "frappe",
            "image": "/static/product/blueberry frappe.png"
        },
        {
            "id": 25,
            "title": "chocolate frappe",
            "price": 2.50,
            "description": "A chocolate frappe is a blended iced coffee drink, typically made with chocolate, ice, milk, and often flavored with chocolate syrup or sauce.",
            "category": "frappe",
            "image": "/static/product/chocolate frappe.png"
        },
        {
            "id": 26,
            "title": "Caramel frappe",
            "price": 2.50,
            "description": "A caramel frappé is a blended iced coffee drink known for its creamy, sweet, and cool caramel flavor.",
            "category": "frappe",
            "image": "/static/product/caramel frappe.png"
        },
        {
            "id": 27,
            "title": "Vanilla frappe",
            "price": 2.50,
            "description": "A vanilla frappe is a blended iced drink, typically featuring a creamy, vanilla-flavored base, often made with milk, ice, and vanilla extract or vanilla bean.",
            "category": "frappe",
            "image": "/static/product/vanilla frappe.png"
        },
        {
            "id": 28,
            "title": "Mocha Frappe",
            "price": 2.50,
            "description": "A Mocha Frappe is a blended, iced coffee drink that combines chocolate and coffee flavors.",
            "category": "frappe",
            "image": "/static/product/mocha frappe.png"
        },
        {
            "id": 29,
            "title": "Strawberry Soda",
            "price": 2.50,
            "description": "Strawberry Soda will delight your taste buds and quench your warm-weather thirst with the natural flavor of fresh strawberries.",
            "category": "soda",
            "image": "/static/product/strawberry soda.png"
        },
        {
            "id": 30,
            "title": "Blue Hawaii Soda",
            "price": 2.50,
            "description": "Blue Hawaiian is a cocktail and a soda flavor known for its tropical taste and vibrant blue color.",
            "category": "soda",
            "image": "/static/product/blue hawaii soda.png"
        },
        {
            "id": 31,
            "title": "Lemon Soda",
            "price": 2.50,
            "description": "Lemon soda is a refreshing, carbonated beverage typically made with lemon juice, sugar (or another sweetener), and soda water.",
            "category": "soda",
            "image": "/static/product/lemon soda.png"
        },
        {
            "id": 32,
            "title": "Watermelon Soda",
            "price": 2.50,
            "description": "Watermelon soda is a refreshing, sweet, and bubbly beverage that captures the flavor of watermelon in a fizzy drink.",
            "category": "soda",
            "image": "/static/product/watermelon soda.png"
        },
        {
            "id": 33,
            "title": "Orange Juice",
            "price": 2.00,
            "description": "Orange juice is a refreshing beverage made from the liquid extracted from oranges.",
            "category": "juice",
            "image": "/static/product/orange juice.png"
        },
        {
            "id": 34,
            "title": "Strawberry Juice",
            "price": 2.00,
            "description": "Strawberry Juice is a refreshing fresh fruit juice that is full of vitamin C and antioxidants and lot of invigorating flavor.",
            "category": "juice",
            "image": "/static/product/strawberry juice.png"
        },
        {
            "id": 35,
            "title": "watermelon juice",
            "price": 2.00,
            "description": "Watermelon juice is so simple to make with a blender. Refreshingly sweet and hydrating, it's perfect for a hot summer day.",
            "category": "juice",
            "image": "/static/product/watermelon juice.png"
        },
        {
            "id": 36,
            "title": "Apple Juice",
            "price": 2.00,
            "description": "Apple juice is a refreshing beverage made from the pressed and filtered juice of apples.",
            "category": "juice",
            "image": "/static/product/apple juice.png"
        },
        {
            "id": 37,
            "title": "Pineapple Juice",
            "price": 2.00,
            "description": "Pineapple juice is a sweet and tangy tropical beverage made from the juice extracted from fresh or canned pineapples.",
            "category": "juice",
            "image": "/static/product/pineapple juice.png"
        },
        {
            "id": 38,
            "title": "Cookies",
            "price": 2.50,
            "description": "A cookies is a small piece of data that a website stores on a user's computer, typically used to remember information about the user or their browsing activity.",
            "category": "cake",
            "image": "/static/product/cookies.png"
        },
        {
            "id": 39,
            "title": "Cake Chocolate",
            "price": 2.50,
            "description": "Chocolate cake is a delicious dessert made from chocolate or cocoa, often enjoyed by both children and adults.",
            "category": "cake",
            "image": "/static/product/cake chocolate.png"
        },
        {
            "id": 40,
            "title": "Cake Strawberry",
            "price": 2.50,
            "description": "Strawberry cake is a cake that uses strawberry as a primary ingredient. Strawberries may be used in the cake batter, atop the cake, and in the frosting.",
            "category": "cake",
            "image": "/static/product/cake strawberry.png"
        },
        {
            "id": 41,
            "title": "Cake Blueberry",
            "price": 2.50,
            "description": "Blueberry cake is easy to put together, has the most moist and tender crumb and is dotted with heaps of juicy blueberries throughout.",
            "category": "cake",
            "image": "/static/product/cake blueberry.png"
        },
        {
            "id": 42,
            "title": "Tiramisu Chocolate",
            "price": 3.00,
            "description": "Chocolate Tiramisu is a decadent layered dessert made up of mascarpone cream, chocolate pastry cream and coffee soaked biscuits.",
            "category": "cake",
            "image": "/static/product/tiramisu chocolate.png"
        },
        {
            "id": 43,
            "title": "Tiramisu Matcha",
            "price": 3.00,
            "description": "Matcha Tiramisu is the perfect fusion no-bake dessert made with layers of rich, velvety matcha mascarpone cream and spongy matcha-soaked ladyfingers.",
            "category": "cake",
            "image": "/static/product/tiramisu matcha.png"
        }

    ]
    return render_template('hot.html', products=products)


@app.get('/iced')
def iced():
    products = [
        {
            "id": 1,
            "title": "Espresso",
            "price": 3.00,
            "description": "Espresso is a concentrated coffee beverage brewed by forcing hot water through finely-ground coffee beans under high pressure.",
            "category": "hot coffee",
            "image": "/static/product/espresso-hot.png"
        },
        {
            "id": 2,
            "title": "Espresso Macchiato",
            "price": 3.75,
            "description": "An espresso macchiato is a strong coffee drink consisting of espresso stained or marked with a small amount of steamed milk foam.",
            "category": "hot coffee",
            "image": "/static/product/espresso-macchiato-hot.png"
        },
        {
            "id": 3,
            "title": "Espresso Con Panna",
            "price": 3.75,
            "description": "Espresso con panna is a simple yet elegant coffee drink consisting of a shot of espresso topped with a dollop of whipped cream.",
            "category": "hot coffee",
            "image": "/static/product/espresso_con_panna_hot.png"
        },
        {
            "id": 4,
            "title": "Americano",
            "price": 3.00,
            "description": "An Americano is a coffee drink made by diluting a shot of espresso with hot water.",
            "category": "hot coffee",
            "image": "/static/product/americano_hot.png"
        },
        {
            "id": 5,
            "title": "Cafe Latte",
            "price": 3.75,
            "description": "A café latte is a coffee drink made with espresso and steamed milk, typically topped with a thin layer of foamed milk.",
            "category": "hot coffee",
            "image": "/static/product/cafe_latte_hot.png"
        },
        {
            "id": 6,
            "title": "Cappuccino",
            "price": 3.50,
            "description": "A cappuccino is a classic coffee drink made with espresso, steamed milk, and foamed milk, typically in equal parts.",
            "category": "hot coffee",
            "image": "/static/product/cappuccino_hot.png"
        },
        {
            "id": 7,
            "title": "Cafe Mocha",
            "price": 3.50,
            "description": "A cafe mocha, also known as caffè mocha or mocha, is a chocolate-flavored warm coffee drink.",
            "category": "hot coffee",
            "image": "/static/product/cafe_mocha_hot.png"
        },
        {
            "id": 8,
            "title": "Caramel Macchiato",
            "price": 4.00,
            "description": "A Caramel Macchiato is a coffee beverage typically consisting of steamed milk, vanilla-flavored syrup, espresso, and a caramel drizzle.",
            "category": "hot coffee",
            "image": "/static/product/caramel_macchiato_hot.png"
        },
        {
            "id": 9,
            "title": "Iced Caramel Cappuccino",
            "price": 4.00,
            "description": "An iced caramel cappuccino is a refreshing coffee beverage that combines the rich flavors of espresso, steamed milk, and caramel, all served cold over ice.",
            "category": "iced coffee",
            "image": "/static/product/iced caramel cappuccino.png"
        },
        {
            "id": 10,
            "title": "Iced Americano",
            "price": 3.25,
            "description": "An Iced Americano is a refreshing coffee drink made by combining espresso with cold water and ice.",
            "category": "iced coffee",
            "image": "/static/product/iced americano.png"
        },
        {
            "id": 11,
            "title": "Iced Latte",
            "price": 4.00,
            "description": "An iced latte is a refreshing, cold coffee drink made with espresso, milk, and ice.",
            "category": "iced coffee",
            "image": "/static/product/iced latte.png"
        },
        {
            "id": 12,
            "title": "Iced Cappuccino",
            "price": 3.75,
            "description": "An iced cappuccino is a refreshing twist on the classic cappuccino, featuring espresso, milk, and a layer of cold, frothy foam, all served over ice.",
            "category": "iced coffee",
            "image": "/static/product/iced cappuccino.png",
        },
        {
            "id": 13,
            "title": "Iced Mocha",
            "price": 3.75,
            "description": "An iced mocha is a cold coffee drink made with espresso, milk, and chocolate syrup, typically served over ice.",
            "category": "iced coffee",
            "image": "/static/product/iced mocha.png"
        },
        {
            "id": 14,
            "title": "Brown Sugar Milk Tea",
            "price": 3.00,
            "description": "Brown sugar milk tea, also known as brown sugar boba or tiger milk tea, is a popular Taiwanese bubble tea drink made with fresh milk, brown sugar syrup, and tapioca pearls.",
            "category": "non coffee",
            "image": "/static/product/brown sugar milk tea.png"
        },
        {
            "id": 15,
            "title": "Milk Tea",
            "price": 3.00,
            "description": "Milk tea is a beverage made by adding milk to brewed tea.",
            "category": "non coffee",
            "image": "/static/product/milk tea.png"
        },
        {
            "id": 16,
            "title": "Green Tea",
            "price": 2.50,
            "description": "Green tea is a type of tea made from the leaves of the Camellia sinensis plant, processed to avoid oxidation or fermentation, thus preserving its green color and a high concentration of beneficial compounds like antioxidants.",
            "category": "non coffee",
            "image": "/static/product/green tea.png"
        },
        {
            "id": 17,
            "title": "Matcha Latte",
            "price": 3.00,
            "description": "A matcha latte is a vibrant green, tea-based beverage made from matcha powder, hot water, and milk (or a milk alternative).",
            "category": "non coffee",
            "image": "/static/product/matcha latte.png"
        },
        {
            "id": 18,
            "title": "Iced Chocolate",
            "price": 2.50,
            "description": "An iced chocolate is a chilled chocolate beverage, often described as a richer, more decadent version of chocolate milk, typically served over ice.",
            "category": "non coffee",
            "image": "/static/product/iced chocolate.png"
        },
        {
            "id": 19,
            "title": "Iced Coconut Water Matcha Cream",
            "price": 2.00,
            "description": "Coconut matcha cream refers to a beverage or dessert that combines the earthy flavor of matcha green tea with the creamy and slightly sweet taste of coconut.",
            "category": "non coffee",
            "image": "/static/product/coconut matcha.png"
        },
        {
            "id": 20,
            "title": "Iced Blue Milk",
            "price": 2.00,
            "description": "Iced Blue Latte is a refreshing and visually stunning drink that's perfect for hot summer days.",
            "category": "non coffee",
            "image": "/static/product/iced blue milk.png"
        },
        {
            "id": 21,
            "title": "Iced Strawberry Milk",
            "price": 2.00,
            "description": "Iced strawberry milk is a refreshing beverage made with milk and strawberries, often featuring a combination of sweet and creamy flavors.",
            "category": "non coffee",
            "image": "/static/product/iced strawberry milk.png"
        },
        {
            "id": 22,
            "title": "Matcha Frappe",
            "price": 2.50,
            "description": "A matcha frappe is a blended, iced beverage typically made with matcha green tea powder, milk, sweetener, and ice, often topped with whipped cream.",
            "category": "frappe",
            "image": "/static/product/matcha frappe.png"
        },
        {
            "id": 23,
            "title": "Strawberry Frappe",
            "price": 2.50,
            "description": "A strawberry frappe is a blended, chilled beverage featuring the sweet and refreshing taste of strawberries.",
            "category": "frappe",
            "image": "/static/product/strawberry frappe.png"
        },
        {
            "id": 24,
            "title": "Blueberry Frappe",
            "price": 2.50,
            "description": "A blueberry frappe is a blended iced drink, often featuring the sweet and tangy taste of blueberries, combined with a creamy base like milk or yogurt, and often includes ice for a refreshing, slushy texture.",
            "category": "frappe",
            "image": "/static/product/blueberry frappe.png"
        },
        {
            "id": 25,
            "title": "chocolate frappe",
            "price": 2.50,
            "description": "A chocolate frappe is a blended iced coffee drink, typically made with chocolate, ice, milk, and often flavored with chocolate syrup or sauce.",
            "category": "frappe",
            "image": "/static/product/chocolate frappe.png"
        },
        {
            "id": 26,
            "title": "Caramel frappe",
            "price": 2.50,
            "description": "A caramel frappé is a blended iced coffee drink known for its creamy, sweet, and cool caramel flavor.",
            "category": "frappe",
            "image": "/static/product/caramel frappe.png"
        },
        {
            "id": 27,
            "title": "Vanilla frappe",
            "price": 2.50,
            "description": "A vanilla frappe is a blended iced drink, typically featuring a creamy, vanilla-flavored base, often made with milk, ice, and vanilla extract or vanilla bean.",
            "category": "frappe",
            "image": "/static/product/vanilla frappe.png"
        },
        {
            "id": 28,
            "title": "Mocha Frappe",
            "price": 2.50,
            "description": "A Mocha Frappe is a blended, iced coffee drink that combines chocolate and coffee flavors.",
            "category": "frappe",
            "image": "/static/product/mocha frappe.png"
        },
        {
            "id": 29,
            "title": "Strawberry Soda",
            "price": 2.50,
            "description": "Strawberry Soda will delight your taste buds and quench your warm-weather thirst with the natural flavor of fresh strawberries.",
            "category": "soda",
            "image": "/static/product/strawberry soda.png"
        },
        {
            "id": 30,
            "title": "Blue Hawaii Soda",
            "price": 2.50,
            "description": "Blue Hawaiian is a cocktail and a soda flavor known for its tropical taste and vibrant blue color.",
            "category": "soda",
            "image": "/static/product/blue hawaii soda.png"
        },
        {
            "id": 31,
            "title": "Lemon Soda",
            "price": 2.50,
            "description": "Lemon soda is a refreshing, carbonated beverage typically made with lemon juice, sugar (or another sweetener), and soda water.",
            "category": "soda",
            "image": "/static/product/lemon soda.png"
        },
        {
            "id": 32,
            "title": "Watermelon Soda",
            "price": 2.50,
            "description": "Watermelon soda is a refreshing, sweet, and bubbly beverage that captures the flavor of watermelon in a fizzy drink.",
            "category": "soda",
            "image": "/static/product/watermelon soda.png"
        },
        {
            "id": 33,
            "title": "Orange Juice",
            "price": 2.00,
            "description": "Orange juice is a refreshing beverage made from the liquid extracted from oranges.",
            "category": "juice",
            "image": "/static/product/orange juice.png"
        },
        {
            "id": 34,
            "title": "Strawberry Juice",
            "price": 2.00,
            "description": "Strawberry Juice is a refreshing fresh fruit juice that is full of vitamin C and antioxidants and lot of invigorating flavor.",
            "category": "juice",
            "image": "/static/product/strawberry juice.png"
        },
        {
            "id": 35,
            "title": "watermelon juice",
            "price": 2.00,
            "description": "Watermelon juice is so simple to make with a blender. Refreshingly sweet and hydrating, it's perfect for a hot summer day.",
            "category": "juice",
            "image": "/static/product/watermelon juice.png"
        },
        {
            "id": 36,
            "title": "Apple Juice",
            "price": 2.00,
            "description": "Apple juice is a refreshing beverage made from the pressed and filtered juice of apples.",
            "category": "juice",
            "image": "/static/product/apple juice.png"
        },
        {
            "id": 37,
            "title": "Pineapple Juice",
            "price": 2.00,
            "description": "Pineapple juice is a sweet and tangy tropical beverage made from the juice extracted from fresh or canned pineapples.",
            "category": "juice",
            "image": "/static/product/pineapple juice.png"
        },
        {
            "id": 38,
            "title": "Cookies",
            "price": 2.50,
            "description": "A cookies is a small piece of data that a website stores on a user's computer, typically used to remember information about the user or their browsing activity.",
            "category": "cake",
            "image": "/static/product/cookies.png"
        },
        {
            "id": 39,
            "title": "Cake Chocolate",
            "price": 2.50,
            "description": "Chocolate cake is a delicious dessert made from chocolate or cocoa, often enjoyed by both children and adults.",
            "category": "cake",
            "image": "/static/product/cake chocolate.png"
        },
        {
            "id": 40,
            "title": "Cake Strawberry",
            "price": 2.50,
            "description": "Strawberry cake is a cake that uses strawberry as a primary ingredient. Strawberries may be used in the cake batter, atop the cake, and in the frosting.",
            "category": "cake",
            "image": "/static/product/cake strawberry.png"
        },
        {
            "id": 41,
            "title": "Cake Blueberry",
            "price": 2.50,
            "description": "Blueberry cake is easy to put together, has the most moist and tender crumb and is dotted with heaps of juicy blueberries throughout.",
            "category": "cake",
            "image": "/static/product/cake blueberry.png"
        },
        {
            "id": 42,
            "title": "Tiramisu Chocolate",
            "price": 3.00,
            "description": "Chocolate Tiramisu is a decadent layered dessert made up of mascarpone cream, chocolate pastry cream and coffee soaked biscuits.",
            "category": "cake",
            "image": "/static/product/tiramisu chocolate.png"
        },
        {
            "id": 43,
            "title": "Tiramisu Matcha",
            "price": 3.00,
            "description": "Matcha Tiramisu is the perfect fusion no-bake dessert made with layers of rich, velvety matcha mascarpone cream and spongy matcha-soaked ladyfingers.",
            "category": "cake",
            "image": "/static/product/tiramisu matcha.png"
        }

    ]
    return render_template('iced.html', products=products)


@app.get('/noncoffee')
def noncoffee():
    products = [
        {
            "id": 1,
            "title": "Espresso",
            "price": 3.00,
            "description": "Espresso is a concentrated coffee beverage brewed by forcing hot water through finely-ground coffee beans under high pressure.",
            "category": "hot coffee",
            "image": "/static/product/espresso-hot.png"
        },
        {
            "id": 2,
            "title": "Espresso Macchiato",
            "price": 3.75,
            "description": "An espresso macchiato is a strong coffee drink consisting of espresso stained or marked with a small amount of steamed milk foam.",
            "category": "hot coffee",
            "image": "/static/product/espresso-macchiato-hot.png"
        },
        {
            "id": 3,
            "title": "Espresso Con Panna",
            "price": 3.75,
            "description": "Espresso con panna is a simple yet elegant coffee drink consisting of a shot of espresso topped with a dollop of whipped cream.",
            "category": "hot coffee",
            "image": "/static/product/espresso_con_panna_hot.png"
        },
        {
            "id": 4,
            "title": "Americano",
            "price": 3.00,
            "description": "An Americano is a coffee drink made by diluting a shot of espresso with hot water.",
            "category": "hot coffee",
            "image": "/static/product/americano_hot.png"
        },
        {
            "id": 5,
            "title": "Cafe Latte",
            "price": 3.75,
            "description": "A café latte is a coffee drink made with espresso and steamed milk, typically topped with a thin layer of foamed milk.",
            "category": "hot coffee",
            "image": "/static/product/cafe_latte_hot.png"
        },
        {
            "id": 6,
            "title": "Cappuccino",
            "price": 3.50,
            "description": "A cappuccino is a classic coffee drink made with espresso, steamed milk, and foamed milk, typically in equal parts.",
            "category": "hot coffee",
            "image": "/static/product/cappuccino_hot.png"
        },
        {
            "id": 7,
            "title": "Cafe Mocha",
            "price": 3.50,
            "description": "A cafe mocha, also known as caffè mocha or mocha, is a chocolate-flavored warm coffee drink.",
            "category": "hot coffee",
            "image": "/static/product/cafe_mocha_hot.png"
        },
        {
            "id": 8,
            "title": "Caramel Macchiato",
            "price": 4.00,
            "description": "A Caramel Macchiato is a coffee beverage typically consisting of steamed milk, vanilla-flavored syrup, espresso, and a caramel drizzle.",
            "category": "hot coffee",
            "image": "/static/product/caramel_macchiato_hot.png"
        },
        {
            "id": 9,
            "title": "Iced Caramel Cappuccino",
            "price": 4.00,
            "description": "An iced caramel cappuccino is a refreshing coffee beverage that combines the rich flavors of espresso, steamed milk, and caramel, all served cold over ice.",
            "category": "iced coffee",
            "image": "/static/product/iced caramel cappuccino.png"
        },
        {
            "id": 10,
            "title": "Iced Americano",
            "price": 3.25,
            "description": "An Iced Americano is a refreshing coffee drink made by combining espresso with cold water and ice.",
            "category": "iced coffee",
            "image": "/static/product/iced americano.png"
        },
        {
            "id": 11,
            "title": "Iced Latte",
            "price": 4.00,
            "description": "An iced latte is a refreshing, cold coffee drink made with espresso, milk, and ice.",
            "category": "iced coffee",
            "image": "/static/product/iced latte.png"
        },
        {
            "id": 12,
            "title": "Iced Cappuccino",
            "price": 3.75,
            "description": "An iced cappuccino is a refreshing twist on the classic cappuccino, featuring espresso, milk, and a layer of cold, frothy foam, all served over ice.",
            "category": "iced coffee",
            "image": "/static/product/iced cappuccino.png",
        },
        {
            "id": 13,
            "title": "Iced Mocha",
            "price": 3.75,
            "description": "An iced mocha is a cold coffee drink made with espresso, milk, and chocolate syrup, typically served over ice.",
            "category": "iced coffee",
            "image": "/static/product/iced mocha.png"
        },
        {
            "id": 14,
            "title": "Brown Sugar Milk Tea",
            "price": 3.00,
            "description": "Brown sugar milk tea, also known as brown sugar boba or tiger milk tea, is a popular Taiwanese bubble tea drink made with fresh milk, brown sugar syrup, and tapioca pearls.",
            "category": "non coffee",
            "image": "/static/product/brown sugar milk tea.png"
        },
        {
            "id": 15,
            "title": "Milk Tea",
            "price": 3.00,
            "description": "Milk tea is a beverage made by adding milk to brewed tea.",
            "category": "non coffee",
            "image": "/static/product/milk tea.png"
        },
        {
            "id": 16,
            "title": "Green Tea",
            "price": 2.50,
            "description": "Green tea is a type of tea made from the leaves of the Camellia sinensis plant, processed to avoid oxidation or fermentation, thus preserving its green color and a high concentration of beneficial compounds like antioxidants.",
            "category": "non coffee",
            "image": "/static/product/green tea.png"
        },
        {
            "id": 17,
            "title": "Matcha Latte",
            "price": 3.00,
            "description": "A matcha latte is a vibrant green, tea-based beverage made from matcha powder, hot water, and milk (or a milk alternative).",
            "category": "non coffee",
            "image": "/static/product/matcha latte.png"
        },
        {
            "id": 18,
            "title": "Iced Chocolate",
            "price": 2.50,
            "description": "An iced chocolate is a chilled chocolate beverage, often described as a richer, more decadent version of chocolate milk, typically served over ice.",
            "category": "non coffee",
            "image": "/static/product/iced chocolate.png"
        },
        {
            "id": 19,
            "title": "Iced Coconut Water Matcha Cream",
            "price": 2.00,
            "description": "Coconut matcha cream refers to a beverage or dessert that combines the earthy flavor of matcha green tea with the creamy and slightly sweet taste of coconut.",
            "category": "non coffee",
            "image": "/static/product/coconut matcha.png"
        },
        {
            "id": 20,
            "title": "Iced Blue Milk",
            "price": 2.00,
            "description": "Iced Blue Latte is a refreshing and visually stunning drink that's perfect for hot summer days.",
            "category": "non coffee",
            "image": "/static/product/iced blue milk.png"
        },
        {
            "id": 21,
            "title": "Iced Strawberry Milk",
            "price": 2.00,
            "description": "Iced strawberry milk is a refreshing beverage made with milk and strawberries, often featuring a combination of sweet and creamy flavors.",
            "category": "non coffee",
            "image": "/static/product/iced strawberry milk.png"
        },
        {
            "id": 22,
            "title": "Matcha Frappe",
            "price": 2.50,
            "description": "A matcha frappe is a blended, iced beverage typically made with matcha green tea powder, milk, sweetener, and ice, often topped with whipped cream.",
            "category": "frappe",
            "image": "/static/product/matcha frappe.png"
        },
        {
            "id": 23,
            "title": "Strawberry Frappe",
            "price": 2.50,
            "description": "A strawberry frappe is a blended, chilled beverage featuring the sweet and refreshing taste of strawberries.",
            "category": "frappe",
            "image": "/static/product/strawberry frappe.png"
        },
        {
            "id": 24,
            "title": "Blueberry Frappe",
            "price": 2.50,
            "description": "A blueberry frappe is a blended iced drink, often featuring the sweet and tangy taste of blueberries, combined with a creamy base like milk or yogurt, and often includes ice for a refreshing, slushy texture.",
            "category": "frappe",
            "image": "/static/product/blueberry frappe.png"
        },
        {
            "id": 25,
            "title": "chocolate frappe",
            "price": 2.50,
            "description": "A chocolate frappe is a blended iced coffee drink, typically made with chocolate, ice, milk, and often flavored with chocolate syrup or sauce.",
            "category": "frappe",
            "image": "/static/product/chocolate frappe.png"
        },
        {
            "id": 26,
            "title": "Caramel frappe",
            "price": 2.50,
            "description": "A caramel frappé is a blended iced coffee drink known for its creamy, sweet, and cool caramel flavor.",
            "category": "frappe",
            "image": "/static/product/caramel frappe.png"
        },
        {
            "id": 27,
            "title": "Vanilla frappe",
            "price": 2.50,
            "description": "A vanilla frappe is a blended iced drink, typically featuring a creamy, vanilla-flavored base, often made with milk, ice, and vanilla extract or vanilla bean.",
            "category": "frappe",
            "image": "/static/product/vanilla frappe.png"
        },
        {
            "id": 28,
            "title": "Mocha Frappe",
            "price": 2.50,
            "description": "A Mocha Frappe is a blended, iced coffee drink that combines chocolate and coffee flavors.",
            "category": "frappe",
            "image": "/static/product/mocha frappe.png"
        },
        {
            "id": 29,
            "title": "Strawberry Soda",
            "price": 2.50,
            "description": "Strawberry Soda will delight your taste buds and quench your warm-weather thirst with the natural flavor of fresh strawberries.",
            "category": "soda",
            "image": "/static/product/strawberry soda.png"
        },
        {
            "id": 30,
            "title": "Blue Hawaii Soda",
            "price": 2.50,
            "description": "Blue Hawaiian is a cocktail and a soda flavor known for its tropical taste and vibrant blue color.",
            "category": "soda",
            "image": "/static/product/blue hawaii soda.png"
        },
        {
            "id": 31,
            "title": "Lemon Soda",
            "price": 2.50,
            "description": "Lemon soda is a refreshing, carbonated beverage typically made with lemon juice, sugar (or another sweetener), and soda water.",
            "category": "soda",
            "image": "/static/product/lemon soda.png"
        },
        {
            "id": 32,
            "title": "Watermelon Soda",
            "price": 2.50,
            "description": "Watermelon soda is a refreshing, sweet, and bubbly beverage that captures the flavor of watermelon in a fizzy drink.",
            "category": "soda",
            "image": "/static/product/watermelon soda.png"
        },
        {
            "id": 33,
            "title": "Orange Juice",
            "price": 2.00,
            "description": "Orange juice is a refreshing beverage made from the liquid extracted from oranges.",
            "category": "juice",
            "image": "/static/product/orange juice.png"
        },
        {
            "id": 34,
            "title": "Strawberry Juice",
            "price": 2.00,
            "description": "Strawberry Juice is a refreshing fresh fruit juice that is full of vitamin C and antioxidants and lot of invigorating flavor.",
            "category": "juice",
            "image": "/static/product/strawberry juice.png"
        },
        {
            "id": 35,
            "title": "watermelon juice",
            "price": 2.00,
            "description": "Watermelon juice is so simple to make with a blender. Refreshingly sweet and hydrating, it's perfect for a hot summer day.",
            "category": "juice",
            "image": "/static/product/watermelon juice.png"
        },
        {
            "id": 36,
            "title": "Apple Juice",
            "price": 2.00,
            "description": "Apple juice is a refreshing beverage made from the pressed and filtered juice of apples.",
            "category": "juice",
            "image": "/static/product/apple juice.png"
        },
        {
            "id": 37,
            "title": "Pineapple Juice",
            "price": 2.00,
            "description": "Pineapple juice is a sweet and tangy tropical beverage made from the juice extracted from fresh or canned pineapples.",
            "category": "juice",
            "image": "/static/product/pineapple juice.png"
        },
        {
            "id": 38,
            "title": "Cookies",
            "price": 2.50,
            "description": "A cookies is a small piece of data that a website stores on a user's computer, typically used to remember information about the user or their browsing activity.",
            "category": "cake",
            "image": "/static/product/cookies.png"
        },
        {
            "id": 39,
            "title": "Cake Chocolate",
            "price": 2.50,
            "description": "Chocolate cake is a delicious dessert made from chocolate or cocoa, often enjoyed by both children and adults.",
            "category": "cake",
            "image": "/static/product/cake chocolate.png"
        },
        {
            "id": 40,
            "title": "Cake Strawberry",
            "price": 2.50,
            "description": "Strawberry cake is a cake that uses strawberry as a primary ingredient. Strawberries may be used in the cake batter, atop the cake, and in the frosting.",
            "category": "cake",
            "image": "/static/product/cake strawberry.png"
        },
        {
            "id": 41,
            "title": "Cake Blueberry",
            "price": 2.50,
            "description": "Blueberry cake is easy to put together, has the most moist and tender crumb and is dotted with heaps of juicy blueberries throughout.",
            "category": "cake",
            "image": "/static/product/cake blueberry.png"
        },
        {
            "id": 42,
            "title": "Tiramisu Chocolate",
            "price": 3.00,
            "description": "Chocolate Tiramisu is a decadent layered dessert made up of mascarpone cream, chocolate pastry cream and coffee soaked biscuits.",
            "category": "cake",
            "image": "/static/product/tiramisu chocolate.png"
        },
        {
            "id": 43,
            "title": "Tiramisu Matcha",
            "price": 3.00,
            "description": "Matcha Tiramisu is the perfect fusion no-bake dessert made with layers of rich, velvety matcha mascarpone cream and spongy matcha-soaked ladyfingers.",
            "category": "cake",
            "image": "/static/product/tiramisu matcha.png"
        }

    ]
    return render_template('noncoffee.html', products=products)


@app.get('/frappe')
def frappe():
    products = [
        {
            "id": 1,
            "title": "Espresso",
            "price": 3.00,
            "description": "Espresso is a concentrated coffee beverage brewed by forcing hot water through finely-ground coffee beans under high pressure.",
            "category": "hot coffee",
            "image": "/static/product/espresso-hot.png"
        },
        {
            "id": 2,
            "title": "Espresso Macchiato",
            "price": 3.75,
            "description": "An espresso macchiato is a strong coffee drink consisting of espresso stained or marked with a small amount of steamed milk foam.",
            "category": "hot coffee",
            "image": "/static/product/espresso-macchiato-hot.png"
        },
        {
            "id": 3,
            "title": "Espresso Con Panna",
            "price": 3.75,
            "description": "Espresso con panna is a simple yet elegant coffee drink consisting of a shot of espresso topped with a dollop of whipped cream.",
            "category": "hot coffee",
            "image": "/static/product/espresso_con_panna_hot.png"
        },
        {
            "id": 4,
            "title": "Americano",
            "price": 3.00,
            "description": "An Americano is a coffee drink made by diluting a shot of espresso with hot water.",
            "category": "hot coffee",
            "image": "/static/product/americano_hot.png"
        },
        {
            "id": 5,
            "title": "Cafe Latte",
            "price": 3.75,
            "description": "A café latte is a coffee drink made with espresso and steamed milk, typically topped with a thin layer of foamed milk.",
            "category": "hot coffee",
            "image": "/static/product/cafe_latte_hot.png"
        },
        {
            "id": 6,
            "title": "Cappuccino",
            "price": 3.50,
            "description": "A cappuccino is a classic coffee drink made with espresso, steamed milk, and foamed milk, typically in equal parts.",
            "category": "hot coffee",
            "image": "/static/product/cappuccino_hot.png"
        },
        {
            "id": 7,
            "title": "Cafe Mocha",
            "price": 3.50,
            "description": "A cafe mocha, also known as caffè mocha or mocha, is a chocolate-flavored warm coffee drink.",
            "category": "hot coffee",
            "image": "/static/product/cafe_mocha_hot.png"
        },
        {
            "id": 8,
            "title": "Caramel Macchiato",
            "price": 4.00,
            "description": "A Caramel Macchiato is a coffee beverage typically consisting of steamed milk, vanilla-flavored syrup, espresso, and a caramel drizzle.",
            "category": "hot coffee",
            "image": "/static/product/caramel_macchiato_hot.png"
        },
        {
            "id": 9,
            "title": "Iced Caramel Cappuccino",
            "price": 4.00,
            "description": "An iced caramel cappuccino is a refreshing coffee beverage that combines the rich flavors of espresso, steamed milk, and caramel, all served cold over ice.",
            "category": "iced coffee",
            "image": "/static/product/iced caramel cappuccino.png"
        },
        {
            "id": 10,
            "title": "Iced Americano",
            "price": 3.25,
            "description": "An Iced Americano is a refreshing coffee drink made by combining espresso with cold water and ice.",
            "category": "iced coffee",
            "image": "/static/product/iced americano.png"
        },
        {
            "id": 11,
            "title": "Iced Latte",
            "price": 4.00,
            "description": "An iced latte is a refreshing, cold coffee drink made with espresso, milk, and ice.",
            "category": "iced coffee",
            "image": "/static/product/iced latte.png"
        },
        {
            "id": 12,
            "title": "Iced Cappuccino",
            "price": 3.75,
            "description": "An iced cappuccino is a refreshing twist on the classic cappuccino, featuring espresso, milk, and a layer of cold, frothy foam, all served over ice.",
            "category": "iced coffee",
            "image": "/static/product/iced cappuccino.png",
        },
        {
            "id": 13,
            "title": "Iced Mocha",
            "price": 3.75,
            "description": "An iced mocha is a cold coffee drink made with espresso, milk, and chocolate syrup, typically served over ice.",
            "category": "iced coffee",
            "image": "/static/product/iced mocha.png"
        },
        {
            "id": 14,
            "title": "Brown Sugar Milk Tea",
            "price": 3.00,
            "description": "Brown sugar milk tea, also known as brown sugar boba or tiger milk tea, is a popular Taiwanese bubble tea drink made with fresh milk, brown sugar syrup, and tapioca pearls.",
            "category": "non coffee",
            "image": "/static/product/brown sugar milk tea.png"
        },
        {
            "id": 15,
            "title": "Milk Tea",
            "price": 3.00,
            "description": "Milk tea is a beverage made by adding milk to brewed tea.",
            "category": "non coffee",
            "image": "/static/product/milk tea.png"
        },
        {
            "id": 16,
            "title": "Green Tea",
            "price": 2.50,
            "description": "Green tea is a type of tea made from the leaves of the Camellia sinensis plant, processed to avoid oxidation or fermentation, thus preserving its green color and a high concentration of beneficial compounds like antioxidants.",
            "category": "non coffee",
            "image": "/static/product/green tea.png"
        },
        {
            "id": 17,
            "title": "Matcha Latte",
            "price": 3.00,
            "description": "A matcha latte is a vibrant green, tea-based beverage made from matcha powder, hot water, and milk (or a milk alternative).",
            "category": "non coffee",
            "image": "/static/product/matcha latte.png"
        },
        {
            "id": 18,
            "title": "Iced Chocolate",
            "price": 2.50,
            "description": "An iced chocolate is a chilled chocolate beverage, often described as a richer, more decadent version of chocolate milk, typically served over ice.",
            "category": "non coffee",
            "image": "/static/product/iced chocolate.png"
        },
        {
            "id": 19,
            "title": "Iced Coconut Water Matcha Cream",
            "price": 2.00,
            "description": "Coconut matcha cream refers to a beverage or dessert that combines the earthy flavor of matcha green tea with the creamy and slightly sweet taste of coconut.",
            "category": "non coffee",
            "image": "/static/product/coconut matcha.png"
        },
        {
            "id": 20,
            "title": "Iced Blue Milk",
            "price": 2.00,
            "description": "Iced Blue Latte is a refreshing and visually stunning drink that's perfect for hot summer days.",
            "category": "non coffee",
            "image": "/static/product/iced blue milk.png"
        },
        {
            "id": 21,
            "title": "Iced Strawberry Milk",
            "price": 2.00,
            "description": "Iced strawberry milk is a refreshing beverage made with milk and strawberries, often featuring a combination of sweet and creamy flavors.",
            "category": "non coffee",
            "image": "/static/product/iced strawberry milk.png"
        },
        {
            "id": 22,
            "title": "Matcha Frappe",
            "price": 2.50,
            "description": "A matcha frappe is a blended, iced beverage typically made with matcha green tea powder, milk, sweetener, and ice, often topped with whipped cream.",
            "category": "frappe",
            "image": "/static/product/matcha frappe.png"
        },
        {
            "id": 23,
            "title": "Strawberry Frappe",
            "price": 2.50,
            "description": "A strawberry frappe is a blended, chilled beverage featuring the sweet and refreshing taste of strawberries.",
            "category": "frappe",
            "image": "/static/product/strawberry frappe.png"
        },
        {
            "id": 24,
            "title": "Blueberry Frappe",
            "price": 2.50,
            "description": "A blueberry frappe is a blended iced drink, often featuring the sweet and tangy taste of blueberries, combined with a creamy base like milk or yogurt, and often includes ice for a refreshing, slushy texture.",
            "category": "frappe",
            "image": "/static/product/blueberry frappe.png"
        },
        {
            "id": 25,
            "title": "chocolate frappe",
            "price": 2.50,
            "description": "A chocolate frappe is a blended iced coffee drink, typically made with chocolate, ice, milk, and often flavored with chocolate syrup or sauce.",
            "category": "frappe",
            "image": "/static/product/chocolate frappe.png"
        },
        {
            "id": 26,
            "title": "Caramel frappe",
            "price": 2.50,
            "description": "A caramel frappé is a blended iced coffee drink known for its creamy, sweet, and cool caramel flavor.",
            "category": "frappe",
            "image": "/static/product/caramel frappe.png"
        },
        {
            "id": 27,
            "title": "Vanilla frappe",
            "price": 2.50,
            "description": "A vanilla frappe is a blended iced drink, typically featuring a creamy, vanilla-flavored base, often made with milk, ice, and vanilla extract or vanilla bean.",
            "category": "frappe",
            "image": "/static/product/vanilla frappe.png"
        },
        {
            "id": 28,
            "title": "Mocha Frappe",
            "price": 2.50,
            "description": "A Mocha Frappe is a blended, iced coffee drink that combines chocolate and coffee flavors.",
            "category": "frappe",
            "image": "/static/product/mocha frappe.png"
        },
        {
            "id": 29,
            "title": "Strawberry Soda",
            "price": 2.50,
            "description": "Strawberry Soda will delight your taste buds and quench your warm-weather thirst with the natural flavor of fresh strawberries.",
            "category": "soda",
            "image": "/static/product/strawberry soda.png"
        },
        {
            "id": 30,
            "title": "Blue Hawaii Soda",
            "price": 2.50,
            "description": "Blue Hawaiian is a cocktail and a soda flavor known for its tropical taste and vibrant blue color.",
            "category": "soda",
            "image": "/static/product/blue hawaii soda.png"
        },
        {
            "id": 31,
            "title": "Lemon Soda",
            "price": 2.50,
            "description": "Lemon soda is a refreshing, carbonated beverage typically made with lemon juice, sugar (or another sweetener), and soda water.",
            "category": "soda",
            "image": "/static/product/lemon soda.png"
        },
        {
            "id": 32,
            "title": "Watermelon Soda",
            "price": 2.50,
            "description": "Watermelon soda is a refreshing, sweet, and bubbly beverage that captures the flavor of watermelon in a fizzy drink.",
            "category": "soda",
            "image": "/static/product/watermelon soda.png"
        },
        {
            "id": 33,
            "title": "Orange Juice",
            "price": 2.00,
            "description": "Orange juice is a refreshing beverage made from the liquid extracted from oranges.",
            "category": "juice",
            "image": "/static/product/orange juice.png"
        },
        {
            "id": 34,
            "title": "Strawberry Juice",
            "price": 2.00,
            "description": "Strawberry Juice is a refreshing fresh fruit juice that is full of vitamin C and antioxidants and lot of invigorating flavor.",
            "category": "juice",
            "image": "/static/product/strawberry juice.png"
        },
        {
            "id": 35,
            "title": "watermelon juice",
            "price": 2.00,
            "description": "Watermelon juice is so simple to make with a blender. Refreshingly sweet and hydrating, it's perfect for a hot summer day.",
            "category": "juice",
            "image": "/static/product/watermelon juice.png"
        },
        {
            "id": 36,
            "title": "Apple Juice",
            "price": 2.00,
            "description": "Apple juice is a refreshing beverage made from the pressed and filtered juice of apples.",
            "category": "juice",
            "image": "/static/product/apple juice.png"
        },
        {
            "id": 37,
            "title": "Pineapple Juice",
            "price": 2.00,
            "description": "Pineapple juice is a sweet and tangy tropical beverage made from the juice extracted from fresh or canned pineapples.",
            "category": "juice",
            "image": "/static/product/pineapple juice.png"
        },
        {
            "id": 38,
            "title": "Cookies",
            "price": 2.50,
            "description": "A cookies is a small piece of data that a website stores on a user's computer, typically used to remember information about the user or their browsing activity.",
            "category": "cake",
            "image": "/static/product/cookies.png"
        },
        {
            "id": 39,
            "title": "Cake Chocolate",
            "price": 2.50,
            "description": "Chocolate cake is a delicious dessert made from chocolate or cocoa, often enjoyed by both children and adults.",
            "category": "cake",
            "image": "/static/product/cake chocolate.png"
        },
        {
            "id": 40,
            "title": "Cake Strawberry",
            "price": 2.50,
            "description": "Strawberry cake is a cake that uses strawberry as a primary ingredient. Strawberries may be used in the cake batter, atop the cake, and in the frosting.",
            "category": "cake",
            "image": "/static/product/cake strawberry.png"
        },
        {
            "id": 41,
            "title": "Cake Blueberry",
            "price": 2.50,
            "description": "Blueberry cake is easy to put together, has the most moist and tender crumb and is dotted with heaps of juicy blueberries throughout.",
            "category": "cake",
            "image": "/static/product/cake blueberry.png"
        },
        {
            "id": 42,
            "title": "Tiramisu Chocolate",
            "price": 3.00,
            "description": "Chocolate Tiramisu is a decadent layered dessert made up of mascarpone cream, chocolate pastry cream and coffee soaked biscuits.",
            "category": "cake",
            "image": "/static/product/tiramisu chocolate.png"
        },
        {
            "id": 43,
            "title": "Tiramisu Matcha",
            "price": 3.00,
            "description": "Matcha Tiramisu is the perfect fusion no-bake dessert made with layers of rich, velvety matcha mascarpone cream and spongy matcha-soaked ladyfingers.",
            "category": "cake",
            "image": "/static/product/tiramisu matcha.png"
        }

    ]
    return render_template('frappe.html', products=products)


@app.get('/soda')
def soda():
    products = [
        {
            "id": 1,
            "title": "Espresso",
            "price": 3.00,
            "description": "Espresso is a concentrated coffee beverage brewed by forcing hot water through finely-ground coffee beans under high pressure.",
            "category": "hot coffee",
            "image": "/static/product/espresso-hot.png"
        },
        {
            "id": 2,
            "title": "Espresso Macchiato",
            "price": 3.75,
            "description": "An espresso macchiato is a strong coffee drink consisting of espresso stained or marked with a small amount of steamed milk foam.",
            "category": "hot coffee",
            "image": "/static/product/espresso-macchiato-hot.png"
        },
        {
            "id": 3,
            "title": "Espresso Con Panna",
            "price": 3.75,
            "description": "Espresso con panna is a simple yet elegant coffee drink consisting of a shot of espresso topped with a dollop of whipped cream.",
            "category": "hot coffee",
            "image": "/static/product/espresso_con_panna_hot.png"
        },
        {
            "id": 4,
            "title": "Americano",
            "price": 3.00,
            "description": "An Americano is a coffee drink made by diluting a shot of espresso with hot water.",
            "category": "hot coffee",
            "image": "/static/product/americano_hot.png"
        },
        {
            "id": 5,
            "title": "Cafe Latte",
            "price": 3.75,
            "description": "A café latte is a coffee drink made with espresso and steamed milk, typically topped with a thin layer of foamed milk.",
            "category": "hot coffee",
            "image": "/static/product/cafe_latte_hot.png"
        },
        {
            "id": 6,
            "title": "Cappuccino",
            "price": 3.50,
            "description": "A cappuccino is a classic coffee drink made with espresso, steamed milk, and foamed milk, typically in equal parts.",
            "category": "hot coffee",
            "image": "/static/product/cappuccino_hot.png"
        },
        {
            "id": 7,
            "title": "Cafe Mocha",
            "price": 3.50,
            "description": "A cafe mocha, also known as caffè mocha or mocha, is a chocolate-flavored warm coffee drink.",
            "category": "hot coffee",
            "image": "/static/product/cafe_mocha_hot.png"
        },
        {
            "id": 8,
            "title": "Caramel Macchiato",
            "price": 4.00,
            "description": "A Caramel Macchiato is a coffee beverage typically consisting of steamed milk, vanilla-flavored syrup, espresso, and a caramel drizzle.",
            "category": "hot coffee",
            "image": "/static/product/caramel_macchiato_hot.png"
        },
        {
            "id": 9,
            "title": "Iced Caramel Cappuccino",
            "price": 4.00,
            "description": "An iced caramel cappuccino is a refreshing coffee beverage that combines the rich flavors of espresso, steamed milk, and caramel, all served cold over ice.",
            "category": "iced coffee",
            "image": "/static/product/iced caramel cappuccino.png"
        },
        {
            "id": 10,
            "title": "Iced Americano",
            "price": 3.25,
            "description": "An Iced Americano is a refreshing coffee drink made by combining espresso with cold water and ice.",
            "category": "iced coffee",
            "image": "/static/product/iced americano.png"
        },
        {
            "id": 11,
            "title": "Iced Latte",
            "price": 4.00,
            "description": "An iced latte is a refreshing, cold coffee drink made with espresso, milk, and ice.",
            "category": "iced coffee",
            "image": "/static/product/iced latte.png"
        },
        {
            "id": 12,
            "title": "Iced Cappuccino",
            "price": 3.75,
            "description": "An iced cappuccino is a refreshing twist on the classic cappuccino, featuring espresso, milk, and a layer of cold, frothy foam, all served over ice.",
            "category": "iced coffee",
            "image": "/static/product/iced cappuccino.png",
        },
        {
            "id": 13,
            "title": "Iced Mocha",
            "price": 3.75,
            "description": "An iced mocha is a cold coffee drink made with espresso, milk, and chocolate syrup, typically served over ice.",
            "category": "iced coffee",
            "image": "/static/product/iced mocha.png"
        },
        {
            "id": 14,
            "title": "Brown Sugar Milk Tea",
            "price": 3.00,
            "description": "Brown sugar milk tea, also known as brown sugar boba or tiger milk tea, is a popular Taiwanese bubble tea drink made with fresh milk, brown sugar syrup, and tapioca pearls.",
            "category": "non coffee",
            "image": "/static/product/brown sugar milk tea.png"
        },
        {
            "id": 15,
            "title": "Milk Tea",
            "price": 3.00,
            "description": "Milk tea is a beverage made by adding milk to brewed tea.",
            "category": "non coffee",
            "image": "/static/product/milk tea.png"
        },
        {
            "id": 16,
            "title": "Green Tea",
            "price": 2.50,
            "description": "Green tea is a type of tea made from the leaves of the Camellia sinensis plant, processed to avoid oxidation or fermentation, thus preserving its green color and a high concentration of beneficial compounds like antioxidants.",
            "category": "non coffee",
            "image": "/static/product/green tea.png"
        },
        {
            "id": 17,
            "title": "Matcha Latte",
            "price": 3.00,
            "description": "A matcha latte is a vibrant green, tea-based beverage made from matcha powder, hot water, and milk (or a milk alternative).",
            "category": "non coffee",
            "image": "/static/product/matcha latte.png"
        },
        {
            "id": 18,
            "title": "Iced Chocolate",
            "price": 2.50,
            "description": "An iced chocolate is a chilled chocolate beverage, often described as a richer, more decadent version of chocolate milk, typically served over ice.",
            "category": "non coffee",
            "image": "/static/product/iced chocolate.png"
        },
        {
            "id": 19,
            "title": "Iced Coconut Water Matcha Cream",
            "price": 2.00,
            "description": "Coconut matcha cream refers to a beverage or dessert that combines the earthy flavor of matcha green tea with the creamy and slightly sweet taste of coconut.",
            "category": "non coffee",
            "image": "/static/product/coconut matcha.png"
        },
        {
            "id": 20,
            "title": "Iced Blue Milk",
            "price": 2.00,
            "description": "Iced Blue Latte is a refreshing and visually stunning drink that's perfect for hot summer days.",
            "category": "non coffee",
            "image": "/static/product/iced blue milk.png"
        },
        {
            "id": 21,
            "title": "Iced Strawberry Milk",
            "price": 2.00,
            "description": "Iced strawberry milk is a refreshing beverage made with milk and strawberries, often featuring a combination of sweet and creamy flavors.",
            "category": "non coffee",
            "image": "/static/product/iced strawberry milk.png"
        },
        {
            "id": 22,
            "title": "Matcha Frappe",
            "price": 2.50,
            "description": "A matcha frappe is a blended, iced beverage typically made with matcha green tea powder, milk, sweetener, and ice, often topped with whipped cream.",
            "category": "frappe",
            "image": "/static/product/matcha frappe.png"
        },
        {
            "id": 23,
            "title": "Strawberry Frappe",
            "price": 2.50,
            "description": "A strawberry frappe is a blended, chilled beverage featuring the sweet and refreshing taste of strawberries.",
            "category": "frappe",
            "image": "/static/product/strawberry frappe.png"
        },
        {
            "id": 24,
            "title": "Blueberry Frappe",
            "price": 2.50,
            "description": "A blueberry frappe is a blended iced drink, often featuring the sweet and tangy taste of blueberries, combined with a creamy base like milk or yogurt, and often includes ice for a refreshing, slushy texture.",
            "category": "frappe",
            "image": "/static/product/blueberry frappe.png"
        },
        {
            "id": 25,
            "title": "chocolate frappe",
            "price": 2.50,
            "description": "A chocolate frappe is a blended iced coffee drink, typically made with chocolate, ice, milk, and often flavored with chocolate syrup or sauce.",
            "category": "frappe",
            "image": "/static/product/chocolate frappe.png"
        },
        {
            "id": 26,
            "title": "Caramel frappe",
            "price": 2.50,
            "description": "A caramel frappé is a blended iced coffee drink known for its creamy, sweet, and cool caramel flavor.",
            "category": "frappe",
            "image": "/static/product/caramel frappe.png"
        },
        {
            "id": 27,
            "title": "Vanilla frappe",
            "price": 2.50,
            "description": "A vanilla frappe is a blended iced drink, typically featuring a creamy, vanilla-flavored base, often made with milk, ice, and vanilla extract or vanilla bean.",
            "category": "frappe",
            "image": "/static/product/vanilla frappe.png"
        },
        {
            "id": 28,
            "title": "Mocha Frappe",
            "price": 2.50,
            "description": "A Mocha Frappe is a blended, iced coffee drink that combines chocolate and coffee flavors.",
            "category": "frappe",
            "image": "/static/product/mocha frappe.png"
        },
        {
            "id": 29,
            "title": "Strawberry Soda",
            "price": 2.50,
            "description": "Strawberry Soda will delight your taste buds and quench your warm-weather thirst with the natural flavor of fresh strawberries.",
            "category": "soda",
            "image": "/static/product/strawberry soda.png"
        },
        {
            "id": 30,
            "title": "Blue Hawaii Soda",
            "price": 2.50,
            "description": "Blue Hawaiian is a cocktail and a soda flavor known for its tropical taste and vibrant blue color.",
            "category": "soda",
            "image": "/static/product/blue hawaii soda.png"
        },
        {
            "id": 31,
            "title": "Lemon Soda",
            "price": 2.50,
            "description": "Lemon soda is a refreshing, carbonated beverage typically made with lemon juice, sugar (or another sweetener), and soda water.",
            "category": "soda",
            "image": "/static/product/lemon soda.png"
        },
        {
            "id": 32,
            "title": "Watermelon Soda",
            "price": 2.50,
            "description": "Watermelon soda is a refreshing, sweet, and bubbly beverage that captures the flavor of watermelon in a fizzy drink.",
            "category": "soda",
            "image": "/static/product/watermelon soda.png"
        },
        {
            "id": 33,
            "title": "Orange Juice",
            "price": 2.00,
            "description": "Orange juice is a refreshing beverage made from the liquid extracted from oranges.",
            "category": "juice",
            "image": "/static/product/orange juice.png"
        },
        {
            "id": 34,
            "title": "Strawberry Juice",
            "price": 2.00,
            "description": "Strawberry Juice is a refreshing fresh fruit juice that is full of vitamin C and antioxidants and lot of invigorating flavor.",
            "category": "juice",
            "image": "/static/product/strawberry juice.png"
        },
        {
            "id": 35,
            "title": "watermelon juice",
            "price": 2.00,
            "description": "Watermelon juice is so simple to make with a blender. Refreshingly sweet and hydrating, it's perfect for a hot summer day.",
            "category": "juice",
            "image": "/static/product/watermelon juice.png"
        },
        {
            "id": 36,
            "title": "Apple Juice",
            "price": 2.00,
            "description": "Apple juice is a refreshing beverage made from the pressed and filtered juice of apples.",
            "category": "juice",
            "image": "/static/product/apple juice.png"
        },
        {
            "id": 37,
            "title": "Pineapple Juice",
            "price": 2.00,
            "description": "Pineapple juice is a sweet and tangy tropical beverage made from the juice extracted from fresh or canned pineapples.",
            "category": "juice",
            "image": "/static/product/pineapple juice.png"
        },
        {
            "id": 38,
            "title": "Cookies",
            "price": 2.50,
            "description": "A cookies is a small piece of data that a website stores on a user's computer, typically used to remember information about the user or their browsing activity.",
            "category": "cake",
            "image": "/static/product/cookies.png"
        },
        {
            "id": 39,
            "title": "Cake Chocolate",
            "price": 2.50,
            "description": "Chocolate cake is a delicious dessert made from chocolate or cocoa, often enjoyed by both children and adults.",
            "category": "cake",
            "image": "/static/product/cake chocolate.png"
        },
        {
            "id": 40,
            "title": "Cake Strawberry",
            "price": 2.50,
            "description": "Strawberry cake is a cake that uses strawberry as a primary ingredient. Strawberries may be used in the cake batter, atop the cake, and in the frosting.",
            "category": "cake",
            "image": "/static/product/cake strawberry.png"
        },
        {
            "id": 41,
            "title": "Cake Blueberry",
            "price": 2.50,
            "description": "Blueberry cake is easy to put together, has the most moist and tender crumb and is dotted with heaps of juicy blueberries throughout.",
            "category": "cake",
            "image": "/static/product/cake blueberry.png"
        },
        {
            "id": 42,
            "title": "Tiramisu Chocolate",
            "price": 3.00,
            "description": "Chocolate Tiramisu is a decadent layered dessert made up of mascarpone cream, chocolate pastry cream and coffee soaked biscuits.",
            "category": "cake",
            "image": "/static/product/tiramisu chocolate.png"
        },
        {
            "id": 43,
            "title": "Tiramisu Matcha",
            "price": 3.00,
            "description": "Matcha Tiramisu is the perfect fusion no-bake dessert made with layers of rich, velvety matcha mascarpone cream and spongy matcha-soaked ladyfingers.",
            "category": "cake",
            "image": "/static/product/tiramisu matcha.png"
        }

    ]
    return render_template('soda.html', products=products)


@app.get('/juice')
def juice():
    products = [
        {
            "id": 1,
            "title": "Espresso",
            "price": 3.00,
            "description": "Espresso is a concentrated coffee beverage brewed by forcing hot water through finely-ground coffee beans under high pressure.",
            "category": "hot coffee",
            "image": "/static/product/espresso-hot.png"
        },
        {
            "id": 2,
            "title": "Espresso Macchiato",
            "price": 3.75,
            "description": "An espresso macchiato is a strong coffee drink consisting of espresso stained or marked with a small amount of steamed milk foam.",
            "category": "hot coffee",
            "image": "/static/product/espresso-macchiato-hot.png"
        },
        {
            "id": 3,
            "title": "Espresso Con Panna",
            "price": 3.75,
            "description": "Espresso con panna is a simple yet elegant coffee drink consisting of a shot of espresso topped with a dollop of whipped cream.",
            "category": "hot coffee",
            "image": "/static/product/espresso_con_panna_hot.png"
        },
        {
            "id": 4,
            "title": "Americano",
            "price": 3.00,
            "description": "An Americano is a coffee drink made by diluting a shot of espresso with hot water.",
            "category": "hot coffee",
            "image": "/static/product/americano_hot.png"
        },
        {
            "id": 5,
            "title": "Cafe Latte",
            "price": 3.75,
            "description": "A café latte is a coffee drink made with espresso and steamed milk, typically topped with a thin layer of foamed milk.",
            "category": "hot coffee",
            "image": "/static/product/cafe_latte_hot.png"
        },
        {
            "id": 6,
            "title": "Cappuccino",
            "price": 3.50,
            "description": "A cappuccino is a classic coffee drink made with espresso, steamed milk, and foamed milk, typically in equal parts.",
            "category": "hot coffee",
            "image": "/static/product/cappuccino_hot.png"
        },
        {
            "id": 7,
            "title": "Cafe Mocha",
            "price": 3.50,
            "description": "A cafe mocha, also known as caffè mocha or mocha, is a chocolate-flavored warm coffee drink.",
            "category": "hot coffee",
            "image": "/static/product/cafe_mocha_hot.png"
        },
        {
            "id": 8,
            "title": "Caramel Macchiato",
            "price": 4.00,
            "description": "A Caramel Macchiato is a coffee beverage typically consisting of steamed milk, vanilla-flavored syrup, espresso, and a caramel drizzle.",
            "category": "hot coffee",
            "image": "/static/product/caramel_macchiato_hot.png"
        },
        {
            "id": 9,
            "title": "Iced Caramel Cappuccino",
            "price": 4.00,
            "description": "An iced caramel cappuccino is a refreshing coffee beverage that combines the rich flavors of espresso, steamed milk, and caramel, all served cold over ice.",
            "category": "iced coffee",
            "image": "/static/product/iced caramel cappuccino.png"
        },
        {
            "id": 10,
            "title": "Iced Americano",
            "price": 3.25,
            "description": "An Iced Americano is a refreshing coffee drink made by combining espresso with cold water and ice.",
            "category": "iced coffee",
            "image": "/static/product/iced americano.png"
        },
        {
            "id": 11,
            "title": "Iced Latte",
            "price": 4.00,
            "description": "An iced latte is a refreshing, cold coffee drink made with espresso, milk, and ice.",
            "category": "iced coffee",
            "image": "/static/product/iced latte.png"
        },
        {
            "id": 12,
            "title": "Iced Cappuccino",
            "price": 3.75,
            "description": "An iced cappuccino is a refreshing twist on the classic cappuccino, featuring espresso, milk, and a layer of cold, frothy foam, all served over ice.",
            "category": "iced coffee",
            "image": "/static/product/iced cappuccino.png",
        },
        {
            "id": 13,
            "title": "Iced Mocha",
            "price": 3.75,
            "description": "An iced mocha is a cold coffee drink made with espresso, milk, and chocolate syrup, typically served over ice.",
            "category": "iced coffee",
            "image": "/static/product/iced mocha.png"
        },
        {
            "id": 14,
            "title": "Brown Sugar Milk Tea",
            "price": 3.00,
            "description": "Brown sugar milk tea, also known as brown sugar boba or tiger milk tea, is a popular Taiwanese bubble tea drink made with fresh milk, brown sugar syrup, and tapioca pearls.",
            "category": "non coffee",
            "image": "/static/product/brown sugar milk tea.png"
        },
        {
            "id": 15,
            "title": "Milk Tea",
            "price": 3.00,
            "description": "Milk tea is a beverage made by adding milk to brewed tea.",
            "category": "non coffee",
            "image": "/static/product/milk tea.png"
        },
        {
            "id": 16,
            "title": "Green Tea",
            "price": 2.50,
            "description": "Green tea is a type of tea made from the leaves of the Camellia sinensis plant, processed to avoid oxidation or fermentation, thus preserving its green color and a high concentration of beneficial compounds like antioxidants.",
            "category": "non coffee",
            "image": "/static/product/green tea.png"
        },
        {
            "id": 17,
            "title": "Matcha Latte",
            "price": 3.00,
            "description": "A matcha latte is a vibrant green, tea-based beverage made from matcha powder, hot water, and milk (or a milk alternative).",
            "category": "non coffee",
            "image": "/static/product/matcha latte.png"
        },
        {
            "id": 18,
            "title": "Iced Chocolate",
            "price": 2.50,
            "description": "An iced chocolate is a chilled chocolate beverage, often described as a richer, more decadent version of chocolate milk, typically served over ice.",
            "category": "non coffee",
            "image": "/static/product/iced chocolate.png"
        },
        {
            "id": 19,
            "title": "Iced Coconut Water Matcha Cream",
            "price": 2.00,
            "description": "Coconut matcha cream refers to a beverage or dessert that combines the earthy flavor of matcha green tea with the creamy and slightly sweet taste of coconut.",
            "category": "non coffee",
            "image": "/static/product/coconut matcha.png"
        },
        {
            "id": 20,
            "title": "Iced Blue Milk",
            "price": 2.00,
            "description": "Iced Blue Latte is a refreshing and visually stunning drink that's perfect for hot summer days.",
            "category": "non coffee",
            "image": "/static/product/iced blue milk.png"
        },
        {
            "id": 21,
            "title": "Iced Strawberry Milk",
            "price": 2.00,
            "description": "Iced strawberry milk is a refreshing beverage made with milk and strawberries, often featuring a combination of sweet and creamy flavors.",
            "category": "non coffee",
            "image": "/static/product/iced strawberry milk.png"
        },
        {
            "id": 22,
            "title": "Matcha Frappe",
            "price": 2.50,
            "description": "A matcha frappe is a blended, iced beverage typically made with matcha green tea powder, milk, sweetener, and ice, often topped with whipped cream.",
            "category": "frappe",
            "image": "/static/product/matcha frappe.png"
        },
        {
            "id": 23,
            "title": "Strawberry Frappe",
            "price": 2.50,
            "description": "A strawberry frappe is a blended, chilled beverage featuring the sweet and refreshing taste of strawberries.",
            "category": "frappe",
            "image": "/static/product/strawberry frappe.png"
        },
        {
            "id": 24,
            "title": "Blueberry Frappe",
            "price": 2.50,
            "description": "A blueberry frappe is a blended iced drink, often featuring the sweet and tangy taste of blueberries, combined with a creamy base like milk or yogurt, and often includes ice for a refreshing, slushy texture.",
            "category": "frappe",
            "image": "/static/product/blueberry frappe.png"
        },
        {
            "id": 25,
            "title": "chocolate frappe",
            "price": 2.50,
            "description": "A chocolate frappe is a blended iced coffee drink, typically made with chocolate, ice, milk, and often flavored with chocolate syrup or sauce.",
            "category": "frappe",
            "image": "/static/product/chocolate frappe.png"
        },
        {
            "id": 26,
            "title": "Caramel frappe",
            "price": 2.50,
            "description": "A caramel frappé is a blended iced coffee drink known for its creamy, sweet, and cool caramel flavor.",
            "category": "frappe",
            "image": "/static/product/caramel frappe.png"
        },
        {
            "id": 27,
            "title": "Vanilla frappe",
            "price": 2.50,
            "description": "A vanilla frappe is a blended iced drink, typically featuring a creamy, vanilla-flavored base, often made with milk, ice, and vanilla extract or vanilla bean.",
            "category": "frappe",
            "image": "/static/product/vanilla frappe.png"
        },
        {
            "id": 28,
            "title": "Mocha Frappe",
            "price": 2.50,
            "description": "A Mocha Frappe is a blended, iced coffee drink that combines chocolate and coffee flavors.",
            "category": "frappe",
            "image": "/static/product/mocha frappe.png"
        },
        {
            "id": 29,
            "title": "Strawberry Soda",
            "price": 2.50,
            "description": "Strawberry Soda will delight your taste buds and quench your warm-weather thirst with the natural flavor of fresh strawberries.",
            "category": "soda",
            "image": "/static/product/strawberry soda.png"
        },
        {
            "id": 30,
            "title": "Blue Hawaii Soda",
            "price": 2.50,
            "description": "Blue Hawaiian is a cocktail and a soda flavor known for its tropical taste and vibrant blue color.",
            "category": "soda",
            "image": "/static/product/blue hawaii soda.png"
        },
        {
            "id": 31,
            "title": "Lemon Soda",
            "price": 2.50,
            "description": "Lemon soda is a refreshing, carbonated beverage typically made with lemon juice, sugar (or another sweetener), and soda water.",
            "category": "soda",
            "image": "/static/product/lemon soda.png"
        },
        {
            "id": 32,
            "title": "Watermelon Soda",
            "price": 2.50,
            "description": "Watermelon soda is a refreshing, sweet, and bubbly beverage that captures the flavor of watermelon in a fizzy drink.",
            "category": "soda",
            "image": "/static/product/watermelon soda.png"
        },
        {
            "id": 33,
            "title": "Orange Juice",
            "price": 2.00,
            "description": "Orange juice is a refreshing beverage made from the liquid extracted from oranges.",
            "category": "juice",
            "image": "/static/product/orange juice.png"
        },
        {
            "id": 34,
            "title": "Strawberry Juice",
            "price": 2.00,
            "description": "Strawberry Juice is a refreshing fresh fruit juice that is full of vitamin C and antioxidants and lot of invigorating flavor.",
            "category": "juice",
            "image": "/static/product/strawberry juice.png"
        },
        {
            "id": 35,
            "title": "watermelon juice",
            "price": 2.00,
            "description": "Watermelon juice is so simple to make with a blender. Refreshingly sweet and hydrating, it's perfect for a hot summer day.",
            "category": "juice",
            "image": "/static/product/watermelon juice.png"
        },
        {
            "id": 36,
            "title": "Apple Juice",
            "price": 2.00,
            "description": "Apple juice is a refreshing beverage made from the pressed and filtered juice of apples.",
            "category": "juice",
            "image": "/static/product/apple juice.png"
        },
        {
            "id": 37,
            "title": "Pineapple Juice",
            "price": 2.00,
            "description": "Pineapple juice is a sweet and tangy tropical beverage made from the juice extracted from fresh or canned pineapples.",
            "category": "juice",
            "image": "/static/product/pineapple juice.png"
        },
        {
            "id": 38,
            "title": "Cookies",
            "price": 2.50,
            "description": "A cookies is a small piece of data that a website stores on a user's computer, typically used to remember information about the user or their browsing activity.",
            "category": "cake",
            "image": "/static/product/cookies.png"
        },
        {
            "id": 39,
            "title": "Cake Chocolate",
            "price": 2.50,
            "description": "Chocolate cake is a delicious dessert made from chocolate or cocoa, often enjoyed by both children and adults.",
            "category": "cake",
            "image": "/static/product/cake chocolate.png"
        },
        {
            "id": 40,
            "title": "Cake Strawberry",
            "price": 2.50,
            "description": "Strawberry cake is a cake that uses strawberry as a primary ingredient. Strawberries may be used in the cake batter, atop the cake, and in the frosting.",
            "category": "cake",
            "image": "/static/product/cake strawberry.png"
        },
        {
            "id": 41,
            "title": "Cake Blueberry",
            "price": 2.50,
            "description": "Blueberry cake is easy to put together, has the most moist and tender crumb and is dotted with heaps of juicy blueberries throughout.",
            "category": "cake",
            "image": "/static/product/cake blueberry.png"
        },
        {
            "id": 42,
            "title": "Tiramisu Chocolate",
            "price": 3.00,
            "description": "Chocolate Tiramisu is a decadent layered dessert made up of mascarpone cream, chocolate pastry cream and coffee soaked biscuits.",
            "category": "cake",
            "image": "/static/product/tiramisu chocolate.png"
        },
        {
            "id": 43,
            "title": "Tiramisu Matcha",
            "price": 3.00,
            "description": "Matcha Tiramisu is the perfect fusion no-bake dessert made with layers of rich, velvety matcha mascarpone cream and spongy matcha-soaked ladyfingers.",
            "category": "cake",
            "image": "/static/product/tiramisu matcha.png"
        }

    ]
    return render_template('juice.html', products=products)


@app.get('/cake')
def cake():
    products = [
        {
            "id": 1,
            "title": "Espresso",
            "price": 3.00,
            "description": "Espresso is a concentrated coffee beverage brewed by forcing hot water through finely-ground coffee beans under high pressure.",
            "category": "hot coffee",
            "image": "/static/product/espresso-hot.png"
        },
        {
            "id": 2,
            "title": "Espresso Macchiato",
            "price": 3.75,
            "description": "An espresso macchiato is a strong coffee drink consisting of espresso stained or marked with a small amount of steamed milk foam.",
            "category": "hot coffee",
            "image": "/static/product/espresso-macchiato-hot.png"
        },
        {
            "id": 3,
            "title": "Espresso Con Panna",
            "price": 3.75,
            "description": "Espresso con panna is a simple yet elegant coffee drink consisting of a shot of espresso topped with a dollop of whipped cream.",
            "category": "hot coffee",
            "image": "/static/product/espresso_con_panna_hot.png"
        },
        {
            "id": 4,
            "title": "Americano",
            "price": 3.00,
            "description": "An Americano is a coffee drink made by diluting a shot of espresso with hot water.",
            "category": "hot coffee",
            "image": "/static/product/americano_hot.png"
        },
        {
            "id": 5,
            "title": "Cafe Latte",
            "price": 3.75,
            "description": "A café latte is a coffee drink made with espresso and steamed milk, typically topped with a thin layer of foamed milk.",
            "category": "hot coffee",
            "image": "/static/product/cafe_latte_hot.png"
        },
        {
            "id": 6,
            "title": "Cappuccino",
            "price": 3.50,
            "description": "A cappuccino is a classic coffee drink made with espresso, steamed milk, and foamed milk, typically in equal parts.",
            "category": "hot coffee",
            "image": "/static/product/cappuccino_hot.png"
        },
        {
            "id": 7,
            "title": "Cafe Mocha",
            "price": 3.50,
            "description": "A cafe mocha, also known as caffè mocha or mocha, is a chocolate-flavored warm coffee drink.",
            "category": "hot coffee",
            "image": "/static/product/cafe_mocha_hot.png"
        },
        {
            "id": 8,
            "title": "Caramel Macchiato",
            "price": 4.00,
            "description": "A Caramel Macchiato is a coffee beverage typically consisting of steamed milk, vanilla-flavored syrup, espresso, and a caramel drizzle.",
            "category": "hot coffee",
            "image": "/static/product/caramel_macchiato_hot.png"
        },
        {
            "id": 9,
            "title": "Iced Caramel Cappuccino",
            "price": 4.00,
            "description": "An iced caramel cappuccino is a refreshing coffee beverage that combines the rich flavors of espresso, steamed milk, and caramel, all served cold over ice.",
            "category": "iced coffee",
            "image": "/static/product/iced caramel cappuccino.png"
        },
        {
            "id": 10,
            "title": "Iced Americano",
            "price": 3.25,
            "description": "An Iced Americano is a refreshing coffee drink made by combining espresso with cold water and ice.",
            "category": "iced coffee",
            "image": "/static/product/iced americano.png"
        },
        {
            "id": 11,
            "title": "Iced Latte",
            "price": 4.00,
            "description": "An iced latte is a refreshing, cold coffee drink made with espresso, milk, and ice.",
            "category": "iced coffee",
            "image": "/static/product/iced latte.png"
        },
        {
            "id": 12,
            "title": "Iced Cappuccino",
            "price": 3.75,
            "description": "An iced cappuccino is a refreshing twist on the classic cappuccino, featuring espresso, milk, and a layer of cold, frothy foam, all served over ice.",
            "category": "iced coffee",
            "image": "/static/product/iced cappuccino.png",
        },
        {
            "id": 13,
            "title": "Iced Mocha",
            "price": 3.75,
            "description": "An iced mocha is a cold coffee drink made with espresso, milk, and chocolate syrup, typically served over ice.",
            "category": "iced coffee",
            "image": "/static/product/iced mocha.png"
        },
        {
            "id": 14,
            "title": "Brown Sugar Milk Tea",
            "price": 3.00,
            "description": "Brown sugar milk tea, also known as brown sugar boba or tiger milk tea, is a popular Taiwanese bubble tea drink made with fresh milk, brown sugar syrup, and tapioca pearls.",
            "category": "non coffee",
            "image": "/static/product/brown sugar milk tea.png"
        },
        {
            "id": 15,
            "title": "Milk Tea",
            "price": 3.00,
            "description": "Milk tea is a beverage made by adding milk to brewed tea.",
            "category": "non coffee",
            "image": "/static/product/milk tea.png"
        },
        {
            "id": 16,
            "title": "Green Tea",
            "price": 2.50,
            "description": "Green tea is a type of tea made from the leaves of the Camellia sinensis plant, processed to avoid oxidation or fermentation, thus preserving its green color and a high concentration of beneficial compounds like antioxidants.",
            "category": "non coffee",
            "image": "/static/product/green tea.png"
        },
        {
            "id": 17,
            "title": "Matcha Latte",
            "price": 3.00,
            "description": "A matcha latte is a vibrant green, tea-based beverage made from matcha powder, hot water, and milk (or a milk alternative).",
            "category": "non coffee",
            "image": "/static/product/matcha latte.png"
        },
        {
            "id": 18,
            "title": "Iced Chocolate",
            "price": 2.50,
            "description": "An iced chocolate is a chilled chocolate beverage, often described as a richer, more decadent version of chocolate milk, typically served over ice.",
            "category": "non coffee",
            "image": "/static/product/iced chocolate.png"
        },
        {
            "id": 19,
            "title": "Iced Coconut Water Matcha Cream",
            "price": 2.00,
            "description": "Coconut matcha cream refers to a beverage or dessert that combines the earthy flavor of matcha green tea with the creamy and slightly sweet taste of coconut.",
            "category": "non coffee",
            "image": "/static/product/coconut matcha.png"
        },
        {
            "id": 20,
            "title": "Iced Blue Milk",
            "price": 2.00,
            "description": "Iced Blue Latte is a refreshing and visually stunning drink that's perfect for hot summer days.",
            "category": "non coffee",
            "image": "/static/product/iced blue milk.png"
        },
        {
            "id": 21,
            "title": "Iced Strawberry Milk",
            "price": 2.00,
            "description": "Iced strawberry milk is a refreshing beverage made with milk and strawberries, often featuring a combination of sweet and creamy flavors.",
            "category": "non coffee",
            "image": "/static/product/iced strawberry milk.png"
        },
        {
            "id": 22,
            "title": "Matcha Frappe",
            "price": 2.50,
            "description": "A matcha frappe is a blended, iced beverage typically made with matcha green tea powder, milk, sweetener, and ice, often topped with whipped cream.",
            "category": "frappe",
            "image": "/static/product/matcha frappe.png"
        },
        {
            "id": 23,
            "title": "Strawberry Frappe",
            "price": 2.50,
            "description": "A strawberry frappe is a blended, chilled beverage featuring the sweet and refreshing taste of strawberries.",
            "category": "frappe",
            "image": "/static/product/strawberry frappe.png"
        },
        {
            "id": 24,
            "title": "Blueberry Frappe",
            "price": 2.50,
            "description": "A blueberry frappe is a blended iced drink, often featuring the sweet and tangy taste of blueberries, combined with a creamy base like milk or yogurt, and often includes ice for a refreshing, slushy texture.",
            "category": "frappe",
            "image": "/static/product/blueberry frappe.png"
        },
        {
            "id": 25,
            "title": "chocolate frappe",
            "price": 2.50,
            "description": "A chocolate frappe is a blended iced coffee drink, typically made with chocolate, ice, milk, and often flavored with chocolate syrup or sauce.",
            "category": "frappe",
            "image": "/static/product/chocolate frappe.png"
        },
        {
            "id": 26,
            "title": "Caramel frappe",
            "price": 2.50,
            "description": "A caramel frappé is a blended iced coffee drink known for its creamy, sweet, and cool caramel flavor.",
            "category": "frappe",
            "image": "/static/product/caramel frappe.png"
        },
        {
            "id": 27,
            "title": "Vanilla frappe",
            "price": 2.50,
            "description": "A vanilla frappe is a blended iced drink, typically featuring a creamy, vanilla-flavored base, often made with milk, ice, and vanilla extract or vanilla bean.",
            "category": "frappe",
            "image": "/static/product/vanilla frappe.png"
        },
        {
            "id": 28,
            "title": "Mocha Frappe",
            "price": 2.50,
            "description": "A Mocha Frappe is a blended, iced coffee drink that combines chocolate and coffee flavors.",
            "category": "frappe",
            "image": "/static/product/mocha frappe.png"
        },
        {
            "id": 29,
            "title": "Strawberry Soda",
            "price": 2.50,
            "description": "Strawberry Soda will delight your taste buds and quench your warm-weather thirst with the natural flavor of fresh strawberries.",
            "category": "soda",
            "image": "/static/product/strawberry soda.png"
        },
        {
            "id": 30,
            "title": "Blue Hawaii Soda",
            "price": 2.50,
            "description": "Blue Hawaiian is a cocktail and a soda flavor known for its tropical taste and vibrant blue color.",
            "category": "soda",
            "image": "/static/product/blue hawaii soda.png"
        },
        {
            "id": 31,
            "title": "Lemon Soda",
            "price": 2.50,
            "description": "Lemon soda is a refreshing, carbonated beverage typically made with lemon juice, sugar (or another sweetener), and soda water.",
            "category": "soda",
            "image": "/static/product/lemon soda.png"
        },
        {
            "id": 32,
            "title": "Watermelon Soda",
            "price": 2.50,
            "description": "Watermelon soda is a refreshing, sweet, and bubbly beverage that captures the flavor of watermelon in a fizzy drink.",
            "category": "soda",
            "image": "/static/product/watermelon soda.png"
        },
        {
            "id": 33,
            "title": "Orange Juice",
            "price": 2.00,
            "description": "Orange juice is a refreshing beverage made from the liquid extracted from oranges.",
            "category": "juice",
            "image": "/static/product/orange juice.png"
        },
        {
            "id": 34,
            "title": "Strawberry Juice",
            "price": 2.00,
            "description": "Strawberry Juice is a refreshing fresh fruit juice that is full of vitamin C and antioxidants and lot of invigorating flavor.",
            "category": "juice",
            "image": "/static/product/strawberry juice.png"
        },
        {
            "id": 35,
            "title": "watermelon juice",
            "price": 2.00,
            "description": "Watermelon juice is so simple to make with a blender. Refreshingly sweet and hydrating, it's perfect for a hot summer day.",
            "category": "juice",
            "image": "/static/product/watermelon juice.png"
        },
        {
            "id": 36,
            "title": "Apple Juice",
            "price": 2.00,
            "description": "Apple juice is a refreshing beverage made from the pressed and filtered juice of apples.",
            "category": "juice",
            "image": "/static/product/apple juice.png"
        },
        {
            "id": 37,
            "title": "Pineapple Juice",
            "price": 2.00,
            "description": "Pineapple juice is a sweet and tangy tropical beverage made from the juice extracted from fresh or canned pineapples.",
            "category": "juice",
            "image": "/static/product/pineapple juice.png"
        },
        {
            "id": 38,
            "title": "Cookies",
            "price": 2.50,
            "description": "A cookies is a small piece of data that a website stores on a user's computer, typically used to remember information about the user or their browsing activity.",
            "category": "cake",
            "image": "/static/product/cookies.png"
        },
        {
            "id": 39,
            "title": "Cake Chocolate",
            "price": 2.50,
            "description": "Chocolate cake is a delicious dessert made from chocolate or cocoa, often enjoyed by both children and adults.",
            "category": "cake",
            "image": "/static/product/cake chocolate.png"
        },
        {
            "id": 40,
            "title": "Cake Strawberry",
            "price": 2.50,
            "description": "Strawberry cake is a cake that uses strawberry as a primary ingredient. Strawberries may be used in the cake batter, atop the cake, and in the frosting.",
            "category": "cake",
            "image": "/static/product/cake strawberry.png"
        },
        {
            "id": 41,
            "title": "Cake Blueberry",
            "price": 2.50,
            "description": "Blueberry cake is easy to put together, has the most moist and tender crumb and is dotted with heaps of juicy blueberries throughout.",
            "category": "cake",
            "image": "/static/product/cake blueberry.png"
        },
        {
            "id": 42,
            "title": "Tiramisu Chocolate",
            "price": 3.00,
            "description": "Chocolate Tiramisu is a decadent layered dessert made up of mascarpone cream, chocolate pastry cream and coffee soaked biscuits.",
            "category": "cake",
            "image": "/static/product/tiramisu chocolate.png"
        },
        {
            "id": 43,
            "title": "Tiramisu Matcha",
            "price": 3.00,
            "description": "Matcha Tiramisu is the perfect fusion no-bake dessert made with layers of rich, velvety matcha mascarpone cream and spongy matcha-soaked ladyfingers.",
            "category": "cake",
            "image": "/static/product/tiramisu matcha.png"
        }

    ]
    return render_template('cake.html', products=products)


@app.get('/product')
def product():
    products = [
        {
            "id": 1,
            "title": "Espresso",
            "price": 3.00,
            "description": "Espresso is a concentrated coffee beverage brewed by forcing hot water through finely-ground coffee beans under high pressure.",
            "category": "hot coffee",
            "image": "/static/product/espresso-hot.png"
        },
        {
            "id": 2,
            "title": "Espresso Macchiato",
            "price": 3.75,
            "description": "An espresso macchiato is a strong coffee drink consisting of espresso stained or marked with a small amount of steamed milk foam.",
            "category": "hot coffee",
            "image": "/static/product/espresso-macchiato-hot.png"
        },
        {
            "id": 3,
            "title": "Espresso Con Panna",
            "price": 3.75,
            "description": "Espresso con panna is a simple yet elegant coffee drink consisting of a shot of espresso topped with a dollop of whipped cream.",
            "category": "hot coffee",
            "image": "/static/product/espresso_con_panna_hot.png"
        },
        {
            "id": 4,
            "title": "Americano",
            "price": 3.00,
            "description": "An Americano is a coffee drink made by diluting a shot of espresso with hot water.",
            "category": "hot coffee",
            "image": "/static/product/americano_hot.png"
        },
        {
            "id": 5,
            "title": "Cafe Latte",
            "price": 3.75,
            "description": "A café latte is a coffee drink made with espresso and steamed milk, typically topped with a thin layer of foamed milk.",
            "category": "hot coffee",
            "image": "/static/product/cafe_latte_hot.png"
        },
        {
            "id": 6,
            "title": "Cappuccino",
            "price": 3.50,
            "description": "A cappuccino is a classic coffee drink made with espresso, steamed milk, and foamed milk, typically in equal parts.",
            "category": "hot coffee",
            "image": "/static/product/cappuccino_hot.png"
        },
        {
            "id": 7,
            "title": "Cafe Mocha",
            "price": 3.50,
            "description": "A cafe mocha, also known as caffè mocha or mocha, is a chocolate-flavored warm coffee drink.",
            "category": "hot coffee",
            "image": "/static/product/cafe_mocha_hot.png"
        },
        {
            "id": 8,
            "title": "Caramel Macchiato",
            "price": 4.00,
            "description": "A Caramel Macchiato is a coffee beverage typically consisting of steamed milk, vanilla-flavored syrup, espresso, and a caramel drizzle.",
            "category": "hot coffee",
            "image": "/static/product/caramel_macchiato_hot.png"
        },
        {
            "id": 9,
            "title": "Iced Caramel Cappuccino",
            "price": 4.00,
            "description": "An iced caramel cappuccino is a refreshing coffee beverage that combines the rich flavors of espresso, steamed milk, and caramel, all served cold over ice.",
            "category": "iced coffee",
            "image": "/static/product/iced caramel cappuccino.png"
        },
        {
            "id": 10,
            "title": "Iced Americano",
            "price": 3.25,
            "description": "An Iced Americano is a refreshing coffee drink made by combining espresso with cold water and ice.",
            "category": "iced coffee",
            "image": "/static/product/iced americano.png"
        },
        {
            "id": 11,
            "title": "Iced Latte",
            "price": 4.00,
            "description": "An iced latte is a refreshing, cold coffee drink made with espresso, milk, and ice.",
            "category": "iced coffee",
            "image": "/static/product/iced latte.png"
        },
        {
            "id": 12,
            "title": "Iced Cappuccino",
            "price": 3.75,
            "description": "An iced cappuccino is a refreshing twist on the classic cappuccino, featuring espresso, milk, and a layer of cold, frothy foam, all served over ice.",
            "category": "iced coffee",
            "image": "/static/product/iced cappuccino.png",
        },
        {
            "id": 13,
            "title": "Iced Mocha",
            "price": 3.75,
            "description": "An iced mocha is a cold coffee drink made with espresso, milk, and chocolate syrup, typically served over ice.",
            "category": "iced coffee",
            "image": "/static/product/iced mocha.png"
        },
        {
            "id": 14,
            "title": "Brown Sugar Milk Tea",
            "price": 3.00,
            "description": "Brown sugar milk tea, also known as brown sugar boba or tiger milk tea, is a popular Taiwanese bubble tea drink made with fresh milk, brown sugar syrup, and tapioca pearls.",
            "category": "non coffee",
            "image": "/static/product/brown sugar milk tea.png"
        },
        {
            "id": 15,
            "title": "Milk Tea",
            "price": 3.00,
            "description": "Milk tea is a beverage made by adding milk to brewed tea.",
            "category": "non coffee",
            "image": "/static/product/milk tea.png"
        },
        {
            "id": 16,
            "title": "Green Tea",
            "price": 2.50,
            "description": "Green tea is a type of tea made from the leaves of the Camellia sinensis plant, processed to avoid oxidation or fermentation, thus preserving its green color and a high concentration of beneficial compounds like antioxidants.",
            "category": "non coffee",
            "image": "/static/product/green tea.png"
        },
        {
            "id": 17,
            "title": "Matcha Latte",
            "price": 3.00,
            "description": "A matcha latte is a vibrant green, tea-based beverage made from matcha powder, hot water, and milk (or a milk alternative).",
            "category": "non coffee",
            "image": "/static/product/matcha latte.png"
        },
        {
            "id": 18,
            "title": "Iced Chocolate",
            "price": 2.50,
            "description": "An iced chocolate is a chilled chocolate beverage, often described as a richer, more decadent version of chocolate milk, typically served over ice.",
            "category": "non coffee",
            "image": "/static/product/iced chocolate.png"
        },
        {
            "id": 19,
            "title": "Iced Coconut Water Matcha Cream",
            "price": 2.00,
            "description": "Coconut matcha cream refers to a beverage or dessert that combines the earthy flavor of matcha green tea with the creamy and slightly sweet taste of coconut.",
            "category": "non coffee",
            "image": "/static/product/coconut matcha.png"
        },
        {
            "id": 20,
            "title": "Iced Blue Milk",
            "price": 2.00,
            "description": "Iced Blue Latte is a refreshing and visually stunning drink that's perfect for hot summer days.",
            "category": "non coffee",
            "image": "/static/product/iced blue milk.png"
        },
        {
            "id": 21,
            "title": "Iced Strawberry Milk",
            "price": 2.00,
            "description": "Iced strawberry milk is a refreshing beverage made with milk and strawberries, often featuring a combination of sweet and creamy flavors.",
            "category": "non coffee",
            "image": "/static/product/iced strawberry milk.png"
        },
        {
            "id": 22,
            "title": "Matcha Frappe",
            "price": 2.50,
            "description": "A matcha frappe is a blended, iced beverage typically made with matcha green tea powder, milk, sweetener, and ice, often topped with whipped cream.",
            "category": "frappe",
            "image": "/static/product/matcha frappe.png"
        },
        {
            "id": 23,
            "title": "Strawberry Frappe",
            "price": 2.50,
            "description": "A strawberry frappe is a blended, chilled beverage featuring the sweet and refreshing taste of strawberries.",
            "category": "frappe",
            "image": "/static/product/strawberry frappe.png"
        },
        {
            "id": 24,
            "title": "Blueberry Frappe",
            "price": 2.50,
            "description": "A blueberry frappe is a blended iced drink, often featuring the sweet and tangy taste of blueberries, combined with a creamy base like milk or yogurt, and often includes ice for a refreshing, slushy texture.",
            "category": "frappe",
            "image": "/static/product/blueberry frappe.png"
        },
        {
            "id": 25,
            "title": "chocolate frappe",
            "price": 2.50,
            "description": "A chocolate frappe is a blended iced coffee drink, typically made with chocolate, ice, milk, and often flavored with chocolate syrup or sauce.",
            "category": "frappe",
            "image": "/static/product/chocolate frappe.png"
        },
        {
            "id": 26,
            "title": "Caramel frappe",
            "price": 2.50,
            "description": "A caramel frappé is a blended iced coffee drink known for its creamy, sweet, and cool caramel flavor.",
            "category": "frappe",
            "image": "/static/product/caramel frappe.png"
        },
        {
            "id": 27,
            "title": "Vanilla frappe",
            "price": 2.50,
            "description": "A vanilla frappe is a blended iced drink, typically featuring a creamy, vanilla-flavored base, often made with milk, ice, and vanilla extract or vanilla bean.",
            "category": "frappe",
            "image": "/static/product/vanilla frappe.png"
        },
        {
            "id": 28,
            "title": "Mocha Frappe",
            "price": 2.50,
            "description": "A Mocha Frappe is a blended, iced coffee drink that combines chocolate and coffee flavors.",
            "category": "frappe",
            "image": "/static/product/mocha frappe.png"
        },
        {
            "id": 29,
            "title": "Strawberry Soda",
            "price": 2.50,
            "description": "Strawberry Soda will delight your taste buds and quench your warm-weather thirst with the natural flavor of fresh strawberries.",
            "category": "soda",
            "image": "/static/product/strawberry soda.png"
        },
        {
            "id": 30,
            "title": "Blue Hawaii Soda",
            "price": 2.50,
            "description": "Blue Hawaiian is a cocktail and a soda flavor known for its tropical taste and vibrant blue color.",
            "category": "soda",
            "image": "/static/product/blue hawaii soda.png"
        },
        {
            "id": 31,
            "title": "Lemon Soda",
            "price": 2.50,
            "description": "Lemon soda is a refreshing, carbonated beverage typically made with lemon juice, sugar (or another sweetener), and soda water.",
            "category": "soda",
            "image": "/static/product/lemon soda.png"
        },
        {
            "id": 32,
            "title": "Watermelon Soda",
            "price": 2.50,
            "description": "Watermelon soda is a refreshing, sweet, and bubbly beverage that captures the flavor of watermelon in a fizzy drink.",
            "category": "soda",
            "image": "/static/product/watermelon soda.png"
        },
        {
            "id": 33,
            "title": "Orange Juice",
            "price": 2.00,
            "description": "Orange juice is a refreshing beverage made from the liquid extracted from oranges.",
            "category": "juice",
            "image": "/static/product/orange juice.png"
        },
        {
            "id": 34,
            "title": "Strawberry Juice",
            "price": 2.00,
            "description": "Strawberry Juice is a refreshing fresh fruit juice that is full of vitamin C and antioxidants and lot of invigorating flavor.",
            "category": "juice",
            "image": "/static/product/strawberry juice.png"
        },
        {
            "id": 35,
            "title": "watermelon juice",
            "price": 2.00,
            "description": "Watermelon juice is so simple to make with a blender. Refreshingly sweet and hydrating, it's perfect for a hot summer day.",
            "category": "juice",
            "image": "/static/product/watermelon juice.png"
        },
        {
            "id": 36,
            "title": "Apple Juice",
            "price": 2.00,
            "description": "Apple juice is a refreshing beverage made from the pressed and filtered juice of apples.",
            "category": "juice",
            "image": "/static/product/apple juice.png"
        },
        {
            "id": 37,
            "title": "Pineapple Juice",
            "price": 2.00,
            "description": "Pineapple juice is a sweet and tangy tropical beverage made from the juice extracted from fresh or canned pineapples.",
            "category": "juice",
            "image": "/static/product/pineapple juice.png"
        },
        {
            "id": 38,
            "title": "Cookies",
            "price": 2.50,
            "description": "A cookies is a small piece of data that a website stores on a user's computer, typically used to remember information about the user or their browsing activity.",
            "category": "cake",
            "image": "/static/product/cookies.png"
        },
        {
            "id": 39,
            "title": "Cake Chocolate",
            "price": 2.50,
            "description": "Chocolate cake is a delicious dessert made from chocolate or cocoa, often enjoyed by both children and adults.",
            "category": "cake",
            "image": "/static/product/cake chocolate.png"
        },
        {
            "id": 40,
            "title": "Cake Strawberry",
            "price": 2.50,
            "description": "Strawberry cake is a cake that uses strawberry as a primary ingredient. Strawberries may be used in the cake batter, atop the cake, and in the frosting.",
            "category": "cake",
            "image": "/static/product/cake strawberry.png"
        },
        {
            "id": 41,
            "title": "Cake Blueberry",
            "price": 2.50,
            "description": "Blueberry cake is easy to put together, has the most moist and tender crumb and is dotted with heaps of juicy blueberries throughout.",
            "category": "cake",
            "image": "/static/product/cake blueberry.png"
        },
        {
            "id": 42,
            "title": "Tiramisu Chocolate",
            "price": 3.00,
            "description": "Chocolate Tiramisu is a decadent layered dessert made up of mascarpone cream, chocolate pastry cream and coffee soaked biscuits.",
            "category": "cake",
            "image": "/static/product/tiramisu chocolate.png"
        },
        {
            "id": 43,
            "title": "Tiramisu Matcha",
            "price": 3.00,
            "description": "Matcha Tiramisu is the perfect fusion no-bake dessert made with layers of rich, velvety matcha mascarpone cream and spongy matcha-soaked ladyfingers.",
            "category": "cake",
            "image": "/static/product/tiramisu matcha.png"
        }

    ]
    return render_template('product.html', products=products)


@app.route('/product/<int:product_id>')
def product_detail(product_id):
    products = [
        {
            "id": 1,
            "title": "Espresso",
            "price": 3.00,
            "description": "Espresso is a concentrated coffee beverage brewed by forcing hot water through finely-ground coffee beans under high pressure.",
            "category": "hot coffee",
            "image": "/static/product/espresso-hot.png"
        },
        {
            "id": 2,
            "title": "Espresso Macchiato",
            "price": 3.75,
            "description": "An espresso macchiato is a strong coffee drink consisting of espresso stained or marked with a small amount of steamed milk foam.",
            "category": "hot coffee",
            "image": "/static/product/espresso-macchiato-hot.png"
        },
        {
            "id": 3,
            "title": "Espresso Con Panna",
            "price": 3.75,
            "description": "Espresso con panna is a simple yet elegant coffee drink consisting of a shot of espresso topped with a dollop of whipped cream.",
            "category": "hot coffee",
            "image": "/static/product/espresso_con_panna_hot.png"
        },
        {
            "id": 4,
            "title": "Americano",
            "price": 3.00,
            "description": "An Americano is a coffee drink made by diluting a shot of espresso with hot water.",
            "category": "hot coffee",
            "image": "/static/product/americano_hot.png"
        },
        {
            "id": 5,
            "title": "Cafe Latte",
            "price": 3.75,
            "description": "A café latte is a coffee drink made with espresso and steamed milk, typically topped with a thin layer of foamed milk.",
            "category": "hot coffee",
            "image": "/static/product/cafe_latte_hot.png"
        },
        {
            "id": 6,
            "title": "Cappuccino",
            "price": 3.50,
            "description": "A cappuccino is a classic coffee drink made with espresso, steamed milk, and foamed milk, typically in equal parts.",
            "category": "hot coffee",
            "image": "/static/product/cappuccino_hot.png"
        },
        {
            "id": 7,
            "title": "Cafe Mocha",
            "price": 3.50,
            "description": "A cafe mocha, also known as caffè mocha or mocha, is a chocolate-flavored warm coffee drink.",
            "category": "hot coffee",
            "image": "/static/product/cafe_mocha_hot.png"
        },
        {
            "id": 8,
            "title": "Caramel Macchiato",
            "price": 4.00,
            "description": "A Caramel Macchiato is a coffee beverage typically consisting of steamed milk, vanilla-flavored syrup, espresso, and a caramel drizzle.",
            "category": "hot coffee",
            "image": "/static/product/caramel_macchiato_hot.png"
        },
        {
            "id": 9,
            "title": "Iced Caramel Cappuccino",
            "price": 4.00,
            "description": "An iced caramel cappuccino is a refreshing coffee beverage that combines the rich flavors of espresso, steamed milk, and caramel, all served cold over ice.",
            "category": "iced coffee",
            "image": "/static/product/iced caramel cappuccino.png"
        },
        {
            "id": 10,
            "title": "Iced Americano",
            "price": 3.25,
            "description": "An Iced Americano is a refreshing coffee drink made by combining espresso with cold water and ice.",
            "category": "iced coffee",
            "image": "/static/product/iced americano.png"
        },
        {
            "id": 11,
            "title": "Iced Latte",
            "price": 4.00,
            "description": "An iced latte is a refreshing, cold coffee drink made with espresso, milk, and ice.",
            "category": "iced coffee",
            "image": "/static/product/iced latte.png"
        },
        {
            "id": 12,
            "title": "Iced Cappuccino",
            "price": 3.75,
            "description": "An iced cappuccino is a refreshing twist on the classic cappuccino, featuring espresso, milk, and a layer of cold, frothy foam, all served over ice.",
            "category": "iced coffee",
            "image": "/static/product/iced cappuccino.png",
        },
        {
            "id": 13,
            "title": "Iced Mocha",
            "price": 3.75,
            "description": "An iced mocha is a cold coffee drink made with espresso, milk, and chocolate syrup, typically served over ice.",
            "category": "iced coffee",
            "image": "/static/product/iced mocha.png"
        },
        {
            "id": 14,
            "title": "Brown Sugar Milk Tea",
            "price": 3.00,
            "description": "Brown sugar milk tea, also known as brown sugar boba or tiger milk tea, is a popular Taiwanese bubble tea drink made with fresh milk, brown sugar syrup, and tapioca pearls.",
            "category": "non coffee",
            "image": "/static/product/brown sugar milk tea.png"
        },
        {
            "id": 15,
            "title": "Milk Tea",
            "price": 3.00,
            "description": "Milk tea is a beverage made by adding milk to brewed tea.",
            "category": "non coffee",
            "image": "/static/product/milk tea.png"
        },
        {
            "id": 16,
            "title": "Green Tea",
            "price": 2.50,
            "description": "Green tea is a type of tea made from the leaves of the Camellia sinensis plant, processed to avoid oxidation or fermentation, thus preserving its green color and a high concentration of beneficial compounds like antioxidants.",
            "category": "non coffee",
            "image": "/static/product/green tea.png"
        },
        {
            "id": 17,
            "title": "Matcha Latte",
            "price": 3.00,
            "description": "A matcha latte is a vibrant green, tea-based beverage made from matcha powder, hot water, and milk (or a milk alternative).",
            "category": "non coffee",
            "image": "/static/product/matcha latte.png"
        },
        {
            "id": 18,
            "title": "Iced Chocolate",
            "price": 2.50,
            "description": "An iced chocolate is a chilled chocolate beverage, often described as a richer, more decadent version of chocolate milk, typically served over ice.",
            "category": "non coffee",
            "image": "/static/product/iced chocolate.png"
        },
        {
            "id": 19,
            "title": "Iced Coconut Water Matcha Cream",
            "price": 2.00,
            "description": "Coconut matcha cream refers to a beverage or dessert that combines the earthy flavor of matcha green tea with the creamy and slightly sweet taste of coconut.",
            "category": "non coffee",
            "image": "/static/product/coconut matcha.png"
        },
        {
            "id": 20,
            "title": "Iced Blue Milk",
            "price": 2.00,
            "description": "Iced Blue Latte is a refreshing and visually stunning drink that's perfect for hot summer days.",
            "category": "non coffee",
            "image": "/static/product/iced blue milk.png"
        },
        {
            "id": 21,
            "title": "Iced Strawberry Milk",
            "price": 2.00,
            "description": "Iced strawberry milk is a refreshing beverage made with milk and strawberries, often featuring a combination of sweet and creamy flavors.",
            "category": "non coffee",
            "image": "/static/product/iced strawberry milk.png"
        },
        {
            "id": 22,
            "title": "Matcha Frappe",
            "price": 2.50,
            "description": "A matcha frappe is a blended, iced beverage typically made with matcha green tea powder, milk, sweetener, and ice, often topped with whipped cream.",
            "category": "frappe",
            "image": "/static/product/matcha frappe.png"
        },
        {
            "id": 23,
            "title": "Strawberry Frappe",
            "price": 2.50,
            "description": "A strawberry frappe is a blended, chilled beverage featuring the sweet and refreshing taste of strawberries.",
            "category": "frappe",
            "image": "/static/product/strawberry frappe.png"
        },
        {
            "id": 24,
            "title": "Blueberry Frappe",
            "price": 2.50,
            "description": "A blueberry frappe is a blended iced drink, often featuring the sweet and tangy taste of blueberries, combined with a creamy base like milk or yogurt, and often includes ice for a refreshing, slushy texture.",
            "category": "frappe",
            "image": "/static/product/blueberry frappe.png"
        },
        {
            "id": 25,
            "title": "chocolate frappe",
            "price": 2.50,
            "description": "A chocolate frappe is a blended iced coffee drink, typically made with chocolate, ice, milk, and often flavored with chocolate syrup or sauce.",
            "category": "frappe",
            "image": "/static/product/chocolate frappe.png"
        },
        {
            "id": 26,
            "title": "Caramel frappe",
            "price": 2.50,
            "description": "A caramel frappé is a blended iced coffee drink known for its creamy, sweet, and cool caramel flavor.",
            "category": "frappe",
            "image": "/static/product/caramel frappe.png"
        },
        {
            "id": 27,
            "title": "Vanilla frappe",
            "price": 2.50,
            "description": "A vanilla frappe is a blended iced drink, typically featuring a creamy, vanilla-flavored base, often made with milk, ice, and vanilla extract or vanilla bean.",
            "category": "frappe",
            "image": "/static/product/vanilla frappe.png"
        },
        {
            "id": 28,
            "title": "Mocha Frappe",
            "price": 2.50,
            "description": "A Mocha Frappe is a blended, iced coffee drink that combines chocolate and coffee flavors.",
            "category": "frappe",
            "image": "/static/product/mocha frappe.png"
        },
        {
            "id": 29,
            "title": "Strawberry Soda",
            "price": 2.50,
            "description": "Strawberry Soda will delight your taste buds and quench your warm-weather thirst with the natural flavor of fresh strawberries.",
            "category": "soda",
            "image": "/static/product/strawberry soda.png"
        },
        {
            "id": 30,
            "title": "Blue Hawaii Soda",
            "price": 2.50,
            "description": "Blue Hawaiian is a cocktail and a soda flavor known for its tropical taste and vibrant blue color.",
            "category": "soda",
            "image": "/static/product/blue hawaii soda.png"
        },
        {
            "id": 31,
            "title": "Lemon Soda",
            "price": 2.50,
            "description": "Lemon soda is a refreshing, carbonated beverage typically made with lemon juice, sugar (or another sweetener), and soda water.",
            "category": "soda",
            "image": "/static/product/lemon soda.png"
        },
        {
            "id": 32,
            "title": "Watermelon Soda",
            "price": 2.50,
            "description": "Watermelon soda is a refreshing, sweet, and bubbly beverage that captures the flavor of watermelon in a fizzy drink.",
            "category": "soda",
            "image": "/static/product/watermelon soda.png"
        },
        {
            "id": 33,
            "title": "Orange Juice",
            "price": 2.00,
            "description": "Orange juice is a refreshing beverage made from the liquid extracted from oranges.",
            "category": "juice",
            "image": "/static/product/orange juice.png"
        },
        {
            "id": 34,
            "title": "Strawberry Juice",
            "price": 2.00,
            "description": "Strawberry Juice is a refreshing fresh fruit juice that is full of vitamin C and antioxidants and lot of invigorating flavor.",
            "category": "juice",
            "image": "/static/product/strawberry juice.png"
        },
        {
            "id": 35,
            "title": "watermelon juice",
            "price": 2.00,
            "description": "Watermelon juice is so simple to make with a blender. Refreshingly sweet and hydrating, it's perfect for a hot summer day.",
            "category": "juice",
            "image": "/static/product/watermelon juice.png"
        },
        {
            "id": 36,
            "title": "Apple Juice",
            "price": 2.00,
            "description": "Apple juice is a refreshing beverage made from the pressed and filtered juice of apples.",
            "category": "juice",
            "image": "/static/product/apple juice.png"
        },
        {
            "id": 37,
            "title": "Pineapple Juice",
            "price": 2.00,
            "description": "Pineapple juice is a sweet and tangy tropical beverage made from the juice extracted from fresh or canned pineapples.",
            "category": "juice",
            "image": "/static/product/pineapple juice.png"
        },
        {
            "id": 38,
            "title": "Cookies",
            "price": 2.50,
            "description": "A cookies is a small piece of data that a website stores on a user's computer, typically used to remember information about the user or their browsing activity.",
            "category": "cake",
            "image": "/static/product/cookies.png"
        },
        {
            "id": 39,
            "title": "Cake Chocolate",
            "price": 2.50,
            "description": "Chocolate cake is a delicious dessert made from chocolate or cocoa, often enjoyed by both children and adults.",
            "category": "cake",
            "image": "/static/product/cake chocolate.png"
        },
        {
            "id": 40,
            "title": "Cake Strawberry",
            "price": 2.50,
            "description": "Strawberry cake is a cake that uses strawberry as a primary ingredient. Strawberries may be used in the cake batter, atop the cake, and in the frosting.",
            "category": "cake",
            "image": "/static/product/cake strawberry.png"
        },
        {
            "id": 41,
            "title": "Cake Blueberry",
            "price": 2.50,
            "description": "Blueberry cake is easy to put together, has the most moist and tender crumb and is dotted with heaps of juicy blueberries throughout.",
            "category": "cake",
            "image": "/static/product/cake blueberry.png"
        },
        {
            "id": 42,
            "title": "Tiramisu Chocolate",
            "price": 3.00,
            "description": "Chocolate Tiramisu is a decadent layered dessert made up of mascarpone cream, chocolate pastry cream and coffee soaked biscuits.",
            "category": "cake",
            "image": "/static/product/tiramisu chocolate.png"
        },
        {
            "id": 43,
            "title": "Tiramisu Matcha",
            "price": 3.00,
            "description": "Matcha Tiramisu is the perfect fusion no-bake dessert made with layers of rich, velvety matcha mascarpone cream and spongy matcha-soaked ladyfingers.",
            "category": "cake",
            "image": "/static/product/tiramisu matcha.png"
        }

    ]
    products = next((p for p in products if p['id'] == product_id), None)
    # if not product:
    #     # return "Product not found", 404
    return render_template('product.html', product=products)


@app.route('/')
def index():
    return render_template("check.html")


@app.route('/master')
def master():
    return render_template("master.html")


@app.route('/receipt')
def receipt():
    return render_template("thank.html")


@app.route("/cart")
def cart():
    cart_items = [
        {"product": "Product A", "qty": 2, "price": 10.00},
        {"product": "Product B", "qty": 1, "price": 15.00}
    ]
    return render_template("cart_list.html", cart_items=cart_items)


@app.route('/send_email', methods=['POST', 'GET'])
def send_email_route():
    products = [
        {
            "id": 1,
            "title": "Espresso",
            "price": 3.00,
            "description": "Espresso is a concentrated coffee beverage brewed by forcing hot water through finely-ground coffee beans under high pressure.",
            "category": "hot coffee",
            "image": "/static/product/espresso-hot.png"
        },
        {
            "id": 2,
            "title": "Espresso Macchiato",
            "price": 3.75,
            "description": "An espresso macchiato is a strong coffee drink consisting of espresso stained or marked with a small amount of steamed milk foam.",
            "category": "hot coffee",
            "image": "/static/product/espresso-macchiato-hot.png"
        },
        {
            "id": 3,
            "title": "Espresso Con Panna",
            "price": 3.75,
            "description": "Espresso con panna is a simple yet elegant coffee drink consisting of a shot of espresso topped with a dollop of whipped cream.",
            "category": "hot coffee",
            "image": "/static/product/espresso_con_panna_hot.png"
        },
        {
            "id": 4,
            "title": "Americano",
            "price": 3.00,
            "description": "An Americano is a coffee drink made by diluting a shot of espresso with hot water.",
            "category": "hot coffee",
            "image": "/static/product/americano_hot.png"
        },
        {
            "id": 5,
            "title": "Cafe Latte",
            "price": 3.75,
            "description": "A café latte is a coffee drink made with espresso and steamed milk, typically topped with a thin layer of foamed milk.",
            "category": "hot coffee",
            "image": "/static/product/cafe_latte_hot.png"
        },
        {
            "id": 6,
            "title": "Cappuccino",
            "price": 3.50,
            "description": "A cappuccino is a classic coffee drink made with espresso, steamed milk, and foamed milk, typically in equal parts.",
            "category": "hot coffee",
            "image": "/static/product/cappuccino_hot.png"
        },
        {
            "id": 7,
            "title": "Cafe Mocha",
            "price": 3.50,
            "description": "A cafe mocha, also known as caffè mocha or mocha, is a chocolate-flavored warm coffee drink.",
            "category": "hot coffee",
            "image": "/static/product/cafe_mocha_hot.png"
        },
        {
            "id": 8,
            "title": "Caramel Macchiato",
            "price": 4.00,
            "description": "A Caramel Macchiato is a coffee beverage typically consisting of steamed milk, vanilla-flavored syrup, espresso, and a caramel drizzle.",
            "category": "hot coffee",
            "image": "/static/product/caramel_macchiato_hot.png"
        },
        {
            "id": 9,
            "title": "Iced Caramel Cappuccino",
            "price": 4.00,
            "description": "An iced caramel cappuccino is a refreshing coffee beverage that combines the rich flavors of espresso, steamed milk, and caramel, all served cold over ice.",
            "category": "iced coffee",
            "image": "/static/product/iced caramel cappuccino.png"
        },
        {
            "id": 10,
            "title": "Iced Americano",
            "price": 3.25,
            "description": "An Iced Americano is a refreshing coffee drink made by combining espresso with cold water and ice.",
            "category": "iced coffee",
            "image": "/static/product/iced americano.png"
        },
        {
            "id": 11,
            "title": "Iced Latte",
            "price": 4.00,
            "description": "An iced latte is a refreshing, cold coffee drink made with espresso, milk, and ice.",
            "category": "iced coffee",
            "image": "/static/product/iced latte.png"
        },
        {
            "id": 12,
            "title": "Iced Cappuccino",
            "price": 3.75,
            "description": "An iced cappuccino is a refreshing twist on the classic cappuccino, featuring espresso, milk, and a layer of cold, frothy foam, all served over ice.",
            "category": "iced coffee",
            "image": "/static/product/iced cappuccino.png",
        },
        {
            "id": 13,
            "title": "Iced Mocha",
            "price": 3.75,
            "description": "An iced mocha is a cold coffee drink made with espresso, milk, and chocolate syrup, typically served over ice.",
            "category": "iced coffee",
            "image": "/static/product/iced mocha.png"
        },
        {
            "id": 14,
            "title": "Brown Sugar Milk Tea",
            "price": 3.00,
            "description": "Brown sugar milk tea, also known as brown sugar boba or tiger milk tea, is a popular Taiwanese bubble tea drink made with fresh milk, brown sugar syrup, and tapioca pearls.",
            "category": "non coffee",
            "image": "/static/product/brown sugar milk tea.png"
        },
        {
            "id": 15,
            "title": "Milk Tea",
            "price": 3.00,
            "description": "Milk tea is a beverage made by adding milk to brewed tea.",
            "category": "non coffee",
            "image": "/static/product/milk tea.png"
        },
        {
            "id": 16,
            "title": "Green Tea",
            "price": 2.50,
            "description": "Green tea is a type of tea made from the leaves of the Camellia sinensis plant, processed to avoid oxidation or fermentation, thus preserving its green color and a high concentration of beneficial compounds like antioxidants.",
            "category": "non coffee",
            "image": "/static/product/green tea.png"
        },
        {
            "id": 17,
            "title": "Matcha Latte",
            "price": 3.00,
            "description": "A matcha latte is a vibrant green, tea-based beverage made from matcha powder, hot water, and milk (or a milk alternative).",
            "category": "non coffee",
            "image": "/static/product/matcha latte.png"
        },
        {
            "id": 18,
            "title": "Iced Chocolate",
            "price": 2.50,
            "description": "An iced chocolate is a chilled chocolate beverage, often described as a richer, more decadent version of chocolate milk, typically served over ice.",
            "category": "non coffee",
            "image": "/static/product/iced chocolate.png"
        },
        {
            "id": 19,
            "title": "Iced Coconut Water Matcha Cream",
            "price": 2.00,
            "description": "Coconut matcha cream refers to a beverage or dessert that combines the earthy flavor of matcha green tea with the creamy and slightly sweet taste of coconut.",
            "category": "non coffee",
            "image": "/static/product/coconut matcha.png"
        },
        {
            "id": 20,
            "title": "Iced Blue Milk",
            "price": 2.00,
            "description": "Iced Blue Latte is a refreshing and visually stunning drink that's perfect for hot summer days.",
            "category": "non coffee",
            "image": "/static/product/iced blue milk.png"
        },
        {
            "id": 21,
            "title": "Iced Strawberry Milk",
            "price": 2.00,
            "description": "Iced strawberry milk is a refreshing beverage made with milk and strawberries, often featuring a combination of sweet and creamy flavors.",
            "category": "non coffee",
            "image": "/static/product/iced strawberry milk.png"
        },
        {
            "id": 22,
            "title": "Matcha Frappe",
            "price": 2.50,
            "description": "A matcha frappe is a blended, iced beverage typically made with matcha green tea powder, milk, sweetener, and ice, often topped with whipped cream.",
            "category": "frappe",
            "image": "/static/product/matcha frappe.png"
        },
        {
            "id": 23,
            "title": "Strawberry Frappe",
            "price": 2.50,
            "description": "A strawberry frappe is a blended, chilled beverage featuring the sweet and refreshing taste of strawberries.",
            "category": "frappe",
            "image": "/static/product/strawberry frappe.png"
        },
        {
            "id": 24,
            "title": "Blueberry Frappe",
            "price": 2.50,
            "description": "A blueberry frappe is a blended iced drink, often featuring the sweet and tangy taste of blueberries, combined with a creamy base like milk or yogurt, and often includes ice for a refreshing, slushy texture.",
            "category": "frappe",
            "image": "/static/product/blueberry frappe.png"
        },
        {
            "id": 25,
            "title": "chocolate frappe",
            "price": 2.50,
            "description": "A chocolate frappe is a blended iced coffee drink, typically made with chocolate, ice, milk, and often flavored with chocolate syrup or sauce.",
            "category": "frappe",
            "image": "/static/product/chocolate frappe.png"
        },
        {
            "id": 26,
            "title": "Caramel frappe",
            "price": 2.50,
            "description": "A caramel frappé is a blended iced coffee drink known for its creamy, sweet, and cool caramel flavor.",
            "category": "frappe",
            "image": "/static/product/caramel frappe.png"
        },
        {
            "id": 27,
            "title": "Vanilla frappe",
            "price": 2.50,
            "description": "A vanilla frappe is a blended iced drink, typically featuring a creamy, vanilla-flavored base, often made with milk, ice, and vanilla extract or vanilla bean.",
            "category": "frappe",
            "image": "/static/product/vanilla frappe.png"
        },
        {
            "id": 28,
            "title": "Mocha Frappe",
            "price": 2.50,
            "description": "A Mocha Frappe is a blended, iced coffee drink that combines chocolate and coffee flavors.",
            "category": "frappe",
            "image": "/static/product/mocha frappe.png"
        },
        {
            "id": 29,
            "title": "Strawberry Soda",
            "price": 2.50,
            "description": "Strawberry Soda will delight your taste buds and quench your warm-weather thirst with the natural flavor of fresh strawberries.",
            "category": "soda",
            "image": "/static/product/strawberry soda.png"
        },
        {
            "id": 30,
            "title": "Blue Hawaii Soda",
            "price": 2.50,
            "description": "Blue Hawaiian is a cocktail and a soda flavor known for its tropical taste and vibrant blue color.",
            "category": "soda",
            "image": "/static/product/blue hawaii soda.png"
        },
        {
            "id": 31,
            "title": "Lemon Soda",
            "price": 2.50,
            "description": "Lemon soda is a refreshing, carbonated beverage typically made with lemon juice, sugar (or another sweetener), and soda water.",
            "category": "soda",
            "image": "/static/product/lemon soda.png"
        },
        {
            "id": 32,
            "title": "Watermelon Soda",
            "price": 2.50,
            "description": "Watermelon soda is a refreshing, sweet, and bubbly beverage that captures the flavor of watermelon in a fizzy drink.",
            "category": "soda",
            "image": "/static/product/watermelon soda.png"
        },
        {
            "id": 33,
            "title": "Orange Juice",
            "price": 2.00,
            "description": "Orange juice is a refreshing beverage made from the liquid extracted from oranges.",
            "category": "juice",
            "image": "/static/product/orange juice.png"
        },
        {
            "id": 34,
            "title": "Strawberry Juice",
            "price": 2.00,
            "description": "Strawberry Juice is a refreshing fresh fruit juice that is full of vitamin C and antioxidants and lot of invigorating flavor.",
            "category": "juice",
            "image": "/static/product/strawberry juice.png"
        },
        {
            "id": 35,
            "title": "watermelon juice",
            "price": 2.00,
            "description": "Watermelon juice is so simple to make with a blender. Refreshingly sweet and hydrating, it's perfect for a hot summer day.",
            "category": "juice",
            "image": "/static/product/watermelon juice.png"
        },
        {
            "id": 36,
            "title": "Apple Juice",
            "price": 2.00,
            "description": "Apple juice is a refreshing beverage made from the pressed and filtered juice of apples.",
            "category": "juice",
            "image": "/static/product/apple juice.png"
        },
        {
            "id": 37,
            "title": "Pineapple Juice",
            "price": 2.00,
            "description": "Pineapple juice is a sweet and tangy tropical beverage made from the juice extracted from fresh or canned pineapples.",
            "category": "juice",
            "image": "/static/product/pineapple juice.png"
        },
        {
            "id": 38,
            "title": "Cookies",
            "price": 2.50,
            "description": "A cookies is a small piece of data that a website stores on a user's computer, typically used to remember information about the user or their browsing activity.",
            "category": "cake",
            "image": "/static/product/cookies.png"
        },
        {
            "id": 39,
            "title": "Cake Chocolate",
            "price": 2.50,
            "description": "Chocolate cake is a delicious dessert made from chocolate or cocoa, often enjoyed by both children and adults.",
            "category": "cake",
            "image": "/static/product/cake chocolate.png"
        },
        {
            "id": 40,
            "title": "Cake Strawberry",
            "price": 2.50,
            "description": "Strawberry cake is a cake that uses strawberry as a primary ingredient. Strawberries may be used in the cake batter, atop the cake, and in the frosting.",
            "category": "cake",
            "image": "/static/product/cake strawberry.png"
        },
        {
            "id": 41,
            "title": "Cake Blueberry",
            "price": 2.50,
            "description": "Blueberry cake is easy to put together, has the most moist and tender crumb and is dotted with heaps of juicy blueberries throughout.",
            "category": "cake",
            "image": "/static/product/cake blueberry.png"
        },
        {
            "id": 42,
            "title": "Tiramisu Chocolate",
            "price": 3.00,
            "description": "Chocolate Tiramisu is a decadent layered dessert made up of mascarpone cream, chocolate pastry cream and coffee soaked biscuits.",
            "category": "cake",
            "image": "/static/product/tiramisu chocolate.png"
        },
        {
            "id": 43,
            "title": "Tiramisu Matcha",
            "price": 3.00,
            "description": "Matcha Tiramisu is the perfect fusion no-bake dessert made with layers of rich, velvety matcha mascarpone cream and spongy matcha-soaked ladyfingers.",
            "category": "cake",
            "image": "/static/product/tiramisu matcha.png"
        }

    ]
    try:
        data = {
            "first_name": request.form.get("first_name", ""),
            "last_name": request.form.get("last_name", ""),
            "phone": request.form.get("phone", ""),
            "email": request.form.get("email", ""),
            "address": request.form.get("address", ""),
            "notes": request.form.get("notes", "")
        }

        cart_json = request.form.get("cart_json")
        if cart_json:
            data["renderCartList"] = json.loads(cart_json)

        checkout_status = process_checkout(data)

        return render_template(
            "thank.html",
            status=checkout_status,
            total_usd=sum(to_number(i['qty']) * to_number(i['price']) for i in data["renderCartList"]),
            total_khr=sum(to_number(i['qty']) * to_number(i['price']) for i in data["renderCartList"]) * USD_TO_KHR
        )

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
if __name__ == '__main__':
    app.run()
