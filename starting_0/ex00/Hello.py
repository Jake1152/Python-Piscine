def main():
    ft_list = ["Hello", "tata!"]
    ft_tuple = ("Hello", "toto!")
    ft_set = {"Hello", "tutu!"}
    ft_dict = {"Hello" : "titi!"}

    #your code here
    ft_list[1] = "World!"
    ft_tuple = ("Hello", "Korea!")
    ft_set.remove("tutu!")
    # ft_set.discard("tutu!") # discard()는 집합이 없음을 증명하고자 할 때 사용함.  ref: https://hbase.tistory.com/111
    ft_set.add("Seoul!")
    ft_dict["Hello"] = "42Seoul!"

    print(ft_list)
    print(ft_tuple)
    print(ft_set)
    print(ft_dict)

if __name__ == "__main__":
    main()