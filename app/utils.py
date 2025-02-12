def validate_receipt(data):
    if not isinstance(data, dict):
        return False, "Invalid data format: Expected a JSON object"

    required_fields = ["retailer", "purchaseDate", "purchaseTime", "items", "total"]
    for field in required_fields:
        if field not in data:
            return False, ("Missing field: "+field)

    if not isinstance(data["items"], list) or len(data["items"]) == 0:
        return False, "Invalid or empty Field: items"


    for i,item in enumerate(data["items"]):
        if not isinstance(item, dict):
            return False, "Invalid data at index "+i+" in items: Expected an object(dict)"

        missing_fields = []
        for item_field in ["shortDescription", "price"]:
            if item_field not in item:
                missing_fields.append(item_field)

        if missing_fields:
            return False, "Missing field at index "+ i +" in items: "+(', '.join(missing_fields))

        try:
            float(item["price"])
        except ValueError:
            return False, "Invalid 'price' at index "+ i +" in items: Must be a numeric value"

    try:
        float(data["total"])
    except ValueError:
        return False, "Invalid 'total': Must be a numeric value"

    return True, ""
