user_info = {
    'name':'aniket',
    'age':18,
    'fav_movies':['coco','kimi no ka wa'],
    'fav_tunes':['awakening','fairy tale'],
}
if 'name' in user_info:
    print('present')
else:
    print('not present')
if 'aniket' in user_info.values():
    print('present')
else:
    print('not present')
user_info_values = user_info.values()
print(user_info_values)
user_info_keys = user_info.keys()
print(user_info_keys)

