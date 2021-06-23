def skip_elements(elements):
	# Initialize variables
	new_list = []
	i = 0

	## PROCESS 1

	# Iterate through the list
	for element in elements:
		if elements.index(element) % 2 == 0:
			# Does this element already exist in the resulting list?
			if element not in new_list:
				# Add this element to the resulting list
				new_list.append(element)

	## PROCESS 2

	for element in elements:
            # Does this element belong in the resulting list?
            if i <= len(elements):
                # Add this element to the resulting list
                new_list.append(elements[i])
            # Increment i
                i += 2

	## PROCESS 2

	new_list=elements[::2]

	return new_list



print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
