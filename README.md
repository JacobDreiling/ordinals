# ordinals
Implementation of computable <a href="https://en.m.wikipedia.org/wiki/Ordinal_number">ordinals</a> below the Small Veblen Ordinal

A countable ordinal can be represented as a function which takes a natural number, n, and returns the n-th ordinal in its fundamental sequence. Zero is simply represented as itself, while successor ordinals are assigned a constant "fundamental sequence" consisting of their predecessor.

In order to actually see what's going on, I represent ordinals as tuples of their functions and text appearances. For example, the ordinal ω+1 may be defined as ((lambda n: ω), 'ω+1'). This adds some extra mess but also makes things way clearer. As a bonus, I implemented two ordinal-indexed function hierarchies.
