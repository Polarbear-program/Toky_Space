# Toky_Space

## [August 4th 2026.] ##
> I'm currently struggling with LeetCode problems; the "easy problems" don't seem easy at all. Who the fuck thinks that this is easy?
>
> Algorithms_Programming 
>> A *Data Structure* is a way to store and organize data in order to access it and modify it. -> There's no best *Data Structure*, so it is crucial to know the strengths and limitations of each one


- NP-Complete
> What is NP-complete? And why is it interesting?
> Definition 
>> NP problems(Non-deterministic Polynomial problems) are computational decision problems that both in the class NP and NP-hard.
>>> There's no efficient algorithm for an NP-complete problem that has ever been found, but no one can prove it, nor has it ever existed.(Bronstein said these NP-problem terms are full of larping, true *xD* )


- Parallelism 
> Chip must have several processing "cores" because if one of its cores went broken, then others can still function in a more computations-per-second sense.


- Efficiency
> Different algorithms devised to slove the same problem often differ dramatically in their efficiency. It can be significant not just due to the differences of software and hardware.
>> In the chapter 2, we will analyze 2 sorting algorithms *Merge* and *Insertion* sort, where *merge sort* takes time roughly equaly to c2n lgn, where lgn stands for log2n and c2 is another constant that does not depend on n.
>>> As we can see that Insertion Sort running time takes c1n.n while Merge Sort takes c2n.lgn which is smaller than Insertion Sort.
>>> While Insertion Sort can run faster than Merge sort if the input is low, but when the amount of data put in Insertion Sort is massive, the advantage of Merge Sort *lg n* will be significant.

## [August 5th 2026.] ##

> Today I've learned another way to call and modify instances inside a class without having to have __init__ function. I will call it self-call parameter because I couldn't found the official name for this:
>>      
        class Solution:
            def twoSum(self, nums: list[int], target: int) -> list[int]:
                # some computing here
                # return resulting list of int
- "-> list[int]:" This is used to return the type(rtype)

- To assign key(dictionaries) to each position/index of an array:
>         # Build hash table key[array[index]] -> index
            for i in range(len(array_given)):
                map[array_given[index]] = i         