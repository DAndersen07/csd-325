#!/usr/bin/env python
# coding: utf-8

# In[1]:


def bottle_word(count):
    return "bottle" if count == 1 else "bottles"
def countdown(bottles):
    while bottles > 0:
        print(f"{bottles} {bottle_word(bottles)} of beer on the wall.")
        print(f"{bottles} {bottle_word(bottles)} of beer.")
        print("Take one down, pass it around.")
        bottles -= 1
        if bottles == 0:
            print("No more bottles of beer on the wall.\n")
        else:
            print(
                f"{bottles} {bottle_word(bottles)} "
                "of beer on the wall.\n"
            )
def main():
    while True:
        try:
            bottles = int(input("How many bottles of beer are on the wall? "))
            if bottles < 1:
                print("Please enter a number greater than zero.")
                continue
            break
        except ValueError:
            print("Please enter a whole number.")
    countdown(bottles)
    print("Time to buy more beer!")
if __name__ == "__main__":
    main()


# In[ ]:




