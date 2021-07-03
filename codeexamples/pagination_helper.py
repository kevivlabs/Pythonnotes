class PaginationHelper:
    

  # The constructor takes in an array of items and a integer indicating
  # how many items fit within a single page
  def __init__(self, collection, items_per_page):
    
    self.collection= collection
    self.items_per_page= items_per_page
    
  
  # returns the number of items within the entire collection
  def item_count(self):
    return len(self.collection)  
  
  # returns the number of pages
  def page_count(self):
        x=(len(self.collection) // self.items_per_page)
        return x+1
    
  # returns the number of items on the current page. page_index is zero based
  # this method should return -1 for page_index values that are out of range
  def page_item_count(self,page_index):
    
    numerator, denominator = divmod(len(self.collection),self.items_per_page)
    page_item_count=[]
    counter=1
    while(counter <= numerator):
        page_item_count.append(self.items_per_page)
        counter+=1
    page_item_count.append(denominator)
    if (page_index > len(page_item_count)-1):
        return -1
    else:
        return (page_item_count[page_index])
    
    
        
        # determines what page an item is on. Zero based indexes.
      # this method should return -1 for item_index values that are out of range
  def page_index(self,item_index): 
    
    if (item_index < len(self.collection) and  item_index >=0 ):
        return item_index// self.items_per_page
    else:
        return -1
    
