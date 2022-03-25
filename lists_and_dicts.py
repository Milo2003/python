def run ():
    # squares = [i for i in range(1, 10000) if i % 36 == 0]
    # print(squares)
    my_dictionary = {i: round(i**0.5, 5) for i in range(1, 1001)}
    
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         my_dict[i] = i**3
    
    print(my_dictionary)



if __name__ == '__main__':
    run()