my_str = 'banashankari'
sub_string = 'm'

try:
    print(my_str.index('s')) # 4
    print(my_str.index(sub_string)) # error
    print(my_str.index('shankari')) 
except ValueError as e:
    print(f'The sub string {sub_string} not found')
    print(e.__str__())
except:
    print('Some error occured')