# Python Difflib Pattern Matching
# difflib � Helpers for computing deltas
# This module provides classes and functions for comparing sequences.
# It can be used for example, for comparing files, and can produce difference information in various formats, including HTML and context and unified diffs.
#
# class difflib.SequenceMatcher 
# This is a flexible class for comparing pairs of sequences of any type, so long as the sequence elements are hashable.
# The basic algorithm predates, and is a little fancier than, an algorithm published in the late 1980�s by Ratcliff and Obershelp under the hyperbolic name
# �gestalt pattern matching.� 
# The idea is to find the longest contiguous matching subsequence that contains no �junk� elements; these �junk� elements are ones that are uninteresting in
# some sense, such as blank lines or whitespace.
# (Handling junk is an extension to the Ratcliff and Obershelp algorithm.)
# The same idea is then applied recursively to the pieces of the sequences to the left and to the right of the matching subsequence.
# This does not yield minimal edit sequences, but does tend to yield matches that �look right� to people.
# Timing: The basic Ratcliff-Obershelp algorithm is cubic time in the worst case and quadratic time in the expected case.
# SequenceMatcher is quadratic time for the worst case and has expected-case behavior dependent in a complicated way on how many elements the sequences have
# in common; best case time is linear.
# Automatic junk heuristic: SequenceMatcher supports a heuristic that automatically treats certain sequence items as junk.
# The heuristic counts how many times each individual item appears in the sequence.
# If an item�s duplicates (after the first one) account for more than 1% of the sequence and the sequence is at least 200 items long, this item is marked
# as �popular� and is treated as junk for the purpose of sequence matching.
# This heuristic can be turned off by setting the autojunk argument to False when creating the SequenceMatcher.
#
# class difflib.Differ 
# This is a class for comparing sequences of lines of text, and producing human-readable differences or deltas.
# Differ uses SequenceMatcher both to compare sequences of lines, and to compare sequences of characters within similar (near-matching) lines.
#

#
# difflib.ndiff(a, b, linejunk=None, charjunk=IS_CHARACTER_JUNK): 
# Compare a and b (lists of strings); return a Differ-style delta (a generator generating the delta lines).
# Optional keyword parameters linejunk and charjunk are filtering functions (or None):
# linejunk: A function that accepts a single string argument, and returns true if the string is junk, or false if not.
# The default is None. There is also a module-level function IS_LINE_JUNK(), which filters out lines without visible characters, except for at most one
# pound character ('#') � however the underlying SequenceMatcher class does a dynamic analysis of which lines are so frequent as to constitute noise, and
# this usually works better than using this function.
# charjunk: A function that accepts a character (a string of length 1), and returns if the character is junk, or false if not.
# The default is module-level function IS_CHARACTER_JUNK(), which filters out whitespace characters (a blank or tab; it�s a bad idea to include newline in
# this!).
 
#
# Tools/scripts/ndiff.py is a command-line front-end to this function.
# 

diff = ndiff('one\ntwo\nthree\n'.splitlines(keepends=True),
                 'ore\ntree\nemu\n'.splitlines(keepends=True))

print(''.join(diff), end="")
