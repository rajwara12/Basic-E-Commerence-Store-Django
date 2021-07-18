from django import template
register = template.Library()


@register.filter(name="is_in_cart")
def is_in_cart(product, cart):
    keys=cart.keys()
    print(keys)
    for id in keys: 
        if int(id)==product.id:
            return True
    return False

@register.filter(name="quantity_cart")
def quantity_cart(product, cart):
    keys=cart.keys()
    print(keys)
    for id in keys: 
        if int(id)==product.id:
            return cart.get(id)
    return 0;        


@register.filter(name="currency")
def currency(num):
    return "روپیہ‎" + str(num)    

@register.filter(name="total_cart")
def total_cart(product, cart):
    return product.price*quantity_cart(product, cart)  


@register.filter(name="multiply")
def multiply(number, number1):
    return number*number1      