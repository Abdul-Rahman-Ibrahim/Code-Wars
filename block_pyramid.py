def block_pyramid(blocks):
    """
    Listen to this story: a boy and his father, a computer programmer,
    are playing with wooden blocks. They are building a pyramid.
    Their pyramid is a bit weird, as it is actually a pyramid-shaped
    wall - it's flat. The pyramid is stacked according to one simple
    principle: each lower layer contains one block more than the layer above.
    The figure illustrates the rule used by the builders:
    Your task is to write a program which reads the number
    of blocks the builders have, and outputs the height of the pyramid that can
    be built using these blocks.
    Note: the height is measured by the number of fully completed layers - if the
    builders don't have a sufficient number of blocks and cannot complete the next
    layer, they finish their work immediately.
    Test your code using the data we've provided.
    """
    height = 0
    count = 0
    while count < blocks:
        count += 1
        blocks -= count
        height += 1
    return height

blocks = int(input("Enter the number of blocks: "))
print("The height of the pyramid:", block_pyramid(blocks))

    

