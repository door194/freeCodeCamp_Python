def verify_card_number(card_num):
    # Remove separators and convert to a list of integer digits
    digits = [int(d) for d in str(card_num) if d.isdigit()]
    
    # Check digits starting from the right ( Luhn algorithm )
    payload = digits[:-1]
    check_digit = digits[-1]
    
    # Reverse payload to process from right to left
    reversed_digits = payload[::-1]
    
    # Double every second digit and subtract 9 if > 9
    total = sum(d if i % 2 == 1 else (d * 2 if d * 2 <= 9 else d * 2 - 9) 
                for i, d in enumerate(reversed_digits))
    
    # Valid if sum + check digit is a multiple of 10
    return "VALID!" if (total + check_digit) % 10 == 0 else "INVALID!"

print(verify_card_number("453914889"))
