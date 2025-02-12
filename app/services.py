import uuid
import math
import re
from datetime import datetime

receipts_database = {}


def process_receipt(data):
    receipt_id = str(uuid.uuid4())
    receipts_database[receipt_id] = calculate_points(data)
    return receipt_id


def calculate_reward_points(receipt_id):
    return receipts_database.get(receipt_id)

def calculate_points_for_retailer_name(receipt):
    retailer = receipt['retailer']
    point = len(re.findall(r'[a-zA-Z0-9]', retailer)) if retailer else 0
    return point

def calculate_points_for_total_round_dollar_amount(receipt):
    point = 0
    total = float(receipt['total'])
    if total.is_integer():
        point = 50
    return point

def calculate_points_if_total_is_multiple(receipt):
    point = 0
    total = float(receipt['total'])
    if total % 0.25 == 0:
        point = 25
    return point

def calculate_points_for_items_in_receipt(receipt):
    point = (len(receipt['items']) // 2) * 5 if receipt['items'] else 0
    return point

def calculate_points_for_item_description(receipt):
    point = 0
    for item in receipt['items']:
        desc = item['shortDescription'].strip()
        if len(desc) % 3 == 0 and len(desc) > 0:
            price = float(item['price'])
            point += math.ceil(price * 0.2)
    return point

def calculate_points_for_purchase_day(receipt):
    point = 0
    date = datetime.strptime(receipt['purchaseDate'], "%Y-%m-%d")
    if date.day % 2 == 1:
        point = 6
    return point

def calculate_points_for_purchase_hour(receipt):
    point = 0
    purchase_time = datetime.strptime(receipt['purchaseTime'], "%H:%M")
    if (purchase_time.hour == 14 and purchase_time.minute > 0) or (15 <= purchase_time.hour < 16):
        point = 10
    return point

def calculate_points(receipt):
    points = 0
    points += calculate_points_for_retailer_name(receipt)
    points += calculate_points_for_total_round_dollar_amount(receipt)
    points += calculate_points_if_total_is_multiple(receipt)
    points += calculate_points_for_items_in_receipt(receipt)
    points += calculate_points_for_item_description(receipt)
    points += calculate_points_for_purchase_day(receipt)
    points += calculate_points_for_purchase_hour(receipt)
    return points
