user_info = {
    'name':'aniket',
    'age':18,
    'fav_movies':['coco','kimi no ka wa'],
    'fav_tunes':['awakening','fairy tale'],
}

user_info['fav_songs']=['song1','song2']
print(user_info)

popped_item=user_info.pop('fav_tunes')
print(f"popped item is {popped_item}")

popped_item = user_info.popitem()
print(user_info)