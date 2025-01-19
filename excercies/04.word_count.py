print("Please enter your paragraph here to count the lower_case_later")
paragraph=input()

split_paragarph=[lower_case_later for lower_case_later in paragraph.split(' ') if lower_case_later]
print(split_paragarph)

print(f"Total number of lower_case_later in paragraph {len(split_paragarph)}")

#Print the lower_case_later occurance count 

occurance_count={}

for lower_case_later in split_paragarph:
    lower_case_later=lower_case_later.lower()
    if lower_case_later in occurance_count:
        occurance_count[lower_case_later]=occurance_count[lower_case_later]+1
    
    else:
           occurance_count[lower_case_later]=1
    print(occurance_count)
