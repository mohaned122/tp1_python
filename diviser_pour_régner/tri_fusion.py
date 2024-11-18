def tri_fusion(tab, d, f):
    if d >= f:
        return

    # Calculate middle point using integer division
    millieu = (d + f) // 2

    # Sort the left and right halves
    tri_fusion(tab, d, millieu)
    tri_fusion(tab, millieu + 1, f)

    # Merge the two halves
    merge(tab, d, millieu, f)


def merge(tab, d, millieu, f):
    # Create two subarrays from the current array
    left_half = tab[d:millieu + 1]
    right_half = tab[millieu + 1:f + 1]

    i = j = 0
    k = d

    # Merge the two halves by comparing their elements
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            tab[k] = left_half[i]
            i += 1
        else:
            tab[k] = right_half[j]
            j += 1
        k += 1

    # Copy remaining elements from left_half if any
    while i < len(left_half):
        tab[k] = left_half[i]
        i += 1
        k += 1

    # Copy remaining elements from right_half if any
    while j < len(right_half):
        tab[k] = right_half[j]
        j += 1
        k += 1


# Example usage
tab = [12, 7, 10, 23, 9]
tri_fusion(tab, 0, len(tab) - 1)
print(tab)
