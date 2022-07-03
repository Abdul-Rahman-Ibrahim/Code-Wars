# TODO: complete this class
import math
class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
  
    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)
      
    # returns the number of pages
    def page_count(self):
        return math.ceil(len(self.collection)/self.items_per_page)
	
    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self,page_index):
        if page_index+1 > math.ceil(len(self.collection)/self.items_per_page):
            return -1
        if page_index == 0:
            return len(self.collection[:self.items_per_page])
        
        item_count = 0
        current_page_index = 0
        for i, item in enumerate(self.collection):
            if i != 0 and i % self.items_per_page == 0:
                current_page_index += 1
            if current_page_index == page_index:
                item_count += 1
        return item_count
            
    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self,item_index):
        if item_index >= len(self.collection) or item_index < 0:
            return -1
        current_page_index = 0
        for i in range(len(self.collection)):
            if i != 0 and i % self.items_per_page == 0:
                current_page_index += 1
            if i == item_index:
                return current_page_index

helper = PaginationHelper(['a','b','c','d','e','f'], 4)
helper = PaginationHelper(['a','b','c','d','e','f'], 2)
print(helper.page_count()) # should == 2
print(helper.item_count()) # should == 6
print(helper.page_item_count(0))  # should == 4
print(helper.page_item_count(1)) # last page - should == 2
print(helper.page_item_count(2)) # should == -1 since the page is invalid

# page_index takes an item index and returns the page that it belongs on
print(helper.page_index(5)) # should == 1 (zero based index)
print(helper.page_index(2)) # should == 0
print(helper.page_index(20)) # should == -1
print(helper.page_index(-10)) # should == -1 because negative indexes are invalid
  
