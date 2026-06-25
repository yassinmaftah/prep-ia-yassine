def check_score(score:int) -> str :
    if (score >= 10):
        return "Admis"
    else:
        return "Recalé"
    
# print(check_score(12))
# print(check_score(8))

def sum_prices(prices : list) -> int :
    total : int = 0
    for price in prices:
        total += price
    return total

# print(sum_prices([10,541,8,0,4]))
# print(sum_prices([1,2,3,4,5]))

def describe_user(user : dict) -> str:
    return f"{user['name']} habite à {user['city']}"
# print(describe_user({"name": "Yassine", "city": "agadir"}))

def filter_positive_v1(numbers : list) -> list:
    return [n for n in numbers if n > 0]

def filter_positive_v2(numbers : list) -> list:
    return list(filter(lambda n : n > 0,numbers))

# print(filter_positive_v1([110,5,6,-9,-5,]))
# print(filter_positive_v2([110,5,6,-9,-5,]))

def count_words(words : list) -> dict :
    result : dict = {}
    for word in words :
        result[word] = result.get(word , 0) + 1
    return result

# print(count_words(['chat', 'chien', 'chat', 'oiseau', 'chien', 'chat']))