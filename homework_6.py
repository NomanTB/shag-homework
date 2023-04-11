# import kem as kem
#
# result = []
#
# def divider(a, b):
#     if a < b:
#         raise ValueError
#     if b > 100:
#         raise IndexError
#     return a/b
#
# try:
#     data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4}
# except TypeError:
#     print("строка не делиться")
#
#
# for key in data:
#     res = divider(key, data[kem])
#     result.append(res)
#
# print(result)

# result = []
#
# def divider(a, b):
#     try:
#         if a < b:
#             raise ValueError
#         if b > 100:
#             raise IndexError
#         return a / b
#     except (ValueError, IndexError) as e:
#         print("Error")
#         return None
#     except Exception as e:
#         print("Unexpected error")
#         return None
#
# data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}
#
# for key in data:
#     res = divider(key, data.get(key))
#     if res is not None:
#         result.append(res)
#
# print(result)

result = []
def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a/b


try:
     data = [10 / 2, 2 / 5, "123" / 4, 18 / 0, [] / 15, 8 / 4]

except TypeError:
    print()
    print("TypeError: unsupported operand type(s) for /: 'str' and 'int'")

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except ValueError:
        print("ValueError")
    except IndexError:
        print("IndexError")

print(result)





