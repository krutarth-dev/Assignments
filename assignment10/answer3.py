def print_subsets(set_string):
    def print_subsets_helper(set_string, subset, index):
        if index == len(set_string):
            print(subset)
            return

        print_subsets_helper(set_string, subset + set_string[index], index + 1)
        print_subsets_helper(set_string, subset, index + 1)

    print_subsets_helper(set_string, "", 0)

print_subsets("abc")
