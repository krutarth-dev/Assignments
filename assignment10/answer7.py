def permute_string(string):
    def backtrack(string, current_permutation, visited, result):
        if len(current_permutation) == len(string):
            result.append(current_permutation)
            return

        for i in range(len(string)):
            if visited[i]:
                continue
            visited[i] = True
            backtrack(string, current_permutation + string[i], visited, result)
            visited[i] = False

    result = []
    visited = [False] * len(string)
    backtrack(string, "", visited, result)
    return result

permutations = permute_string("cd")
print(permutations)
