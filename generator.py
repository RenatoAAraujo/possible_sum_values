def subsets_with_sum(numbers_set:list, target:int, with_replacement:bool):
    print(f"The numbers that will be used to reach the sum of {target} are:\n{numbers_set}\nThe sets can have replaced numbers? {with_replacement}.")
    print("The larger of \"target\" is the longer this will take")

    def generator(index, generation_list, generated_set, generation_target):
        if generation_target == sum(generation_list):
            generated_set.append(generation_list)
        elif generation_target < sum(generation_list):
            return
    
        for u in range(index, len(numbers_set)):
            generator(u + replacement_variable, generation_list + [numbers_set[u]], generated_set, generation_target)
            print(str(generated_set) + "\n")

        return generated_set
    
    replacement_variable = int(not with_replacement)
    return generator(0, [], [], target)
