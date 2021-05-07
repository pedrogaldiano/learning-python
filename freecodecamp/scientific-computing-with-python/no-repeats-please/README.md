## No Repeats Please
https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/no-repeats-please

Return the number of total permutations of the provided string that don't have repeated consecutive letters. Assume that all characters in the provided string are unique.
For example, aab should return 2 because it has 6 total permutations (aab, aab, aba, aba, baa, baa), but only 2 of them (aba and aba) don't have the same letter (in this case a) repeating.

-----------------------------------------------------------------------------------------
I create two solutions for this algorithm. One using the itertools library which implements permutations, and another one using the random library which is more "brute force" style. The first option is way more efficient, especially when you work with are more than 4 elements.
